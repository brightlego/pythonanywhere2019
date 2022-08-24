import numpy as np
import random

turn_n = -2
name1 = raw_input("What is the Player's  name? ")
name1 = 'John'
print ''
difficulty = 0
while difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != '1' and difficulty != '2' and difficulty != '3':
    difficulty = input('How hard do you want the AI to be? (1 for easy, 2 for medium and 3 for hard) ')
#    print difficulty

while turn_n < -1:
    turnstart = raw_input('Do you want to be X (1st) or O (2nd)? ')
    if turnstart == 'X' or turnstart == 'x':
        turn_n = 0
    elif turnstart == 'O' or turnstart == 'o':
        turn_n = -1
A1 = ' '
A2 = ' '
A3 = ' '
B1 = ' '
B2 = ' '
B3 = ' '
C1 = ' '
C2 = ' '
C3 = ' '
clamedA1 = 0
clamedA2 = 0
clamedA3 = 0
clamedB1 = 0
clamedB2 = 0
clamedB3 = 0
clamedC1 = 0
clamedC2 = 0
clamedC3 = 0



def AI(A1,A2,A3,B1,B2,B3,C1,C2,C3):
    if difficulty == 1:
        smallpriority = random.randint(-2,1)
        mediumpriority = random.randint(-4,8)
        highpriority = random.randint(-4,4)
        blockedpriority = 0
    elif difficulty == 2:
        smallpriority = 1
        mediumpriority = random.randint(2,8)
        highpriority = random.randint(2,8)
        blockedpriority = 0
    elif difficulty == 3:
        smallpriority = int(np.load('small_priority_o.npy'))
        mediumpriority = int(np.load('medium_priority_o.npy'))+15
        highpriority = int(np.load('high_priority_o.npy'))
        blockedpriority = int(np.load('blocked.npy'))
    gridlist = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    flaggedA1 = 0
    flaggedA2 = 0
    flaggedA3 = 0
    flaggedB1 = 0
    flaggedB2 = 0
    flaggedB3 = 0
    flaggedC1 = 0
    flaggedC2 = 0
    flaggedC3 = 0
    if A1 == 'O':
        flaggedA2 = flaggedA2+blockedpriority
        flaggedA3 = flaggedA3+blockedpriority
        flaggedB1 = flaggedB1+blockedpriority
        flaggedB2 = flaggedB2+blockedpriority
        flaggedC1 = flaggedC1+blockedpriority
        flaggedC3 = flaggedC3+blockedpriority
    if A2 == 'O':
        flaggedA1 = flaggedA1+blockedpriority
        flaggedA3 = flaggedA3+blockedpriority
        flaggedB2 = flaggedB2+blockedpriority
        flaggedC2 = flaggedC2+blockedpriority
    if A3 == 'O':
        flaggedA2 = flaggedA2+blockedpriority
        flaggedA1 = flaggedA1+blockedpriority
        flaggedB2 = flaggedB2+blockedpriority
        flaggedB3 = flaggedB3+blockedpriority
        flaggedC1 = flaggedC1+blockedpriority
        flaggedC3 = flaggedC3+blockedpriority
    if B1 == 'O':
        flaggedA1 = flaggedA1+blockedpriority
        flaggedB2 = flaggedB2+blockedpriority
        flaggedB3 = flaggedB3+blockedpriority
        flaggedC1 = flaggedC1+blockedpriority
    if B2 == 'O':
        flaggedA2 = flaggedA2+blockedpriority
        flaggedA3 = flaggedA3+blockedpriority
        flaggedB1 = flaggedB1+blockedpriority
        flaggedA1 = flaggedA1+blockedpriority
        flaggedB3 = flaggedB3+blockedpriority
        flaggedC1 = flaggedC1+blockedpriority
        flaggedC2 = flaggedC2+blockedpriority
        flaggedC3 = flaggedC3+blockedpriority
    if B3 == 'O':
        flaggedA3 = flaggedA3+blockedpriority
        flaggedB1 = flaggedB1+blockedpriority
        flaggedB2 = flaggedB2+blockedpriority
        flaggedC3 = flaggedC3+blockedpriority
    if C1 == 'O':
        flaggedA3 = flaggedA3+blockedpriority
        flaggedB1 = flaggedB1+blockedpriority
        flaggedB2 = flaggedB2+blockedpriority
        flaggedA1 = flaggedA1+blockedpriority
        flaggedC2 = flaggedC2+blockedpriority
        flaggedC3 = flaggedC3+blockedpriority
    if C2 == 'O':
        flaggedA2 = flaggedA2+blockedpriority
        flaggedB2 = flaggedB2+blockedpriority
        flaggedC1 = flaggedC1+blockedpriority
        flaggedC3 = flaggedC3+blockedpriority
    if C3 == 'O':
        flaggedA3 = flaggedA3+blockedpriority
        flaggedB2 = flaggedB2+blockedpriority
        flaggedB3 = flaggedB3+blockedpriority
        flaggedC1 = flaggedC1+blockedpriority
        flaggedC2 = flaggedC2+blockedpriority
        flaggedA1 = flaggedA1+blockedpriority

    if A1 == 'X':
        flaggedA2 = flaggedA2+smallpriority
        flaggedA3 = flaggedA3+smallpriority
        flaggedB1 = flaggedB1+smallpriority
        flaggedB2 = flaggedB2+smallpriority
        flaggedC1 = flaggedC1+smallpriority
        flaggedC3 = flaggedC3+smallpriority
    if A2 == 'X':
        flaggedA1 = flaggedA1+smallpriority
        flaggedA3 = flaggedA3+smallpriority
        flaggedB2 = flaggedB2+smallpriority
        flaggedC2 = flaggedC2+smallpriority
    if A3 == 'X':
        flaggedA2 = flaggedA2+smallpriority
        flaggedA1 = flaggedA1+smallpriority
        flaggedB2 = flaggedB2+smallpriority
        flaggedB3 = flaggedB3+smallpriority
        flaggedC1 = flaggedC1+smallpriority
        flaggedC3 = flaggedC3+smallpriority
    if B1 == 'X':
        flaggedA1 = flaggedA1+smallpriority
        flaggedB2 = flaggedB2+smallpriority
        flaggedB3 = flaggedB3+smallpriority
        flaggedC1 = flaggedC1+smallpriority
    if B2 == 'X':
        flaggedA2 = flaggedA2+smallpriority
        flaggedA3 = flaggedA3+smallpriority
        flaggedB1 = flaggedB1+smallpriority
        flaggedA1 = flaggedA1+smallpriority
        flaggedB3 = flaggedB3+smallpriority
        flaggedC1 = flaggedC1+smallpriority
        flaggedC2 = flaggedC2+smallpriority
        flaggedC3 = flaggedC3+smallpriority
    if B3 == 'X':
        flaggedA3 = flaggedA3+smallpriority
        flaggedB1 = flaggedB1+smallpriority
        flaggedB2 = flaggedB2+smallpriority
        flaggedC3 = flaggedC3+smallpriority
    if C1 == 'X':
        flaggedA3 = flaggedA3+smallpriority
        flaggedB1 = flaggedB1+smallpriority
        flaggedB2 = flaggedB2+smallpriority
        flaggedA1 = flaggedA1+smallpriority
        flaggedC2 = flaggedC2+smallpriority
        flaggedC3 = flaggedC3+smallpriority
    if C2 == 'X':
        flaggedA2 = flaggedA2+smallpriority
        flaggedB2 = flaggedB2+smallpriority
        flaggedC1 = flaggedC1+smallpriority
        flaggedC3 = flaggedC3+smallpriority
    if C3 == 'X':
        flaggedA3 = flaggedA3+smallpriority
        flaggedB2 = flaggedB2+smallpriority
        flaggedB3 = flaggedB3+smallpriority
        flaggedC1 = flaggedC1+smallpriority
        flaggedC2 = flaggedC2+smallpriority
        flaggedA1 = flaggedA1+smallpriority
    if A1 == B1 and A1 == 'X':
        flaggedC1 = flaggedC1+mediumpriority
    if A1 == C1 and A1 == 'X':
        flaggedB1 = flaggedB1+mediumpriority
    if A1 == A2 and A1 == 'X':
        flaggedA3 = flaggedA3+mediumpriority
    if A1 == A3 and A1 == 'X':
        flaggedA2 = flaggedA2+mediumpriority
    if A1 == B2 and A1 == 'X':
        flaggedC3 = flaggedC3+mediumpriority
    if A1 == C3 and A1 == 'X':
        flaggedB2 = flaggedB2+mediumpriority
    if A2 == A3 and A2 == 'X':
        flaggedA1 = flaggedA1+mediumpriority
    if B1 == C1 and B1 == 'X':
        flaggedA1 = flaggedA1+mediumpriority
    if B2 == C3 and B2 == 'X':
        flaggedA1 = flaggedA1+mediumpriority
    if A2 == B2 and A2 == 'X':
        flaggedC2 = flaggedC2+mediumpriority
    if A2 == C2 and A2 == 'X':
        flaggedB2 = flaggedB2+mediumpriority
    if B2 == C2 and B2 == 'X':
        flaggedA2 = flaggedA2+mediumpriority
    if A3 == B3 and A3 == 'X':
        flaggedC3 = flaggedC3+mediumpriority
    if A3 == C3 and A3 == 'X':
        flaggedB3 = flaggedB3+mediumpriority
    if B3 == C3 and B3 == 'X':
        flaggedA3 = flaggedA3+mediumpriority
    if B1 == B2 and B2 == 'X':
        flaggedB3 = flaggedB3+mediumpriority
    if B1 == B3 and B1 == 'X':
        flaggedB2 = flaggedB2+mediumpriority
    if B2 == B3 and B2 == 'X':
        flaggedB1 = flaggedB1+mediumpriority
    if C1 == C2 and C2 == 'X':
        flaggedC3 = flaggedC3+mediumpriority
    if C1 == C3 and C1 == 'X':
        flaggedC2 = flaggedC2+mediumpriority
    if C2 == C3 and C2 == 'X':
        flaggedC1 = flaggedC1+mediumpriority
    if C1 == B2 and C1 == 'X':
        flaggedA3 = flaggedA3+mediumpriority
    if B2 == A3 and B2 == 'X':
        flaggedC1 = flaggedC1+mediumpriority
    if C1 == A3 and C1 == 'X':
        flaggedB2 = flaggedB2+mediumpriority

    if A1 == B1 and A1 == 'O':
        flaggedC1 = flaggedC1+highpriority
    if A1 == C1 and A1 == 'O':
        flaggedB1 = flaggedB1+highpriority
    if A1 == A2 and A1 == 'O':
        flaggedA3 = flaggedA3+highpriority
    if A1 == A3 and A1 == 'O':
        flaggedA2 = flaggedA2+highpriority
    if A1 == B2 and A1 == 'O':
        flaggedC3 = flaggedC3+highpriority
    if A1 == C3 and A1 == 'O':
        flaggedB2 = flaggedB2+highpriority
    if A2 == A3 and A2 == 'O':
        flaggedA1 = flaggedA1+highpriority
    if B1 == C1 and B1 == 'O':
        flaggedA1 = flaggedA1+highpriority
    if B2 == C3 and B2 == 'O':
        flaggedA1 = flaggedA1+highpriority
    if A2 == B2 and A2 == 'O':
        flaggedC2 = flaggedC2+highpriority
    if A2 == C2 and A2 == 'O':
        flaggedB2 = flaggedB2+highpriority
    if B2 == C2 and B2 == 'O':
        flaggedA2 = flaggedA2+highpriority
    if A3 == B3 and A3 == 'O':
        flaggedC3 = flaggedC3+highpriority
    if A3 == C3 and A3 == 'O':
        flaggedB3 = flaggedB3+highpriority
    if B3 == C3 and B3 == 'O':
        flaggedA3 = flaggedA3+highpriority
    if B1 == B2 and B2 == 'O':
        flaggedB3 = flaggedB3+highpriority
    if B1 == B3 and B1 == 'O':
        flaggedB2 = flaggedB2+highpriority
    if B2 == B3 and B2 == 'O':
        flaggedB1 = flaggedB1+highpriority
    if C1 == C2 and C2 == 'O':
        flaggedC3 = flaggedC3+highpriority
    if C1 == C3 and C1 == 'O':
        flaggedC2 = flaggedC2+highpriority
    if C2 == C3 and C2 == 'O':
        flaggedC1 = flaggedC1+highpriority
    if C1 == B2 and C1 == 'O':
        flaggedA3 = flaggedA3+highpriority
    if B2 == A3 and B2 == 'O':
        flaggedC1 = flaggedC1+highpriority
    if C1 == A3 and C1 == 'O':
        flaggedB2 = flaggedB2+highpriority


    flaggedlist = [flaggedA1,flaggedA2,flaggedA3,flaggedB1,flaggedB2,flaggedB3,flaggedC1,flaggedC2,flaggedC3]

    zippedup = zip(flaggedlist,gridlist)
    prioritisedtile = sorted(zippedup)
    return(prioritisedtile)


