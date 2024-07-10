# This script demonstrates the use of methods from the SoSoPricesApi
# to retrieve system operator to system operator prices data from the Elexon API.


from datetime import datetime
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.so_so_prices_api import SOSOPricesApi

# Initialize API client
api_client = ApiClient()
soso_prices_api = SOSOPricesApi(api_client)

# Define date range
from_date = datetime(2024, 7, 1)
to_date = datetime(2024, 7, 2)

try:
    # Fetch SO-SO prices data from API
    response = soso_prices_api.soso_prices_get(
        _from=from_date,
        to=to_date,
        format='json'
    )

    # Convert response to DataFrame
    df = pd.DataFrame([data.to_dict() for data in response.data])

    # Print DataFrame
    print("\n--- System Operator to System Operator Prices Data ---")
    print(df.head())

except Exception as e:
    print(f"Error fetching SO-SO prices data: {str(e)}")