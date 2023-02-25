import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Generate 100 values of an exponentially distributed random variate with a mean of 0.5

x = np.random.exponential(scale=0.5, size=100)

# Count the number of values in each subinterval of length 0.25
bins = np.arange(0, max(x), 0.25)
hist, bin_edges = np.histogram(x, bins=bins)


# Plot the histogram
plt.hist(x, bins=bins, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Exponentially Distributed Random Variates')
plt.show()

# Perform a Chi-square test to test the goodness-of-fit

chi_square, p_value = chisquare(hist)

# Comment on the test results
if p_value < 0.05:
    print("The Chi-square test indicates that the goodness-of-fit is not acceptable (p-value = {:.3f})".format(p_value))
else:
    print("The Chi-square test indicates that the goodness-of-fit is acceptable (p-value = {:.3f})".format(p_value))
