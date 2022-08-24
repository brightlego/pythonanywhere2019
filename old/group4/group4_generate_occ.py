import numpy as np

def rfao (rain_mean,rain_sd,prr,prn):
    length_ts = 365  # a one year dayly time series
    occurrence = np.zeros(length_ts) # generating an array which has zero values for the lenght of ts
    amount =  np.zeros(length_ts)

    rainonfirstday= 1
    occurrence [0] = rainonfirstday  # the first day occurence is assumed to be rainy
    amount[0] = abs(np.random.normal(rain_mean,rain_sd)) # first day amount

    number = np.random.uniform(0,1) # this genereate a random number between 0 and 1
    for i in np.arange(1,length_ts):
        if ((occurrence[i-1]>0) and (number<prr)): # checks for the conditions for occurence before day i and probability is below the P_rr
            amount[i] = abs(np.random.normal(rain_mean,rain_sd)) # generate a rainfall amount and put it in the array amount
            occurrence[i] = 1 # changes occurerence array from 0 to 1 if the conditions are fulfilled
        if ((occurrence[i-1]==0) and (number<prn)):
            amount[i] = abs(np.random.normal(rain_mean,rain_sd)) # generate a rainfall amount and put it in the array amount
            occurrence[i] = 1 # changes occurerence array from 0 to 1 if the conditions are fulfilled
        number = np.random.uniform(0,1)
    print occurrence
    print amount
    return(occurrence,amount)