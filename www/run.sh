#!/bin/sh

set +e
echo "Restarting."
docker stop toothris-www
docker rm toothris-www
set -e

mkdir -p /var/tmp/toothris-www
chown 1000:1000 /var/tmp/toothris-www

docker run --rm -t \
    -v /etc/localtime:/etc/localtime:ro \
    -v /etc/toothris-www:/etc/toothris-www:ro \
    -v /var/tmp/toothris-www:/var/tmp/toothris-www \
    --name toothris-www -h toothris-www \
    toothris/toothris-www:0.0.0dev-2015-01-02 \
    sudo -iu user /toothris-www/run/run.sh
