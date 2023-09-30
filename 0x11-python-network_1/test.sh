#!/usr/bin/bash
read file_name
echo $(pycodestyle $file_name)
echo $(chmod u+x $file_name)
read message
echo $(git add .)
echo $(git commit -m "$message")
echo $(git push)
