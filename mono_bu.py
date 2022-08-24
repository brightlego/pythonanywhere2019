import random

def dice(a = 6,b = 2):
    """This program throws the dice"""
    dicenumber = 1
    dicescore = 0
    dicevalue1 = 0
    dicevalue2 = 0
    for number in range(b):
        score = random.randint(1,a)
 #       print(score)
        dicescore = dicescore + score
        if dicenumber == 1:
            dicevalue1 = score
        else:
            dicevalue2 = score
        dicenumber = dicenumber + 1
#    print(dicevalue1)
#    print(dicevalue2)
#    print(dicescore)
#    print(" ")
    return(dicescore,dicevalue1,dicevalue2)

def board():
    tile = 0
    dicescore = 0
    dicescore, dicevalue1, dicevalue2 = dice(a = 6,b = 2)
    if tile < 40:
        tile = tile + dicescore
    else:
        tile = tile - 40
        tile = tile + dicescore
    return(tile)

def movement(tile):
    goscore = 0
    if tile <= 39:
        tile = tile + board()
 #       print(tile)
        goscore = 0
    else:
        tile = (tile + board()) - 40
  #      print(tile)
        goscore = 1
    return(goscore,tile)

def money(goscore,moneyin,tile):
    if goscore == 1:
        moneyin = moneyin + 200
        print("You passed Go. +200")
        print(" ")
    if tile == 4:
        moneyin = moneyin - 200
        print("You paid income tax. -200")
        print(" ")
    if tile == 38:
        moneyin = moneyin - 100
        print("You paid super tax. -100")
        print(" ")
    return(moneyin)

def movement_money():
    '''this is movement money
    it's the main bit of monopoly'''
    go = 1
    tile = 0
    moneyin = 1500
    jailfree = 0
    ownedscore = 0
    propertylist1 = []
    propertylist2 = []
    dict = tile_dic()
    property_tile = tile_owned()
#    print(property_tile[1].tile)
    turn = 1
    player1 = player(tile,moneyin,"player1",jailfree)
    player2 = player(tile,moneyin,"player2",jailfree)
    player1.name = raw_input("Please type Player 1's name in here. -> ")
    player2.name = raw_input("Please type Player 2's name in here. -> ")
    print(" ")
    while go == 1:
        print(player1.name + "'s jailfree: " + str(player1.jailfree))
        print(player2.name + "'s jailfree: " + str(player2.jailfree))
        if turn == 1:
            tile = player1.tile
            moneyin = player1.money
            print(str(player1.name) + str("'s turn."))
            print(" ")
        elif turn == 2:
            tile = player2.tile
            moneyin = player2.money
            print(str(player2.name) + str("'s turn."))
            print(" ")
        if tile == -1:
            jailout = input("Pay, role or use a 'get out of jail free'card? ")
            if jailout == 1:
                moneyin = moneyin - 50
                print("You paid 50 pounds to get out of Jail.")
                print(" ")
                tile = 10
            elif jailout == 2:
                dicescore, dicevalue1, dicevalue2 = dice()
                if dicevalue1 == dicevalue2:
                    print("You rolled a double. Your now out of Jail.")
                    print(" ")
                    tile = 10
                else:
                    print("You didn't role a double")
            elif jailout == 3:
                if turn == 1:
                    if player1.jailfree > 0:
                        player1.jailfree = player1.jailfree - 1
                        jailfree = 0
                        print("You used up one of your get out of jail free card. Your now out of Jail.")
                        tile = 10
                    else:
                        print("You don't hane a get out of jail free card")
                elif turn == 2:
                    if player2.jailfree > 0:
                        player2.jailfree = player2.jailfree - 1
                        jailfree = 0
                        print("You used up one of your get out of jail free card. Your now out of Jail.")
                        tile = 10
                    else:
                        print("You don't have a get out of jail free card")
                        print(" ")
                else:
                    print("Type Error")
        if tile == 30:
            print("Go to Jail.")
            print(" ")
            tile = -1
        if tile != -1:
            goscore, tile = movement(tile)
            if tile > 39:
                tile = tile - 40
                goscore = 1
            moneyout = money(goscore,moneyin,tile)
            moneyin = moneyout
        if tile == 2 or tile == 7 or tile == 17 or tile == 22 or tile == 33 or tile == 36:
            tile,moneyout,card_picked_number = test_com_chest(tile,moneyin)
            moneyin = moneyout
            if card_picked_number == 3:
                jailfree = 1
        print(str("Tile: ") + str(dict[tile]))
        print(str("Money: ")+str(moneyout))
        print(" ")
        for z in range(0,27):
            if tile == property_tile[z].tile:
                if property_tile[z].owned == 0:
                    if turn == 1:
                        ownedscore = input("Do you want to buy this tile? ")
                        property_tile[z].owned = ownedscore
                        if ondscore == 1:
                            propertylist1 = [property_monop[z]]
                    elif turn == 2:
                        ownedscore = input("Do you want to buy this tile? ")
                        property_tile[z].owned = ownedscore + 1
                        if ondscore == 2:
                            propertylist2 = [property_monop[z]]
                    if ownedscore == 1:
                        moneyin = moneyin - property_tile[z].cost
                if turn == 1 and property_tile[z].owned == 2:
                    if property_tile[z].house_number == 0:
                        moneyin = moneyin - property_tile[z].rent_0
                        player2.money = player2.money + property_tile[z].rent_0
                        print("You paid rent. -" + str(property_tile[z].rent_0))
                if turn == 2 and property_tile[z].owned == 1:
                    if property_tile[z].house_number == 0:
                        moneyin = moneyin - property_tile[z].rent_0
                        player1.money = player1.money + property_tile[z].rent_0
                        print("You paid rent. -" + str(property_tile[z].rent_0))
        if go == 1:
            go = input("One more go? ")
            print(" ")
        if go != 1:
            go = input("Are you sure? ")
            print(" ")
        if turn == 1:
            turn = 2
            player1.tile = tile
            player1.money = moneyin
            player1.jailfree = player1.jailfree + jailfree
        elif turn == 2:
            turn = 1
            player2.tile = tile
            player2.money = moneyin
            player2.jailfree = player2.jailfree + jailfree
        jailfree = 0
        ownedscore = 0
    return(str(player1.name) + str(": ") + str(player1.money) + str(" ") + str(player2.name) + str(": ") + str(player2.money))

