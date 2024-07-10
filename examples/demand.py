# This script demonstrates the use of methods from the DemandApi
# to retrieve various types of demand data from the Elexon API.

from datetime import datetime, timedelta
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.demand_api import DemandApi

def get_actual_total_load():
    """
    Retrieves Actual Total Load (ATL/B0610) data using the demand_actual_total_get method
    from the Swagger-generated client, prints the results, and returns it as a pandas DataFrame.
    """
    api_client = ApiClient()
    demand_api = DemandApi(api_client)

    from_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    to_date = from_date + timedelta(days=1)  # Next day

    try:
        response = demand_api.demand_actual_total_get(
            _from=from_date,
            to=to_date,
            settlement_period_from=1,
            settlement_period_to=48,
            format='json'
        )

        if hasattr(response, 'data'):
            df = pd.DataFrame([data.to_dict() for data in response.data])
            print("\n--- Actual Total Load Data ---")
            print(df.head())
            return df
        else:
            print("Response object does not contain 'data' attribute.")
            return pd.DataFrame()

    except Exception as e:
        print(f"Error fetching actual total load data: {str(e)}")
        return pd.DataFrame()

# Just call the function to execute
get_actual_total_load()