# Converts CSV to DataFrame to HTML

import numpy as np
import pandas as pd

#load csv and prepare dataframe.
file = "cities.csv"
cities_df = pd.read_csv(file, delimiter = ',')

#conversion and directory
cities_df.to_html('../resources/cities_data.html')
