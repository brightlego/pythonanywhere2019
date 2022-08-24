import numpy as np
import random
from copy import deepcopy
def cs():
    for i in range(0,60):
        print('')

def average(inlist):
    list_a = 0.0
    for i in range(0,len(inlist)):
        list_a = list_a + inlist[i]
    list_a = list_a/len(inlist)
    return(list_a)

def validmove(size,alphabet):
    validmoves = []
    for i in range(0,size):
        for j in range(0,size):
            move1 = [i,j]
            if move1[0] == 0 and move1[1] == 0:
                move2 = [[i+1,j],[i,j+1]]
            elif move1[0] == 0 and move1[0] < size-1:
                move2 = [[i+1,j],[i,j+1],[i,j-1]]
            elif move1[1] == 0 and move1[1] < size-1:
                move2 = [[i+1,j],[i-1,j],[i,j+1]]
            elif move1[0] == size-1 and move1[1] == size-1:
                move2 = [[i-1,j],[i,j-1]]
            elif move1[0] == size-1:
                move2 = [[i-1,j],[i,j+1],[i,j-1]]
            elif move1[1] == size-1:
                move2 = [[i+1,j],[i-1,j],[i,j-1]]
            else:
                move2 = [[i+1,j],[i-1,j],[i,j+1],[i-1,j]]
            move1[0] = alphabet[move1[0]]
            move1[1] = str(move1[1]+1)
            move1 = move1[0] + move1[1]
            for k in range(0,len(move2)):
                if move2[k][0] >= size or move2[k][1] >= size:
                    move2[k] = []
            for k in range(0,len(move2)):
                if move2[k] != []:
                    move2[k][0] = alphabet[move2[k][0]]
                    move2[k][1] = str(move2[k][1]+1)
                    move2[k] = move2[k][0] + move2[k][1]
                    validmoves.append([move1,move2[k]])
                for l in range(0,len(validmoves)-1):
                    if validmoves[l][0] == validmoves[len(validmoves)-1][1] and validmoves[l][1] == validmoves[len(validmoves)-1][0]:
                        validmoves.pop()
    return(validmoves)

def AI(blist,win,pinput,ilist,size,turn,scores,cinput,nnames,alphabet,names,nilist):
    blist_ = deepcopy(blist)
    win_ = deepcopy(win)
    pinput_ = deepcopy(pinput)
    ilist_ = deepcopy(ilist)
    size_ = deepcopy(size)
    turn_ = deepcopy(turn)
    turn_1 = deepcopy(turn)
    scores_ = deepcopy(scores)
    cinput_ = deepcopy(cinput)
    nnames_ = deepcopy(nnames)
    alphabet_ = deepcopy(alphabet)
    names_ = deepcopy(names)
    nilist_ = deepcopy(nilist)
    ppositions = []
    pscores = []
    validmoves = validmove(size_,alphabet_)
    nturn_ = 0
    box3 = [0,[]]
    for i in range(0,len(validmoves)):
 #       print validmoves[i]
        if isbox(drawline(validmoves[i],blist_,alphabet_,size_)[0],size_,names_,turn_,scores_)[1][turn] > scores[turn] and drawline(ilist_,blist_,alphabet_,size_)[1] == 1:
            box3[0] = 1
            box3[1].append(i)
    if box3[0] == 0 or len(box3[1]) > 0:
        for i in range(0,len(validmoves)):
            ascore = []
            win = 0
            turn_1 = deepcopy(turn)
            nturn_ = 0
            scores_ = deepcopy(scores)
            blist_ = deepcopy(blist)
            while win == 0 and turn_1 < nnames_*4:
                i_ = 0
                while i_ < len(validmoves) and win == 0:
                    pinput_ = 0
                    while pinput_ == 0 and win == 0 and i_ < len(validmoves):
                        cinput_ = 0
                        while cinput_ == 0 and pinput_==0 and win == 0 and i_ < len(validmoves):
                            if nturn_ != 0:
                                ilist_ = validmoves[i_]
                                i_ = i_ + 1
                            else:
                                ilist_ = validmoves[i]
                                i_ = i_ + 1
                            [blist_,cinput_] = drawline(ilist_,blist_,alphabet_,size_)
                            [blist_,scores_,pinput_] = isbox(blist_,size_,names_,turn_,scores_)
                        [win_,pinput_] = iswin(size_,scores_,names_,pinput_,0,blist_)
                    nturn_ = nturn_ + 1
                    pscore = 0
                    for j in range(0,len(scores)):
                        if j != turn-1:
                            pscore = pscore + scores_[j]-scores[j]
                    if turn_ == turn:
                        ascore.append(scores_[turn])
                turn_ = (turn_+1)%nnames_
                turn_1 = turn_1 + 1
                nturn_ = nturn_ + 1
            ascore = average(ascore)
            pscores.append(ascore)
            ppositions.append(validmoves[i])
    else:
        pscores = [999]
        if len(box3[1]) > 1:
            ppositions = [validmoves[box3[1][random.randint(0,len(box3[1])-1)]]]
        else:
            #print box3[1]
            #print validmoves
            ppositions = [validmoves[box3[1][0]]]
    pmove = zip(pscores,ppositions)
    #print pmove
    pmove.sort()
    if len(pmove) > 0:
        for i in range(0,nilist_):
            pmove.pop()
    pmove.reverse()
    pmove_ = deepcopy(pmove)
    for i in range(0,len(pmove_)-1):
        if pmove[i][0] == pmove[i+1][0]:
            pmove[i] = (average([pmove[i][0],pmove[i+1][0]]),pmove[i][1])
    pmove.sort()
    pmove.reverse()
    spmove = 0
    if len(pmove) > 0:
        for i in range(0,len(pmove)):
            if pmove[i][1] == pmove[0][1]:
                spmove = i
        pmove = pmove[random.randint(0,spmove)][1]
    else:
        pmove = ['','']
    return(pmove)

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
    #print ilist, 'ilist'
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
    if coords[0] == coords[1]:
        return([blist,0])
    elif coords[0][0] > size or coords[0][1] > size or coords[1][0] > size or coords[1][1] > size:
        return([blist,0])
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
    return([blist,1])

