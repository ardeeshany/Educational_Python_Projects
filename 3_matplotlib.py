import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("fmri").query("subject == 's13'")

# A container(fig) and objects(ax) for subplots -------------------------------
fig, ax = plt.subplots(1,2, sharex=True) # share x or y axis


# dot-line plot: for timeseries, rtc
ax[0].plot(data2.timepoint, data2.signal,
  marker = "o",
  linestyle = "--", 
  color = "#48C9B0")

ax[0].set_title("My Title")

ax[0].set_ylabel("My second Singal")

ax[0].set_xlabel("My first Time")
ax[0].set_xticklabels(data2.timepoint, rotation = 90)
ax[0].tick_params('x', colors = 'red')


plt.show()


# time series with a `datatime64` col type ----------------------------------
d1 = pd.read_csv("Election_info.CSV", 
                  parse_dates = ['election_date'],   # d1['election_date'] = pd.to_datetime(d1['election_date'])
                  index_col = "election_date")
                  
d1['evl'] = np.log(d1['event_number'])                 

fig, ax = plt.subplots()

ax.plot(d1.index, d1['event_number']) # matplotlib knows how to handle type datetime64: better x labeling
# new ax with sharing the same x
ax2 = ax.twinx()
ax2.plot(d1.index, d1['evl'],
        color = "red")
ax2.tick_params('y', colors = 'red')   
# annotate
ax2.annotate("Critical points",
      xy = (pd.Timestamp('2015-10-12'), 8.34),
      xytext = (pd.Timestamp('2015'), 8.25),
      arrowprops = {"arrowstyle": "<-", 
                    "color": "grey"})
plt.show()




# Quantitative Comparisons -----------------------------------
## bar-chart: summary number for each category
data = sns.load_dataset("titanic").dropna()

d3 = data.groupby('class')[['adult_male', 'alone']].agg(np.sum)

fig, ax = plt.subplots()

ax.bar(d3.index, d3.adult_male, label = "Male") # create bars for diff levels from a dataframe
ax.bar(d3.index, d3.alone, bottom = d3.adult_male, label = "Alone") # second bar, on top of first, with exactly the same levels
ax.bar("Mean of Age for Adult male", d3.adult_male.mean(),
      yerr = d3.adult_male.std()) # directly create one bar

ax.legend()

plt.show()

d4 = data.sort_values('age').groupby(['age'])[['fare']].agg([np.mean, np.std])
# Errorbar plot
fig, ax = plt.subplots()

ax.errorbar(d4.index, d4.iloc[:, 0], yerr = d4.iloc[:, 1])
ax.errorbar(d4.index, d4.iloc[:, 0])

plt.show()

## Histogram: one continuous variable
fig, ax = plt.subplots()

ax.hist(data.query('sex == "female"').age,
        label = "Female",
        histtype = 'step', 
        alpha = 0.7,
        bins = [0, 25, 50, 60, 80])

ax.hist(data.query('sex == "male"').age,
        label = "Male",
        histtype = 'step', 
        alpha = 0.7,
        bins = [0, 25, 50, 60, 80])


ax.legend()

plt.show()



# Box plot: one continuous variable
fig, ax = plt.subplots()

ax.boxplot([data.age, data.fare])  # two continuous variables
ax.set_xticklabels(["Age", "Fare"], rotation = 0)

plt.show()


# Scatter plot: comparison of two continuous variables
plt.style.use('ggplot')  # default, bmh, etc; for print using gray style
fig, ax = plt.subplots()

ax.scatter(data.query("sex == 'male'").age, data.query("sex == 'male'").fare,
      color = "red",
      label = "Male")

ax.scatter(data.query("sex == 'female'").age, data.query("sex == 'female'").fare,
      color = "blue",
      label = "Female")


# ax.scatter(data.age, data.fare,
#       c = data.pclass)    # color as the thirs continuous variable

ax.legend()

plt.show()


# Automating creation of a plot by using a for loop
fig, ax = plt.subplots()

for s in data.sex.unique():
  ax.bar(s, data[data.sex == s].mean(), yerr = data[data.sex == s].std())

plt.show()  
  


# Define a function for your repetitive plots

def my_plot(axes, x, y, col, label):
  axes.scatter(x, y, color = col, label = label)
  axes.set_xlabel("Time")
  
  

fig, ax = plt.subplots()
my_plot(ax, data.age, data.fare, "red", "Fare")
my_plot(ax, data.age, data.pclass, "blue", "pclass")
ax.legend()
plt.show()

# save your plot
fig.set_size_inches([3, 6])  # [width, height]
fig.savefig("Fare_vs_pclass.png", dpi = 300)
  





