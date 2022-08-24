from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import random

def wrapper_obs(file,length):
    timeseries = readindata(file)
    outstats = calculate_statistics(timeseries)
    output = gen_timeseries(outstats,length)
    return(output)

def readindata(file):
    '''opens a file named by the user and puts the data into an array'''
    timeseries = np.loadtxt(file)
    return(timeseries)

def calculate_statistics(timeseries):
    '''outputs statistics of the weather for a user specified time series array'''

    #initialising the variables
    count_rr = int(0)
    count_nr = int(0)
    count_nn = int(0)
    count_rn = int(0)
    rainydays = float(1.0)

#At each point in the time series, we count dry/wet days where there has/hasn't been rainfall the day before.

    for i in np.arange(1,len(timeseries)-1):
        if ((timeseries[i] > 0) & (timeseries[i-1] > 0)):
            count_rr = count_rr + 1

        if ((timeseries[i] == 0) & (timeseries[i-1] > 0)):
            count_nr = count_nr + 1

        if ((timeseries[i] == 0) & (timeseries[i-1] == 0)):
            count_nn = count_nn + 1

        if ((timeseries[i] > 0) & (timeseries[i-1] == 0)):
            count_rn = count_rn + 1

        if (timeseries[i] > 0):
            rainydays = np.append(timeseries[i],rainydays)

#Based on the counts in the previous part of the code, we calculate prr (probability of rain given rain the day before)
#and prn (probability of rain given no rain the day before).
#Note that in order for this to work, we must have from __future__ import division at the top of the file.
#otherwise, we run into problems of rounding to the nearest integer (eg 1/3 = 0)

    prr = count_rr/(count_rr + count_nr)
    prn = count_rn/(count_rn + count_nn)
    meanrain = np.mean(rainydays)
    sdrain = np.std(rainydays)

    return([prr,prn,meanrain,sdrain])


def plottimeseries(timeseries):

    fig = plt.figure()
    plt.plot(timeseries)
    fig.savefig('graph.png')



def gen_timeseries(stats,length_ts):
    '''Reads in a vector containing the statistics of the weather and an integer giving the length of the time series'''
#assign the elements of the array to the probabilities.
    prr = stats[0]
    prn = stats[1]
    meanrain = stats[2]
    sdrain = stats[3]

#set up arrays for the generated intensity and occurrence
    gen_intensity = np.zeros(length_ts)
    gen_occurrence = np.zeros(length_ts)

#initialise arrays with user given values.  These could be set as arguments to the function.
    gen_intensity[0] = 4.0
    gen_occurrence[0] = 1

    for i in np.arange(1,length_ts+1):

#generate the intensity for each point in time
        gen_intensity[i] = np.abs(random.gauss(meanrain,sdrain))

#generate the occurrence at each point in time
        if ((gen_occurrence[i-1] > 0) & (random.random() < prr)):
            gen_occurrence[i] = 1

        if ((gen_occurrence[i-1] > 0) & (random.random() > prr)):
            gen_occurrence[i] = 0

        if ((gen_occurrence[i-1] == 0) & (random.random() < prn)):
            gen_occurrence[i] = 1

        if ((gen_occurrence[i-1] == 0) & (random.random() > prn)):
            gen_occurrence[i] = 0


    outts = gen_occurrence * gen_intensity

    return(outts)

def calculate_flood_risk(timeseries,threshold):

#initialise the flood counter
    count_floods = np.zeros(len(timeseries))

    for i in np.arange(1,len(timeseries)+1):
        if (timeseries[i] > threshold):
            count_floods[i] = 1

    return(np.sum(count_floods))





