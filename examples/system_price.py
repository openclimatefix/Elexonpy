# This script demonstrates the use of methods from the IndicativeImbalanceSettlementApi
# to retrieve settlement system prices data from the Elexon API.


from datetime import datetime
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.indicative_imbalance_settlement_api import IndicativeImbalanceSettlementApi

## Initialize API client
api_client = ApiClient()
imbalance_settlement_api = IndicativeImbalanceSettlementApi(api_client)

# Define settlement date
settlement_date = '2024-07-02'

# Fetch system prices data from API
df = imbalance_settlement_api.balancing_settlement_system_prices_settlement_date_get(
    settlement_date=settlement_date,
    format='dataframe'
)

# Print DataFrame
print("\n--- Settlement System Prices Data ---")
print(df.head())
