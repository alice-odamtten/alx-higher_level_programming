#!/bin/bash
# Bash script that takes in a URL and displays.
curl -sIX OPTIONS $1 | grep "Allow:" | cut -d ' ' -f 2-