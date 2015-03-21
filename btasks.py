# -*- coding: cp1251 -*-

# LIBS
import rabbyt
import stackless

# BASE
import bprofile

# CONSTS

ITERATIONS_REALTIME = 99999
ITERATIONS_HIGH     = 100
ITERATIONS_MEDIUM   = 500
ITERATIONS_LOW      = 100


class Event :
    def __init__ ( self ) :
        self.channel = stackless.channel ()
        self.call_tag = 0
        self.tasks_tags = {}

    def __call__ ( self, arg = None ) :
        self.call_all ( arg )

    def anybody_waiting ( self ) :
        return self.waiting_count () > 0

    def waiting_count ( self ) :
        return max ( - self.channel.balance, 0 )

    def skip_missed ( self ) :
        self.tasks_tags [ current_task ().tag ] = self.call_tag

    def missed ( self ) :
        if current_task ().tag not in self.tasks_tags.keys () :
            return self.call_tag != 0
        else :
            return self.tasks_tags [ current_task ().tag ] != self.call_tag

    def wait ( self ) :
        self.skip_missed ()
        return self.channel.receive ()

    def call_all ( self, arg = None ) :
        self.call_tag += 1
        for i in range ( self.waiting_count () ) :
            if working ( self.channel.queue ) :
                self.tasks_tags [ self.channel.queue.tag ] = self.call_tag
                self.channel.send ( arg )

    def call_one ( self, arg = None ) :
        self.call_tag += 1
        if self.anybody_waiting () :
            if working ( self.channel.queue ) :
                self.tasks_tags [ self.channel.queue.tag ] = self.call_tag
                self.channel.send ( arg )

task_tag = 0

class Task ( stackless.tasklet ) :
    def __init__ ( self, f ) :
        stackless.tasklet.__init__ ( self, f )
        self.priority_event = None

        global task_tag
        self.tag = task_tag
        task_tag += 1

    def start ( self, * args, ** kws ) :
        return stackless.tasklet.__call__ ( self, * args, ** kws )

    def stop ( self ) :
        stackless.tasklet.kill ( self )

    def __call__ ( self, * args, ** kws ) :
        return self.start ( * args, ** kws )

    def working ( self ) :
        return self.alive


# GLOBALS

priority_realtime   = Event ()
priority_high       = Event ()
priority_medium     = Event ()
priority_low        = Event ()

PRIORITY_DEFAULT    = priority_low

waiters             = []


def skip_missed ( event ) :
    event.skip_missed ()

def wait_missed ( event ) :
    if event.missed () :
        event.skip_missed ()
    else :
        event.wait ()

def wait ( arg ) :
    if arg == None :
        return
    elif isinstance ( arg, Task ) :
        while working ( arg ) :
            work_async ()
    elif isinstance ( arg, Event ) :
        arg.wait ()
    else :
        if arg == 0 :
            return
        event = Event ()
        end_time = rabbyt.get_time () + arg
        waiters.append ( ( end_time, event ) )
        waiters.sort ()
        event.wait ()


def current_task () :
    if isinstance ( stackless.getcurrent (), Task ) :
        return stackless.getcurrent ()
    else :
        return None


def start_async ( f ) :
    def callf ( * args, ** kws ) :
        t = Task ( f )
        t.priority_event = PRIORITY_DEFAULT
        return t ( * args, ** kws )
    return callf


def start_async_realtime ( f ) :
    def callf ( * args, ** kws ) :
        t = Task ( f )
        t.priority_event = priority_realtime
        return t ( * args, ** kws )
    return callf


def stop ( f ) :
    if isinstance ( f, Task ) :
        f.stop ()
    else :
        assert f == None


def working ( f ) :
    if isinstance ( f, Task ) :
        return f.working ()
    else :
        return False


def work_async () :
    wait ( current_task ().priority_event )
    return True


def run () :


    def run_event ( event, iterations ) :
        n = min ( event.waiting_count (), iterations )
        for i in range ( n ) :
            event.call_one ()
        stackless.run ()


    def run_waiters () :
        while len ( waiters ) :
            end_time = waiters [ 0 ] [ 0 ]
            if end_time <= rabbyt.get_time () :
                event = waiters [ 0 ] [ 1 ]
                del waiters [ 0 ]
                event.call_all ()
            else :
                break


    bprofile.begin ( "all tasks" )

    bprofile.begin ( "waiters" )
    run_waiters ()
    bprofile.end ( "waiters" )

    bprofile.begin ( "realtime tasks" )
    run_event ( priority_realtime , ITERATIONS_REALTIME   )
    bprofile.end ( "realtime tasks" )

    bprofile.begin ( "high priority tasks" )
    run_event ( priority_high     , ITERATIONS_HIGH       )
    bprofile.end ( "high priority tasks" )

    bprofile.begin ( "medium priority tasks" )
    run_event ( priority_medium   , ITERATIONS_MEDIUM     )
    bprofile.end ( "medium priority tasks" )

    bprofile.begin ( "low priority tasks" )
    run_event ( priority_low      , ITERATIONS_LOW        )
    bprofile.end ( "low priority tasks" )

    bprofile.end ( "all tasks" )