def tile_dic():
    dict = {-2 : 'permanant jail', -1 : 'Jail' , 0 : 'Go' , 1 : 'Old Kent Road' , 2 : 'Comunity Chest' , 3 : 'Whitechapel Road' , 4 : 'Income tax' , 5 : 'Kings Cross Station' , 6 : 'The Angel, Islington' , 7 : 'Chance' ,
    8 : 'Euston Road' ,9 : 'Pentoville Road' , 10 : 'Just Visiting' , 11 : 'Pall Mall' , 12 : 'Electric Company' , 13 : 'Whitehall' , 14 : 'Northunbererland Avenue' , 15 : 'Marylebone Station' , 16 : 'Bow Street' ,
    17 : 'Comunity Chest' ,18 : 'Marlborough Street' , 19 : 'Vine Street' , 20 : 'Free Parking', 21 : 'Strand', 22 : 'Chance', 23: 'Fleet Street', 24 : 'Trafalgar Square', 25 : 'Fenchurch St. Station', 26 : 'Leicester Square',
    27 : 'Coventry Street', 28 : 'Water Works', 29 : 'Piccadilly', 30 : 'Go to Jail', 31 : 'Regent Street', 32 : 'Oxford Street', 33 : 'Community chest', 34 : 'Bond Street', 35 : 'Liverpool St. Station',
    36 : 'Chance', 37 : 'Park Lane', 38 : 'Super Tax', 39 : 'Mayfair'};
    return(dict)

def christ_dic():
    dict = {-2 : 'permanant jail', -1 : 'Santas Workshop' , 0 : 'The North Pole' , 1 : 'Old Kent Road' , 2 : 'Elf Chest' , 3 : 'Whitechapel Road' , 4 : 'Santa tax' , 5 : 'Santas Cross Station' , 6 : 'The Angel, Islington' ,
    7 : 'Christmas Chance', 8 : 'Euston Road' , 9 : 'Pentoville Road' , 10 : 'Just Visiting' , 11 : 'Pall Mall' , 12 : 'Toy Making Factory' , 13 : 'Whitehall' , 14 : 'Northunbererland Avenue' , 15 : 'Rudolf Station' ,
    16 : 'Bow Street' , 17 : 'Elf Chest' , 18 : 'Marlborough Street' , 19 : 'Vine Street' , 20 : 'Raindeer Parking', 21 : 'Candy Cane', 22 : 'Christmas Chance', 23: 'Fleet Street', 24 : 'Trafalgar Square',
    25 : 'North Pole Station', 26 : 'Leicester Square', 27 : 'Coventry Street' , 28 : 'Hot Chocolate Works', 29 : 'Piccadilly', 30 : 'Go to Santas Workshop', 31 : 'Regent Street', 32 : 'Oxford Street', 33 : 'Elf chest',
    34 : 'Bond Street', 35 : 'Raindeer Street Station', 36 : 'Christmas Chance', 37 : 'Park Lane', 38 :'Elf Tax', 39 : 'Mayfair'};
    return(dict)

