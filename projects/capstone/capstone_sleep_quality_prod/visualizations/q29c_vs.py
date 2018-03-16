import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0, '../lib')
from visuals import Visuals


# Loadint the dataset
df = pd.read_csv("../2013SleepinAmericaPollExerciseandSleepRawDataExcel.csv")
columun = 'q29c'

# Removing unnecessary lines which contain unnecessary values
df = df[np.logical_not(df[columun].isin([97,98,99]))]

def make_histogram(num_of_classes,r_min,r_max, title):
        # Getting counts of each range
        vs = Visuals()
        ranges, sum_of_each_range =  vs.count_each_num_of_values_belongs_to_each_class(df[columun], num_of_classes,r_min,r_max,'tuples')

        # Making labels
        labels = list(ranges)

        # Setting the positions and width for the bars
        pos = range(len(sum_of_each_range))
        width = 0.25

        # Plotting bars
        fig, ax = plt.subplots(figsize=(10,5))

        # Configuration of the bars
        rects = plt.bar(
                pos,
                sum_of_each_range,
                width,
                alpha=0.5,
                color='#7C5852',
                label=labels
        )

        # Setting margins above each bar
        ax.margins(y=0.2)

        # Setting a x axis label
        ax.set_xlabel('Numer of Servings')

        # Set a y axis label
        ax.set_ylabel('Numer of Samples')

        # Setting a chart's title
        ax.set_title(title)

        # Setting position of the x ticks
        ax.set_xticks(pos)

        # Setting labels for the x ticks
        ax.set_xticklabels(labels)

        # Displays numbers of samples above each bar
        vs.autolabel(ax, rects)

        # Adding grid to the plot
        plt.grid()

        # Adjusting shape of the plot
        plt.subplots_adjust(top=0.85)

        # Showing the plot
        plt.show()

# To make histograms, I have to count nums of values which belong to each_range
# This is a setting for it.
# Output Example: OrderedDict([('0-200', 948), ('201-400', 31), ('401-600', 17)])
r_min = 0 # set a lower limit of range
r_max = 33 # set a higher limit of range
num_of_classes = 11 # The number of classes
title = 'q29c: Number of 12 ounce servings of caffeinated beverages \n the respondents take between 5:00 PM and 5:00 AM the next morning \n on an average weekday or workday'

# Showing the histogram
make_histogram(num_of_classes,r_min,r_max,title)

# Making a histogram which focuses on the range where a lot of respondents belongs to
r_min = 0 # set a lower limit of range
r_max = 10 # set a higher limit of range
num_of_classes = 11
title = title + "\n(Only shows the range between 0 to 10)"

# Showing the histogram
make_histogram(num_of_classes,r_min,r_max,title)

