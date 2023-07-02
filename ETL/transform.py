from typing import Any
import polars as pl


def clean_data(raw_data: dict[str, Any]):
    """
    Cleans and transforms raw data into a clean DataFrame.

    Parameters:
        raw_data (dict[str, Any]): Raw weather data in dictionary format.

    Returns:
        pl.DataFrame: Cleaned DataFrame with columns for time, temperature, and humidity.
    """
    df = pl.DataFrame(
        {
            "time": raw_data["hourly"]["time"],
            "temperature": raw_data["hourly"]["temperature_2m"],
            "humidity": raw_data["hourly"]["relativehumidity_2m"],
        }
    )

    if df.select("time").is_duplicated().any():
        raise Exception("A value in time is duplicated")

    clean_df = df.with_columns(
        pl.col("time").str.strptime(pl.Datetime).dt.time(),
        pl.col("time").str.strptime(pl.Datetime).dt.date().alias("date"),
    )

    print(df.dtypes)
    print("--------------------------")
    print(clean_df.dtypes)

    return clean_df
