from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pandas as pds
import os
import scipy
import random

def wrapper_obs(file,month,length):
    timeseries = markov(file,month)
    outstats = calcobsstats(timeseries)
    output = gen_timeseries(outstats,length)
    return(output)

def readindata(file):
    '''opens a file of format year month day data and extracts data for a user specified month'''
    indata = np.loadtxt(file)
    return(indata)

def markov(file,month):

    dims = np.shape(indata)

    month_ts = [0.0]
    for i in np.arange(0,dims[0]-1):
        if ((indata[i,1] > month - 0.5) & (indata[i,1] < 1.5)):
            month_ts = np.append(month_ts,indata[i,3])
    return(month_ts)

def plottimeseries(timeseries):

    fig = plt.figure()
    plt.plot(timeseries)
    fig.savefig('graph.png')

def calcobsstats(timeseries):

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

def gen_timeseries(stats,length_ts):

    prr = stats[0]
    prn = stats[1]
    meanrain = stats[2]
    sdrain = stats[3]
    gen_intensity = np.zeros(length_ts)
    gen_occurrence = np.zeros(length_ts)

    for i in np.arange(1,length_ts):
        gen_intensity[i] = np.abs(random.gauss(meanrain,sdrain))
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




