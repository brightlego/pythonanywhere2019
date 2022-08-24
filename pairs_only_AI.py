import random

def cs():
    for i in range(30):
        print '\n'

def shuffle(cards):
    cards_ = []
    random_list = [-1]
    for i in range(len(cards)):
        random_number = -1
        while random_number in random_list:
            random_number = random.randint(0,len(cards)-1)
        random_list.append(random_number)
    for i in range(1,len(cards)+1):
        cards_.append(cards[random_list[i]])
    return(cards_)

def make_board(cards):
    board = [[' ','    A   ','      B   ','      C   ','      D   ' ,'      E   ','      F   ','      G   ','      H    ']]
    cards_remaining = 48
    for i in range(1,7):
        board.append([i])
        for j in range(0,8):
            if cards[8*(i-1)+j][1] == 0:
                board[i].append(' (-------)')
            elif cards[8*(i-1)+j][1] == 1:
                board[i].append(' (' + str(cards[8*(i-1)+j][0])+')')
            else:
                cards_remaining -= 1
                board[i].append('          ')
    board_str = ''
    for i in range(0,7):
        for j in range(0,9):
            board_str += str(board[i][j])
        board_str += '\n'
    print(board_str)
    return(cards_remaining)

def make_cards():
    suits = ['S','C','H','D']
    numbers = ['2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','Q ','K ']
    cards = []
    for i in range(0,4):
        for j in range(0,12):
            cards.append([numbers[j] + ' of ' + suits[i],0])
    return(cards)

def AI(cards,AI_memory):
    for i in AI_memory:
        if cards[i][1] != 0:
            AI_memory.remove(i)
    while len(AI_memory) > 5:
        del AI_memory[random.randint(0,len(AI_memory)-1)]
    for i in AI_memory:
        for j in AI_memory:
            if i != j:
                if cards[i][0][:2] == cards[j][0][:2]:
                    return([i,j,AI_memory])
    random_card_0 = 0
    start = True
    while cards[random_card_0][1] != 0 or start:
        start = False
        random_card_0 = random.randint(0,47)
    for i in AI_memory:
        if cards[random_card_0][0][:2] == cards[i][0][:2]:
            return([random_card_0,i,AI_memory])
    random_card_1 = 0
    start = True
    while cards[random_card_1][1] != 0 or start:
        start = False
        random_card_1 = random.randint(0,47)
    return([random_card_0,random_card_1,AI_memory])


alphabet = 'ABCDEFGH'
numbers = '123456'
name = raw_input('What is your name? ')
cards = make_cards()
cards = shuffle(cards)
cards_selected = []
turn = 0
scores = [0,0]
make_board(cards)
AI_memory = []
cards_remaining = 999
while cards_remaining > 0:
    if turn == 2:
        for i in range(2):
            correct_input = False
            while not correct_input:
                print(name + "'s turn.")
                player_input = list(raw_input('What tile do you want to change? ').upper())
                cs()
                if len(player_input) != 2:
                    correct_input = False
                    cards_remaining = make_board(cards)
                elif player_input[0] not in alphabet:
                    correct_input = False
                    cards_remaining = make_board(cards)
                elif player_input[1] not in numbers:
                    correct_input = False
                    cards_remaining = make_board(cards)
                else:
                    player_input[0] = alphabet.index(player_input[0])
                    player_input[1] = numbers.index(player_input[1])
                    player_input = 8*player_input[1] + player_input[0]
                    if cards[player_input][1] != 0:
                        correct_input = False
                        cards_remaining = make_board(cards)
                    else:
                        cards[player_input][1] = 1
                        correct_input = True
                        cards_selected.append([cards[player_input],player_input])
                        cards_remaining = make_board(cards)
    else:
        if cards_remaining > 0:
            print("The AI's turn")
            inputs = AI(cards,AI_memory)
            if inputs[0] < 47 and inputs[0] > 0:
                inputs[0] += int(random.randint(-1,1)*(random.randint(0,5)/5))
            if inputs[1] < 47 and inputs[1] > 0:
                inputs[1] += int(random.randint(-1,1)*(random.randint(0,5)/5))
            if inputs[1] == inputs[0]:
                if inputs[1] < 47:
                    while cards[inputs[1]][1] != 0:
                        inputs[1] += 1
                else:
                    while cards[inputs[1]][1] != 0:
                        inputs[1] -= 1
            cards_selected.extend([[cards[inputs[0]],inputs[0]],[cards[inputs[1]],inputs[1]]])
            cards[inputs[0]][1] = 1
            cards[inputs[1]][1] = 1
            AI_memory.extend(inputs[2])
            cards_remaining = make_board(cards)

    if len(cards_selected) == 2:
        AI_memory.extend([cards_selected[0][1],cards_selected[1][1]])
        if cards_selected[0][0][0][:2] == cards_selected[1][0][0][:2]:
            cards[cards_selected[0][1]][1] = 2
            cards[cards_selected[1][1]][1] = 2
            scores[turn] += 1
            make_board(cards)
            print cards_remaining
            print cards_selected
        else:
            cards[cards_selected[0][1]][1] = 0
            cards[cards_selected[1][1]][1] = 0

            turn += 1
            turn %= 2
        cards_selected = []
if scores[0] > scores[1]:
    print(name + ' won!')
elif scores[1] > scores[0]:
    print('The AI won!')
else:
    print("It's a draw!")