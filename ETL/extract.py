from typing import Any
import requests


def get_weather(days: int = 14) -> dict[str, Any]:
    """
    Retrieves weather data from the Open-Meteo API.
    It makes a GET request to the API endpoint with the specified latitude, longitude, and other parameters.
    The API response in JSON format, which is then returned as a Python dictionary.

    Parameters:
        days (int): Number of past days to retrieve weather data for (default: 14)
    Returns:
        dict[str, Any]: Weather data in the form of a dictionary
    """
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude=6.2518&longitude=-75.5636&hourly=temperature_2m,relativehumidity_2m&timezone=auto&past_days={days}&forecast_days=1"
    )
    return response.json()
