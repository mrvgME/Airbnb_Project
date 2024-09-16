import os
from pathlib import WindowsPath
from typing import Optional

import pandas as pd
from dotenv import load_dotenv

from sql_manager import SQLManager

load_dotenv()


class OnboardAirbnbData:

    def __init__(self, data_path: Optional[WindowsPath], file_name: str):
        """
        Create path to file.

        Parameter:
        data_path: Path to the data.
        file_name: name of the file.
        """

        __implementedFiles__ = ["listings.csv"]
        __project_dir = os.getenv("project_dir")

        if file_name not in __implementedFiles__:
            raise ValueError(
                "{} is not implemented. Implemented files are {}".format(
                    file_name, __implementedFiles__
                )
            )

        if data_path is None:
            data_path = WindowsPath("data/raw/kaggle_data")

        self.file_path = os.path.join(__project_dir, data_path, file_name)
        self.SQL_obj = SQLManager("airbnb", "postgres", "1234", "localhost", 5432)

    def create_SQL_table(self):
        """
        Create SQL table for the listing.csv file.
        """

        self.SQL_obj.execute_query(
            """
            CREATE TABLE IF NOT EXISTS listing (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            host_id FLOAT,
            host_name VARCHAR(255),
            neighbourhood_group VARCHAR(255),
            neighbourhood VARCHAR(255),
            latitude FLOAT,
            longitude FLOAT,
            room_type VARCHAR(255),
            price FLOAT,
            minimum_nights INT,
            number_of_reviews INT,
            last_review DATE,
            reviews_per_month FLOAT,
            calculated_host_listings_count INT,
            availability_365 INT
            );
            """
        )

        self.SQL_obj.commit_changes()

        print("Listing table created succesfully")

    def insert_csv_to_sql_table(self):
        """
        Read csv as a pandas dataframe an insert it to the SQL table.
        """

        # Read csv as DataFrame
        df = pd.read_csv(self.file_path)

        # Insert DataFrame
        self.SQL_obj.insert_dataframe(df, "listing")

        # Close session
        self.SQL_obj.close_session()


if __name__ == "__main__":
    onboarding = OnboardAirbnbData(None, "listings.csv")
    onboarding.create_SQL_table()
    onboarding.insert_csv_to_sql_table()
