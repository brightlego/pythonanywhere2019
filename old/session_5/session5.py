from scipy.stats.stats import pearsonr, linregress
import numpy as np
import matplotlib.pyplot as plt

def taskone():
#this is an example of a wrapper function
#read in data from lusaka_ccd_gauge.txt.  You will need to edit this with the path fo your data
    allmonth_ts = readindata('session_5/lusaka_ccd_gauge.txt')
#months is an array containing the months of interest for this practical (October - March)
    months = np.array([10,11,12,1,2,3])
#initialize an output array
    calibration_params_all = np.zeros(shape=(6,2))

#loop over months
    for i in np.arange(0,6):
#extract a time series for each month
        month = months[i]
        singlemonth_ts = extractmonth(allmonth_ts,month)
#carry out a calibration for each month and put the data in the output array
        calibration_params_month = calibratedata(singlemonth_ts)
        calibration_params_all[i,0] = calibration_params_month[0]
        calibration_params_all[i,1] = calibration_params_month[1]
#the output is an array containing calibration parameters for each month
    return(calibration_params_all)


def readindata(filename):
#readindata reads in numerical data into a numpy array from an ascii text file
    inputdata = np.genfromtxt(filename)
    return(inputdata)

def extractmonth(indata,month):
#extractmonth extracts a time series of data for a single month from an input array indata
#indata is an array with four columns of data:  year, month, ccd, rain gauge measurement

#the monthly data is extracted by selecting every 12th row, starting from the month of interest
#note that python arrays start at zero
    monthdata = indata[np.arange(month-1,len(indata[:,0]),12),:]
    return(monthdata)

def calibratedata(indata):
#calibratedata takes an input file of format year, month, ccd (dependent variable, i.e. predictor),
#gauge measurement (independent variable, i.e. predictand)

#slice the array to select the gauge and ccd data
    gauge = indata[:,3]
    ccd = indata[:,2]

#derive a linear model using the intrinsic function linregress, imported from the scipy package
    linmodel=linregress(ccd,gauge)
    a1 = linmodel[0]
    a0 = linmodel[1]

#return a tuple containing the calibration parameters
    return(a0,a1)

def makerfe(a0,a1,ccd):
#this function makes a time series of rainfall estimates, based on ccd observations and calibration parameters a0 and a1

    rfe = a0 + a1*ccd
    return(rfe)

