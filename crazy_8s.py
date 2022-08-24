from time import sleep
import random

def cs():
    for i in range(30):
        print('\n')
def print_hands(hands,discard_pile,turn):
    discard_top = ''
    str_hands = ''
    opponents_hands = ''
    for i in range(len(hands[(turn+1)%2])):
        opponents_hands += ' [-------] '
    for i in range(len(hands[turn])):
        str_hands += (' [' + hands[turn][i] + '] ')
        if i < len(hands[turn])/2 or i > len(hands[turn])/2:
            discard_top += ('           ')
        else:
            discard_top += (' [' + discard_pile[len(discard_pile)-1] + '] ')
    print(opponents_hands)
    print('')
    print(discard_top)
    print('')
    print(str_hands)

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

def cards_maker():
    numbers = ['2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','K ','Q ','A ']
    suits = ['S','C','H','D']
    cards = []
    for i in range(0,13):
        for j in range(0,4):
            cards.append(numbers[i] + ' OF ' + suits[j])
    cards = shuffle(cards)
    return(cards)

cards = cards_maker()

hands = [[],[]]
discard_pile = []

def AI(hands,discard_top):
    suit_counter = [[0,0],[0,1],[0,2],[0,3]] #[S,C,H,D]
    for i in hands[1]:
        if i.endswith('S') and not i.startswith('8'):
            suit_counter[0][0] += 1
        elif i.endswith('C') and not i.startswith('8')
            suit_counter[1][0] += 1
        elif i.endswith('H') and not i.startswith('8'):
            suit_counter[2][0] += 1
        elif not i.startswith('8'):
            suit_counter[3][0] += 1
    suit_counter.sort()
    suit_counter_same = 1
    for i in range(1,4):
        if suit_counter[i] == suit_coutner[0]:
            suit_coutner += i
    suit_counter[:i] = random.suffle(suit_counter[:i])
    for i in suit_counter:
        i.reverse()
    playble_suit = discard_top[6]
    playable_number = discard_top[:2]
    possible_cards = hands[1][:]
    for i in possible_cards:
        if not(i[6] == playable_suit or i[:2] == playable_number or i[:2] == '8 '):
            del i
    only_8 = True
    for i in possible_cards:
        if not i.startswith('8'):
            only_8 = False
    if only_8:
        return(possible_cards[0],suit_counter[0][0])
    if len(possible_cards) == 1:
        return(possible_cards[0],'')
    possible_moves = []
    if suit_counter[suit_counter.index(playable_suit)][1] == 0:
        for i in possible_cards:
            if i[:2] == playable_number or i[6] == playable_suit:
                if i[:2] != 8:
                    possible_moves.append(i)
    if len(possible_moves) > 0:
        possible_moves_ = [[],[],[],[]] #[S,C,H,D]
        for i in possible_moves:
            if i[6] == 'S':
                possible_moves[0].append(i)
            elif i[6] == 'C':
                possible_moves[1].append(i)
            elif i[6] == 'H':
                possible_moves[2].append(i)
            elif i[6] == 'D':
                possible_moves[3].append(i)
        possible_moves = possible_moves_[:]
        possible_moves = possible_moves[suit_counter[0][0]]
        return(random.choice(possible_moves),'')



for i in range(7):
    hands[0].append(cards.pop())
    hands[1].append(cards.pop())
discard_pile.append(cards.pop())
numbers = ['2','3','4','5','6','7','8','9','10','J','K','Q','A']
suits = ['S','C','D','H']
drawn_8 = False

turn = 0

while len(hands[0]) > 0 and len(hands[1]) > 0:
    discard_top = discard_pile[len(discard_pile)-1]
    if drawn_8:
        discard_top = list(discard_top)
        discard_top[6:] = desired_suit
        discard_top = ''.join(discard_top)
        drawn_8 = False
    incorrect_input = True
    while incorrect_input:
        if drawn_8:
            print discard_top
        if len(cards) == 0:
            discard_pile.reverse()
            cards = discard_pile[:]
            discard_pile = []
        cs()
        print_hands(hands,discard_pile,turn)
        playable_card = False
        for i in hands[turn]:
            if i[:2] == discard_top[:2] or i[6:] == discard_top[6:]:
                playable_card = True
            if i[:2] == '8 ':
                playable_card = True
        if playable_card:
            player_input = raw_input('What card do you want to draw? ').upper().split()
            if len(player_input) != 3:
                incorrect_input = True
            elif player_input[0] not in numbers:
                incorrect_input = True
            elif player_input[1] != 'OF':
                incorrect_input = True
            elif player_input[2] not in suits:
                incorrect_input = True
            else:
                if len(player_input[0]) == 1:
                    player_input[0] += ' '
                if player_input[0] + ' ' + player_input[1] + ' ' + player_input[2] in hands[turn] and (player_input[0] == discard_top[:2] or player_input[2] == discard_top[6:] or player_input[0] == '8 '):
                    del hands[turn][hands[turn].index(player_input[0] + ' ' + player_input[1] + ' ' + player_input[2])]
                    discard_pile.append(player_input[0] + ' ' + player_input[1] + ' ' + player_input[2])
                    if player_input[0] == '8 ':
                        drawn_8 = True
                        desired_suit = ' '
                        while desired_suit not in 'SCHD':
                            desired_suit = raw_input('What suit do you want? (S,C,H,D) ').upper()
                    incorrect_input = False
                else:
                    incorrect_input = True
        else:
            print('You must draw a card.')
            hands[turn].append(cards.pop())
            sleep(0.3)
    turn += 1
    turn %= 2
