# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:53:31 2020

@author: MADCAT
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


x = [16,15,12,15,10,16,16,15,15,15,12,18,12,14,10,18,15,14,15,15]

y = [10,9,7,9,8,9,5,4]




print("mean =", np.mean(x))
print("median =", np.median(x))
print("mode =", stats.mode(x))



ex2 = [10,9,7,9,8,9,5,4]

print("mean =", np.mean(ex2))
print("Variance = ", (np.var(ex2)))
print("Std = ", (np.std(ex2)))
print(10 * "--")
salary = [120, 80, 85, 85, 80, 83, 100, 105, 105, 85, 75, 125, 120, 105, 85, 80, 95, 90, 95, 85, 80, 85, 120, 100, 105, 90]

print("mean =", np.mean(salary))
print("median =", np.median(salary))
print("mode =", stats.mode(salary))
print("Range =", (np.max(salary)-np.min(salary)))
print("IQR =", stats.iqr(salary))
print("Variance =", (np.var(salary)))
print("Std =", (np.std(salary)))

plt.plot(sorted(salary))
fig, ax = plt.subplots()

ax.boxplot(salary)
q1 = np.percentile(salary,25)
q3 = np.percentile(salary,75)

low_out = q1 - (stats.iqr(salary) * (3/2))
high_out = q3 + (stats.iqr(salary) * (3/2))

print(low_out)
print(high_out)
print(np.max(salary))
print(np.min(salary))
