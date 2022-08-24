import numpy as np
import random as rand
def timeseries(mean,sd,prr,prn):
    length=100
    occurrence = np.zeros(length)
    amount = np.zeros(length)
    rainonfirstday = 1
    occurrence[0] = rainonfirstday
    amount[0] = abs(np.random.normal(mean,sd))

    number = rand.uniform(0,1)
    for i in np.arange(1,length):
        amount[i] = abs(np.random.normal(mean,sd))
        if ( (occurrence[i-1] >0) & (number < prr) ):
            occurrence[i] = 1

    rainfall = amount * occurrence
    return(rainfall)