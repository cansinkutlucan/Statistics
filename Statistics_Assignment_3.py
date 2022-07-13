import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)
################################################################
# EXERCISE 1
# . General   :  Mu = 13.20  sigma = 2.5
#   A company : n=40 , Mu=12.20 alfa = 0.01

# H0: Mu1  = 12.20 
# H1: Mu1 < 12.20

xbar  = 12.2
sigma = 2.5
n = 40
mu = 13.2

# Under the assumption of normal distribution;
z = (xbar-mu) / (sigma / np.sqrt(n))  # statistic : -2.5298221281347035
p = stats.norm.cdf(z)                 #         p : 0.005706018193000826
p  
# p<0.01. Reject H0. The company can be accused of paying substandart wages

################################################################
# EXERCISE 2
df = pd.read_csv("soil - Sheet1.csv")
df

# Hypothesis
# H0:  The soils appear doesn't differ with respect to average
# H1:  The soils appear to differ with respect to average

# Assumptions
# Normality
# H0: The sampling distribution of the mean is normal
# H1: The sampling distribution of the mean is not normal

test_stat, pvalue = stats.shapiro(df["Soil1"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Fail to reject H0. The sampling distribution of the mean is normal

test_stat, pvalue = stats.shapiro(df["Soil2"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Fail to reject H0. The sampling distribution of the mean is normal

# Variance
# H0: The sampling variance is normal
# H1: The sampling variance is not normal

test_stat, pvalue = stats.levene(df["Soil1"].dropna(), df["Soil2"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Fail to reject H0. The sampling variance is normal

# Test statistic
test_stat, pvalue = stats.ttest_ind(df["Soil1"].dropna(),df["Soil2"]) # varyans homojenliği = True
# (5.1681473319343345, 2.593228732352821e-06)
# p<0.01. Reject H0. The soils appear to differ with respect to average

################################################################
# EXERCISE 3

df_ = pd.read_csv("2015 PISA Test - Sheet1.csv")
df_.head()
df_.shape
df_.groupby(["Continent_Code"]).describe()

# Under assumption of normality and equal variances
# H0: There is no any difference (on the average) for the math scores among European (EU) and Asian (AS)
# H1: there is any difference (on the average) for the math scores among European (EU) and Asian (AS)

test_stat, pvalue = stats.ttest_ind(df_.loc[df_["Continent_Code"] == "EU", "Math"],
                              df_.loc[df_["Continent_Code"] == "AS", "Math"],
                              equal_var=True) # varyans homojenliği = True

# (0.870055317967983, 0.38826888111307345)
# p>0.05. Fail to reject H0. There is no any difference ...

df_new = df_[(df_["Continent_Code"] == 'EU') | (df_["Continent_Code"] == 'AS')]
sns.boxplot(x=df_new["Continent_Code"], y=df_new['Math'])

################################################################
# EXERCISE 4
df1 = pd.read_csv("weight - Sheet1.csv")
df1.head()
df1["dbar"] = df1["starting"] - df1["ending"]

# H0: dbar = 0
# H1: dbar > 0

stats.ttest_rel(df1.starting, df1.ending, alternative = "greater")
# Ttest_relResult(statistic=2.6780834840499255, pvalue=0.00900646517506626)
# p < 0.01. Reject H0. It means diet program was effective























