from time import time
prime = input('Minimum Number? ')
#prime = 2
#max_prime = 10000
if prime <= 1:
    prime = 2
max_prime = input('Maximum Number? ')

prime_list = [2]
counter = 2
timestart=time()
for i in xrange(1,max_prime):
    number = 0
    div = 2
    prime_check = True
    while number < len(prime_list) and prime_check:
        if (counter%div) == 0:
            prime_check = False
        div = prime_list[number]
        number = number + 1
    if prime_check:
        prime_list = prime_list + [counter]
    counter = counter + 1
while prime_list[0] < prime:
    del prime_list[0]
if max_prime < 2:
    prime_list = []
timeend=time()
print(prime_list)
print('Length: ' + str(len(prime_list)))
print('')
print(timeend-timestart)