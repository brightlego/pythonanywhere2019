import re
global turn
global board

def cs():
    for i in range(40):
        print("\n")

def create_board():
    global board
    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(' ')

def display_board():
    cs()
    print(['X','O'][turn] +"'s turn")
    v_separator = ' | '
    h_separator = '----'
    board_str = []
    board_ = [["A","B","C"]] + board
    for i in range(len(board_)):
        board_[i] = [str(i)*bool(i) + ' '*(not bool(i))] + board_[i]
        board_str.append(v_separator.join(board_[i]))
    board_str = ('\n' + (h_separator*len(board_[i]))[len(v_separator):] + '\n').join(board_str)
    print(board_str)

def check_move(move):
    move = move.lower()
    if len(move) != 2:
        print("Invalid move")
        return False
    elif not re.match("[a-c][1-3]",move):
        print("Invalid move")
        return False
    else:
        move = [int(move[1])-1,{"a":0,"b":1,'c':2}[move[0]]]
        if board[move[0]][move[1]] != ' ':
            print("Invalid move")
            return False
        else:
            board[move[0]][move[1]] = ["O","X"][turn]
            display_board()
            return True

def check_win():
    full = False
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != ' ':
                if board[i][j] == board[i][(j+1)%3] and board[i][j] == board[i][(j+2)%3]:
                    return board[i][j]
                elif board[i][j] == board[(i+1)%3][j] and board[i][j] == board[(i+2)%3][j]:
                    return board[i][j]
                elif board[i][j] == board[(i+1)%3][(j+1)%3] and board[i][j] == board[(i+2)%3][(j+2)%3] and [i,j] in [[0,0],[1,1],[2,2]]:
                    return board[i][j]
                elif board[i][j] == board[(i+1)%3][(j-1)%3] and board[i][j] == board[(i+2)%3][(j-2)%3] and [i,j] in [[0,2],[1,1],[2,0]]:
                    return board[i][j]
            else:
                full = board[i][j]
    if not full:
        return "No one"
    return False

def play():
    create_board()
    display_board()
    win = False
    global turn
    turn = 0
    while not win:
        valid_move = False
        while not valid_move:
            move = raw_input("Where do you want to move? ")
            valid_move = check_move(move)
        win = check_win()
        turn = 1-turn
    print(win + " won!")

