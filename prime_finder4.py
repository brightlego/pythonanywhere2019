from math import sqrt
from time import time
max_num = input("What is the maximum number? ")
primes = {0:2}
start = time()
for i in range(3,max_num,2):
    isprime = True
    j = 0
    while primes[j] < sqrt(i):
        if i%primes[j] == 0:
            isprime = False
            break
        j += 1
    if isprime:
        primes[len(primes)] = i
end = time()
print primes.values()
print end - start