#!/bin/bash

#read -p "Enter filename " filename

ls -d /home/*/group4* > filelist
ls -d /home/*/Group4* >> filelist
ls -d /home/*/*/group4* >> filelist
ls -d /home/*/*/Group4* >> filelist

awk -v var=$filename '{print "cp "}' filelist > tmp1
awk '{print " group4"}' filelist > tmp2

paste -d " " tmp1 filelist > tmp3
paste -d "" tmp3 tmp2 > tmp4

chmod +x tmp4
#./tmp4
