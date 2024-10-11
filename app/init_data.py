import pandas as pd 
import sqlite3
import os

data_dir = "./data"

class EmptyDataFrameException(Exception):
    pass

def process_files():

    combined_data = pd.DataFrame()

    print("Processing files...")
    for filename in os.listdir(data_dir):
        print(f"...{filename}") 
        if filename.endswith(".csv"):
            file_path = os.path.join(data_dir, filename)
            if os.path.getsize(file_path) > 0:
                temp_data = pd.read_csv(file_path)
                combined_data = pd.concat([combined_data, temp_data], ignore_index=True)
    print("Processing files...")
    return combined_data


def main():
    print("""
            Extracting data...
            WARNING: This program assumes that all 
          data cleaning task has been perfomed on the 
          content of ./data/ directory and that every
          file in ./data/ directory has the same colums.""")

    data = process_files()
    if data.empty:
        raise EmptyDataFrameException("Data error: no valid csv file in data directory")

    connection = sqlite3.connect('sqlDB.db')

    data.to_sql('consolidated_data', connection, if_exists='replace', index=False)

    print("Upload data SUCCESS into `sqlDB.db`")


if __name__ == "__main__":
    main()
