from time import time
from math import sqrt

max_num = input('What is the maximum number? ')+1
primes = []
timestart = time()
for i in range(2,max_num):
    primes.append(i)
i = 0
for i in primes:
    while j < len(primes):
        if i!=primes[j] and primes[j]%i == 0:
            print primes[j]
            del primes[j]
        j += 1

    print i
timeend = time()
print(primes)
print(timeend-timestart)
print(len(primes))