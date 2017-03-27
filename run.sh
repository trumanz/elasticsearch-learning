#!/bin/bash
./clearn_all_es_containers.sh
source ./start_es_within_docker.sh
echo $ES_IP