def board(A1,A2,A3,B1,B2,B3,C1,C2,C3):
    print '''
      1 | 2 | 3
    A|''' + A1 + ' | ' + A2 + ' | ' + A3 +'''
    B|''' + B1 + ' | ' + B2 + ' | ' + B3 +'''
    C|''' + C1 + ' | ' + C2 + ' | ' + C3

def win_(A1,A2,A3,B1,B2,B3,C1,C2,C3,win):
    if A1 == A2 and A2 == A3:
        if A1 == 'X':
            win = 1
        elif A1 == 'O':
            win = 2
        else:
            win = 0
    elif A1 == B1 and B1 == C1:
        if A1 == 'X':
            win = 1
        elif A1 == 'O':
            win = 2
        else:
            win = 0
    elif A1 == B2 and B2 == C3:
        if A1 == 'X':
            win = 1
        elif A1 == 'O':
            win = 2
        else:
            win = 0
    elif A2 == B2 and B2 == C2:
        if A2 == 'X':
            win = 1
        elif A2 == 'O':
            win = 2
        else:
            win = 0
    elif A3 == B3 and B3 == C3:
        if A3 == 'X':
            win = 1
        elif A3 == 'O':
            win = 2
        else:
            win = 0
    elif A3 == B2 and B2 == C1:
        if A3 == 'X':
            win = 1
        elif A3 == 'O':
            win = 2
        else:
            win = 0
    elif B1 == B2 and B2 == B3:
        if B1 == 'X':
            win = 1
        elif B1 == 'O':
            win = 2
        else:
            win = 0
    elif C1 == C2 and C2 == C3:
        if C1 == 'X':
            win = 1
        elif C1 == 'O':
            win = 2
        else:
            win = 0
    return(win)

