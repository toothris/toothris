#!/bin/bash

set -e

TMPDIR=/var/tmp/toothris-www

# main static content
cp /toothris-www/www/* $TMPDIR

# bootstrap
cd /toothris-www/bootstrap.git
git checkout .
git apply /toothris-www/setup/bootstrap/bootstrap.patch
grunt dist
cp -r /toothris-www/bootstrap.git/dist/* $TMPDIR

# jquery
cp -r /toothris-www/jquery/node_modules/jquery/dist/cdn/* $TMPDIR
