import numpy as np
import matplotlib.pyplot as plt

#Import time series into script

timeseries = np.genfromtxt("/home/crowdave/ecb/obsdata.mtma33.txt")

#Define variable x that includes all dates from 0 to 899

#x=np.arange(0,899,1)

#def makeplot():
'''    fig = plt.figure()
    plt.plot(x,timeseries)
    plt.xlabel('Date')
    plt.ylabel('Rainfall (mm)')
    fig.savefig("/home/crowdave/ecb/group5_timeseries.png")

#makeplot()

a=np.std(timeseries)
b=np.mean(timeseries)

print a,b
'''
def time_series():
    occurrence = np.zeros(length_ts)
    amount = np.zeros(length_ts)
    rainonfirstday = 0
    occurrence[0] = rainonfirstday
    number = rand.uniform(0,1)
    for i in np.arange(1,length_ts):
        amount[i] = abs(np.random.normal(rain_mean,rain_sd))
        if ((occurrence[i-1] > 0) & (number < prr)):
            occurrence[i] = 1
    amount=abs(np.random.normal(mean,sd))
    rainfall = amount * occurrence
    number_rr = 0
    for i in np.arange(1,len(timeseries)):
        if ((timeseries[i] > 0) & (timeseries[i-1] > 0)):
            number_rr = number_rr + 1
            rainydays = float(1.0)
        if (timeseries[i] > 0):
            raindays = np.append(timeseries[i],rainydays)
            mean_rain = np.mean(rainydays[1:len(rainydays)])
            sd_rain = np.std(rainydays[1:len(rainydays)])



