from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import and replace index with ID column
df = pd.read_csv(r'/mnt/LinuxStorage/School/SIT384/4.1p/attack-type-frequency.csv', index_col=0, engine='python')
# group and sum number of attacks and frequency into their respective categories

# bar chart
labels = ['DOS', 'U2R', 'R21', 'PROBE']
fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
x_pos = np.arange(len(df['number_of_attack']))
# creates the bar chart with initial values: x_axis, y_axis, args..
ax.bar(x_pos, df['number_of_attack'], align='center', color=['blue', 'red', 'green', 'yellow'])
# overall chart labels
ax.set_xlabel("Hair Colour")
ax.set_ylabel("Number of participants")
ax.set_title("Hair Colour Distribution")
# this sets the x axis and the label for each bar
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
plt.show()

# pie chart
labels = ['DOS', 'U2R', 'R21', 'PROBE']
fig, ax = plt.subplots(figsize=(10, 10))
# creates the bar chart with initial values: values, labels, etc.
ax.pie(df['number_of_attack'], labels=labels, autopct='%1.1f', colors=['blue', 'red', 'green', 'yellow'])
plt.show()
