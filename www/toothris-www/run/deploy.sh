#!/bin/bash

set -e

. /etc/toothris-www/config.sh

export AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY
export AWS_DEFAULT_REGION

set +e
aws s3 rm --recursive s3://$S3_BUCKET
aws s3 rb s3://$S3_BUCKET
set -e

aws s3 mb s3://$S3_BUCKET
aws s3api put-bucket-website --bucket $S3_BUCKET \
  --website-configuration '{"IndexDocument": {"Suffix": "index.html"}}'
aws s3 cp --recursive --acl 'public-read' /var/tmp/toothris-www s3://$S3_BUCKET
