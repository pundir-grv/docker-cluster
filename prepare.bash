#!/bin/bash
mkdir -p /tmp/mongo/dbdata_m1 /tmp/mongo/dbdata_m1 /tmp/mongo/dbdata_m3 /tmp/mongo/dbdata_m4 /tmp/mongo/dbdata_m5 /tmp/mongo/log_m1 /tmp/mongo/log_m2 /tmp/mongo/log_m3 /tmp/mongo/log_m4 /tmp/mongo/log_m5
if [[ ! -f mongo_access.key ]]; then
    openssl rand -base64 756 > mongo_access.key
    chmod 400 mongo_access.key
fi
docker-compose --file docker-compose-replset.yml up --build -d
