class Cards:
    def __init__(self,name,born,age,fame,deeds,death,owner,order):
        self.name = name
        self.born = born
        self.age = age
        self.fame = fame
        self.deeds = deeds
        self.death = death
        self.owner = owner
        self.order = order

def card_pack():
    card_list = []
    card_list.append(Cards(name = 'Li Shimin', born = 598, age = 51, fame = 35, deeds = 17, death = 51, owner = 0, order = 0))
    card_list.append(Cards(name = 'Attila the Hun', born = 406, age = 47, fame = 48, deeds = 19, death = 81, owner = 0, order = 0))
    card_list.append(Cards(name = 'Genghis Khan', born = 1162, age = 65, fame = 48, deeds = 20, death = 57, owner = 0, order = 0))
    card_list.append(Cards(name = 'William the Conqueror', born = 1027, age = 60, fame = 49, deeds = 16, death = 66, owner = 0, order = 0))
    card_list.append(Cards(name = 'Draco', born = -600, age = -1, fame = 29, deeds = 12, death = 64, owner = 0, order = 0))
    card_list.append(Cards(name = 'Adolf Hitler', born = 1889, age = 56, fame = 46, deeds = 20, death = 86, owner = 0, order = 0))
    card_list.append(Cards(name = 'Josef Stalin', born = 1879, age = 74, fame = 48, deeds = 20, death = 43, owner = 0, order = 0))
    card_list.append(Cards(name = 'Edward Teach (Blackbeard)', born = 1680, age = 38, fame = 45, deeds = 19, death = 93, owner = 0, order = 0))
    card_list.append(Cards(name = 'Henry VIII', born = 1491, age = 56, fame = 50, deeds = 17, death = 87, owner = 0, order = 0))
    card_list.append(Cards(name = 'Ashurnasipal', born = -883, age = 24, fame = 11, deeds = 18, death = 49, owner = 0, order = 0))