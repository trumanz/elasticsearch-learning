#!/bin/bash
sudo sysctl -w vm.max_map_count=262144
CID=$(docker run  --name elastics01 -d -it  trumanz/elasticsearch   /es_entrypoint.sh)
echo "Container ID $CID"
IP=$(docker inspect  $CID | python -c  'import json,sys;obj=json.load(sys.stdin); print obj[0]["NetworkSettings"]["IPAddress"]')
echo $IP
export ES_IP=$IP

for i in {1..10}; do
  echo "waitting $IP:9200 up"
  if nc -q 1 $IP 9200 < /dev/null ; then
     echo "$IP:9200 up"
     break
  fi
  sleep 2
done

#while ! nc -q 1 $IP 9200 < /dev/null; do
#  echo "wait $IP:9200 up"
#  sleep 1
#done

curl -XGET $IP:9200

