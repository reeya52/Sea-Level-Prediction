import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def draw_plot():
    # Read data from file
    df = pd.read_csv("C:/Users/Reeya/OneDrive/Desktop/Learning/epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"].astype(float), df["CSIRO Adjusted Sea Level"])
    # plt.show()

    # Create first line of best fit
    result1 = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    slope1 = result1.slope
    intercept1 = result1.intercept

    x1 = list(range(1880, 2051))
    y1 = []

    for year in x1:
        y1.append(intercept1 + slope1 * year)
    
    ax = plt.plot(x1, y1, color='red')

    # Create second line of best fit
    new_x = df[df["Year"] >= 2000]["Year"]
    new_y = df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"]

    result2 = stats.linregress(new_x, new_y)
    slope2 = result2.slope
    intercept2 = result2.intercept

    x1 = list(range(2000, 2051))
    y1 = []

    for year in x1:
        y1.append(intercept2 + slope2 * year)
    
    ax = plt.plot(x1, y1, color='Green')
    plt.xticks(np.arange(1850, 2080, step=25).astype(float))

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('C:/Users/Reeya/OneDrive/Desktop/Learning/sea_level_plot.png')
    return plt.gca()


if(__name__) == "__main__":
    draw_plot()