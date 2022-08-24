from random import randint
from random import shuffle
from time import sleep

name = raw_input('What is your name? ')
difficulty = raw_input('Easy, Medium, Hard or Impossible (Imp)? ')
desired_rounds = input('How many rounds do you want? ')
rounds = 1
player_tally = 0
AI_tally = 0
while rounds <= desired_rounds:
    print '''


    '''
    print 'Round ' + str(rounds) + '.'


    cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'Jack','Jack','Jack','Jack','Queen','Queen','Queen'
    ,'Queen','King','King','King','King','Ace','Ace','Ace','Ace']
    shuffle(cards)
    bu_cards = cards

    value = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'Jack':10,'Queen':10,'King':10}

    players = [name,'AI']
    turns = 0

    player_total = 0
    AI_total = 0
    end_v = 'FALSE'
    AI_end_v = 'FALSE'
    both_end = 'FALSE'
    player_cards = []
    AI_cards = []

    for i in range(0,2):
        drawn_card = cards.pop()
        player_cards.append(drawn_card)
        if drawn_card == 'Ace':
            drawn_card = input('You drew an Ace. Do you want it to be a 1 or an 11? ')
            if drawn_card == 1 or drawn_card == 11:
                player_total = player_total + drawn_card
            else:
                print 'You cheat! Your ace is worthless now.'
        else:
            player_total = player_total + value[drawn_card]
            print 'You picked up a ' + str(drawn_card) + '. This brings your total up to ' + str(player_total) + '.'
        drawn_card = cards.pop()
        AI_cards.append(drawn_card)
        if drawn_card == 'Ace':
            if AI_total < 11:
                AI_total = AI_total + 11
            else:
                AI_total = AI_total + 1
        else:
            AI_total = AI_total + value[drawn_card]
    print ''
    print 'The AI picked up 2 cards.'
    print ''
    print('------------------------------------------------START------------------------------------------------')
    while (player_total < 21 and AI_total < 21) and both_end == 'FALSE':
        if len(cards) == 0:
            cards = bu_cards
        turn = players[turns%2]
        if end_v == 'TRUE' and AI_end_v == 'TRUE':
            both_end = 'TRUE'
        if turn == name and end_v == 'FALSE':
            draw = raw_input('Do you want to Draw, Hold or End, D/H/E? ')
            if draw == 'E' or draw == 'e':
                end_v = 'TRUE'
                print(name + ' ended the game.')
            elif draw == 'D' or draw == 'd':
                drawn_card = cards.pop()
                player_cards.append(drawn_card)
                if drawn_card == 'Ace':
                    drawn_card = int(input('You picked up an Ace. Do you want it to be a 1 or an 11? '))
                    if drawn_card == 1 or drawn_card == 11:
                        player_total = player_total+drawn_card
                        print 'This brings your total up to ' + str(player_total) + '.'
                    else:
                        print 'You Cheat! Your Ace is worthless now.'
                else:
                    player_total = player_total + value[drawn_card]
                    print 'You picked up a ' + str(drawn_card) + ', bringing your total up to ' + str(player_total) + '.'
            if draw == 'H' or draw == 'h':
                print 'Your total is ' + str(player_total) + '.'
            print ''
        elif turn == 'AI' and AI_end_v == 'FALSE':
            drawn_card = cards.pop()
            if difficulty == 'Easy' or difficulty == 'easy':
                print 'The AI drew a card.'
                AI_cards.append(drawn_card)
                if drawn_card == 'Ace':
                    if AI_total < 11:
                        AI_total = AI_total + 11
                    else:
                        AI_total = AI_total + 1
                else:
                    AI_total = AI_total + value[drawn_card]
            elif difficulty == 'Medium' or difficulty == 'medium':
                AI_draw = randint(0,1)
                if AI_draw != 0:
                    cards.append(drawn_card)
                    print 'The AI did not draw a card.'
                else:
                    print 'The AI drew a card.'
                    AI_cards.append(drawn_card)
                    if drawn_card == 'Ace':
                        if AI_total < 11:
                            AI_total = AI_total + 11
                        else:
                            AI_total = AI_total + 1
                    else:
                        AI_total = AI_total + value[drawn_card]
            elif difficulty == 'Hard' or difficulty == 'hard':
                AI_draw = randint(0,AI_total)
                if AI_draw != 0:
                    cards.append(drawn_card)
                    print 'The AI did not draw a card.'
                else:
                    print 'The AI drew a card.'
                    AI_cards.append(drawn_card)
                    if AI_total < 11:
                        AI_total = AI_total + 11
                    else:
                        AI_total = AI_total + 1
            elif difficulty == 'Impossible' or difficulty == 'impossible' or difficulty == 'Imp' or difficulty == 'imp':
                if AI_total > 12:
                    AI_draw = 0
                elif AI_total > 15:
                    AI_draw = randint(0,int(AI_total/2))
                else:
                    AI_draw = randint(0,int(AI_total/4))
                if AI_total > 18:
                    AI_end_v = 'TRUE'
                    print 'The AI has stoped.'
                    print ''
                elif AI_draw != 0:
                    cards.append(drawn_card)
                    print 'The AI did not draw a card.'
                else:
                    print 'The AI drew a card.'
                    AI_cards.append(drawn_card)
                    if drawn_card == 'Ace':
                        if AI_total < 11:
                            AI_total = AI_total + 11
                        else:
                            AI_total = AI_total + 1
                    else:
                        AI_total = AI_total + value[drawn_card]
                print ''
        turns = turns + 1
    if player_total > 21 or AI_total > 21:
        print 'BUST!'
        print ''

    if both_end== 'TRUE':
        if player_total > AI_total:
            print name + ' won with ' + str(player_total) + ", against the AI's " + str(AI_total) + '!'
            player_tally = player_tally + 1
        elif AI_total > player_total:
            print 'AI won with ' + str(AI_total) + ' against ' + name + "'s " + str(player_total) + '!'
            AI_tally = AI_tally + 1
        else:
            print "It's a draw with both " + name + ' and the AI having ' + str(player_total) + '! You will have an extra round'
            desired_rounds = desired_rounds + 1
    if player_total == 21:
        print name + ' has won as they have a total of 21!'
        player_tally = player_tally + 1
    elif AI_total == 21:
        print 'The AI won as it reached a total of 21.'
        AI_tally = AI_tally + 1
    elif 21 < AI_total:
        print name + ' won with ' + str(player_total) + ", against the AI's " + str(AI_total) + '!'
        player_tally = player_tally + 1
    elif 21 < player_total:
        print 'AI won with ' + str(AI_total) + ' against ' + name + "'s " + str(player_total) + '!'
        AI_tally = AI_tally + 1

    print name + "'s cards: " + str( ', '.join( repr(e) for e in player_cards ) )
    print 'AI cards; ' + str( ', '.join( repr(e) for e in AI_cards ) )
    if (rounds) == desired_rounds and player_tally == AI_tally:
        rounds = rounds - 1
        print 'You both scored ' + str(player_tally) + ' so there is a tie-breaker round'
    rounds = rounds + 1
    sleep(3)
if player_tally > AI_tally:
    print name + ' won with ' + str(player_tally) + ' to ' + str(AI_tally) + '.'
elif AI_tally > player_tally:
    print 'The AI won with ' + str(AI_tally) + ' to ' + str(player_tally) + '.'