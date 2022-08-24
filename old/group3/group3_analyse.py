from __future__ import division
import numpy as np

#filename = "/home/tashadenn/ecb/obsdata.mtma33.txt"

'''This function takes the filename of rainfall data, processes it and returns 4 values:
    ret1 - prob of rain, ret2 - prob no rain, ret3 - mean rain, ret4 - std dev
'''
def analyse(filename):
    timeseries = np.genfromtxt(filename)

    rainydays = []

    number_rr = 0
    #number_rr = number	of rainy days following	a rainy	day

    number_nr = 0
    #number_nr =  number of	dry	days following a rainy	day

    number_rn = 0
    #number_rn =  number of	rainy days following a dry day

    number_nn = 0
    #number_nn =  number of	rainy days following a dry day

    for i in np.arange(1,len(timeseries)):
        if ((timeseries[i] > 0) & (timeseries[i-1] > 0)):
            number_rr = number_rr + 1
        if ((timeseries[i] == 0) & (timeseries[i-1] > 0)):
            number_nr = number_nr + 1
        if ((timeseries[i] > 0) & (timeseries[i-1] == 0)):
            number_rn = number_rn + 1
        if ((timeseries[i] > 0) & (timeseries[i-1] == 0)):
            number_nn = number_nn + 1
        if (timeseries[i] > 0):
            rainydays = np.append(timeseries[i], rainydays)

    prr = number_rr / (number_nr + number_rr)
    prn = number_rn / (number_rn + number_nn)

    mean_rain = np.mean (rainydays [0:len(rainydays)] )
    sd_rain = np.std (rainydays [0:len(rainydays)] )

    return prr, prn, mean_rain, sd_rain
























