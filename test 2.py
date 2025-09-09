import scipy.stats as st
import pandas as pd 
import math
import statistics as stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

df2 = pd.read_csv('dataset2.csv')

with_rat = df2[df2['rat_arrival_number'] > 0]
without_rat = df2[df2['rat_arrival_number'] == 0]
#histogram rats are around 
nummber_of_bats = with_rat['bat_landing_number']
#print(nummber_of_bats.describe())
max_bats = np.max(nummber_of_bats)
min_bats = np.min(nummber_of_bats)
range = max_bats - min_bats
median_bats_with_rats = stats.median(nummber_of_bats)
bin_width = 5
bin_count = int(range/bin_width)
plt.hist(nummber_of_bats, color='blue', edgecolor='black', bins=bin_count)
plt.title("The number of bats per 30 mins when rats appears")
plt.xlabel("The number of bats")
plt.ylabel("The numbers of times when rats appears")
plt.show()
#histogram when rats are not around 
nummber_of_bats2 = without_rat['bat_landing_number']
#print(nummber_of_bats2.describe())
max_bats2 = np.max(nummber_of_bats2)
min_bats2 = np.min(nummber_of_bats2)
range2 = max_bats2 - min_bats2
median_bats_without_rats = stats.median(nummber_of_bats2)
bin_width2 = 5
bin_count2 = int(range2/bin_width2)
plt.hist(nummber_of_bats2, color='blue', edgecolor='black', bins=bin_count2)
plt.title("The number of bats per 30 mins when rats does not appear")
plt.xlabel("The number of bats")
plt.ylabel("The numbers of times when rats does not appear")
plt.show()
# Comparison of the medians
print(f'The median of bats number when rats were not around is: {median_bats_without_rats}')
print(f'Meanwhile, the median of bats number when rats were around is: {median_bats_with_rats}')
# Return the result of the comparison:
if median_bats_with_rats >= median_bats_without_rats:
    print('The comparison showed that the number of bats did not decline when rats appear => bats perceive rats just as competitors')
else:
    print('The comparison showed that the number of bats declined when rats appear => bats may seem rats as predator')
# Nonparametric test for skewed distribution
test = mannwhitneyu(nummber_of_bats, nummber_of_bats2)
if test.pvalue < 0.05:
    print('We reject the null hypothesis')
else:
    print('We accept the null hypothesis')
