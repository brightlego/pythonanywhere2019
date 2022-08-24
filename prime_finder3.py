# -*- coding: utf-8 -*-
from math import sqrt
from time import time
import numpy as np

max_num = input("Max num: ")
time_start = time()
primes = range(max_num)
i = 2
while i<=sqrt(max_num+1):
    for j in range(i*2,max_num,primes[i]):
        primes[j] = -1
    i += 1
time_end = time()
'''
for i in range(max_num+2)[2:]:
    if primes[i-2] != -1:
        print(i)
'''
units = ['s','ms','μs']
u = 0
delta_t = time_end-time_start
while delta_t < 1:
    u += 1
    delta_t *= 1000

print delta_t,units[u]