#!/usr/bin/env python3

    """This script must be executed from the raw_data directory
    """

# Import libraries
import pandas as pd
import numpy as np
import os
import sys


# Create a path that works for all OS
data_path = os.path.join(os.getcwd(), str(sys.argv[1]))

# Load the data
df = pd.read_csv(data_path)

# Set the file name as the index and rename its header
df = df.rename(columns={"Unnamed: 1": "csv_index", "Unnamed: 2": "file_name"})
df = df.set_index(["csv_index","file_name"])

# Delete the first two columns which do not provide useful info
df = df.iloc[:, 1:]

# Create a list with the first three rows concatenated to modify the headers
columns = []
for i in range(df.shape[1]):
    columns.append("_".join(list(df.iloc[:3, i])))

# Delete the first three rows
df = df.iloc[3:, :]

# Rename the columns
df.columns = columns

# Export the dataframe to csv
df.to_csv(os.path.join(os.pardir, "cleaned_data", "cleaned_" + str(sys.argv[1])))