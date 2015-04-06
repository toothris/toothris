#!/bin/bash
set -e
/toothris-www/run/makevideo.sh
/toothris-www/run/makewww.sh
/toothris-www/run/deploy.sh
