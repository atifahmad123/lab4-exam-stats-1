
import pandas as pd
import numpy as np
from scipy import stats

scores = pd.Series([72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69])

# Display descriptive statistics
print(scores.describe())

# Drop missing values before calculating skewness and kurtosis
scores_dropped = scores.dropna()
print("Skewness:", stats.skew(scores_dropped))
print("Kurtosis:", stats.kurtosis(scores_dropped))

# Count missing scores
print("Missing values:", scores.isnull().sum())

# Fill missing scores with the Series mean
scores_filled = scores.fillna(scores.mean())
print("Filled scores:")
print(scores_filled)