class player:
    def __init__(self,tile,money,name,jailfree):
        self.tile = tile
        self.money = money
        self.name = name
        self.jailfree = jailfree

class com_chest:
    def __init__(self,tile,money,message):
        self.tile = tile
        self.money = money
        self.message = message

class tile_house:
    def __init__(self,tile,money,house,owned):
        self.tile = tile
        self.money = money
        self.house = house
        self.owned = owned

class property_monop:
    def __init__(self,tile,name,cost,rent_0,rent_1,rent_2,rent_3,rent_4,rent_5,owned,house_cost,house_number):
        self.name = name
        self.rent_0 = rent_0
        self.rent_1 = rent_1
        self.rent_2 = rent_2
        self.rent_3 = rent_3
        self.rent_4 = rent_4
        self.rent_5 = rent_5
        self.owned = owned
        self.tile = tile
        self.house_cost = house_cost
        self.house_number = house_number
        self.cost = cost

def tile_owned():
    ownedscore = 0
    properties = []
    properties.append(property_monop(tile = 1, name = "Old Kent Road", cost = 60, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 3, name = "Whitechapel Road", cost = 60, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 5, name = "Kings Cross Station", cost = 200, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 6, name = "The Angel, Islington", cost = 100, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 8, name = "Euston Road", cost = 100, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 9, name = "Pentoville Road", cost = 120, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 11, name = "Pall Mall", cost = 140, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 12, name = "Electric Company", cost = 150, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 13, name = "Whitehall", cost = 140, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 14, name = "Northunbererland Avenue", cost = 160, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 15, name = "Marylebone Station", cost = 200, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 16, name = "Bow Street", cost = 180, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 18, name = "Marlborough Street", cost = 180, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 19, name = "Vine Street", cost = 200, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 21, name = "Strand", cost = 220, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 23, name = "Fleet Street", cost = 220, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 24, name = "Trafalgar Square", cost = 240, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 25, name = "Fenchurch St. Station", cost = 200, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 26, name = "Leicester Square", cost = 260, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 27, name = "Coventry Street", cost = 260, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 28, name = "Water Works", cost = 150, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 29, name = "Piccadilly", cost = 280, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 31, name = "Regent Street", cost = 300, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 32, name = "Oxford Street", cost = 300, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 34, name = "Bond Street", cost = 320, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 35, name = "Liverpool St. Station", cost = 200, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 37, name = "Park Lane", cost = 350, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    properties.append(property_monop(tile = 39, name = "Mayfair", cost = 400, rent_0 = 2, rent_1 = 10, rent_2 = 30, rent_3 = 90, rent_4 = 160, rent_5 = 250, owned = 0, house_cost = 50, house_number = 0))
    return(properties)



def test_com_chest(tile,money):
    com_chest_card = []
    com_chest_card.append(com_chest(tile = 1,money = 0,message = "Go back to Old Kent Road."))
    com_chest_card.append(com_chest(tile = 0,money = 200,message = "Bank error in your favour.  Get 200 pounds."))
    com_chest_card.append(com_chest(tile = 0,money = 100,message = "Annuity matures.  Collect 100 pounds."))
    com_chest_card.append(com_chest(tile = 0,money = 0,message = "Get out of jail free."))
    com_chest_card.append(com_chest(tile = 0,money = -50,message = "Doctor's fee.  Pay 50 pounds."))
    com_chest_card.append(com_chest(tile = 0,money = 200,message = "Tax refund.  Collect 200 pounds"))
    com_chest_card.append(com_chest(tile = 0,money = -50,message = "Pay your insurance premium of 50 pounds."))
    com_chest_card.append(com_chest(tile = 0,money = 100,message = "You inherit 100 pounds."))
    com_chest_card.append(com_chest(tile = 0,money = -100,message = "Pay hospital bill of 100 pounds."))
    com_chest_card.append(com_chest(tile = 0,money = 10,message = "You have won second prize in a beauty contest.  Collect 10 pounds."))
    com_chest_card.append(com_chest(tile = 0,money = 25,message = "Receive interest on shares of 25 pounds."))
    com_chest_card.append(com_chest(tile = -1,money = 0,message = "Go to jail."))
    com_chest_card.append(com_chest(tile = 0,money = 10,message = "It's your birthday.  Get 10 pounds"))
    com_chest_card.append(com_chest(tile = 0,money = 50,message = "From sale of stock, you get 50 pounds."))
    card_picked_number = random.randint(0,13)
    card_picked = com_chest_card[card_picked_number]
    if card_picked.tile != 0:
        tile = card_picked.tile
    money = money + card_picked.money
    print(card_picked.message)
    return(tile,money,card_picked_number)

