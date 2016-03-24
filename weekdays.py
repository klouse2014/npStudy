import numpy as np
from datetime import datetime


def strdate2num(s):
    return datetime.strptime(s, '\"%Y-%m-%d').date().weekday()

dates, close = np.loadtxt("data.csv", delimiter=',', usecols=(0,5), converters={0:strdate2num}, unpack=True)

print dates, close
