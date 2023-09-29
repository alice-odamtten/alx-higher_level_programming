#!/bin/bash
# Bash script that takes in a URL that sends and displays respone
curl -s $1 | wc -c
