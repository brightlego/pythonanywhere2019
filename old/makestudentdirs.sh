#!/bin/bash

ls -d /home/* > filelist

awk '{print "mkdir"}' filelist > tmp1
awk '{print "/ecb"}' filelist > tmp2

paste -d "" filelist tmp2 > tmp3
paste -d " " tmp1 tmp3 > tmp4

chmod +x tmp4
./tmp4
