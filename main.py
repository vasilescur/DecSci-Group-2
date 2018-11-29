"""
Data analysis program for Decision Science 101 research project - Group 9

Author: Radu Vasilescu
Date:   2018-11-07
"""

import pandas as pd
import numpy as np

from scipy import stats

# ===== Data Ingest ===== #

# Read the data from the data file
data = pd.read_csv('data.csv')

# ===== Data Processing ===== #

# Convert into percentage increases
data['inc_first'] = (data['exp_first'] - data['base_first']) / data['base_first']
data['inc_last'] = (data['exp_last'] - data['base_last']) / data['base_last']

# Extract the two sets to do the t-test
inc_first = data['inc_first'].dropna()
inc_last = data['inc_last'].dropna()

# ===== Statistical Analysis ===== #

# Run the t-test
inc_t, inc_p = stats.ttest_ind(inc_first, inc_last)

# ===== Results Reporting ===== #

# Display Results
print('Increase (first) vs. Increase (last): ')
print('T = ' + str(inc_t))
print('P = ' + str(inc_p))