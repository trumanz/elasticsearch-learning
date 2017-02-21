#!/bin/bash
git clone https://github.com/trumanz/dockerBuild
cd dockerBuild && git pull && cd ELK/elasticsearch/  &&  ./build.sh
