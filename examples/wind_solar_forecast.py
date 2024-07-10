# This script demonstrates the use of methods from the GenerationForecastApi
# to retrieve day-ahead forecast data for wind and solar generation from the Elexon API.

from datetime import datetime
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.generation_forecast_api import GenerationForecastApi

# Initialize API client
api_client = ApiClient()
forecast_api = GenerationForecastApi(api_client)

# Define date range for fetching day-ahead wind and solar forecast data
from_date = datetime(2024, 7, 1)
to_date = datetime(2024, 7, 7)  # Note: Maximum data output range is 7 days

try:
    # Fetch day-ahead forecast data for wind and solar from API
    response = forecast_api.forecast_generation_wind_and_solar_day_ahead_get(
        _from=from_date,
        to=to_date,
        process_type='day ahead',
        format='json'
    )

    # Handle response data as needed
    if hasattr(response, 'data'):
        # Convert response data to DataFrame
        df = pd.DataFrame([data.to_dict() for data in response.data])

        # Print DataFrame
        print("\n--- Day-Ahead Wind and Solar Forecast Data ---")
        print(df.head())
    else:
        print("Response object does not contain 'data' attribute.")

except Exception as e:
    print(f"Error fetching day-ahead wind and solar forecast data: {str(e)}")