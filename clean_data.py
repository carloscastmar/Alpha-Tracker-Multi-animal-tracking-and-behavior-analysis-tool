#!/usr/bin/env python3

"""This script must be executed from the raw_data directory. Type:
for FILE in *; do python3 ../clean_data.py $FILE; done"""

import pandas as pd
import os
import sys

# Get the file name from command line argument
file_name = sys.argv[1]

# Create the path to the file
data_path = os.path.join(os.getcwd(), file_name)

# Load the data into a Pandas DataFrame
df = pd.read_csv(data_path)

# Rename the columns
df = df.rename(columns={
    "Unnamed: 1": "csv_index", 
    "Unnamed: 2": "file_name"
})

# Set the csv index and file name as the DataFrame index
df = df.set_index(["csv_index", "file_name"])

# Drop the first column as it doesn't contain useful information
df = df.iloc[:, 1:]

# Get the first three rows to modify the headers
headers = df.iloc[:3, :].copy()

# Concatenate the first three rows to form the new headers
new_headers = []
for i in range(headers.shape[1]):
    new_header = "_".join(headers.iloc[:, i].tolist())
    new_headers.append(new_header)

# Drop the first three rows from the DataFrame
df = df.iloc[3:, :]

# Rename the columns with the new headers
df.columns = new_headers

# Save the cleaned data to a new file
cleaned_data_path = os.path.join(os.pardir, "cleaned_data", f"cleaned_{file_name}")
df.to_csv(cleaned_data_path)