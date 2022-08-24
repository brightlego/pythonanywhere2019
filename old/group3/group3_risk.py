import numpy as np

''' this function calculates the occurance number of floods'''

def risk(amount):
    number_flood = 0    #this is the number of floods

    for i in np.arrange(1,len(amount)):
        if amount[i] > 20:
            number_flood += 1

    return number_flood
