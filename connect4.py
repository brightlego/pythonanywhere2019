from copy import deepcopy
import random

def cs():
    for i in range(40):
        print('\n')

def board(size,tiles,start):
    board_ = []
    if start == True:
        for i in range(size[1]):
            tiles.append([])
            for j in range(0,size[0],2):
                tiles[i].append('  ')
    board_.append(['  '])
    for j in range(1,(size[0]/2)+1):
        if j < 10:
            board_[0].append(' '+str(j)+'  ')
        else:
            board_[0].append(' '+str(j)+' ')
    for i in range(size[1]):
        board_.extend([[],[]])
        for j in range(0,size[0],2):
            board_[2*i+1].extend([' |',tiles[i][j/2]])
            board_[2*i+2].extend(['--','--'])
        board_[2*i+1].append(' |')
        board_[2*i+2].append('---')
    board_ = board_[:len(board_)-2]
    if start == True:
        return(board_,tiles)
    else:
        return(board_)
def print_board(board_):
    board_str = ''
    for i in range(len(board_)):
        for j in range(len(board_[i])):
            board_str += board_[i][j]
        board_str += '\n'
    print(board_str)

def input_(tiles,player_input,size_1,turn_symbol):
    for i in range(1,size_1):
        if tiles[i][player_input-1] != '  ' or i == size_1-1:
            if tiles[i-1][player_input-1] == '  ':
                tiles[i-1][player_input-1] = turn_symbol
            return(tiles)

def is_row(tiles,size,turn_symbols):
    row_of_4 = [0,0]
    for i in range(0,size[1]-1):
        for j in range(0,(size[0]+1)/2):
            if tiles[i][j] != '  ':
                if i > 2:
                    if tiles[i-1][j] == tiles[i][j]:
                        if tiles[i-2][j] == tiles[i][j]:
                            if tiles[i-3][j] == tiles[i][j]:
                                row_of_4[turn_symbols.index(tiles[i][j])] += 1
                    if j > 2:
                        if tiles[i-1][j-1] == tiles[i][j]:
                            if tiles[i-2][j-2] == tiles[i][j]:
                                if tiles[i-3][j-3] == tiles[i][j]:
                                    row_of_4[turn_symbols.index(tiles[i][j])] += 1
                if j > 2:
                    if tiles[i][j-1] == tiles[i][j]:
                        if tiles[i][j-2] == tiles[i][j]:
                            if tiles[i][j-3] == tiles[i][j]:
                                row_of_4[turn_symbols.index(tiles[i][j])] += 1
                    if i < size[1]+1-2:
                        if tiles[i+1][j-1] == tiles[i][j]:
                            if tiles[i+2][j-2] == tiles[i][j]:
                                if tiles[i+3][j-3] == tiles[i][j]:
                                    row_of_4[turn_symbols.index(tiles[i][j])] += 1
    return(row_of_4)

