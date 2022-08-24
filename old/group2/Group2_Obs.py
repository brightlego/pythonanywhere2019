from __future__ import division
import numpy as np

def obs():
    timeseries = np.genfromtxt('/home/Rachael/ecb/obsdata.mtma33.txt')
    #Obsmean=np.mean(timeseries)
    #Obsstd=np.std(timeseries) #Standard Deviation
    number_rr=0
    number_nr=0
    number_rn=0
    number_nn=0
    for i in np.arange(1,len(timeseries)):
        if ((timeseries[i]>0) & (timeseries[i-1] > 0)):
            number_rr=number_rr+1
        if ((timeseries[i]==0) & (timeseries[i-1] > 0)):
            number_nr=number_nr+1
        if ((timeseries[i]>0) & (timeseries[i-1]==0)):
            number_rn=number_rn+1
        if ((timeseries[i]==0) & (timeseries[i-1]==0)):
            number_nn=number_nn+1


    #print ('number_rr='+str(number_rr))
    #print ('number_nr='+str(number_nr))
    #print ('number_rn='+str(number_rn))
    #print ('number_nn='+str(number_nn))

    rainydays = float(1.0)
    for i in np.arange(1,len(timeseries)):
        if (timeseries[i]>0):
            rainydays=np.append(timeseries[i], rainydays)

    #print (len(rainydays))
    mean_rain = np.mean(rainydays[1:len(rainydays)])
    sd_rain = np.std(rainydays[1:len(rainydays)])
    #print (mean_rain)
    #print (sd_rain)

    prr=number_rr/(number_nr+number_rr)
    prn=number_rn/(number_rn+number_nn)
    #print (prr)
    #print (prn)

    return ([prr,prn,mean_rain,sd_rain])

