from random import randint

cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'Jack','Jack','Jack','Jack','Queen','Queen','Queen'
,'Queen','King','King','King','King','Ace','Ace','Ace','Ace']

value = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'Jack':10,'Queen':10,'King':10}

name = raw_input('What is your name? ')

players = [name,'AI']
turns = 0

player_total = 0
AI_total = 0

difficulty = raw_input('Easy, Medium or Hard? ')
print '------------------------------------------------START------------------------------------------------'
if difficulty == 'Easy' or difficulty == 'easy':
    while player_total < 22 or AI_total < 22:
        turn = players[turns%2]
        draw = 1
        if turn == name:
            draw = raw_input('Do you want to draw, Y/N? ')
            if draw == 'Y':
                player_card = cards[randint(1,len(cards))]
                player_total =
                if player_card == 'Ace':
                    player_card = int(input('You picked up an Ace. Do you want it to be a 1 or an 11? '))
                    if player_card == 1 or player_card == 11:
                        player_total = player_total+player_card
                        print ' this brings your total up to ' + str(player_total) + '.'
                    else:
                        print 'You Cheat! Your Ace is worthless now.'

                print 'You picked up a ' + str(player_card) + ', bringing your total up to ' + str(player_total) + '.'


