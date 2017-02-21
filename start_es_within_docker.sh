#!/bin/bash
CID=$(docker run -d -it  trumanz/elasticsearch   /es_entrypoint.sh)
IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'  $CID)
echo $IP
