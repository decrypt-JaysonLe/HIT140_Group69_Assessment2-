import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest


df1 = pd.read_csv("dataset1.csv")
df2 = pd.read_csv("dataset2.csv")


#check missing values
print(df1.isnull().sum())   #41 missing values in 'habit'
print(df2.isnull().sum())   #no missing values

#check data types => start_time, rat_period, sunset_time, is object => transform to datetime
#print(df1.dtypes)
#print(df2.dtypes)


#mean, median, std
bat_landing_mean = st.mean(df1['bat_landing_to_food'])
print("bat landing mean: ", bat_landing_mean )

bat_landing_median = st.median(df1['bat_landing_to_food'])
print("bat landing median: ", bat_landing_median)

bat_landing_std = np.std(df1['bat_landing_to_food'])
print("bat landing std: ", bat_landing_std)



#compare bat_landing_to_food between risk=0 and risk=1
print("Bat landing to food between avoiding and taking risk\n", df1.groupby("risk")["bat_landing_to_food"].describe())

#histogram of risk = 0
group_risk_0 = df1[df1["risk"]==0]["bat_landing_to_food"]
plt.hist(group_risk_0, bins=20, alpha=0.5, label="Risk = 0 (Avoidance)")

#histogram of risk = 1
group_risk_1 = df1[df1["risk"]==1]["bat_landing_to_food"]
plt.hist(group_risk_1, bins=20, alpha=0.5, label="Risk = 1 (Taking)")

#plot histogram of Bat landing to food by risk distribution
plt.title("Histogram of Bat landing to food by Risk")
plt.xlabel("Bat landing to food time (seconds)")
plt.ylabel("Frequency of Bats")
plt.legend()
plt.show()


#two sample t-test
t_stats, p_val = stats.ttest_ind(group_risk_0, group_risk_1, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.2f" % t_stats) 

print("\n Computing p-value ...")
print("\t p-value: %.9f" % p_val)   

print("\n Conclusion:")
if p_val < 0.05:
    print("\t We reject the null hypothesis.")
    print("\t => There is a significant difference in approach times between the two risk groups.")
else:
    print("\t We accept the null hypothesis.")
    print("\t => There is no significant difference in approach times between the two risk groups.")


#Crosstab for risk and reward => avoid: 84% reward, take risk: 22% reward
table_prop = pd.crosstab(df1["risk"], df1["reward"], normalize="index")
print("Crosstab cho risk and reward:\n", table_prop)

#z-test for proportions
count = np.array([
    df1[df1["risk"]==0]["reward"].sum(),    # total reward of risk=0
    df1[df1["risk"]==1]["reward"].sum()     # total reward of risk=1
])
print("count = ", count)
#total of observations in each risk
total = np.array([
    len(df1[df1["risk"]==0]),
    len(df1[df1["risk"]==1])
])
print("total = ", total)

z_stats, p_value = proportions_ztest(count, total)
print("\n Computing z* ...")
print("\t z-statistic (z*): %.2f" % z_stats)    #z*=18.85

print("\n Computing p-value ...")
print("\t p-value: %.4f" % p_value)  

print("\n Conclusion:")
if p_value < 0.05:
    print("\t We reject the null hypothesis.")
    print("\t => There is a statistically significant difference in the reward rates between the two risk groups.")
else:
    print("\t We accept the null hypothesis.")
    print("\t => There is not enough evidence to suggest that the two risk groups differ in their reward rates.")


#Total minutes of rats' presence every 30 minutes
print("\nTotal null in rat_minutes: ", df2['rat_minutes'].isnull().sum())   #0 null
print("Mean of rat_minutes: ", df2["rat_minutes"].mean())     #2mins