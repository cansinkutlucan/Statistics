#%% Descriptive Statistics
# [mean, mode, median , std deviation, variance, range ]

#%% Import NumPy, SciPy, and Pandas
import numpy as np
import pandas as pd
from scipy import stats

#%% Randomly generate 1,000 samples from the normal distribution using np.random.normal()(mean = 100, standard deviation = 15)
samples = np.random.normal(100, 15, 1000)
samples

#%% Compute the mean, median, and mode
list1 = [102, 33, 26, 27, 30, 25, 33, 33, 24]
print("mean: ",np.mean(list1))
print("median: ",np.median(list1))
print("mode: ",stats.mode(list1))

#%%Compute the min, max, Q1, Q3, and interquartile range
list1 = [102, 33, 26, 27, 30, 25, 33, 33, 24]
print("min:", (np.min(list1)))
print("max:", (np.max(list1)))
print("Q1:", (np.percentile(list1, 25)))
print("Q3:", (np.percentile(list1, 75)))
print("IQR:", (stats.iqr(list1)))

#%% Compute the variance and standard deviation
print("variance: ", np.var(list1))
print("std deviation: ", np.std(list1))

#%% Compute the skewness and kurtosis
from scipy import stats
list1 = [102, 33, 26, 27, 30, 25, 33, 33, 24]
print("skewness: ", stats.skew(list1, bias=False))
print("kurtosis: ", stats.kurtosis(list1, bias=False))

#%% Create an array x of integers between 10 (inclusive) and 20 (exclusive). Use np.arange()
x = np.arange(10,20)
x

#%% Then use np.array() to create a second array y containing 10 arbitrary integers.
y = np.array([2,15,4,23,6,37,8,19,10,14])
y

#%%Once you have two arrays of the same length, you can compute the correlation coefficient between x and y
r = np.corrcoef(x, y)
r[0,1]

#%%Pandas Correlation Calculation
x = pd.Series(range(10, 20))
y = pd.Series([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

#%% Call the relevant method to calculate Pearson's r correlation.
r = print("correlation coefficient and p-value: ", stats.pearsonr(x, y))

#%%OPTIONAL. Call the relevant method to calculate Spearman's rho correlation.
rho = print("correlation coefficient and p-value: ", stats.spearmanr(x, y))

#%% Seaborn Dataset Tips
#Import Seaborn Library
import seaborn as sns

#%% Load "tips" dataset from Seaborn
tips = sns.load_dataset("tips")

#%%Generate descriptive statistics include those that summarize the central tendency, dispersion
tips.describe()

#%% Call the relevant method to calculate pairwise Pearson's r correlation of columns
tips.corr()
