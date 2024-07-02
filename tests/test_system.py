import os
import sys
import pytest
import requests
import requests_mock
from datetime import datetime
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyelexon.constants import BASE_URL
from pyelexon.system.system_module import SystemPricesFetcher

@pytest.fixture
def fetcher():
    return SystemPricesFetcher()

def test_get_buy_prices_with_datetime(fetcher):
    settlement_date = datetime(2023, 7, 1)
    expected_date_str = settlement_date.strftime('%Y-%m-%d')

    with requests_mock.Mocker() as m:
        url = f"{BASE_URL}/balancing/settlement/system-prices/{expected_date_str}?format=json"
        m.get(url, json={
            "data": [
                {"settlementDate": "2023-07-01", "settlementPeriod": "1", "systemBuyPrice": 50.0}
            ]
        })

        df = fetcher.get_buy_prices(settlement_date)
        assert not df.empty
        assert df.shape[0] == 1
        assert list(df.columns) == ['settlementDate', 'settlementPeriod', 'systemBuyPrice']
        assert df.iloc[0]['systemBuyPrice'] == 50.0

def test_get_buy_prices_with_string(fetcher):
    settlement_date = "2023-07-01"

    with requests_mock.Mocker() as m:
        url = f"{BASE_URL}/balancing/settlement/system-prices/{settlement_date}?format=json"
        m.get(url, json={
            "data": [
                {"settlementDate": "2023-07-01", "settlementPeriod": "1", "systemBuyPrice": 50.0}
            ]
        })

        df = fetcher.get_buy_prices(settlement_date)
        assert not df.empty
        assert df.shape[0] == 1
        assert list(df.columns) == ['settlementDate', 'settlementPeriod', 'systemBuyPrice']
        assert df.iloc[0]['systemBuyPrice'] == 50.0

def test_get_buy_prices_invalid_date(fetcher):
    settlement_date = "invalid-date"

    with pytest.raises(requests.exceptions.HTTPError):
        with requests_mock.Mocker() as m:
            url = f"{BASE_URL}/balancing/settlement/system-prices/{settlement_date}?format=json"
            m.get(url, status_code=400)

            fetcher.get_buy_prices(settlement_date)

def test_get_buy_prices_api_failure(fetcher):
    settlement_date = "2023-07-01"

    with pytest.raises(Exception):
        with requests_mock.Mocker() as m:
            url = f"{BASE_URL}/balancing/settlement/system-prices/{settlement_date}?format=json"
            m.get(url, status_code=500)

            fetcher.get_buy_prices(settlement_date)
