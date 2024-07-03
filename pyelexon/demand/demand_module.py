import requests
import pandas as pd
from pyelexon.constants import BASE_URL

class Demand:

    def fetch_data(self, endpoint, params=None, convert_to_dataframe=False):
        """
        Helper method to fetch data from a specified API endpoint.

        Parameters:
        - endpoint (str): The endpoint path to fetch data from.
        - params (dict): Optional query parameters.
        - convert_to_dataframe (bool): Flag to convert response to a DataFrame (default: False).

        Returns:
        - dict or DataFrame: JSON response from the API or DataFrame if convert_to_dataframe is True.
        """
        url = f"{BASE_URL}{endpoint}"

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for errors

            if convert_to_dataframe:
                # Check if response is a list of dictionaries
                if isinstance(response.json(), list):
                    df = pd.DataFrame(response.json())
                else:
                    df = pd.DataFrame(response.json().get('data', []))
                return df
            else:
                return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        return None

    def fetch_actual_total_demand(self, from_date, to_date, convert_to_dataframe=True):
        """
        Parameters:
        - from_date (str): The start date for fetching actual demand.
        - to_date (str): The end date for fetching actual demand.
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the actual total demand endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Actual Total Demand API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-actual-total-from-from-to-to).
        """
        endpoint = '/demand/actual/total'
        params = {
            'from': from_date,
            'to': to_date,
            'format': 'json'  # Optional
        }
        return self.fetch_data(endpoint, params, convert_to_dataframe)

    def fetch_indicative_peak_demand(self, data_type, triad_season_start_year=None, from_date=None, to_date=None, format='json', convert_to_dataframe=True):
        """
        Parameters:
        - data_type (str): Type of data. Should be 'operational' or 'settlement'.
        - triad_season_start_year (int): Optional. Year indicating the Triad season starting on 1 November of the given year.
        - from_date (str): Optional. Start date for fetching indicative peak demand data.
        - to_date (str): Optional. End date for fetching indicative peak demand data.
        - format (str): Optional. Response data format. Defaults to 'json'. Use 'json' or 'xml'.
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the indicative peak demand endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Indicative Peak Demand API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-peak-indicative).
        """
        endpoint = '/demand/peak/indicative'
        params = {
            'data': data_type,
            'triadSeasonStartYear': triad_season_start_year,
            'from': from_date,
            'to': to_date,
            'format': format
        }

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching indicative peak demand: {e}")
            return None

    def fetch_initial_national_demand_outturn(self, settlement_date_from=None, settlement_date_to=None, settlement_period=None, format='json', convert_to_dataframe=True):
        """
        Parameters:
        - settlement_date_from (str): Optional. Start settlement date for fetching data (format: yyyy-MM-dd).
        - settlement_date_to (str): Optional. End settlement date for fetching data (format: yyyy-MM-dd).
        - settlement_period (int): Optional. Settlement period for fetching data.
        - format (str): Optional. Response data format. Defaults to 'json'. Use 'json' or 'xml'.
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the initial national demand outturn endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Initial National Demand Outturn API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-outturn).
        """
        endpoint = '/demand/outturn'
        params = {
            'settlementDateFrom': settlement_date_from,
            'settlementDateTo': settlement_date_to,
            'settlementPeriod': settlement_period,
            'format': format
        }

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching initial national demand outturn: {e}")
            return None

    def fetch_initial_national_demand_outturn_stream(self, settlement_date_from=None, settlement_date_to=None, settlement_period=None, convert_to_dataframe=True):
        """
        Parameters:
        - settlement_date_from (str): Optional. Start settlement date for fetching data (format: yyyy-MM-dd).
        - settlement_date_to (str): Optional. End settlement date for fetching data (format: yyyy-MM-dd).
        - settlement_period (list of int): Optional. Settlement periods for fetching data (e.g., [1, 2, 3]).
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the INDO stream endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Initial National Demand Outturn Stream API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-outturn-stream).
        """
        endpoint = '/demand/outturn/stream'
        params = {
            'settlementDateFrom': settlement_date_from,
            'settlementDateTo': settlement_date_to,
            'settlementPeriod': settlement_period
        }

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching initial national demand outturn stream: {e}")
            return None

    def fetch_initial_national_demand_outturn_daily(self, settlement_date_from=None, settlement_date_to=None, convert_to_dataframe=True):
        """
        Parameters:
        - settlement_date_from (str): Optional. Start settlement date for fetching data (format: yyyy-MM-dd).
        - settlement_date_to (str): Optional. End settlement date for fetching data (format: yyyy-MM-dd).
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the INDOD endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Initial National Demand Outturn per day API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-outturn-daily).
        """
        endpoint = '/demand/outturn/daily'
        params = {
            'settlementDateFrom': settlement_date_from,
            'settlementDateTo': settlement_date_to,
            'format': 'json'  # Optional: default to JSON format
        }

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching initial national demand outturn daily: {e}")
            return None

    def fetch_initial_national_demand_outturn_daily_stream(self, settlement_date_from=None, settlement_date_to=None, convert_to_dataframe=True):
        """

        Parameters:
        - settlement_date_from (str): Optional. Start settlement date for fetching data (format: yyyy-MM-dd).
        - settlement_date_to (str): Optional. End settlement date for fetching data (format: yyyy-MM-dd).
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the INDOD stream endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Initial National Demand Outturn per day Stream API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-outturn-daily-stream).
        """
        endpoint = '/demand/outturn/daily/stream'
        params = {
            'settlementDateFrom': settlement_date_from,
            'settlementDateTo': settlement_date_to
        }

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching initial national demand outturn daily stream: {e}")
            return None

    def fetch_operational_demand_peaks_triad_season(self, triad_season_year, format='json', convert_to_dataframe=True):
        """
        Parameters:
        - triad_season_year (int): Year indicating the Triad season starting on 1 November of the given year.
        - format (str): Optional. Response data format (default: 'json').
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the operational demand peaks for a Triad season endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Operational Demand Peaks for Triad Season API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-peak-indicative-operational-triadSeason).
        """
        endpoint = f'/demand/peak/indicative/operational/{triad_season_year}'
        params = {
            'format': format
        }

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching operational demand peaks for Triad season: {e}")
            return None

    def fetch_peak_demand_per_day_itsdo(self, from_date=None, to_date=None, format='json', convert_to_dataframe=True):
        """
        Parameters:
        - from_date (str): Optional. The start date of the requested date range (format: yyyy-MM-dd).
        - to_date (str): Optional. The end date of the requested date range (format: yyyy-MM-dd).
        - format (str): Optional. Response data format ('json' or 'xml', default: 'json').
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the peak demand per day (ITSDO) endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Peak Demand per Day (ITSDO) API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-peak).
        """
        endpoint = '/demand/peak'
        params = {
            'from': from_date,
            'to': to_date,
            'format': format
        }

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching peak demand per day (ITSDO) data: {e}")
            return None

    def fetch_settlement_data_demand_peaks(self, triad_season, format='json', convert_to_dataframe=True):
        """
        Parameters:
        - triad_season (int): A year indicating the Triad season starting on 1 November of the given year (format: yyyy).
        - format (str): Optional. Response data format ('json' or 'xml', default: 'json').
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the settlement data demand peaks endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Settlement Data Demand Peaks API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-peak-indicative-settlement-triadSeason).
        """
        endpoint = f'/demand/peak/indicative/settlement/{triad_season}'
        params = {
            'format': format
        }

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching settlement data demand peaks for Triad season {triad_season}: {e}")
            return None

    def fetch_system_demand_summary(self, from_date=None, to_date=None, format='json', convert_to_dataframe=True):
        """
        Fetch system demand summary (FUELINST) from /demand/outturn/summary endpoint.

        Parameters:
        - from_date (str): Optional. The start date for fetching demand summary (format: yyyy-MM-dd'T'HH:mm:ssZ).
        - to_date (str): Optional. The end date for fetching demand summary (format: yyyy-MM-dd'T'HH:mm:ssZ).
        - format (str): Optional. Response data format ('json' or 'xml', default: 'json').
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the system demand summary endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [System Demand Summary API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-outturn-summary).
        """
        endpoint = '/demand/outturn/summary'
        params = {
            'format': format
        }

        # Check if both from_date and to_date are provided and ensure they are within 7 days
        if from_date and to_date:
            from_date_dt = pd.to_datetime(from_date)
            to_date_dt = pd.to_datetime(to_date)
            if (to_date_dt - from_date_dt).days > 7:
                raise ValueError("Date range between From and To inclusive must not exceed 7 days.")

            params.update({
                'from': from_date,
                'to': to_date
            })

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching system demand summary: {e}")
            return None

    def fetch_triad_demand_peaks(self, data_type, triad_season_start_year=None, format='json', convert_to_dataframe=True):
        """
        Parameters:
        - data_type (str): Type of data ('operational' or 'settlement').
        - triad_season_start_year (int): Optional. A year indicating the Triad season starting on 1 November of the given year.
        - format (str): Optional. Response data format ('json' or 'xml', default: 'json').
        - convert_to_dataframe (bool): Convert the response to a DataFrame (default: True).

        Returns:
        - dict or DataFrame: JSON response from the Triad demand peaks endpoint or DataFrame if convert_to_dataframe is True.

        API Documentation:
        For more details on this API endpoint, refer to the [Triad Demand Peaks API Documentation](https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get-demand-peak-triad).
        """
        endpoint = '/demand/peak/triad'
        params = {
            'data': data_type,
            'format': format
        }

        if triad_season_start_year:
            params['triadSeasonStartYear'] = triad_season_start_year

        try:
            return self.fetch_data(endpoint, params=params, convert_to_dataframe=convert_to_dataframe)
        except Exception as e:
            print(f"Error fetching Triad demand peaks: {e}")
            return None

# Example usage

demand_client = Demand()

# Example 1: Fetch actual total demand data for one day
from_date = '2024-01-01'
to_date = '2024-01-01'
actual_demand_data = demand_client.fetch_actual_total_demand(from_date, to_date, convert_to_dataframe=True)

if actual_demand_data is not None:
    print("Actual Total Demand Data:")
    print(actual_demand_data.head())
else:
    print("Failed to fetch actual total demand data.")


#Example 2 : indicative_peak_demand

data_type = 'operational'
indicative_peak_data = demand_client.fetch_indicative_peak_demand(data_type, triad_season_start_year=2023, format='json', convert_to_dataframe=True)

if indicative_peak_data is not None and not indicative_peak_data.empty:
    print("Indicative Peak Demand Data:")
    print(indicative_peak_data.head())
else:
    print("Failed to fetch indicative peak demand data.")
