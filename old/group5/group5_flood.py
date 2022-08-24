import numpy as np
import matplotlib.pyplot as plt

def floodcounter(threshold,filename = "/home/tomclaxton/ecb/obsdata.mtma33.txt"):
    rainfall = np.genfromtxt(filename)
    length_ts = len(rainfall)
    #np.sum(rainfall>threshold) counts the number of floods without a loop
    flood = 0
    for i in np.arange(0,length_ts):
        if rainfall[i] > threshold:
            flood += 1

    return flood


def floodcounter2(threshold,filename = "/home/tomclaxton/ecb/obsdata.mtma33.txt"):
    rainfall = np.genfromtxt(filename)
    length_ts = len(rainfall)
    flood = 0
    rainave = np.array([])
    for i in np.arange(0,length_ts-5):
        rainave = np.append(rainave,sum(rainfall[i:i+5]))
        if sum(rainfall[i:i+5]) > threshold:
            flood +=1

            print(rainfall[i:i+5])

    fig = plt.figure()
    plt.plot(rainave)
    plt.plot((rainave>threshold)*rainave, "r")
    plt.xlabel("time")
    plt.ylabel("rainfall average")
    fig.savefig("/home/tomclaxton/session3/rainfall2.png")
    plt.close(fig)




    return flood

def floodcounter3(threshold,filename = "/home/tomclaxton/ecb/obsdata.mtma33.txt"):
    rainfall = np.genfromtxt(filename)
    length_ts = len(rainfall)
    #np.sum(rainfall>threshold) counts the number of floods without a loop
    flood = 0
    for i in np.arange(0,length_ts):
        if rainfall[i] > threshold:
            flood += 1

    fig = plt.figure()
    plt.plot(rainfall)
    plt.plot((rainfall>threshold)*rainfall, "r")
    plt.xlabel("time")
    plt.ylabel("rainfall")
    fig.savefig("/home/tomclaxton/session3/rainfall.png")
    plt.close(fig)

    return flood

