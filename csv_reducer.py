import numpy as np
import pandas as pd
import os

#Read CSV file and return a DataFrame
def read_csv_file(file_path):
    """
    Reads a CSV file and returns a DataFrame.
    
    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing the CSV data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    df = pd.read_csv(file_path)
    return df
user_input = input("Enter filename (e.g., chicago.csv): ")
df = read_csv_file(user_input)

# Print the size of the DataFrame
print(f"DataFrame size: {df.shape}")

# Prompt the user to select the truncated csv file size
def get_truncated_csv_size(df, size):
    """
    Returns a truncated DataFrame based on the specified size.
    
    Args:
        df (pd.DataFrame): The original DataFrame.
        size (int): The number of rows to truncate to.
    
    Returns:
        pd.DataFrame: Truncated DataFrame.
    """
    if size <= 0 or size > len(df):
        raise ValueError("Size must be a positive integer within the range of the DataFrame.")
    
    return df.head(size)
#User selects the size of the truncated CSV
print("Please enter the number of rows you want to truncate the CSV to:")
user_input = input("Enter a number (e.g., 1000): ")
try:
    truncated_size = int(user_input)
except ValueError:
    print("Invalid input. Using default size of 1000.")
    truncated_size = 1000

df = get_truncated_csv_size(df, truncated_size)

#Saves the truncated DataFrame to a new CSV file
def save_truncated_csv(df, output_file):
    """
    Saves the DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_file (str): The path to the output CSV file.
    """
    df.to_csv(output_file, index=False)
    print(f"Truncated DataFrame saved to {output_file}")
user_input = input("Enter the new filename to save the truncated CSV (e.g., chicago_small.csv): ")
save_truncated_csv(df, user_input)