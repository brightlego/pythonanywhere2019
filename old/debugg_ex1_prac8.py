#This script will plot a July temperature time series

from __future__ import division
import matplotlib.pyplot as plt

temperature_ts = np.genfromtxt('nh_temperature.txt')
plt.plot(temperature_ts[0,:],temperature_ts[:,6])
plt.xlabel('Year')
plt.ylabel('Temperature anomaly')
plt.show()