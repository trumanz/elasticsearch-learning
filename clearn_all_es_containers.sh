#!/bin/sh
docker ps -a  | grep elastics   | awk   '{print $1}'   |  xargs docker rm -f
