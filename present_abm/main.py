import random
import math

class People:
    def __init__(self,money,max_presents_given):
        self.money = money
        self.presents_gained = 0
        self.max_presents_given = int(math.log10(random.randint(1,10**max_presents_given)))
        self.presents_given = 0
        self.generosity = random.randint(0,money//2)
    def give_present(self,people):
        people = sort_by_presents_gained(people)
        self.presents_given += 1
        self.money -= self.generosity
        people[random.randint(0,10-(10>len(people))*len(people)].presents_gained += 1
        return(people)
    def check_give_presents(self,people,date):
        if self.money > self.generosity and self.presents_given < self.max_presents_given and date < 25 and random.randint(date,25) in [23,24,25]:
            people = self.give_present(people)
        return(people)

def sort_by_presents_gained(people, *reverse):
    s_l  = []
    i = 0
    num_list = []
    for i in people:
        if i.presents_gained not in num_list:
            num_list.append(i.presents_gained)
    num_list.sort()
    for i in num_list:
        for j in people:
            if i == j.presents_gained:
                s_l.append(j)
    if reverse:
        s_l.reverse()
    return(s_l)

def init():
    num_people = int(input('Number of people: '))
    for i in range(num_people)