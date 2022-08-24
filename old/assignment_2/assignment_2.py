from scipy.stats.stats import pearsonr, linregress
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import datetime


def task_one():
    """
    This is an example of a wrapper function
    Read in data from lusaka_ccd_gauge.txt.  You will need to edit this with the path fof your data

    :return: none
    """
    baresoil_ts = read_in_data('/home/emilyblack/assignment_2/baresoil_temperature_1962_2010_dl.nc','tstar_gb')
    broadleaftree_ts = read_in_data('/home/emilyblack/assignment_2/broadleaftree_temperature_1962_2010_dl.nc','tstar_gb')

    dates = np.arange(1962,2011,1.0/12.0)

#    x = np.arange(0,1000,1)
 #   y = 285+5*np.sin(x/5.)+np.random.randn(1000)
 #   datelist = [datetime.datetime(1982,1,1)+i*datetime.timedelta(days=10) for i in range(1000)]
 #   start_date = 1982.
 #   end_date = datelist[-1].year+datelist[-1].timetuple().tm_yday/365.
 #   datelist_new = np.linspace(start_date,end_date,len(datelist))
 #   plt.plot(datelist_new,y)
 #   plt.xticks(np.arange(1982,2010,2))
 #   plt.show()

    fig = plt.figure()
    plt.plot(dates,baresoil_ts)
    plt.plot(dates,broadleaftree_ts)
    plt.xticks(np.arange(1962,2010,5))
    fig.savefig('graph_one.png')

    fig = plt.figure()
    plt.scatter(baresoil_ts,broadleaftree_ts)
    fig.savefig('graph_two.png')

    return baresoil_ts, broadleaftree_ts
    # loop over months

    #return calibration_params_all

def task_two():
    """
    This is an example of a wrapper function
    Read in data from lusaka_ccd_gauge.txt.  You will need to edit this with the path fof your data

    :return: none
    """
    baresoil_ts = read_in_data('/home/emilyblack/assignment_2/baresoil_temperature_1962_2010_dl.nc','tstar_gb')
    broadleaftree_ts = read_in_data('/home/emilyblack/assignment_2/broadleaftree_temperature_1962_2010_dl.nc','tstar_gb')
    clim_bs = np.zeros(12)
    clim_bl = np.zeros(12)
    for i in np.arange(1,13):
        clim_bs[i-1] = np.mean(extract_month(baresoil_ts,i))
        clim_bl[i-1] = np.mean(extract_month(broadleaftree_ts,i))

    fig = plt.figure()
    plt.plot(clim_bs)
    plt.plot(clim_bl)
    fig.savefig('graph_three.png')

    # loop over months
    return clim_bs, clim_bl
    #return calibration_params_all



def read_in_data(filename,variable):
    """
    readindata reads in numerical data into a numpy array from an ascii text file

    :param filename: the fully qualified pathname of the data file
    :return: the data from the file
    """
    input_data_nc = Dataset(filename, mode='r')
    input_data_out = input_data_nc.variables[variable][:,:]
    input_data = input_data_out[:,0,0]
    return input_data


def extract_month(in_data, month):
    """
    Extracts a time series of data for a single month from an input array
    :param in_data: input array with four columns of data:  year, month, ccd, rain gauge measurement
    :param month: the month for which to extract data
    :return: the data for the specified month
    """

    # the monthly data is extracted by selecting every 12th row, starting from the month of interest
    # note that python arrays start at zero
    month_data = in_data[np.arange(month-1, len(in_data), 12)]
    return month_data


def calibrate_data(in_data):
    """
    Takes an input file of format year, month, ccd (dependent variable, i.e. predictor),
    gauge measurement (independent variable, i.e. predictand)
    :param in_data: input file
    :return: calibration parameters
    """

    # slice the array to select the gauge and ccd data
    gauge = in_data[:, 3]
    ccd = in_data[:, 2]

    # derive a linear model using the intrinsic function linregress, imported from the scipy package
    linear_model = linregress(ccd, gauge)
    a1 = linear_model[0]
    a0 = linear_model[1]

    # return a tuple containing the calibration parameters
    return a0, a1


def make_rfe(a0, a1, ccd):
    """
    This function makes a time series of rainfall estimates, based on ccd observations and calibration parameters.
    :param a0: calibration parameter
    :param a1: calibration parameter
    :param ccd: observations
    :return: rainfall estimate timeseries
    """

    rfe = a0 + (a1 * ccd)
    return rfe
