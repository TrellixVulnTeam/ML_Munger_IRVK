from matplotlib import pyplot as plt
from numpy import sin

from random import seed, randint
from numpy.random import randn




#display the plot
# pyplot.show()

# save an image
# plot.savefig("my_image.png")

# line plot
# pyplog.plot(x, y)

#Good for time series data, sequence data
# ordering between obsertvations

# x = [x*0.1 for x in range(100)]

# function of x for y-axis
# y = sin(x)

# create the line plot
# plt.plot(x, y)
# plt.show()

# Create a bar chart
# useful for comparing multiple point quantities / estimations
# plt.bar(x, y)

#seed random generator
# seed(1)

# x = ['red', 'green', 'blue']

# quantities in each catagory
# y = [randint(0,100), randint(0, 100), randint(0,100)]
#create a bar chart
# pyplot.bar(x, y)
# show line plot
# pyplot.show()

# histogram
# valuable for summarizing distributoin of data samples
# seed(1)
# random numbers drawn from a Gaussian distribution
# x = randn(1000)
# create histogram plot
# can vary the number of bins. increasing can show more of a curve. 
# plt.hist(x, bins = 100)
# show line plot
# plt.show()

# box & whisker 
# summarize distribution of data sample
# x-axis represents data sample
# y-axis observation values
# box is middle 50% of dataset starting at 25th percentile, ends 75th percentile. (IQR),
# median is a line, whiskers expected range of sensible values in distribution (1.5 X IQR)

# create box and whisker plot
# plt.bloxplot(x)
#used for non-Gaussian distribution

# random numbers drawn from a Gaussian distribution
# x = [randn(1000), 5 * randn(1000), 10 * randn(1000)]
# create box and whisker plot
# plt.boxplot(x)
# show line plot
# plt.show()

# scatter plot
# used to summarize relationship 2 pared data examples.
# x first, y second sample
# plt.scatter(x, y)

# scatter plot matrix is dataset w/ more 2 variables.

x = 20 * randn(1000) + 100

y = x + (10 * randn(1000) + 50)

# create scatter plot
plt.scatter(x, y)
plt.show()
