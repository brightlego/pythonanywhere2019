import numpy as np
import random

difficulty = 4
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

smallpriority_1 = int(np.load('small_priority_o.npy'))
mediumpriority_1 = int(np.load('medium_priority_o.npy'))
highpriority_1 = int(np.load('high_priority_o.npy'))
blockedpriority_1 = int(np.load('blocked.npy'))

smallpriority_2 = random.randint((int(np.load('small_priority_o.npy'))-10),(int(np.load('small_priority_o.npy'))+10))
mediumpriority_2 = random.randint((int(np.load('medium_priority_o.npy'))-10),(int(np.load('medium_priority_o.npy'))+10))
highpriority_2 = random.randint((int(np.load('high_priority_o.npy'))-10),(int(np.load('high_priority_o.npy'))+10))
blockedpriority_2 = random.randint((int(np.load('blocked.npy'))-10),(int(np.load('blocked.npy'))+10))

def AI(A1,A2,A3,B1,B2,B3,C1,C2,C3,turn):
    if turn == 'X':
        smallpriority = smallpriority_1
        mediumpriority = mediumpriority_1
        highpriority = highpriority_1
        blockedpriority = blockedpriority_1
    elif turn == 'O':
        smallpriority = smallpriority_2
        mediumpriority = mediumpriority_2
        highpriority = highpriority_2
        blockedpriority = blockedpriority_2
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
    while correctimput == 0 and win == 0 and try_ < 9:
        if (turn_n%2) == 1:
            desired_tile_zip = sorted(AI(A1,A2,A3,B1,B2,B3,C1,C2,C3,'X'))
            turn = 'X'
        else:
            desired_tile_zip = sorted(AI(A1,A2,A3,B1,B2,B3,C1,C2,C3,'O'))
            turn = 'O'
        length = 0
        same_priority = 8
        while length == 0:
            if desired_tile_zip[9-try_][0] == desired_tile_zip[9-same_priority-try_][0]:
                randomtile = random.randint(8-same_priority-try_,8-try_)
                desired_tile = desired_tile_zip[randomtile+1][1]
                length = 1
                AI_tile = desired_tile
            else:
                same_priority = same_priority - 1
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
    win = win_(A1,A2,A3,B1,B2,B3,C1,C2,C3,win)
if win == 2:
    np.save('small_priority_o',np.array([[smallpriority_2]]))
    np.save('medium_priority_o',np.array([[mediumpriority_2]]))
    np.save('high_priority_o',np.array([[highpriority_2]]))
    np.save('blocked',np.array([[blockedpriority_2]]))


