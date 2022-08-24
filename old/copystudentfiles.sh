#!/bin/bash

read -p "Enter filename " filename

ls -d /home/* > filelist

awk -v var=$filename '{print "cp ",var}' filelist > tmp1
awk '{print "/ecb"}' filelist > tmp2

paste -d " " tmp1 filelist > tmp3
paste -d "" tmp3 tmp2 > tmp4

chmod +x tmp4
#./tmp4
