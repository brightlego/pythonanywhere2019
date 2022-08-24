name1 = raw_input("What is Player 1's  name? ")
name2 = raw_input("What is Player 2's  name? ")
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
correctimput = 0
while win == 0:
    for i in range(0,50):
        print ''
    turn_n = turn_n + 1
    if (turn_n%2) == 1:
        turn = 'X'
        print name1 + "'s turn."
    else:
        turn = 'O'
        print name2 + "'s turn."
    correctimput = 0
    while correctimput == 0 and win == 0:
        board(A1,A2,A3,B1,B2,B3,C1,C2,C3)
        desired_tile = raw_input('What tile do you want to change? ')
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
        if A1 != ' ' and B1 != ' ' and C1 != ' ' and A2 != ' ' and B2 != ' ' and C2 != ' ' and A3 != ' ' and B3 != ' ' and C3 != ' ':
            win = 3
    win = win_(A1,A2,A3,B1,B2,B3,C1,C2,C3,win)

for i in range(1,55):
    print ''
board(A1,A2,A3,B1,B2,B3,C1,C2,C3)
if win == 1:
    print name1 + " won!"
elif win == 2:
    print name2 + " won!"
elif win == 3:
    print "It's a draw!"


