from time import time
from math import sqrt
max_num = input('What is the maximum number? ')+1
primes = [2]
timestart = time()
for i in xrange(3,max_num,2):
    isprime = 1
    j=0
    while isprime and primes[j]<=sqrt(i):
        if not i%primes[j]:
            isprime = 0
        j=j+1
    if isprime:
        primes.append(i)

timeend = time()
print(primes)
print(timeend-timestart)
print(len(primes))