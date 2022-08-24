import matplotlib.pyplot as plt
import random

def guessanumber():
    number = random.randint(1,10)
    guess = makeguess()
    while guess != number:
        print("Try again")
        guess = makeguess()
    print("You win")

def makeguess():
    guess = int(raw_input('Guess a number '))
    return(guess)

def makeplot(gameresults):
    fig = plt.figure()
    plt.plot(gameresults)
    plt.xlabel('Attempt number')
    plt.ylabel('Guess')
    fig.savefig('graph.png')
