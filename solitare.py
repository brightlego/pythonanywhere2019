def cs():
    for i in range(40):
        print '\n'
def make_board(tiles):
    alphabet = 'ABCDEFGHIJ'
    board = [[' '],[' ']]
    for i in range(0,9):
        board[0].append('  ' + alphabet[i] + ' ')
        board[1].append('----')
    board[1].append('-')
    for i in range(2,20,2):
        board.extend([[],[]])
        board[i].append(str(i/2)+'| ')
        board[i+1].append(' -')
        for j in range(9):
            board[i].extend([tiles[i/2-1][j],' | '])
            board[i+1].extend(['--','--'])
    str_board = ''
    for i in range(len(board)):
        for j in range(len(board[i])):
            str_board += board[i][j]
        str_board += '\n'
    print(str_board)

def input_(tiles,player_input):
    alphabet = 'abcdefghi'
    player_input[0] = list(player_input[0])
    player_input[0][0] = alphabet.index(player_input[0][0])
    player_input[0][1] = int(player_input[0][1])-1
    if tiles[player_input[0][1]][player_input[0][0]] == 'o':
        if player_input[1] == 'up':
            if player_input[0][1] > 1:
                if tiles[player_input[0][1]-1][player_input[0][0]] == 'o':
                    if tiles[player_input[0][1]-2][player_input[0][0]] == ' ':
                        tiles[player_input[0][1]][player_input[0][0]] = ' '
                        tiles[player_input[0][1]-1][player_input[0][0]] = ' '
                        tiles[player_input[0][1]-2][player_input[0][0]] = 'o'
                        return(tiles,True)
        if player_input[1] == 'right':
            if player_input[0][0] < 8:
                if tiles[player_input[0][1]][player_input[0][0]+1] == 'o':
                    if tiles[player_input[0][1]][player_input[0][0]+2] == ' ':
                        tiles[player_input[0][1]][player_input[0][0]] = ' '
                        tiles[player_input[0][1]][player_input[0][0]+1] = ' '
                        tiles[player_input[0][1]][player_input[0][0]+2] = 'o'
                        return(tiles,True)
        if player_input[1] == 'down':
            if player_input[0][1] < 8:
                if tiles[player_input[0][1]+1][player_input[0][0]] == 'o':
                    if tiles[player_input[0][1]+2][player_input[0][0]] == ' ':
                        tiles[player_input[0][1]][player_input[0][0]] = ' '
                        tiles[player_input[0][1]+1][player_input[0][0]] = ' '
                        tiles[player_input[0][1]+2][player_input[0][0]] = 'o'
                        return(tiles,True)
        if player_input[1] == 'left':
            if player_input[0][0] > 1:
                if tiles[player_input[0][1]][player_input[0][0]-1] == 'o':
                    if tiles[player_input[0][1]][player_input[0][0]-2] == ' ':
                        tiles[player_input[0][1]][player_input[0][0]] = ' '
                        tiles[player_input[0][1]][player_input[0][0]-1] = ' '
                        tiles[player_input[0][1]][player_input[0][0]-2] = 'o'
                        return(tiles,True)
    return(tiles,False)

