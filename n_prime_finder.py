desired_number = int(input('What is your desired prime? '))
number = 2
prime = desired_number
possible_prime = 2
while number <= desired_number:
    div = int(prime/2)+1
    prime_check = 0
    while div > 1 and prime_check == 0:
        if int(prime)/(div) == float(prime)/float(div):
            prime_check = 1
        div = div - 1
    if prime_check == 0:
        possible_prime = prime
        number = number + 1
    prime = prime + 1
print(possible_prime)