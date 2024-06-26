import pandas as pd
# download excel file from here: https://www.kaggle.com/datasets/paultimothymooney/recipenlg?resource=download&select=RecipeNLG_license.png
# the code will print the header text from the excel file in order to check titles in my code  


# Specify the file path to the dataset
file_path = 'RecipeNLG_dataset.csv'

def read_csv_file(file_path, encoding):
    """
    Reads a CSV file with the specified encoding and returns a DataFrame.
    """
    try:
        df = pd.read_csv(file_path, encoding=encoding, low_memory=False)
        return df
    except Exception as e:
        print(f"Error reading the file with {encoding} encoding: {e}")
        return pd.DataFrame()

# Try reading the file with utf-8 encoding first
df = read_csv_file(file_path, 'utf-8')

# If utf-8 encoding fails or DataFrame is empty, try ISO-8859-1 encoding
if df.empty:
    df = read_csv_file(file_path, 'ISO-8859-1')

# Print the first 20 rows of the DataFrame if it is not empty
if not df.empty:
    print(df.head(20))
    print(f"Number of rows read: {len(df)}")
else:
    print("Failed to read the file with both utf-8 and ISO-8859-1 encodings.")
