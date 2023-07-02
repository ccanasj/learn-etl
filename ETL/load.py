import polars as pl
from models import Weather
from utils import Session


def save_data(cleaned_data: pl.DataFrame):
    """
    Saves cleaned weather data to a database using the SQLAlchemy ORM.

    Parameters:
        cleaned_data (pl.DataFrame): Cleaned weather data in DataFrame format.
    """
    with Session() as session:
        session.bulk_insert_mappings(
            Weather, [row for row in cleaned_data.iter_rows(named=True)]
        )
        session.commit()
