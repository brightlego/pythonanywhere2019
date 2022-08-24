from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import random


def wrapper():
    """
    This wrapper defines a set of perturbations and a flood threshold
    and calculates then plots the [increased risk of floods (flood risk) / control] against the factor
    by which the mean rainfall intensity is scaled by.  As asked for in the practical this is done for
    a scenario in which the length of dry spells is increased (here prn = 0.5 prn_control)
    """
    # Setting the threshold and the two sets of perturbations (to the mean and the standard deviation)
    threshold = 20
    perturbations_mean = np.array(
        [[1, 0.75, 1, 1], [1, 0.75, 1.5, 1], [1, 0.75, 2, 1], [1, 0.75, 2.5, 1], [1, 0.75, 3, 1], [1, 0.75, 10, 1]])
    perturbations_sd = np.array(
        [[1, 0.75, 1, 1], [1, 0.75, 1, 1.5], [1, 0.75, 1, 2], [1, 0.75, 1, 2.5], [1, 0.75, 1, 3], [1, 0.75, 1, 10]])

    output_mean = np.array([0.0])
    output_sd = np.array([0.0])

    # Carrying out a control simulation, for which there is no perturbation to the statistics
    control = np.array([1, 1, 1, 1])
    floodrisk_control = perturb_stats(control, threshold)

    # Looping over perturbations_mean and perturbations_sd to determine flood risk for each set of statistics
   

    dims = np.shape(perturbations_mean)
    for i in np.arange(0, dims[0]):
        tmp = perturb_stats(perturbations_mean[i, ], threshold)
        output_mean = np.append(output_mean, tmp)

    dims = np.shape(perturbations_sd)
    for i in np.arange(0, dims[0]):
        tmp = perturb_stats(perturbations_sd[i, ], threshold)
        output_sd = np.append(output_sd, tmp)

    # Scaling by the control flood risk
    floodrisks_mean = output_mean[1:dims[0] + 1] / floodrisk_control
    floodrisks_sd = output_sd[1:dims[0] + 1] / floodrisk_control

    # Displaying the results
    fig = plt.figure()
    plt.plot(perturbations_mean[:, 2], floodrisks_mean)
    plt.plot(perturbations_sd[:, 3], floodrisks_sd)
    fig.savefig("floodrisk_vs_perturbed_mean.png")
    plt.close(fig)

    return ()


def perturb_stats(perturbation, threshold):
    """
    This function calculates the observed statistics, perturbs them, then
    calculates the resulting flood risk (for a user defined threshold) using a weather generator.

    :param perturbation: a vector of length 4 containing the factors that the four statistics of the weather
    (prob(rain|rain the day before), prob(rain|no rain the day before),mean intensity
    standard deviation intensity) should be scaled by.
    :param threshold: the threshold for which the user defines a flood has occurred
    :return: an array of flood risk values
    """

    

    # First we calculate the observed statistics by using the observed time series as an argument to the
    # calculate_statistics function
    timeseries = read_in_data("/home/emilyblack/session_4/obsdata.mtma33.txt")
    obs_stats = calculate_statistics(timeseries)

    # Now we calculate the perturbed statistics by scaling with the user-defined vector
    # perturbation

    perturbed_stats = obs_stats * perturbation

    # Now calculate the flood risk resulting from the perturbation
    flood_risk = calculate_flood_risk(perturbed_stats, threshold)

    return flood_risk


def calculate_flood_risk(stats, threshold):
    """
    Calculates the flood risk as defined by the likelihood of events over a threshold.

    :param stats: the statistics of the weather (prr,prn,mean intensity, standard deviation of intensity)
    :param threshold: the threshold above which a value is considered a flood risk
    :return: an array of flood risk values
    """

    length = 10000
   
    # Generate a time series with the given statistics of the weather
    output = gen_timeseries(stats, length)

    # Calculate the flood risk for the time series

    flood_risk = flood_risk_timeseries(output, threshold)
    return flood_risk


