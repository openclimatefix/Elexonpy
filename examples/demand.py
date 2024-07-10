# This script demonstrates the use of methods from the DemandApi
# to retrieve various types of demand data from the Elexon API.

from datetime import datetime, timedelta
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.demand_api import DemandApi

# Initialize API client
api_client = ApiClient()
demand_api = DemandApi(api_client)

# Define date range
from_date = datetime(2024, 7, 1)
to_date = datetime(2024, 7, 2)

# Fetch data from API
response = demand_api.demand_actual_total_get(
    _from=from_date,
    to=to_date,
    settlement_period_from=1,
    settlement_period_to=48,
    format='json'
)

# Convert response to DataFrame
df = pd.DataFrame([data.to_dict() for data in response.data])

# Display DataFrame
print("\n--- Actual Total Load Data ---")
print(df.head())