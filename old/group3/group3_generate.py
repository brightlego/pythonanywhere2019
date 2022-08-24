import numpy as np
import random as rand
''' this function generates rainfall given arguments for mean, std dev, prob rain, prob no rain
    It returns two arrays of 1000 data points, the first is for occurence, the second for amount
'''
def generate(mean,sd,prr_r,prr_nr):
    # make empty arrays to hold 1000 data points - one for occurence, one for amount

    length_ts = 1000
    occurrence = np.zeros(length_ts)
    amount = np.zeros(length_ts)

#    rainonfirstday = 1
#    occurrence[0] = rainonfirstday
#    # to do: add in rainfall amount



    # iterate over array - for loop, for each item in array
    for i in np.arange(0, length_ts+1):
    #decide if it's rainy - how does it compare to the probability of rain?
        num = rand.uniform(0,1)
        if (num < prr_r):
            more_rain = 1
            # randomly generating an amount for each item in array based on the mean and sd (Gaussian distribution)
            amount[i] = abs(np.random.normal(mean,sd))

        else:
            more_rain = 0
        # put the more-rain value into the occurence array
        occurrence[i] = more_rain

    # return the arrays
    return amount