def win(tiles):
    counter = 45
    unplayable_counter = 0
    marked_counters = []
    for i in range(9):
        for j in range(9):
            if tiles[i][j] == ' ':
                counter -= 1
            if tiles[i][j] == 'o':
                if i < 8 and i > 0:
                    if j < 8 and j > 0:
                        if tiles[i+1][j] != 'o' and tiles[i-1][j] != 'o' and tiles[i][j+1] != 'o' and tiles[i][j-1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                    elif j < 8:
                        if tiles[i+1][j] != 'o' and tiles[i-1][j] != 'o' and tiles[i][j+1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                    elif j > 0:
                        if tiles[i+1][j] != 'o' and tiles[i-1][j] != 'o' and tiles[i][j-1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                elif i < 8:
                    if j < 8 and j > 0:
                        if tiles[i+1][j] != 'o' and tiles[i][j+1] != 'o' and tiles[i][j-1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                    elif j < 8:
                        if tiles[i+1][j] != 'o' and tiles[i][j+1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                    elif j > 0:
                        if tiles[i+1][j] != 'o' and tiles[i][j-1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                elif i > 0:
                    if j < 8 and j > 0:
                        if tiles[i-1][j] != 'o' and tiles[i][j+1] != 'o' and tiles[i][j-1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                    elif j < 8:
                        if tiles[i-1][j] != 'o' and tiles[i][j+1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                    elif j > 0:
                        if tiles[i-1][j] != 'o' and tiles[i][j-1] != 'o':
                            unplayable_counter += 1
                            marked_counters.append([i,j])
                if [i,j] not in marked_counters:
                    if i < 7 and i > 1:
                        if j < 7 and j > 1:
                            if not (tiles[i+2][j] == ' ' and tiles[i+1][j] == 'o') and not (tiles[i-2][j] == ' ' and tiles[i-1][j] == 'o') and not (tiles[i][j+2] == ' ' and tiles[i][j+1] == 'o') and not (tiles[i][j-2] == ' ' and tiles[i][j-1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
                        elif j < 7:
                            if not (tiles[i+2][j] == ' ' and tiles[i+1][j] == 'o') and not (tiles[i-2][j] == ' ' and tiles[i-1][j] == 'o') and not (tiles[i][j+2] == ' ' and tiles[i][j+1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
                        elif j > 1:
                            if not (tiles[i+2][j] == ' ' and tiles[i+1][j] == 'o') and not (tiles[i-2][j] == ' ' and tiles[i-1][j] == 'o') and not (tiles[i][j-2] == ' ' and tiles[i][j-1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
                    elif i < 7:
                        if j < 7 and j > 1:
                            if not (tiles[i+2][j] == ' ' and tiles[i+1][j] == 'o') and not (tiles[i][j+2] == ' ' and tiles[i][j+1] == 'o') and not (tiles[i][j-2] == ' ' and tiles[i][j-1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
                        elif j < 7:
                            if not (tiles[i+2][j] == ' ' and tiles[i+1][j] == 'o') and not (tiles[i][j+2] == ' ' and tiles[i][j+1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
                        elif j > 1:
                            if not (tiles[i+2][j] == ' ' and tiles[i+1][j] == 'o') and not (tiles[i][j-2] == ' ' and tiles[i][j-1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
                    elif i > 1:
                        if j < 7 and j > 1:
                            if not (tiles[i-2][j] == ' ' and tiles[i-1][j] == 'o') and not (tiles[i][j+2] == ' ' and tiles[i][j+1] == 'o') and not (tiles[i][j-2] == ' ' and tiles[i][j-1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
                        elif j < 7:
                            if not (tiles[i-2][j] == ' ' and tiles[i-1][j] == 'o') and not (tiles[i][j+2] == ' ' and tiles[i][j+1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
                        elif j > 1:
                            if not (tiles[i-2][j] == ' ' and tiles[i-1][j] == 'o') and not (tiles[i][j-2] == ' ' and tiles[i][j-1] == 'o'):
                                unplayable_counter += 1
                                marked_counters.append([i,j])
    if counter == 1:
        return(False,'You Won!')
    elif counter == unplayable_counter:
        return(False,'You Lost with ' + str(counter) + ' counters left.')
    else:
        return(True,'')


tiles = []
for i in range(9):
    tiles.append([])
    for j in range(9):
        if i != 4 or j != 4:
            if i < 3 and j < 3:
                tiles[i].append('.')
            elif i > 5 and j < 3:
                tiles[i].append('.')
            elif i < 3 and j > 5:
                tiles[i].append('.')
            elif i > 5 and j > 5:
                tiles[i].append('.')
            else:
                tiles[i].append('o')
        else:
            tiles[i].append(' ')
make_board(tiles)
not_win = True
alphabet = 'abcdefghi'
numbers = '123456789'
directions = ['up','down','left','right']
while not_win:
    correct_input = False
    while not correct_input:
        player_input = raw_input('What do you want to move and in which direction? (Format: letter number space up/down/left/right)\n').lower().split()
        if len(player_input) != 2:
            correct_input = False
        elif type(player_input) != list:
            correct_input = False
        elif len(player_input[0]) != 2:
            correct_input = False
        elif player_input[0][0] not in alphabet:
            correct_input = False
        elif player_input[0][1] not in numbers:
            correct_input = False
        elif player_input[1] not in directions:
            correct_input = False
        else:
            tiles,correct_input = input_(tiles,player_input)
        cs()
        make_board(tiles)
    not_win,win_message = win(tiles)
print(win_message)