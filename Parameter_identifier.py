## This script takes the GAR vulnerability curve data points and fits a curve to them and derives the mu/sigma values
## It produces a csv file containing the GAR building identifier, mu, and sigma for the curves of interest.
## It will also create figures that can be used to sanity check the results, which I highly recommend doing.

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import norm
import matplotlib.pyplot as plt
import os

# Define the log-normal CDF
def lognorm_cdf(x, mu, sigma):
    return norm.cdf((np.log(x) - mu) / sigma)

# Initial guesses for mu and sigma (you can modify these if needed)
initial_guess = [1, 1]

# hazard should equal: Ash, Earthquake, Flood, Tsunami, or Wind depending on what curves you want to derive.
# If you want the script to iterate across all the perils do this: ["Ash", "Earthquake", "Flood", "Tsunami", "Wind"]
hazard = ["Ash"]

for i in hazard:
    # Path to the directory containing the CSV files from the GA Github repo. Change as appropriate.
    dir_path = 'GAR15_Regional_Vulnerability_Functions/' + i + '/'

    # List to store the results
    results = []

    # Loop over all CSV files in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith('.csv'):
            filename_without_extension = os.path.splitext(filename)[0]

            # Load the data
            df = pd.read_csv(os.path.join(dir_path, filename))

            # Remove zero values from 'Intensity'
            df = df[df['IM'] > 0]

            df['CDV'] = df['MEAN']
            df['Stdev+2'] = df['MEAN'] + (df['STD']*2)
            df['Stdev-2'] = df['MEAN'] - (df['STD']*2)

            # Perform the curve fitting
            popt, pcov = curve_fit(lognorm_cdf, df['IM'], df['CDV'], p0=initial_guess)
            popt_2, pcov_2 = curve_fit(lognorm_cdf, df['IM'], df['Stdev+2'], p0=initial_guess)
            popt_22, pcov_22 = curve_fit(lognorm_cdf, df['IM'], df['Stdev-2'], p0=initial_guess)

            exp_mu = np.exp(popt[0])
            exp_mu_2 = np.exp(popt_2[0])
            exp_mu_22 = np.exp(popt_22[0])

            # Generate x values for the fitted curve
            x_fit = np.linspace(df['IM'].min(), df['IM'].max(), 1000)
            x_fit_2 = np.linspace(df['IM'].min(), df['IM'].max(), 1000)
            x_fit_22 = np.linspace(df['IM'].min(), df['IM'].max(), 1000)

            # Calculate the fitted y values
            y_fit = lognorm_cdf(x_fit, popt[0], popt[1])
            y_fit_2 = lognorm_cdf(x_fit_2, popt_2[0], popt_2[1])
            y_fit_22 = lognorm_cdf(x_fit_22, popt_22[0], popt_22[1])

            # Add the results to the list. This is set to get the curve parameters for the CDV. Change if you want
                # the standard deviation curve parameters.
            results.append([filename_without_extension, exp_mu, popt[1]])

            # Plot the fitted curve
            plt.plot(x_fit, y_fit_2, color='green')
            plt.plot(x_fit, y_fit_22, color='green', label='2 STDev')
            plt.plot(x_fit, y_fit, color='black', label='Central damage value')

            # Add labels and a legend
            plt.xlabel('Ash load (kPa)')
            plt.ylabel('Damage Ratio')
            plt.legend()

            # Show the plot
            #plt.show()
            plt.savefig("Figures/" + i + "/" + filename_without_extension +'.png')
            plt.clf()

    # Convert the results to a DataFrame
    results_df = pd.DataFrame(results, columns=['Building_code', 'mu', 'sigma'])

    # Save the results to a new CSV file. This produces the parameters for the CDV curve.
    results_df.to_csv(i + '_CDV_parameters.csv', index=False)