def AI(size,turn,turn_symbols,tiles,difficulty):
    iscore = []
    turn_play = []
    for i in range((size[0]+1)/2):
        iscore.append(0)
        turn_play.append(i+1)
        for j in range((size[0]+1)/2):
            for k in range((size[0]+1)/2):
                for l in range((size[0]+1)/2):
                    ijkl = [i+1,j+1,k+1,l+1]
                    size_ = deepcopy(size)
                    turn_ = 0
                    turn_symbols_ = deepcopy(turn_symbols)
                    tiles_ = deepcopy(tiles)
                    win_ = False
                    while not win_ and turn_ < 5:
                        turn_ += 1
                        correct_input_ = False
                        columbs = []
                        for m in range(size[1]-1):
                            if tiles[0][m] != '  ':
                                columbs.append(m+1)
                        while not correct_input_ and not win_ and turn_ < 5:
                            player_input_ = ijkl[(turn_-1)%4]
                            if player_input_ >= size_[0]/2+1:
                                iscore[i] -= 100
                            elif player_input_ in columbs:
                                iscore[i] -= 100
                            correct_input_ = True
                            if player_input_ not in columbs:
                                tiles_ = input_(tiles_,player_input_,size_[1],turn_symbols_[turn_%2])
                            scores = is_row(tiles_,size_,turn_symbols_)
                            if scores[1] > scores[0]:
                                if turn_ != 1:
                                    iscore[i] += 1
                                else:
                                    iscore[i] += 1000000
                                win_ = True
                            elif scores[0] == scores[1] and scores[0] > 0:
                                win_ = True
                                iscore[i] -= 100
                            elif scores[0] > scores[1]:
                                win_ = True
                                iscore[i] -= 100
    iscore = zip(iscore,turn_play)
    iscore.sort(reverse = True)
    if difficulty == 'normal':
        if random.randint(1,10) == 1:
            iscore = iscore[random.randint(0,len(iscore)-1)]
    elif difficulty == 'easy':
        if random.randint(1,3) == 1:
            iscore = iscore[random.randint(0,len(iscore)-1)]
    else:
        same_score = 0
        for i in range(1,len(iscore)):
            if iscore[i][0] == iscore[0][0]:
                same_score += 1
        iscore = iscore[random.randint(0,same_score)]
    return(iscore[1])

win = False
numbers = '1234567890'
cs()

name = raw_input('What is your name? ')
correct_size = False
while not correct_size:
    correct_size = True
    number = False
    size = raw_input('How big do you want the board to be? ')
    for i in size:
        if i not in numbers:
            number = True
            if i != 'x':
                correct_size = False
    if correct_size:
        if number:
            size = size.split('x')
        else:
            size = [size,size]
        for i in range(0,2):
            size[i] = int(size[i])
        if size[0] < 4 or size[1] < 4 or size[0] > 20 or size[1] > 20:
            correct_size = False
    if not correct_size:
        print('That is not a viable dimetion format.\nEither use AxB for a rectangle where A is the length and B is the hight or just C for a square where C is the area for one of the sides. \n(A,B and C must be between 4 and 20 inclusive).')
difficulty = ''
while difficulty != 'easy' and difficulty != 'normal' and difficulty != 'hard':
    difficulty = raw_input('How difficult do you want it to be (Easy, Normal or Hard)? ').lower()
cs()

for i in range(2):
    size[i] += 1
size[0] *= 2
size[0] -= 2
board_,tiles = board(size,[],True)
print_board(board_)
turn = -1
turn_symbols = [' o',' x']
turn_names = [name + "'s (o)", "AI's (x)"]
while not win:
    turn += 1
    correct_input = False
    columbs = []
    for i in range(size[0]/2):
        if tiles[0][i] != '  ':
            columbs.append(i+1)
    while not correct_input and not win:
        scores = is_row(tiles,size,turn_symbols)
        if scores[1] > scores[0]:
            print('The AI picked column ' + str(AI_input))
            print('The AI won!')
            win = True
        elif (scores[0] == scores[1] and scores[0] > 0) or len(columbs) == size[0]/2:
            print("It' a draw!")
            win = True
        elif scores[0] > scores[1]:
            print('Well done ' + name + ', You won!')
            win = True
        else:
            print(turn_names[turn%2] + ' turn:')
            if turn%2 == 0:
                if turn > 0:
                    print('The AI picked column ' + str(AI_input))
                player_input = input('What column do you want to insert a counter? ')
            else:
                player_input = AI(size,turn,turn_symbols,tiles,difficulty)
                AI_input = player_input
            cs()
        if player_input >= size[0]/2+1:
            print('That column does not exist, pick one that does.')
            print('')
        elif player_input in columbs and not win:
            print('That column is full, pick another.')
            print('')
        else:
            correct_input = True
            if player_input not in columbs:
                tiles = input_(tiles,player_input,size[1],turn_symbols[turn%2])
        if not win:
            print_board(board(size,tiles,False))
            print('')
