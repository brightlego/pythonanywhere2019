import random
import numpy as np
mode = ''
words_ = list(np.load('Words.npy'))[0].splitlines()
def cs():
    for i in range(0,60):
        print('')
def drawer(lives):
    drawing = [
    '','''
----------
    ''','''
|
|
|
|
|
|
----------
    ''','''
|
|
|
|
|
|\\
----------
    ''','''
|-----
|
|
|
|
|\\
----------
    ''','''
|-----
|/
|
|
|
|\\
----------
    ''','''
|-----
|/   |
|
|
|
|\\
----------
    ''','''
|-----
|/   |
|    O
|
|
|\\
----------
    ''','''
|-----
|/   |
|    O
|    |
|
|\\
----------
    ''','''
|-----
|/   |
|    O
|   /|
|
|\\
----------
    ''','''
|-----
|/   |
|    O
|   /|\\
|
|\\
----------
    ''','''
|-----
|/   |
|    O
|   /|\\
|   /
|\\
----------
    ''','''
|-----
|/   |
|    O
|   /|\\
|   / \\
|\\
----------
    ''']
    print(drawing[lives])


guessed_word_str = ''

successful_guess = 0
while mode != 'singleplayer' and mode != 'multiplayer':
    mode = raw_input('Singleplayer or multiplayer? ').lower()
if mode == 'multiplayer':
    name1 = raw_input('Player 1, what is your name? ')
    name2 = raw_input('Player 2, what is your name? ')
    cs()
    word_ = raw_input(name1+' what word do you want to pick? ')
else:
    name2 = raw_input('What is your name? ')
    word_ = words_[random.randint(0,len(words_)-1)]

word = word_.upper()
words = word
words = words.split()
lwords = []
for i in range(0,len(words)):
    lwords.append(list(words[i]))
    lwords.append('/')
cs()
word = word.replace(' ','/')
lword = list(word)
guessed_word = []
for i in range(0,len(lword)):
    if lword[i] != '/':
        guessed_word.append('_')
    else:
        guessed_word.append('/')

win = 0
lives = 12
guessed_letters = ''
while win == 0 and lives > 0:
    p = 0
    guessed_word_str = ''
    for i in range(0,len(guessed_word)):
        guessed_word_str = guessed_word_str + ' ' + guessed_word[i]
    print('')
    drawer(12-lives)
    print('Guessed letters: ' + guessed_letters)
    print('Guessed word: ' + guessed_word_str)
    c = 1
    successful_guess = 0
    while successful_guess == 0:
        letter = raw_input(name2 + ', what do you want to guess? ')
        letter = letter.upper()
        if letter in guessed_letters:
            print('You already picked that.')
            print('')
        else:
            successful_guess = 1

    if letter in word:
        if len(letter) > 1:
            for i in range(0,len(lwords)):
                p = 0
                if list(letter) == lwords[i]:
                    if i > 0:
                        for j in range(0,i):
                            p = p + len(lwords[j])
                    for k in range(0,len(letter)):
                        guessed_word[p+k] = letter[k]
        else:
            for i in range(0,len(word)):
                if word[i] == letter:
                    guessed_word[i] = letter
        cs()
    else:
        guessed_letters = guessed_letters + ' ' + letter
        lives = lives-1
        cs()
        print(letter + ' is not in ' + guessed_word_str)
    if guessed_word == lword:
        win = 1
        cs()
        print(name2 + ' correctly guessed ' + word_ + '!')
if lives == 0:
    drawer(12)
    print(name2 + ' did not manage to guess ' + word_ + '!')