def read_in_data(filename):
    """
    opens a file named by the user and puts the data into an array

    :param filename: a user supplied file to open and read
    :return: an 1D array containing the values in the file
    """
   

    timeseries = np.loadtxt(filename)
    return timeseries


def calculate_statistics(timeseries):
    """
    outputs statistics of the weather for a user specified time series array

    :param timeseries: a 1D array of data
    :return: an array containing prob of rain, prob of no rain, mean and std dev
    """


    # initialising the variables
    count_rr = int(0)
    count_nr = int(0)
    count_nn = int(0)
    count_rn = int(0)
    rainydays = float(1.0)

    # At each point in the time series, we count dry/wet days where there has/hasn't been rainfall the day before.

    for i in np.arange(1, len(timeseries)):
        if (timeseries[i] > 0) & (timeseries[i - 1] > 0):
            count_rr += 1

        if (timeseries[i] == 0) & (timeseries[i - 1] > 0):
            count_nr += 1

        if (timeseries[i] == 0) & (timeseries[i - 1] == 0):
            count_nn += 1

        if (timeseries[i] > 0) & (timeseries[i - 1] == 0):
            count_rn += 1

        if timeseries[i] > 0:
            rainydays = np.append(timeseries[i], rainydays)

    # Based on the counts in the previous part of the code, we calculate prr (probability of rain given rain the day
    # before) and prn (probability of rain given no rain the day before).
    # Note that in order for this to work, we must have from __future__ import division at the top of the file.
    # otherwise, we run into problems of rounding to the nearest integer (eg 1/3 = 0)

    prr = count_rr / (count_rr + count_nr)
    prn = count_rn / (count_rn + count_nn)
    meanrain = np.mean(rainydays)
    sdrain = np.std(rainydays)

    return [prr, prn, meanrain, sdrain]


def gen_timeseries(stats, length_ts):
    """
    Reads in a vector containing the statistics of the weather and an integer giving the length of the time series

    :param stats: 1D array containing prob of rain, prob of no rain, mean and std dev
    :param length_ts: length of data timeseries
    :return: a 1D array of occurrence multiplied by intensity
    """
 

    # assign the elements of the array to the probabilities.
    prr = stats[0]
    prn = stats[1]
    meanrain = stats[2]
    sdrain = stats[3]

    # set up arrays for the generated intensity and occurrence
    gen_intensity = np.zeros(length_ts)
    gen_occurrence = np.zeros(length_ts)

    # initialise arrays with user given values.  These could be set as arguments to the function.
    gen_intensity[0] = 4.0
    gen_occurrence[0] = 1

    for i in np.arange(1, length_ts):

        # generate the intensity for each point in time
        gen_intensity[i] = np.abs(random.gauss(meanrain, sdrain))

        # generate the occurrence at each point in time

        if (gen_occurrence[i - 1] > 0) & (random.random() < prr):
            gen_occurrence[i] = 1

        if (gen_occurrence[i - 1] > 0) & (random.random() > prr):
            gen_occurrence[i] = 0

        if (gen_occurrence[i - 1] == 0) & (random.random() < prn):
            gen_occurrence[i] = 1

        if (gen_occurrence[i - 1] == 0) & (random.random() > prn):
            gen_occurrence[i] = 0

    # this is element-wise array multiplication to produce a product array
    outts = gen_occurrence * gen_intensity

    return outts


def flood_risk_timeseries(timeseries, threshold):
    """
    Counts the number of times a threshold is breached and outputs the risk of the threshold being breached.

    :param timeseries: the 1D array of data
    :param threshold: the threshold considered for flood risk
    :return: the risk of the threshold being breached
    """
    # initialise the flood counter array
    count_floods = np.zeros(len(timeseries))

    # loop over the time series changing the 0 in the counter array to 1 if the
    # threshold is breached
    for i in np.arange(1, len(timeseries)):
        if timeseries[i] > threshold:
            count_floods[i] = 1

        # the number of breaches is the sum of count_floods array.

    return np.sum(count_floods) / len(timeseries)
