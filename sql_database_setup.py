import pandas as pd
import sqlite3

if __name__ == '__main__':

    csv_file = 'era5_dataset.csv'
    database_file = 'era5_database.sqlite'
    main_table = 'main'

    conn = sqlite3.connect(database_file)

    chunksize = 100000
    for chunk in pd.read_csv(csv_file, chunksize=chunksize):
        chunk.to_sql(main_table, conn, if_exists='append', index=False)
        