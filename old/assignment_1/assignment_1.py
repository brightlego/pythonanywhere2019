from scipy.stats.stats import pearsonr, linregress
import numpy as np
import matplotlib.pyplot as plt

def taskthree():
    indata = readindata('assignment_1/assignment_1_datafile.txt')
    decdec = makeprediction(indata,12,0)
    decdecmodel = makemodel(decdec[0],decdec[1])
    prediction = decdecmodel[2] + decdecmodel[3] * -0.6
    print(prediction)


def tasktwo():
    indata = readindata('assignment_1/assignment_1_datafile.txt')

#makeprediction returns the predictor and the predictand
    aprapr = makeprediction(indata,4,0)
    augaug = makeprediction(indata,8,0)
    decdec = makeprediction(indata,12,0)

#makemodel returns the predictand and the prediction
    apraprmodel = makemodel(aprapr[0],aprapr[1])
    augaugmodel = makemodel(augaug[0],augaug[1])
    decdecmodel = makemodel(decdec[0],decdec[1])

#lead time three months relationships - use makeprediction with leadtime set to three
    janapr = makeprediction(indata,4,3)
    mayaug = makeprediction(indata,8,3)
    sepdec = makeprediction(indata,12,3)

#makemodel returns the predictand and the prediction
    janaprmodel = makemodel(janapr[0],janapr[1])
    mayaugmodel = makemodel(mayaug[0],mayaug[1])
    sepdecmodel = makemodel(sepdec[0],sepdec[1])


    fig = plt.figure()
    plt.subplot(2,2,1)
    plt.plot(apraprmodel[0],apraprmodel[1],'bo')
    plt.subplot(2,2,2)
    plt.plot(augaugmodel[0],augaugmodel[1],'bo')
    plt.subplot(2,2,3)
    plt.plot(decdecmodel[0],decdecmodel[1],'bo')


    fig.savefig("fig2.1.png")
    fig = plt.close()

    fig = plt.figure()
    plt.subplot(2,2,1)
    plt.plot(janaprmodel[0],janaprmodel[1],'bo')
    plt.subplot(2,2,2)
    plt.plot(mayaugmodel[0],mayaugmodel[1],'bo')
    plt.subplot(2,2,3)
    plt.plot(sepdecmodel[0],sepdecmodel[1],'bo')


    fig.savefig("fig2.2.png")
    fig = plt.close()



def taskone():

    indata = readindata('assignment_1/assignment_1_datafile.txt')
#contemporaneous relationships - use makeprediction with leadtime set to zero
    aprapr = makeprediction(indata,4,0)
    augaug = makeprediction(indata,8,0)
    decdec = makeprediction(indata,12,0)

#scatter plots for contemporaneous relationships
    fig = plt.figure()
    plt.subplot(2,2,1)
    plt.plot(aprapr[0],aprapr[1],'bo')
    plt.subplot(2,2,2)
    plt.plot(augaug[0],augaug[1],'bo')
    plt.subplot(2,2,3)
    plt.plot(decdec[0],decdec[1],'bo')
    fig.savefig("figone.png")
    fig = plt.close()

#scatter plots for lead time three months
    fig = plt.figure()
    plt.subplot(2,2,1)
    plt.plot(janapr[0],janapr[1],'bo')
    plt.subplot(2,2,2)
    plt.plot(mayaug[0],mayaug[1],'bo')
    plt.subplot(2,2,3)
    plt.plot(sepdec[0],sepdec[1],'bo')
    fig.savefig("figtwo.png")
    fig = plt.close()




def readindata(filename):
#filename gives the name of a file with four columns of data:  year, month, dam inflow, nino3.4 anomaly
    contents = np.genfromtxt(filename)
    return(contents)

def extractmonth(indata,month):
#indata is an array with four columns of data:  year, month, dam inflow, nino3.4 anomaly
    outdata = indata[np.arange(month-1,len(indata[:,0]),12),:]
    return(outdata)

def makeprediction(indata,month,leadtime):
    if month-leadtime > 0:
        tmp = extractmonth(indata,month-leadtime)
        predictor = tmp[:,3]
        tmp = extractmonth(indata,month)
        predictand = tmp[:,2]
    else:
        tmp = extractmonth(indata,(12-leadtime+month))
        predictor = tmp[np.arange(0,len(tmp[:,3])-1),3]
        tmp = extractmonth(indata,1)
        predictand = tmp[np.arange(1,len(tmp[:,3])),2]

    fig = plt.figure()
    plt.plot(predictor,predictand,'bo')
    fig.savefig("myplot.png")
    fig = plt.close()


    return(predictor,predictand)

def makemodel(predictor,predictand):
    model = linregress(predictor,predictand)
    prediction = model[1] + model[0]*predictor
    return(prediction,predictand,model[1],model[0])