win  = 0
turn = 'X'
turn_n = 0
win = 0
while win == 0:
    correctimput = 0
    try_ = 1
    turn_n = turn_n + 1
    while correctimput == 0 and win == 0:
        for i in range(0,55):
            print ''

        if (turn_n%2) == 1:
            turn = 'X'
            print name1 + "'s turn."
        else:
            desired_tile_zip = sorted(AI(A1,A2,A3,B1,B2,B3,C1,C2,C3))
#            print desired_tile_zip
            turn = 'O'
            print "AI's turn."
        if turnstart == turn and turn_n != 1:
            print 'The AI picked ' + AI_tile + '.'
        board(A1,A2,A3,B1,B2,B3,C1,C2,C3)
        if turnstart == turn:
            desired_tile = raw_input('What tile do you want to change? ')
        else:
            length = 0
            same_priority = 8
            while length == 0:
                if desired_tile_zip[9-try_][0] == desired_tile_zip[9-same_priority-try_][0]:
                    randomtile = random.randint(8-same_priority-try_,8-try_)
#                    print randomtile
                    desired_tile = desired_tile_zip[randomtile+1][1]
                    length = 1
                    AI_tile = desired_tile
#                    print desired_tile
                else:
                    same_priority = same_priority - 1
            if turn == 0:
                desired_tile = 'B2'
