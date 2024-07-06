# About Matplotlib

Here we are only using it to plot our data, to get familiar with plotting data see this: [Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

## Styling the Chart

Let's look at a couple of methods that will help us style our chart:
- `.figure()` - allows us to resize our chart
- `.xticks()` - configures our x-axis
- `.yticks()` - configures our y-axis
- `.xlabel()` - add text to the x-axis
- `.ylabel()` - add text to the y-axis
- `.ylim()` - allows us to set a lower and upper bound 

# What all I learnt from this lesson?
- used `.groupby()` to explore the number of posts and entries per programming language
- converted strings to Datetime objects with `pd.to_datetime()` for easier plotting
- reshaped our DataFrame by converting categories to columns using `.pivot()`
- used `.count()` and `isna().values.any()` to look for NaN values in our DataFrame, which we then replaced using `.fillna()`
- created (multiple) line charts using `.plot()` with a `for-loop`
- styled our charts by **changing the size, the labels, and the upper and lower bounds** of our axis.
- added a **legend** to tell apart which line is which by colour
- smoothed out our time-series observations with `.rolling().mean()` and plotted them to better identify trends over time.