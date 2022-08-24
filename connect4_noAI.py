def cs():
    for i in range(40):
        print'\n'

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

win = False
size = raw_input('How big do you want the board to be? ')
if len(size) > 1:
    size = size.split('x')
else:
    size = [size,size]
size.reverse()
for i in range(2):
    size[i] = int(size[i])+1
size[0] *= 2
size[0] -= 2
board_,tiles = board(size,[],True)
print_board(board_)
turn = -1
turn_symbols = [' o',' x']
while not win:
    turn += 1
    correct_input = False
    columbs = []
    for i in range(size[1]-1):
        if tiles[0][i] != '  ':
            columbs.append(i+1)
    while not correct_input and not win:
        scores = is_row(tiles,size,turn_symbols)
        if scores[1] > scores[0]:
            print('x won!')
            win = True
        elif scores[0] == scores[1] and scores[0] > 0:
            print("It' a draw!")
            win = True
        elif scores[0] > scores[1]:
            print('o won!')
            win = True
        else:
            player_input = input('What columb do you want to insert a counter? ')
            cs()
        if player_input >= size[0]+2/2:
            print('That columb does not exist, pick one that does.')
            print('')
        elif player_input in columbs:
            print('That columb is full, pick another.')
            print('')
        else:
            correct_input = True
            if player_input not in columbs:
                tiles = input_(tiles,player_input,size[1],turn_symbols[turn%2])
        if not win:
            print_board(board(size,tiles,False))
            print('')
