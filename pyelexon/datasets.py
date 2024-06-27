""" Functions for /datasets """

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

import requests

class Datasets:
    """
    A class to interact with Elexon API datasets.
    """

    def fetch_data(self, endpoint, params=None):
        """
        Fetches data from the specified Elexon API endpoint.

        Parameters:
        - endpoint (str): The endpoint path to fetch data from.
        - params (dict): Optional query parameters.

        Returns:
        - dict: JSON response from the API.
        """
        base_url = "https://data.elexon.co.uk/bmrs/api/v1"
        url = f"{base_url}{endpoint}"

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        return None

    def fetch_abuc(self):
        """
        Fetches data from the ABUC dataset endpoint.

        Returns:
        - dict: JSON response from the ABUC dataset endpoint.
        """
        endpoint = '/datasets/ABUC'
        params = {
            'publishDateTimeFrom': '2024-06-25T00:00:00Z',
            'publishDateTimeTo': '2024-06-26T00:00:00Z',
            'format': 'json'  # Optional: Example format parameter
        }
        return self.fetch_data(endpoint, params)

    def fetch_abuc_stream(self):
        """
        Fetches data from the ABUC stream dataset endpoint.

        Returns:
        - dict: JSON response from the ABUC stream dataset endpoint.
        """
        endpoint = '/datasets/ABUC/stream'
        params = {
            'publishDateTimeFrom': '2024-06-25T00:00:00Z',
            'publishDateTimeTo': '2024-06-26T00:00:00Z',
            'format': 'json'  # Optional: Example format parameter
        }
        return self.fetch_data(endpoint, params)

# Example usage
if __name__ == "__main__":
    datasets_instance = Datasets()

    # Fetch ABUC dataset
    abuc_data = datasets_instance.fetch_abuc()
    if abuc_data:
        print("ABUC dataset fetched successfully:", abuc_data)

    # Fetch ABUC stream dataset
    abuc_stream_data = datasets_instance.fetch_abuc_stream()
    if abuc_stream_data:
        print("ABUC stream dataset fetched successfully:", abuc_stream_data)




