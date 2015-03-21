import os

TAB_SIZE = 4

for name in os.listdir ( '.' ) :
    if name.endswith ( '.py' ) :
        f = open ( name + '_', 'w' )
        for line in open ( name, 'r' ).readlines () :
            pos = 0
            buf = ""
            for ch in line :
                if ch == '\t' :
                    indent = TAB_SIZE - ( pos % TAB_SIZE )
                    buf += indent * ' '
                    pos += indent
                else :
                    pos += 1
                    buf += ch
                    if ch != ' ' :
                        if ch == '\n' :
                            f.write ( '\n' )
                        else :
                            f.write ( buf )
                            buf = ""
        f.close ()

