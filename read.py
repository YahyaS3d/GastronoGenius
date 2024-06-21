import pandas as pd
# download excel file from here: https://www.kaggle.com/datasets/paultimothymooney/recipenlg?resource=download&select=RecipeNLG_license.png
# the code will print the header text from the excel file in order to check titles in my code  
file_path = 'RecipeNLG_dataset.csv'

# Try reading the file
try:
    df = pd.read_csv(file_path, encoding='utf-8', low_memory=False)
    print(df.head())
except Exception as e:
    print(f"Error reading the file: {e}")

# If utf-8 encoding fails, try a different encoding
if df.empty:
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1', low_memory=False)
        print(df.head())
    except Exception as e:
        print(f"Error reading the file with ISO-8859-1 encoding: {e}")