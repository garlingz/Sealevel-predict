import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df_scatter = df.copy()

    fig, ax = plt.subplots(figsize=(8, 6))
    #    Create first line of best fit
    x= df_scatter['Year']
    y= df_scatter['CSIRO Adjusted Sea Level']

    #   Extended years so that the prediction can go on past data
    years_extended = np.arange(1880, 2051)
    years_2000_to_2050 = np.arange(2000, 2051)

    # Creating the plot(s)
    reg = stats.linregress(x, y)
    predicted_sea_levels = reg.intercept + reg.slope * years_extended

    markersize = 100
    plt.scatter(x, y, label= 'CSIRO Adjusted Sea Level', marker='.', s= markersize)
    #plt.plot(x, reg.intercept + reg.slope * x, 'r', label= 'Prediction')
    plt.plot(years_extended, predicted_sea_levels, 'r', label= 'All Data Prediction')

    newx = df_scatter[df_scatter['Year'] >= 2000]['Year']
    newy = df_scatter[df_scatter['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    newreg = stats.linregress(newx, newy)
    new_predict = newreg.intercept + newreg.slope * years_2000_to_2050

    plt.plot(years_2000_to_2050, new_predict, 'g', label= "2000's Data with Future Predictions")

    # Labels and Legends
    plt.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()