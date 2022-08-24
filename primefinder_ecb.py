from __future__ import division
import numpy as np

from time import time
min_prime=2
max_prime=10000

all_numbers=np.arange(min_prime,max_prime)

def findfirstnumber(min_prime,number_test):
    firstflag=0
    firstflag=0
    i=min_prime-1
    while firstflag==0:
        i=i+1
        if i % number_test == 0:
            firstnumber=i
            firstflag=1
    return(firstnumber)

def checkprime(numberin):
    prime_check=0
    j=2
    while (prime_check == 0) & (j < numberin):

        if numberin % j == 0:
            prime_check=1
        j=j+1

    return prime_check

test_primes=[2,3,5,7,11,13]
mult_two=np.arange(findfirstnumber(min_prime,2),max_prime,2)
mult_three=np.arange(findfirstnumber(min_prime,3),max_prime,3)
mult_five=np.arange(findfirstnumber(min_prime,5),max_prime,5)
mult_seven=np.arange(findfirstnumber(min_prime,7),max_prime,7)
mult_eleven=np.arange(findfirstnumber(min_prime,11),max_prime,11)

res_two = [i for i in all_numbers if i not in mult_two]
res_three = [i for i in res_two if i not in mult_three]
res_five = [i for i in res_three if i not in mult_five]
res_seven = [i for i in res_five if i not in mult_seven]
res_eleven = [i for i in res_seven if i not in mult_eleven]
res_eleven = [i for i in res_eleven if i > min_prime]
prime_list=[i for i in res_eleven if i >= min_prime]

#array elements
timestart=time()
timetotal = 0.0
prime_list_out = [2,3,5,7,11,13]
counter = 14
reps = 0
for i in np.arange(0,len(prime_list)):
    number = 0
    div = 2
    prime_check_true = 'true'
    while number < len(prime_list_out) and prime_check_true == 'true':
        if (counter%div) == 0:
            prime_check_true = 'false'
        div = prime_list_out[number]
        number = number + 1
    if prime_check_true == 'true':
        prime_list_out.append(counter)
    counter = counter + 1
    reps = reps + 1
while prime_list_out[0] < min_prime:
    del prime_list_out[0]
if max_prime < 2:
    prime_list_out = []
timeend=time()
print(prime_list_out)
print('reps: ' + str(counter))
print(len(prime_list_out))
print('')

print(timeend-timestart)