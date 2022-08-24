def cs():
    for i in range(0,60):
        print('')

def board(blist):
    bstr = ' '
    for i in range(0,size*2):
        for j in range(0,size*2-1):
            bstr = bstr + blist[i][j]
        bstr = bstr + '\n'
    print(bstr)

def drawline(ilist,blist,alphabet,size):
    cinput = 0
    coords = [[],[]]
    if len(ilist[0]) != 2 or len(ilist[1]) !=2:
        return([blist,0])
    for i in range(0,2):
        for j in range(0,len(alphabet)):
            for k in range(0,size+1):
                if ilist[i][0] == alphabet[j] and ilist[i][1] == str(k):
                    cinput = cinput + 1
                else:
                    cinput = cinput + 0
    if cinput == 0:
        return([blist,cinput])
    for i in range(0,2):
        coords[i].append(int(ilist[i][1]))
        coords[i].append(alphabet.index(ilist[i][0]))
    if coords[0][0] == coords[1][0] and (coords[0][1] == coords[1][1]+1 or coords[0][1] == coords[1][1]-1):
        line = '--'
    elif coords[0][1] == coords[1][1] and (coords[0][0] == coords[1][0]+1 or coords[0][0] == coords[1][0]-1):
        line = '|'
    else:
        return([blist,0])
    if coords[1][0] < coords[0][0] or coords[1][1] < coords[0][1]:
        coords.reverse()
    if line == '--' and blist[coords[0][0]*2-1][coords[0][1]*2+1] != line:
        blist[coords[0][0]*2-1][coords[0][1]*2+1] = line
    elif line == '|':
        if coords[0][1] == 0:
            start = '  '
        else:
            start = ''
        if blist[coords[0][0]*2][coords[0][1]*2] != start + line:
            blist[coords[0][0]*2][coords[0][1]*2] = start + line
        else:
            return([blist,0])
    else:
        return([blist,0])
    return([blist,cinput])

def isbox(blist,size,name,turn,scores):
    pinput = 1
    for i in range(1,(size)):
        for j in range(1,(size)):
            if blist[2*i-1][2*j-1] == '--':
                if blist[2*i+1][2*j-1] == '--':
                    if (blist[2*i][2*j-2] == '|' or blist[2*i][2*j-2] == '  |'):
                        if blist[2*i][2*j] == '|':
                            if blist[2*i][2*j-1] == '  ':
                                blist[2*i][2*j-1] = name[turn][0] + ' '
                                scores[turn] = scores[turn] + 1
                                pinput = 0
    return([blist,scores,pinput])

def iswin(size,scores,name,pinput):
    tscore = 0
    for i in range(0,len(scores)):
        tscore = tscore + scores[i]
    if tscore == (size-1)**2:
        name_score = zip(scores,name)
        name_score.sort()
        name_score.reverse()
        i = 0
        winners = ''
        if scores[0] == scores[len(scores)-1]:
            print("It's a Draw!")
            return([1,1])
        while name_score[0][0] == name_score[i][0]:
            if len(winners) > 0:
                winners = winners + ', ' + name_score[i][1]
            else:
                winners = winners + name_score[i][1]
            i = i+1
        print(winners + ' won!')
        return([1,1])
    else:
        return([0,pinput])



alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
name = []
scores = []
nname = input('How many players do you want? ')
for i in range(0,nname):
    name1 = raw_input('What is your name, player ' + str(i+1) + '? ')
    name.append(name1)
    scores.append(0)
size = input('How big do you want the board to be? ')
cs()
for i in range(0,(size-size%26)/26):
    if 26*i < size:
        for j in range(0,26):
            alphabet = alphabet + [alphabet[i]+alphabet[j]]
blist = [[]]
for i in range(0,size):
    blist[0] = blist[0] + [alphabet[i]] + ['  ']
blist[0][0] = ' '+ blist[0][0]
blist = blist + [['1 *','  ']]
for i in range(1,size*2+1):
    for j in range(0,size):
        if i % 2 == 1:
            if j > 0:
                blist[i] = blist[i] + ['  ','*']
            else:
                if i > 1:
                    blist[i] = blist[i] + [str((i+1)/2)+' *']
                else:
                    blist[i] = blist[i] + ['*']
        else:
            if j > 0:
                blist[i] = blist[i] + ['  ',' ']
            else:
                blist[i] = blist[i] + ['   ']
    blist = blist + [[]]
blist.pop()
win = 0
turn = 0
while win == 0:
    pinput = 0
    while pinput == 0:
        cinput = 0
        while cinput == 0:
            ilist = ''
            while len(ilist) != 2 :
                print(name[turn] + "'s turn.")
                board(blist)
                ilist = raw_input('What line do you want to draw?\n(split co-ordinates with ":" and letter then number. Such as A1:B1 or c2:c3)\n').upper().split(':')
                cs()
            [blist,cinput] = drawline(ilist,blist,alphabet,size)
            [blist,scores,pinput] = isbox(blist,size,name,turn,scores)
        [win,pinput] = iswin(size,scores,name,pinput)
    turn = (turn+1)%nname

