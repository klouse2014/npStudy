import numpy as np
from datetime import datetime

def strdate2num(s):
    return datetime.strptime(s, '%Y-%m-%d').date().weekday()

def str2num(s):
    if s == '--':
        return 0
    else:
        return float(s)


def dayAverage():
    dates, close, w = np.loadtxt("data.csv", delimiter=',', usecols=(0,5,11), converters={0:strdate2num, 11:strExpect}, unpack=True)

    dayAver = []
    for i in range(5):
        index = np.where(dates == i)
        daysData = np.take(close, index)
        dayAver.append(np.mean(daysData))
        print "%d: %s" % (i, daysData)

    return dayAver









