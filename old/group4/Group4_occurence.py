import numpy as np
import random as rand
number = rand.uniform(0,1)
    if (number < probability):
occurrence = 1
    else:
occurrence = 0
occurrence = np.zeros(length_ts)
amount = np.zeros(length_ts)
rainonfirstday = 1
occurrence[0] = rainonfirstday

number = rand.uniform(0,1)
    for i in np.arange(1,length_ts+1):
    amount[i] = abs(np.random.normal(rain_mean,rain_sd))
    if ((occurrence[i-1] > 0) & (number < prr)):
 occurrence[i] = 1
int(number_rr) = 0
for i in np.arange(1,len(timeseries)):
    if ((timeseries[i] > 0) & (timeseries[i-1] > 0)):
 number_rr = number_rr + 1



