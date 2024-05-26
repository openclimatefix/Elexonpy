""" Functions for /balancing/settlement

 See https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api for more information 
This file should contain the following routes:
"""

from typing import Union
from datetime import datetime
import pandas as pd
import requests
from pyelexon.constants import url_base

# Path: /balancing/settlement/acceptances/all/{settlementDate}/{settlementPeriod}
# Path: /balancing/settlement/default-notices
# Path: /balancing/settlement/market-depth/{settlementDate}
# Path: /balancing/settlement/market-depth/{settlementDate}/{settlementPeriod}
# Path: /balancing/settlement/messages/{settlementDate}
# Path: /balancing/settlement/messages/{settlementDate}/{settlementPeriod}
# Path: /balancing/settlement/stack/all/{bidOffer}/{settlementDate}/{settlementPeriod}
# Path: /balancing/settlement/system-prices/{settlementDate}
# Path: /balancing/settlement/system-prices/{settlementDate}/{settlementPeriod}


def get_system_prices(
    settlement_date: Union[datetime, str],
) -> pd.DataFrame:
    """
    Get the system prices for a given settlement date and period

    This function requests data from the /balancing/settlement/system-prices/{settlementDate}/{settlementPeriod} endpoint
    See https://developer.data.elexon.co.uk/api-details#balancing-settlement-system-prices for more information

    Note: as of 2024-05-26, data only available from 2024-01-31 onwards

    Args:
        settlement_date (Union[datetime, str]): The settlement date to get data for

    """

    url = f"{url_base}/balancing/settlement/system-prices/{settlement_date}?format=json"

    response = requests.get(url)
    response.raise_for_status()

    # convert to pandas as this is the expected output
    data = response.json()
    df = pd.DataFrame(data["data"])
    return df
