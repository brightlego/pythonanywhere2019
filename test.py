from __future__ import division
import random
import numpy as np
from time import sleep

def tt():
    times_table = input("What times table do you want to know?")
    up_to = input("How far do you want to go?")

    for number in range(up_to+1):
        print(str(times_table),str("x"),str(number),str("="),str((times_table*number)))

def mummy():
    number_3 = input("How many times?")
    for number in range(number_3):
        print("Mummy I love you!")

def mummy2():
    number_3 = input("How many times?")
    for number in range(number_3):
        print("Mummy I love you!")
        print("...and mummy loves John")

def mummy3():
    number_3 = input("How many times?")
    number = 0
    while number < number_3:
        print("Mummy I love you!")
        print("...and mummy loves John")
        number = number + 1

def number_game():
    number = 23
    number_2 = 0
    while number_2 <= number:
        print(number_2)
        number_2 = number_2 + 1

def guess_game():
    print("Easy is between 1 and 10. Normal is between 1 and 15. Hard is in between 1 and 20")
    print(" ")
    gamemode = raw_input("Do you want it to be: easy, normal or hard? ")
    print(" ")
    if gamemode == 'easy':
        a= 10
    if gamemode == 'normal':
        a = 15
    if gamemode == 'hard':
        a = 20
    print("enjoy")
    print("34 lines of code")
    lives = 5
    number_1 = random.randint(1,a)
    guess = 0
    correct = 0
    while lives > 0 and guess != number_1:
        lives = lives - 1
        print(" ")
        guess = input("Guess the number: ")
        if guess == number_1:
            print(" ")
            print(str("You Win. You had ") + str(lives + 1) + str(" guesses left."))
            print(" ")
            correct = 1
        if lives == 0 and correct == 0:
            print(" ")
            print("Game Over. My number was ",number_1)
        print(" ")
        if lives > 0 and correct == 0:
            print(str("that is not my number. You have ") + str(lives) + str(" guesses left"))
            if guess < number_1:
                print("Higher")
            if guess > number_1:
                print("Lower")

def daddy():
        number = 0
        number2 = input("How many times?")
        while number < number2:
            print("Daddy is the best daddy ever!")
            print("Daddy I love you")

def prime_numbers(prime):
#    prime = input("Awating input")
    number2 = prime - 1
    primescore = 1
    while number2 != 1:
        number1 = prime % number2
        number2 = number2 - 1
        if number1 == 0 :
            primescore = 0
#    if primescore == 1:
#        print("This is a prime")
#    else:
#        print("This is not a prime.")
    return(primescore)

def to_100():
        prime = 3
        counter = 2
        number_of_primes = input("how many primes? ")
        print(1)
        print(2)
        while counter <= number_of_primes:
            primescore = prime_numbers(prime)
            if primescore == 1:
                counter = counter + 1
                print(prime)
            prime = prime + 1

def triangle_sides():
    print(" ")
    side_1 = input("What is side 1? ")
    print(" ")
    side_2 = input("what is side 2? ")
    print(" ")
    side_3 = (side_1**2 + side_2**2)**0.5
    print(side_3)

def rps():
    crps = random.randint(1,3)
    cscore = 0
    pscore = 0
    rounds = input("How many rounds? ")
    print(" ")
    while rounds > 0:
        prps = input("Rock(1), Paper(2) or Scissors(3) ")
        print(" ")
        if prps == crps:
            print("It's a Draw")
            print(" ")
            rounds = rounds - 1
        if (prps == 1 and crps == 3) or (prps == 2 and crps == 1) or (prps == 3 and crps == 2):
            print("You Win This Round")
            print(" ")
            rounds = rounds - 1
            pscore = pscore + 1
        if(crps == 1 and prps == 3) or (crps == 2 and prps == 1) or (crps == 3 and prps == 2):
            print("You Lose This Round")
            print(" ")
            rounds = rounds - 1
            cscore = cscore + 1
    if pscore >= cscore:
        if cscore == pscore:
            print("You Draw")
        else:
            print("You Win")
    else:
        print("You Lose")

def list_primes_up_to(numberupto):
    a = 0
    prime = 2
    while prime <= numberupto:
            primescore = prime_numbers(prime)
            if primescore == 1:
                a = np.append(a,prime)
            prime = prime + 1
    return(a[1:len(a)])

