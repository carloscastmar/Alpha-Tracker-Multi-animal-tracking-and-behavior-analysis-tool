# Import libraries
import pandas as pd
import numpy as np
import os

# List with all csv files
csv_path = os.path.join(os.getcwd(), "cleaned_data")
csv_files = os.listdir(csv_path)
csv_files_path = list(("cleaned_data/" + csv for csv in csv_files))

# Load all the datasets in one data frame
df = pd.concat(map(pd.read_csv, csv_files_path))

# Sort the data frame by the csv index and the png file name
df = df.set_index(["csv_index", "file_name"])
df = df.sort_index()

df["mouse1_topleft_x"] = pd.to_numeric(df["mouse1_topleft_x"], errors='coerce')

# Create new features for mouse 1
df["height_1"] = df["mouse1_topleft_y"] - df["mouse1_rightdown_y"]
df["width_1"] = df["mouse1_rightdown_x"] -  df["mouse1_topleft_x"]
df["x_1"] = df["mouse1_topleft_x"]
df["y_1"] = df["mouse1_rightdown_y"]

# Create new features for mouse 2
df["height_2"] = df["mouse2_topleft_y"] - df["mouse2_rightdown_y"]
df["width_2"] = df["mouse2_rightdown_x"] -  df["mouse2_topleft_x"]
df["x_2"] = df["mouse2_topleft_x"]
df["y_2"] = df["mouse2_rightdown_y"]

# Set the final columns
columns = df.columns[4:-8]
columns = (df.columns[-8:]).append(columns)

# Generate the final data frame with the desired columns
df = df[columns]

# Write the data frame into a csv file
df.to_csv("processed_data.csv")