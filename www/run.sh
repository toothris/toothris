#!/bin/sh

set +e
docker stop toothris-www
docker rm toothris-www
docker rmi toothris/toothris-www
set -e

mkdir -p /var/tmp/toothris-www
chown 1000:1000 /var/tmp/toothris-www

docker build --rm -t toothris/toothris-www /usr/share/toothris-www/www

docker run --rm \
    -v /etc/localtime:/etc/localtime:ro \
    -v /etc/toothris-www:/etc/toothris-www:ro \
    -v /var/tmp/toothris-www:/var/tmp/toothris-www \
    --name toothris-www -h toothris-www toothris/toothris-www \
    sudo -iu user /toothris-www/run.sh
