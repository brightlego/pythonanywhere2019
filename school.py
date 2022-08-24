import random
from time import sleep
import math

def clock():
    hour = 0
    minute = 0
    second = 0
    time = 0
    wait_time = input("How long do you want to wait? ")
    while wait_time != time:
        if second < 59:
            sleep(1)
            second = second + 1
        elif second == 59:
            sleep(1)
            second = 0
            if minute != 50:
                minute = minute + 1
            elif minute == 59:
                hour = hour + 1
        print(str(hour) + str(" : ") + str(minute) + str(" : ") + str(second))
        time = time + 1

def dice():
    number = input("How many dice? ")
    print("")
    sides = input("How many sides? ")
    print("")
    dicescore = 0
    for i in range(number):
        dicescore = dicescore + random.randint(1,sides)
    print(dicescore)

def calcuator():
    answer = 0
    asdm = input("Do you want to add, subtract, times or divide? ")
    if asdm == 1 or 2 or 3 or 4:
        number1 = input("What do you want your first number to be? ")
        number2 = input("What do you want your second number to be? ")
        if asdm == 1:
            answer = number1 + number2
            print(answer)
        elif asdm == 2:
            answer = number1 - number2
            print(answer)
        elif asdm == 3:
            answer = number1 * number2
            print(answer)
        elif asdm == 4:
            answer = number1 / number2
            print(answer)
        else:
            print("ERROR")
    else:
        print("ERROR")

def snakes_ladders():
    tile1 = 0
    tile2 = 0
    win = 0
    turn = 1
    continue_ = 1
    dicescore = 0
    dict = {1 : 38, 2 : 2, 3 : 3, 4 : 14, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 31, 10 : 10, 11 : 11, 12 : 12, 13 : 13, 14 : 14, 15 : 15, 16 : 16, 17 : 7, 18 : 18,
    19 : 19, 20 : 20, 21 : 42, 22 : 22, 23 :23, 24 : 24, 25 : 25, 26 : 26, 27 : 27, 28 : 84, 29 : 29, 30 : 30, 31 : 31, 32 : 32, 33 : 33, 34 : 34, 35 : 35,
    36 : 36, 37 : 37, 38 : 38, 39 : 39, 40 : 40, 41 : 41, 42 : 42, 43 : 43, 44 : 44, 45 : 45, 46 : 46, 47 : 47, 48 : 48, 49 : 49, 50 : 50, 51 : 67, 52 : 52,
    53 : 53, 54 : 34, 55 : 55, 56 : 56, 57 : 57, 58 : 58, 59 : 59, 60 : 60, 61 : 61, 62 : 62, 63 : 63, 64 : 60, 65 : 65, 66 : 66, 67 : 67, 68 : 68, 69 : 69,
    70 : 70, 71 : 91, 72 : 72, 73 : 73, 74 : 74, 75 : 75, 76 : 76, 77 : 77, 78 : 78, 79 : 79, 80 : 100, 81 : 81, 82 : 82, 83 : 83, 84 : 84, 85 : 85, 86 : 86,
    87 : 24, 88 : 88, 89 : 89, 90 : 90, 91 : 91, 92 : 92, 93 : 73, 94 : 94, 95 : 75, 96 : 96, 97 : 97, 98 : 79, 99 : 99, 100 : 100, 101 : 101, 102 : 102,
    103 : 103, 104 : 104, 105 : 105, 106 : 106, 107 : 107, 108 : 108, 109 : 109, 110 : 110, 111 : 111, 112 : 112};
    player1 = player(tile1,"player1")
    player2 = player(tile1,"player2")
    player1.name = raw_input("Who is player 1? ")
    player2.name = raw_input("Who is player 2? ")
    while continue_ == 1 and win == 0:
        if turn == 1:
            tile1 = player1.tile
            print(player1.name + "'s turn")
            print("")
        elif turn == 2:
            tile1 = player2.tile
            print(player2.name + "'s turn")
            print("")
        for i in range(2):
            dicescore = dicescore + random.randint(1,6)
        tile1 = tile1 + dicescore
        print("You roled a " + str(dicescore))
        print("")
        tile2 = dict[tile1]
        print("You are on tile " + str(tile1))
        if tile1 > tile2:
            print("You slid down a snake.")
            print("You are now on tile " + str(tile2))
        elif tile1 < tile2:
            print("You climed up a ladder.")
            print("You are now on tile " + str(tile2))
        print("")
        if turn == 1 and tile2 >= 100:
            win = 1
        elif turn == 2 and tile2 >= 100:
            win = 2
        if turn == 1:
            player1.tile = tile2
            turn = 2
        elif turn == 2:
            player2.tile = tile2
            turn = 1
        dicescore = 0
        continue_ = input("Do you want to continue? ")
        print("")
    if win == 1:
        print(player1.name + " Wins")
    elif win == 2:
        print(player2.name +" Wins")



class player:
    def __init__(self,tile,name):
        self.tile = tile
        self.name = name

def cristmass_tree():
    print("""

                                        ^^
                                       <**>
                                        ||
                                        ==
                                       ####
                                      =o==o=
                                     ########
                                    ==o==o==o=
                                   ############
                                  =o==o==o==o==o
                                 ################
                                o==o==o==o==o==o==
                               ####################
                              ==o==o==o==o==o==o==o=
                                        ||
                                        ||
                                     ___||___
                                     \/\/\/\/
                                      \____/


                              Merry Christmass and a
                                  Happy New Year.                                                                                           """)


def tri_angle():
    a1 = input('What is the first angle? ')
    a2 = input('What is the second angle? ')
    a3 = 180 - (a1 + a2)
    print(str('the third angle is ') + str(a3) + str('.'))

def python_agoras():
    a = input("What is length a? ")
    b = input("What is length b? ")
    c = math.sqrt((a*a)+(b*b))
    print(str('Lenghth c is ') + str(c) + str('.'))
