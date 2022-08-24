from __future__ import division
import numpy as np

def calc_stats():
    timeseries = np.genfromtxt("/home/gc867060/ecb/obsdata.mtma33.txt") # reads in rainfall observed values

    number_rr = 0 #Initialising the counter rainy days following a rainy day
    number_nr = 0 #Initialising the counter dry days following a rainy day
    number_rn = 0 #Initialising the counter rainy days following a dry day
    number_nn = 0 #Initialising the counter dry days following a dry day

    for i in np.arange(1,len(timeseries)):
        if((timeseries[i] > 0) & (timeseries[i-1] > 0)): #counting number of days
            number_rr = number_rr + 1
        if((timeseries[i] == 0) & (timeseries[i-1] > 0)):
            number_nr = number_nr + 1
        if((timeseries[i] > 0) & (timeseries[i-1] == 0)):
            number_rn = number_rn + 1
        if((timeseries[i] == 0) & (timeseries[i-1] == 0)):
            number_nn = number_nn + 1

    print 'number_rr', number_rr
    print 'number_nr', number_nr
    print 'number_rn', number_rn
    print 'number_nn', number_nn

    prr = number_rr / (number_nr + number_rr) # Probability of rain given rain day before
    prn = number_rn / (number_rn + number_nn) # Probbaility of rain given none day before

    rainydays = float(1.0)
    for i in np.arange(1, len(timeseries)):
        if (timeseries[i] > 0):
            rainydays = np.append(timeseries[i],rainydays)

    mean_rain = np.mean(rainydays[1:len(rainydays)])
    sd_rain = np.std(rainydays[1:len(rainydays)])
    stats = np.array([prr,prn,mean_rain,sd_rain])
    return(stats)