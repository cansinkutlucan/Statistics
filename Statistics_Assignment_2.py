import numpy as np
from scipy import stats

# 1. Unknown population mean and a population standard deviation of 3 points
sigma = 3
n1 = 36
x_bar= 68
std_error1 = sigma / np.sqrt(n1)
# confidence level: %90

# Population standard is known
stats.norm.interval(0.90, loc=x_bar, scale = std_error1)      # ci # (67.17757318652427, 68.82242681347573)

# 2.Unknown population mean and Unknown population variance
n2 = 130
x_bar = 98.25
s = 0.73
std_error2 = s/np.sqrt(n2) 
# confidence level: %99

# Population variance is unknown
stats.t.interval(0.99, df=n2-1, loc=x_bar, scale= std_error2) # ci # (98.08260738705933, 98.41739261294067)

# 3.Unknown population mean and Unknown population variance
n3 = 500
x_bar = 5.4
s = 3.1
std_error3 = s/np.sqrt(n3) 
# confidence level: %95

# Population variance is unknown
stats.t.interval(0.95, df=n3-1, loc=x_bar, scale= std_error3) # ci # (5.127617354510309, 5.672382645489692)








 