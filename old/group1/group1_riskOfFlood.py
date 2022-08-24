import numpy as np

def group1_riskOfFlood(timeseries):
    number_flood = 1
    days = len(timeseries)
    for i in np.arange(0, days):
        if timeseries[i] > 20:
            number_flood = number_flood + 1
    riskOfFlood = float(number_flood / days)

    return riskOfFlood

