from __future__ import division
import numpy as np
def analysis ():
    '''function generates an array from a file of input data and from this
    computes the mean and standard deviation of the rainfall on non dry days returned as a tuple'''
    timeseries = np.genfromtxt("/home/rmcruwys/ecb/obsdata.mtma33.txt")
    rainydays = np.array([])
    for i in np.arange(len(timeseries)):
        if (timeseries[i])!=0:
            rainydays = np.append(rainydays, timeseries[i])
    mean_rain = np.mean(rainydays)
    sd_rain = np.std(rainydays)
    return mean_rain, sd_rain
mean, std = analysis()
print mean
print std

def probability():
    rainafterrain = 0
    dryafterrain = 0
    timeseries = np.genfromtxt("/home/rmcruwys/ecb/obsdata.mtma33.txt")
    totalrainydays = np.sum(timeseries !=0)
    for i in np.arange(1,len(timeseries)):
        if ((timeseries[i]>0)&(timeseries[i-1]>0)):
            rainafterrain = rainafterrain + 1
        elif (timeseries[i]>0)&(timeseries[i-1] == 0):
            dryafterrain += 1
    prr = rainafterrain/totalrainydays
    pnr = dryafterrain/totalrainydays
    return prr, pnr
prr, pnr = probability()
print prr
print pnr