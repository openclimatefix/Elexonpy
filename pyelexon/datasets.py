import requests
import pandas as pd
from constants import BASE_URL

class Datasets:
    """
    A class to interact with Elexon API datasets.
    """

    def fetch_data(self, endpoint, params=None, convert_to_dataframe=False):
        """
        Parameters:
        - endpoint (str): The endpoint path to fetch data from.
        - params (dict): Optional query parameters.
        - convert_to_dataframe (bool): Flag to convert response to DataFrame (default: False).

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
                    df = pd.DataFrame(response.json()['data'])
                return df
            else:
                return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error: {http_err}")
        except Exception as err:
            print(f"Other error: {err}")

        return None

    def fetch_abuc(self, convert_to_dataframe=True):
        """
        Fetches data from the ABUC dataset endpoint.

        Returns:
        - dict or DataFrame: JSON response from the ABUC dataset endpoint or DataFrame if convert_to_dataframe is True.
        """
        endpoint = '/datasets/ABUC'
        publish_date_time_from = '2024-06-25T00:00:00Z'
        publish_date_time_to = '2024-06-26T00:00:00Z'
        params = {
            'publishDateTimeFrom': publish_date_time_from,
            'publishDateTimeTo': publish_date_time_to,
            'format': 'json'  # Optional
        }

        return self.fetch_data(endpoint, params, convert_to_dataframe)

    def fetch_abuc_stream(self, convert_to_dataframe=True):
        """
        Fetches data from the ABUC stream dataset endpoint.

        Returns:
        - dict or DataFrame: JSON response from the ABUC stream dataset endpoint or DataFrame if convert_to_dataframe is True.
        """
        endpoint = '/datasets/ABUC/stream'
        publish_date_time_from = '2024-06-25T00:00:00Z'
        publish_date_time_to = '2024-06-26T00:00:00Z'
        params = {
            'publishDateTimeFrom': publish_date_time_from,
            'publishDateTimeTo': publish_date_time_to,
            'format': 'json'  # Optional
        }

        return self.fetch_data(endpoint, params, convert_to_dataframe)


"""
See https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api for more information
This file should contain the following routes:
"""

# Path: /datasets/ABUC
# Path: /datasets/ABUC/stream
# Path: /datasets/AGPT
# Path: /datasets/AGPT/stream
# Path: /datasets/AGWS
# Path: /datasets/AGWS/stream
# Path: /datasets/AOBE
# Path: /datasets/AOBE/stream
# Path: /datasets/ATL
# Path: /datasets/ATL/stream
# Path: /datasets/B1610
# Path: /datasets/B1610/stream
# Path: /datasets/BEB
# Path: /datasets/BEB/stream
# Path: /datasets/BOALF
# Path: /datasets/BOALF/stream
# Path: /datasets/BOD
# Path: /datasets/BOD/stream
# Path: /datasets/CBS
# Path: /datasets/CBS/stream
# Path: /datasets/CCM
# Path: /datasets/CCM/stream
# Path: /datasets/CDN
# Path: /datasets/CDN/stream
# Path: /datasets/DAG
# Path: /datasets/DAG/stream
# Path: /datasets/DATL
# Path: /datasets/DATL/stream
# Path: /datasets/DCI
# Path: /datasets/DCI/stream
# Path: /datasets/DGWS
# Path: /datasets/DGWS/stream
# Path: /datasets/DISBSAD
# Path: /datasets/DISBSAD/stream
# Path: /datasets/FEIB
# Path: /datasets/FEIB/stream
# Path: /datasets/FOU2T14D
# Path: /datasets/FOU2T3YW
# Path: /datasets/FREQ
# Path: /datasets/FREQ/stream
# Path: /datasets/FUELHH
# Path: /datasets/FUELHH/stream
# Path: /datasets/FUELINST
# Path: /datasets/FUELINST/stream
# Path: /datasets/IGCA
# Path: /datasets/IGCA/stream
# Path: /datasets/IGCPU
# Path: /datasets/IGCPU/stream
# Path: /datasets/IMBALNGC
# Path: /datasets/IMBALNGC/stream
# Path: /datasets/INDDEM
# Path: /datasets/INDDEM/stream
# Path: /datasets/INDGEN
# Path: /datasets/INDGEN/stream
# Path: /datasets/INDO
# Path: /datasets/INDOD
# Path: /datasets/INDOD/stream
# Path: /datasets/ITSDO
# Path: /datasets/LOLPDRM
# Path: /datasets/LOLPDRM/stream
# Path: /datasets/MATL
# Path: /datasets/MATL/stream
# Path: /datasets/MDP
# Path: /datasets/MDP/stream
# Path: /datasets/MDV
# Path: /datasets/MDV/stream
# Path: /datasets/MELNGC
# Path: /datasets/MELNGC/stream
# Path: /datasets/MELS
# Path: /datasets/MELS/stream
# Path: /datasets/MID
# Path: /datasets/MID/stream
# Path: /datasets/MILS
# Path: /datasets/MILS/stream
# Path: /datasets/MNZT
# Path: /datasets/MNZT/stream
# Path: /datasets/MZT
# Path: /datasets/MZT/stream
# Path: /datasets/NDF
# Path: /datasets/NDF/stream
# Path: /datasets/NDFD
# Path: /datasets/NDFD/stream
# Path: /datasets/NDFW
# Path: /datasets/NDFW/stream
# Path: /datasets/NDZ
# Path: /datasets/NDZ/stream
# Path: /datasets/NETBSAD
# Path: /datasets/NETBSAD/stream
# Path: /datasets/NONBM
# Path: /datasets/NONBM/stream
# Path: /datasets/NOU2T14D
# Path: /datasets/NOU2T3YW
# Path: /datasets/NTB
# Path: /datasets/NTB/stream
# Path: /datasets/NTO
# Path: /datasets/NTO/stream
# Path: /datasets/OCNMF3Y
# Path: /datasets/OCNMF3Y/stream
# Path: /datasets/OCNMF3Y2
# Path: /datasets/OCNMF3Y2/stream
# Path: /datasets/OCNMFD
# Path: /datasets/OCNMFD/stream
# Path: /datasets/OCNMFD2
# Path: /datasets/OCNMFD2/stream
# Path: /datasets/PBC
# Path: /datasets/PBC/stream
# Path: /datasets/PN
# Path: /datasets/PN/stream
# Path: /datasets/PPBR
# Path: /datasets/PPBR/stream
# Path: /datasets/QAS
# Path: /datasets/QAS/stream
# Path: /datasets/QPN
# Path: /datasets/QPN/stream
# Path: /datasets/RDRE
# Path: /datasets/RDRE/stream
# Path: /datasets/RDRI
# Path: /datasets/RDRI/stream
# Path: /datasets/REMIT
# Path: /datasets/REMIT/stream
# Path: /datasets/RURE
# Path: /datasets/RURE/stream
# Path: /datasets/RURI
# Path: /datasets/RURI/stream
# Path: /datasets/SEL
# Path: /datasets/SEL/stream
# Path: /datasets/SIL
# Path: /datasets/SIL/stream
# Path: /datasets/SOSO
# Path: /datasets/SOSO/stream
# Path: /datasets/SYSWARN
# Path: /datasets/SYSWARN/stream
# Path: /datasets/TEMP
# Path: /datasets/TSDF
# Path: /datasets/TSDF/stream
# Path: /datasets/TSDFD
# Path: /datasets/TSDFD/stream
# Path: /datasets/TSDFW
# Path: /datasets/TSDFW/stream
# Path: /datasets/TUDM
# Path: /datasets/TUDM/stream
# Path: /datasets/UOU2T14D
# Path: /datasets/UOU2T14D/stream
# Path: /datasets/UOU2T3YW
# Path: /datasets/UOU2T3YW/stream
# Path: /datasets/WATL
# Path: /datasets/WATL/stream
# Path: /datasets/WINDFOR
# Path: /datasets/WINDFOR/stream
# Path: /datasets/YAFM
# Path: /datasets/YAFM/stream
# Path: /datasets/YATL
# Path: /datasets/YATL/stream
# Path: /datasets/metadata/latest