#        print clamedA1, 'clamed A1'
#        print clamedA2, 'clamed A2'
#        print clamedA3, 'clamed A3'
#        print clamedB1, 'clamed B1'
#        print clamedB2, 'clamed B2'
#        print clamedB3, 'clamed B3'
#        print clamedC1, 'clamed C1'
#        print clamedC2, 'clamed C2'
#        print clamedC3, 'clamed C3'

        if desired_tile == 'A1' and clamedA1 == 0:
            A1 = turn
            correctimput = 1
            clamedA1 = 1
        elif desired_tile == 'A2' and clamedA2 == 0:
            A2 = turn
            correctimput = 1
            clamedA2 = 1
        elif desired_tile == 'A3' and clamedA3 == 0:
            A3 = turn
            correctimput = 1
            clamedA3 = 1
        elif desired_tile == 'B1' and clamedB1 == 0:
            B1 = turn
            correctimput = 1
            clamedB1 = 1
        elif desired_tile == 'B2' and clamedB2 == 0:
            B2 = turn
            correctimput = 1
            clamedB2 = 1
        elif desired_tile == 'B3' and clamedB3 == 0:
            B3 = turn
            correctimput = 1
            clamedB3 = 1
        elif desired_tile == 'C1' and clamedC1 == 0:
            C1 = turn
            correctimput = 1
            clamedC1 = 1
        elif desired_tile == 'C2' and clamedC2 == 0:
            C2 = turn
            correctimput = 1
            clamedC2 = 1
        elif desired_tile == 'C3' and clamedC3 == 0:
            C3 = turn
            correctimput = 1
            clamedC3 = 1
        else:
            correctimput = 0
        if A1 != ' ' and B1 != ' ' and C1 != ' ' and A2 != ' ' and B2 != ' ' and C2 != ' ' and A3 != ' ' and B3 != ' ' and C3 != ' ':
            win = 3
        try_ = try_ + 1
#        print try_
#        print correctimput, 'correct input'
    win = win_(A1,A2,A3,B1,B2,B3,C1,C2,C3,win)

for i in range(1,55):
    print ''
board(A1,A2,A3,B1,B2,B3,C1,C2,C3)
if (win == 1 and turnstart == 'X') or (win == 2 and turnstart == 'O'):
    print name1 + " won!"
elif (win == 1 and turnstart == 'O') or (win == 2 and turnstart == 'X'):
    print "The AI won!"
elif win == 3:
    print "It's a draw!"