def isbox(blist,size,name,turn,scores):
    pinput = 1
    for h in range(0,(size-1)**2):
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

def iswin(size,scores,name,pinput,AI,blist):
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
            if AI == 1:
                cs()
                board(blist)
                print("It's a Draw!")
            return([1,1])
        while name_score[0][0] == name_score[i][0]:
            if len(winners) > 0:
                winners = winners + ', ' + name_score[i][1]
            else:
                winners = winners + name_score[i][1]
            i = i+1
        if AI == 1:
            board(blist)
            print(winners + ' won!')
        return([1,1])
    else:
        return([0,pinput])


alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
name = []
scores = []
ainames = np.load('Names.npy')
cs()
nname_ = input('How many human players do you want? ')
cs()
nai = input('How many AI do you want? ')
cs()
nname = nname_ + nai
nplayers = 0
aiturn = []
for i in range(0,nname_):
    if i == 0:
        name1 = raw_input('What is your name, player ' + str(i+1) + '? ')
    else:
        while name1 in name:
            name1 = raw_input('What is your name, player ' + str(i+1) + '? ')
            cs()
            if name1 in name:
                print('Player ' + str(name.index(name1)+1) + ' already picked that.')
    cs()
    name.append(name1)
    scores.append(0)
    nplayers = nplayers + 1
nameai = []
snameai = ''
for i in range(0,nai):
    while name1 in name:
        j = random.randint(0,len(ainames))
        name1 = ainames[j]
        ainame = ainames[j]
    name.append(name1)
    nameai.append(ainame)
    scores.append(0)
    aiturn.append(nplayers)
    nplayers = nplayers + 1
if len(nameai) > 1:
    for i in range(0,len(nameai)-2):
        snameai = snameai + nameai[i] + ', '
    snameai = snameai + nameai[len(nameai)-2] + ' and ' + nameai[len(nameai)-1]
    print('The AI are called ' + snameai + '.')
elif len(nameai) > 0:
    snameai = nameai[0]
    print('The AI is called ' + snameai + '.')
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
turn1 = 0
nilist = 0
sai = 0
while win == 0:
    pinput = 0
    while pinput == 0:
        cinput = 0
        while cinput == 0:
            ilist = ['','','']
            while len(ilist) != 2:
                if turn1 > 0:
                    print(name[turn-1] + ' Picked ' + previlist[0] + ':' + previlist[1] + '.')
                print(name[turn] + "'s turn.")
                board(blist)
                if turn not in aiturn:
                    ilist = raw_input('What line do you want to draw?\n(split co-ordinates with ":" and letter then number. Such as A1:B1 or c2:c3)\n').upper().split(':')
                    nilist = 0
                else:
                    if sai != turn:
                        nilist = nilist + 1
                    else:
                        sai = sai + 1
                    ilist = AI(blist,win,pinput,ilist,size,turn,scores,cinput,nname,alphabet,name,nilist)
                cs()
            [blist,cinput] = drawline(ilist,blist,alphabet,size)
            [blist,scores,pinput] = isbox(blist,size,name,turn,scores)
        [win,pinput] = iswin(size,scores,name,pinput,1,blist)
    previlist = ilist
    turn = (turn+1)%nname
    turn1 = turn1 + 1
    sai = turn