def prime_factors(number):
    c = 1
    b = list_primes_up_to(number)
    i = 0
    while i <= len(b)-1:
        if number % b[i] == 0:
            c = np.append(c,b[i])
            number = number / b[i]
            if number % b[i] == 0:
                c = np.append(c,b[i])
                number = number / b[i]
            else:
                i = i+1
        else:
            i = i + 1
    return(c[1:len(c)])

def dice(a=6,b=2):
#    a = input("How many sides? ")
#    b = input("How many dice? ")
    dicescore = 0
    for number in range(b):
        score = random.randint(1,a)
        print(score)
        dicescore = dicescore + score
    print(" ")
    print("The total is...")
    print(dicescore)

def prime_number():
    prime = input("Awating input ")
    number2 = prime - 1
    primescore = 1
    while number2 != 1:
        number1 = prime % number2
        number2 = number2 - 1
        if number1 == 0 :
            primescore = 0
    if primescore == 1:
        print("This is a prime")
    else:
        print("This is not a prime.")
    return(primescore)

def leap_years(year):
    leap_year = 0
    if year % 4 == 0:
        leap_year = 1
    return(leap_year)

def dict_test():
    dict = { 'name' : 'John' , 'age' : '10' , 'class' : '6'};
    print(dict["name"])

class ball:
    def __init__(self,color,size,shape,direction):
        self.color = color
        self.size = size
        self.direction = direction
        self.shape = shape

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

def sleep_test():
    print("1")
    sleep(1)
    print("2")

def random_n_g():
    int_ = 0
    str_ =("")
    nod = input("How many digits? ")
    int_ = random.randint(1,9)
    str_ = str_ + str(int_)
    int_ = 0
    for i in range(1,nod):
        int_ = random.randint(0,9)
        str_ = str_ + str(int_)
        int_ = 0
    print(str_)

def binary_n_g():
    int_ = 0
    str_ =("")
    nod = input("How many digits? ")
    int_ = random.randint(1,1)
    str_ = str_ + str(int_)
    int_ = 0
    for i in range(1,nod):
        int_ = random.randint(0,1)
        str_ = str_ + str(int_)
        int_ = 0
    print(str_)

def hexadecimal_n_g():
    int_ = 0
    str_ =("")
    nod = input("How many digits? ")
    int_ = random.randint(0,15)
    str_ = str_ + str(int_)
    int_ = 0
    for i in range(1,nod):
        int_ = random.randint(0,1)
        str_ = str_ + str(int_)
        int_ = 0
    print(str_)

def guess_game2():
    cnumber = 0
    win = 0
    int_n = random.randint(1,20)
    name = raw_input('What is your name? ')
    print('Welcome ' + str(name) + '. I hope you like my second atemt at making a guessing game.')
    print('')
    while cnumber == 0:
        print 'Press 0 to cancel.'
        amount = input('Now, do you want to have 3, 5 or 10 guesses for a random number from 1 to 20?')
        print ('')
        if amount == 3 or amount == 5 or amount == 10 or amount == 100 or amount == 3005364:
            while amount > 0 and win == 0 and amount != 100 and amount != 3005364:
                int_guess = input ('What is your  guess? ')
                print ''
                if int_guess != int_n:
                    amount = amount - 1
                    if int_guess > int_n:
                        print'Your guess is a bit too high. You have ' + str(amount) + ' guesses left.'
                    elif int_guess < int_n:
                        print'Your guess is a bit too low. You have' + str (amount) + ' guesses left.'
                    print ''
                else:
                    print(' You win! You had ' + str (amount) + ' guesses left.')
                    win = 1
            if amount == 0:
                print 'You lost. Bad luck. The number was ' + str(int_n) + '.'
            if amount == 100:
                print 'How funny'
                print ''
                amount == -1
                cnumber = 0
            if amount == 3005364:
                print "Congrats. You have earnd the 'Random Numbers' achevement."
                cnumber = 1
        if amount == 0:
            cnumber = 1
        elif amount != 0:
            cnumber = 1
            print 'Try again'
            print ''




def Rand_base (b):
    b = b-1
    i = int(input('How many digits?'))
    answer = ''
    while i > 0:

        a = str(random.randint(0,b))
        answer = answer + a
        i = i-1
    print(answer)

def onefinder (onetobe):
    onecounter = 1
    while onetobe != 1:
        if onetobe%2 == 1:
            onetobe = (onetobe*3)+1
        else:
            onetobe = onetobe/2
        onecounter = onecounter + 1
    print 'One found in ' + str(onecounter) + ' steps.'







