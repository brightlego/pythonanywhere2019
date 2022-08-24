import numpy as np
def floodevents(timeseries): #based on daily time series data
    count=0 #intial point
    for i in np.arange(0,len(timeseries)):#daily rain amounts in time series
        if timeseries[i] >20:# criteria that indicate a high probability of a flood event
            count=count + 1# value of a flood occured
    return(count)#total number of flood events