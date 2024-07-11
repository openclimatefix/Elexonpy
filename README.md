# elexonpy
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

**elexonpy** is a Python package that provides a convenient interface to the ELEXON API. This package is generated using Swagger Codegen, ensuring compatibility and ease of use with the ELEXON API services. The package is available on PyPI and can be easily installed via pip.

## Requirements.

Python 2.7 and 3.4+

## Installation

You can install the `elexonpy` package via pip from PyPI or directly from GitHub.

### Install from PyPI

```shell
pip install elexonpy
```

### Install from GitHub

To install the package directly from the GitHub repository, use the following command:

```shell
 pip install git+https://github.com/openclimatefix/Elexonpy.git
```

## Examples from `examples` folder

### Example 1 :

This example demonstrates how to use methods from the `DemandApi` to retrieve various types of demand data from the Elexon API and format it into a DataFrame using pandas.


```
# This script demonstrates the use of methods from the DemandApi
# to retrieve various types of demand data from the Elexon API.

from datetime import datetime
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.demand_api import DemandApi

# Initialize API client
api_client = ApiClient()
demand_api = DemandApi(api_client)

# Define date range for Actual Total Load Data
from_date = datetime(2024, 7, 1)
to_date = datetime(2024, 7, 2)

# Fetch Actual Total Load Data from API
response = demand_api.demand_actual_total_get(
    _from=from_date,
    to=to_date,
    settlement_period_from=1,
    settlement_period_to=48,
    format='json'
)

# Convert response to DataFrame
df = pd.DataFrame([data.to_dict() for data in response.data])

# Print Actual Total Load Data DataFrame
print("\n--- Actual Total Load Data ---")
print(df.head())

# Define date range for Demand Outturn Daily Data
from_date = datetime(2024, 6, 1)
to_date = datetime(2024, 6, 2)

# Fetch Demand Outturn Daily Data from API
response = demand_api.demand_outturn_daily_get(
    settlement_date_from=from_date.date(),
    settlement_date_to=to_date.date(),
    format='json'
)

# Convert response to DataFrame
df = pd.DataFrame([data.to_dict() for data in response.data])

# Print Demand Outturn Daily Data DataFrame
print("\n--- Demand Outturn Daily Data ---")
print(df.head())
```

### Example 2:

This example demonstrates how to use methods from the `IndicativeImbalanceSettlementApi` to retrieve settlement system prices data from the Elexon API and format it into a DataFrame using pandas.

```
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
response = imbalance_settlement_api.balancing_settlement_system_prices_settlement_date_get(
    settlement_date=settlement_date,
    format='json'
)

# Convert response data to DataFrame
df = pd.DataFrame([data.to_dict() for data in response.data])

# Print DataFrame
print("\n--- Settlement System Prices Data ---")
print(df.head())
```

### Example 3 :

This example demonstrates how to use methods from the `GenerationForecastApi` to retrieve day-ahead forecast data for wind and solar generation from the Elexon API and format it into a DataFrame using pandas.

```
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

# Fetch day-ahead forecast data for wind and solar from API
response = forecast_api.forecast_generation_wind_and_solar_day_ahead_get(
    _from=from_date,
    to=to_date,
    process_type='day ahead',
    format='json'
)

df = pd.DataFrame([data.to_dict() for data in response.data])

# Print DataFrame
print("\n--- Day-Ahead Wind and Solar Forecast Data ---")
print(df.head())
```


## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = elexonpy.AvailabilityApi(elexonpy.ApiClient(configuration))
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Fourteen-day generation forecast
    api_instance.generation_availability_summary14_d_get(format=format)
except ApiException as e:
    print("Exception when calling AvailabilityApi->generation_availability_summary14_d_get: %s\n" % e)

# create an instance of the API class
api_instance = elexonpy.AvailabilityApi(elexonpy.ApiClient(configuration))
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Three-year generation forecast
    api_instance.generation_availability_summary3_yw_get(format=format)
except ApiException as e:
    print("Exception when calling AvailabilityApi->generation_availability_summary3_yw_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AvailabilityApi* | [**generation_availability_summary14_d_get**](docs/AvailabilityApi.md#generation_availability_summary14_d_get) | **GET** /generation/availability/summary/14D | Fourteen-day generation forecast
*AvailabilityApi* | [**generation_availability_summary3_yw_get**](docs/AvailabilityApi.md#generation_availability_summary3_yw_get) | **GET** /generation/availability/summary/3YW | Three-year generation forecast
*BalancingMechanismDynamicApi* | [**balancing_dynamic_all_get**](docs/BalancingMechanismDynamicApi.md#balancing_dynamic_all_get) | **GET** /balancing/dynamic/all | Market-wide dynamic data (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)
*BalancingMechanismDynamicApi* | [**balancing_dynamic_get**](docs/BalancingMechanismDynamicApi.md#balancing_dynamic_get) | **GET** /balancing/dynamic | Dynamic data per BMU (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)
*BalancingMechanismDynamicApi* | [**balancing_dynamic_rates_all_get**](docs/BalancingMechanismDynamicApi.md#balancing_dynamic_rates_all_get) | **GET** /balancing/dynamic/rates/all | Market-wide rate data (RDRE, RURE, RDRI, RURI)
*BalancingMechanismDynamicApi* | [**balancing_dynamic_rates_get**](docs/BalancingMechanismDynamicApi.md#balancing_dynamic_rates_get) | **GET** /balancing/dynamic/rates | Rate data per BMU (RDRE, RURE, RDRI, RURI)
*BalancingMechanismPhysicalApi* | [**balancing_physical_all_get**](docs/BalancingMechanismPhysicalApi.md#balancing_physical_all_get) | **GET** /balancing/physical/all | Market-wide physical data (PN, QPN, MILS, MELS)
*BalancingMechanismPhysicalApi* | [**balancing_physical_get**](docs/BalancingMechanismPhysicalApi.md#balancing_physical_get) | **GET** /balancing/physical | Physical data per BMU (PN, QPN, MILS, MELS)
*BalancingServicesAdjustmentDisaggregatedApi* | [**balancing_nonbm_disbsad_details_get**](docs/BalancingServicesAdjustmentDisaggregatedApi.md#balancing_nonbm_disbsad_details_get) | **GET** /balancing/nonbm/disbsad/details | Disaggregated balancing services adjustment per settlement period (DISBSAD)
*BalancingServicesAdjustmentDisaggregatedApi* | [**balancing_nonbm_disbsad_summary_get**](docs/BalancingServicesAdjustmentDisaggregatedApi.md#balancing_nonbm_disbsad_summary_get) | **GET** /balancing/nonbm/disbsad/summary | Disaggregated balancing services adjustment time series (DISBSAD)
*BalancingServicesAdjustmentNetApi* | [**balancing_nonbm_netbsad_events_get**](docs/BalancingServicesAdjustmentNetApi.md#balancing_nonbm_netbsad_events_get) | **GET** /balancing/nonbm/netbsad/events | Net balancing services adjustment events (NETBSAD)
*BalancingServicesAdjustmentNetApi* | [**balancing_nonbm_netbsad_get**](docs/BalancingServicesAdjustmentNetApi.md#balancing_nonbm_netbsad_get) | **GET** /balancing/nonbm/netbsad | Net balancing services adjustment time series (NETBSAD)
*BidOfferApi* | [**balancing_bid_offer_all_get**](docs/BidOfferApi.md#balancing_bid_offer_all_get) | **GET** /balancing/bid-offer/all | Market-wide bid-offer data (BOD)
*BidOfferApi* | [**balancing_bid_offer_get**](docs/BidOfferApi.md#balancing_bid_offer_get) | **GET** /balancing/bid-offer | Bid-offer data per BMU (BOD)
*BidOfferAcceptancesApi* | [**balancing_acceptances_all_get**](docs/BidOfferAcceptancesApi.md#balancing_acceptances_all_get) | **GET** /balancing/acceptances/all | Market-wide bid-offer acceptances (BOALF)
*BidOfferAcceptancesApi* | [**balancing_acceptances_all_latest_get**](docs/BidOfferAcceptancesApi.md#balancing_acceptances_all_latest_get) | **GET** /balancing/acceptances/all/latest | Latest market-wide bid-offer acceptances (BOALF)
*BidOfferAcceptancesApi* | [**balancing_acceptances_get**](docs/BidOfferAcceptancesApi.md#balancing_acceptances_get) | **GET** /balancing/acceptances | Bid-offer acceptances per BMU (BOALF)
*CreditDefaultNoticeApi* | [**c_dn_get**](docs/CreditDefaultNoticeApi.md#c_dn_get) | **GET** /CDN | [DEPRECATED] Credit default notices (CDN)
*DatasetsApi* | [**datasets_abuc_get**](docs/DatasetsApi.md#datasets_abuc_get) | **GET** /datasets/ABUC | Amount Of Balancing Reserves Under Contract (ABUC / B1720)
*DatasetsApi* | [**datasets_abuc_stream_get**](docs/DatasetsApi.md#datasets_abuc_stream_get) | **GET** /datasets/ABUC/stream | Amount Of Balancing Reserves Under Contract (ABUC / B1720) stream
*DatasetsApi* | [**datasets_agpt_get**](docs/DatasetsApi.md#datasets_agpt_get) | **GET** /datasets/AGPT | Actual Aggregated Generation Per Type (AGPT / B1620)
*DatasetsApi* | [**datasets_agpt_stream_get**](docs/DatasetsApi.md#datasets_agpt_stream_get) | **GET** /datasets/AGPT/stream | Actual Aggregated Generation Per Type (AGPT / B1620) stream
*DatasetsApi* | [**datasets_agws_get**](docs/DatasetsApi.md#datasets_agws_get) | **GET** /datasets/AGWS | Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630)
*DatasetsApi* | [**datasets_agws_stream_get**](docs/DatasetsApi.md#datasets_agws_stream_get) | **GET** /datasets/AGWS/stream | Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630) stream
*DatasetsApi* | [**datasets_aobe_get**](docs/DatasetsApi.md#datasets_aobe_get) | **GET** /datasets/AOBE | Accepted Offered Balancing Energy (AOBE)
*DatasetsApi* | [**datasets_aobe_stream_get**](docs/DatasetsApi.md#datasets_aobe_stream_get) | **GET** /datasets/AOBE/stream | Accepted Offered Balancing Energy (AOBE) stream
*DatasetsApi* | [**datasets_atl_get**](docs/DatasetsApi.md#datasets_atl_get) | **GET** /datasets/ATL | Actual Total Load Per Bidding Zone (ATL / B0610)
*DatasetsApi* | [**datasets_atl_stream_get**](docs/DatasetsApi.md#datasets_atl_stream_get) | **GET** /datasets/ATL/stream | Actual Total Load Per Bidding Zone (ATL / B0610) stream
*DatasetsApi* | [**datasets_b1610_get**](docs/DatasetsApi.md#datasets_b1610_get) | **GET** /datasets/B1610 | Actual Generation Output Per Generation Unit (B1610)
*DatasetsApi* | [**datasets_b1610_stream_get**](docs/DatasetsApi.md#datasets_b1610_stream_get) | **GET** /datasets/B1610/stream | Actual Generation Output Per Generation Unit (B1610) stream
*DatasetsApi* | [**datasets_beb_get**](docs/DatasetsApi.md#datasets_beb_get) | **GET** /datasets/BEB | Balancing Energy Bids (BEB)
*DatasetsApi* | [**datasets_beb_stream_get**](docs/DatasetsApi.md#datasets_beb_stream_get) | **GET** /datasets/BEB/stream | Balancing Energy Bids (BEB) stream
*DatasetsApi* | [**datasets_boalf_get**](docs/DatasetsApi.md#datasets_boalf_get) | **GET** /datasets/BOALF | Bid Offer Acceptance Level Flagged (BOALF)
*DatasetsApi* | [**datasets_boalf_stream_get**](docs/DatasetsApi.md#datasets_boalf_stream_get) | **GET** /datasets/BOALF/stream | Bid Offer Acceptance Level Flagged (BOALF) stream
*DatasetsApi* | [**datasets_bod_get**](docs/DatasetsApi.md#datasets_bod_get) | **GET** /datasets/BOD | Bid Offer Data (BOD)
*DatasetsApi* | [**datasets_bod_stream_get**](docs/DatasetsApi.md#datasets_bod_stream_get) | **GET** /datasets/BOD/stream | Bid-Offer Data (BOD) stream
*DatasetsApi* | [**datasets_cbs_get**](docs/DatasetsApi.md#datasets_cbs_get) | **GET** /datasets/CBS | Current Balancing State (CBS)
*DatasetsApi* | [**datasets_cbs_stream_get**](docs/DatasetsApi.md#datasets_cbs_stream_get) | **GET** /datasets/CBS/stream | Current Balancing State (CBS) stream
*DatasetsApi* | [**datasets_ccm_get**](docs/DatasetsApi.md#datasets_ccm_get) | **GET** /datasets/CCM | Cost of Congestion Management (CCM / B1330)
*DatasetsApi* | [**datasets_ccm_stream_get**](docs/DatasetsApi.md#datasets_ccm_stream_get) | **GET** /datasets/CCM/stream | Cost of Congestion Management (CCM / B1330) stream
*DatasetsApi* | [**datasets_cdn_get**](docs/DatasetsApi.md#datasets_cdn_get) | **GET** /datasets/CDN | Credit default notices (CDN)
*DatasetsApi* | [**datasets_cdn_stream_get**](docs/DatasetsApi.md#datasets_cdn_stream_get) | **GET** /datasets/CDN/stream | Credit default notices (CDN)
*DatasetsApi* | [**datasets_dag_get**](docs/DatasetsApi.md#datasets_dag_get) | **GET** /datasets/DAG | Day-Ahead Aggregated Generation (DAG / B1430)
*DatasetsApi* | [**datasets_dag_stream_get**](docs/DatasetsApi.md#datasets_dag_stream_get) | **GET** /datasets/DAG/stream | Day-Ahead Aggregated Generation (DAG / B1430) stream
*DatasetsApi* | [**datasets_datl_get**](docs/DatasetsApi.md#datasets_datl_get) | **GET** /datasets/DATL | Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620)
*DatasetsApi* | [**datasets_datl_stream_get**](docs/DatasetsApi.md#datasets_datl_stream_get) | **GET** /datasets/DATL/stream | Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620) stream
*DatasetsApi* | [**datasets_dci_get**](docs/DatasetsApi.md#datasets_dci_get) | **GET** /datasets/DCI | Demand control instructions (DCI)
*DatasetsApi* | [**datasets_dci_stream_get**](docs/DatasetsApi.md#datasets_dci_stream_get) | **GET** /datasets/DCI/stream | Demand control instructions (DCI) stream
*DatasetsApi* | [**datasets_dgws_get**](docs/DatasetsApi.md#datasets_dgws_get) | **GET** /datasets/DGWS | Day-Ahead Generation For Wind And Solar (DGWS / B1440)
*DatasetsApi* | [**datasets_dgws_stream_get**](docs/DatasetsApi.md#datasets_dgws_stream_get) | **GET** /datasets/DGWS/stream | Day-Ahead Generation For Wind And Solar (DGWS / B1440) stream
*DatasetsApi* | [**datasets_disbsad_get**](docs/DatasetsApi.md#datasets_disbsad_get) | **GET** /datasets/DISBSAD | Disaggregated Balancing Services Adjustment Data (DISBSAD)
*DatasetsApi* | [**datasets_disbsad_stream_get**](docs/DatasetsApi.md#datasets_disbsad_stream_get) | **GET** /datasets/DISBSAD/stream | Disaggregated Balancing Services Adjustment Data (DISBSAD) stream
*DatasetsApi* | [**datasets_feib_get**](docs/DatasetsApi.md#datasets_feib_get) | **GET** /datasets/FEIB | Financial Expenses and Income for Balancing (FEIB / B1790)
*DatasetsApi* | [**datasets_feib_stream_get**](docs/DatasetsApi.md#datasets_feib_stream_get) | **GET** /datasets/FEIB/stream | Financial Expenses and Income for Balancing (FEIB / B1790) stream
*DatasetsApi* | [**datasets_fou2_t14_d_get**](docs/DatasetsApi.md#datasets_fou2_t14_d_get) | **GET** /datasets/FOU2T14D | 2 to 14 days ahead generation availability aggregated by fuel type (FOU2T14D)
*DatasetsApi* | [**datasets_fou2_t3_yw_get**](docs/DatasetsApi.md#datasets_fou2_t3_yw_get) | **GET** /datasets/FOU2T3YW | 2 to 156 weeks ahead generation availability aggregated by fuel type (FOU2T3YW)
*DatasetsApi* | [**datasets_freq_get**](docs/DatasetsApi.md#datasets_freq_get) | **GET** /datasets/FREQ | System frequency (FREQ)
*DatasetsApi* | [**datasets_freq_stream_get**](docs/DatasetsApi.md#datasets_freq_stream_get) | **GET** /datasets/FREQ/stream | System frequency (FREQ) stream
*DatasetsApi* | [**datasets_fuelhh_get**](docs/DatasetsApi.md#datasets_fuelhh_get) | **GET** /datasets/FUELHH | Half-hourly generation outturn by fuel type (FUELHH)
*DatasetsApi* | [**datasets_fuelhh_stream_get**](docs/DatasetsApi.md#datasets_fuelhh_stream_get) | **GET** /datasets/FUELHH/stream | Half-hourly generation outturn by fuel type (FUELHH) stream
*DatasetsApi* | [**datasets_fuelinst_get**](docs/DatasetsApi.md#datasets_fuelinst_get) | **GET** /datasets/FUELINST | Instantaneous generation outturn by fuel type (FUELINST)
*DatasetsApi* | [**datasets_fuelinst_stream_get**](docs/DatasetsApi.md#datasets_fuelinst_stream_get) | **GET** /datasets/FUELINST/stream | Instantaneous generation outturn by fuel type (FUELINST) stream
*DatasetsApi* | [**datasets_igca_get**](docs/DatasetsApi.md#datasets_igca_get) | **GET** /datasets/IGCA | Installed Generation Capacity Aggregated (IGCA / B1410)
*DatasetsApi* | [**datasets_igca_stream_get**](docs/DatasetsApi.md#datasets_igca_stream_get) | **GET** /datasets/IGCA/stream | Installed Generation Capacity Aggregated (IGCA / B1410) stream
*DatasetsApi* | [**datasets_igcpu_get**](docs/DatasetsApi.md#datasets_igcpu_get) | **GET** /datasets/IGCPU | Installed Generation Capacity per Unit (IGCPU / B1420)
*DatasetsApi* | [**datasets_igcpu_stream_get**](docs/DatasetsApi.md#datasets_igcpu_stream_get) | **GET** /datasets/IGCPU/stream | Installed Generation Capacity per Unit (IGCPU / B1420) stream
*DatasetsApi* | [**datasets_imbalngc_get**](docs/DatasetsApi.md#datasets_imbalngc_get) | **GET** /datasets/IMBALNGC | Day and day-ahead indicated imbalance (IMBALNGC)
*DatasetsApi* | [**datasets_imbalngc_stream_get**](docs/DatasetsApi.md#datasets_imbalngc_stream_get) | **GET** /datasets/IMBALNGC/stream | Day and day-ahead indicated imbalance (IMBALNGC) stream
*DatasetsApi* | [**datasets_inddem_get**](docs/DatasetsApi.md#datasets_inddem_get) | **GET** /datasets/INDDEM | Day and day-ahead indicated demand (INDDEM)
*DatasetsApi* | [**datasets_inddem_stream_get**](docs/DatasetsApi.md#datasets_inddem_stream_get) | **GET** /datasets/INDDEM/stream | Day and day-ahead indicated demand (INDDEM) stream
*DatasetsApi* | [**datasets_indgen_get**](docs/DatasetsApi.md#datasets_indgen_get) | **GET** /datasets/INDGEN | Day and day-ahead indicated generation (INDGEN)
*DatasetsApi* | [**datasets_indgen_stream_get**](docs/DatasetsApi.md#datasets_indgen_stream_get) | **GET** /datasets/INDGEN/stream | Day and day-ahead indicated generation (INDGEN) stream
*DatasetsApi* | [**datasets_indo_get**](docs/DatasetsApi.md#datasets_indo_get) | **GET** /datasets/INDO | Initial National Demand outturn (INDO)
*DatasetsApi* | [**datasets_indod_get**](docs/DatasetsApi.md#datasets_indod_get) | **GET** /datasets/INDOD | Initial National Demand outturn daily (INDOD)
*DatasetsApi* | [**datasets_indod_stream_get**](docs/DatasetsApi.md#datasets_indod_stream_get) | **GET** /datasets/INDOD/stream | Initial National Demand outturn daily (INDOD) stream
*DatasetsApi* | [**datasets_itsdo_get**](docs/DatasetsApi.md#datasets_itsdo_get) | **GET** /datasets/ITSDO | Initial Transmission System Demand outturn (ITSDO)
*DatasetsApi* | [**datasets_lolpdrm_get**](docs/DatasetsApi.md#datasets_lolpdrm_get) | **GET** /datasets/LOLPDRM | Loss of load probability and de-rated margin (LOLPDRM)
*DatasetsApi* | [**datasets_lolpdrm_stream_get**](docs/DatasetsApi.md#datasets_lolpdrm_stream_get) | **GET** /datasets/LOLPDRM/stream | Loss of load probability and de-rated margin (LOLPDRM)
*DatasetsApi* | [**datasets_matl_get**](docs/DatasetsApi.md#datasets_matl_get) | **GET** /datasets/MATL | Month-Ahead Total Load Forecast Per Bidding Zone (MATL / B0640)
*DatasetsApi* | [**datasets_matl_stream_get**](docs/DatasetsApi.md#datasets_matl_stream_get) | **GET** /datasets/MATL/stream | Month-Ahead Total Load Forecast Per Bidding Zone (MATL / B0640) stream
*DatasetsApi* | [**datasets_mdp_get**](docs/DatasetsApi.md#datasets_mdp_get) | **GET** /datasets/MDP | Maximum Delivery Period (MDP)
*DatasetsApi* | [**datasets_mdp_stream_get**](docs/DatasetsApi.md#datasets_mdp_stream_get) | **GET** /datasets/MDP/stream | Maximum Delivery Period (MDP) stream
*DatasetsApi* | [**datasets_mdv_get**](docs/DatasetsApi.md#datasets_mdv_get) | **GET** /datasets/MDV | Maximum Delivery Volume (MDV)
*DatasetsApi* | [**datasets_mdv_stream_get**](docs/DatasetsApi.md#datasets_mdv_stream_get) | **GET** /datasets/MDV/stream | Maximum Delivery Volume (MDV) stream
*DatasetsApi* | [**datasets_melngc_get**](docs/DatasetsApi.md#datasets_melngc_get) | **GET** /datasets/MELNGC | Day and day-ahead indicated margin (MELNGC)
*DatasetsApi* | [**datasets_melngc_stream_get**](docs/DatasetsApi.md#datasets_melngc_stream_get) | **GET** /datasets/MELNGC/stream | Day and day-ahead indicated margin (MELNGC) stream
*DatasetsApi* | [**datasets_mels_get**](docs/DatasetsApi.md#datasets_mels_get) | **GET** /datasets/MELS | Maximum Export Limit (MELS)
*DatasetsApi* | [**datasets_mels_stream_get**](docs/DatasetsApi.md#datasets_mels_stream_get) | **GET** /datasets/MELS/stream | Maximum Export Limit (MELS) stream
*DatasetsApi* | [**datasets_metadata_latest_get**](docs/DatasetsApi.md#datasets_metadata_latest_get) | **GET** /datasets/metadata/latest | Returns the time when each dataset was last updated
*DatasetsApi* | [**datasets_mid_get**](docs/DatasetsApi.md#datasets_mid_get) | **GET** /datasets/MID | Market Index Data (MID)
*DatasetsApi* | [**datasets_mid_stream_get**](docs/DatasetsApi.md#datasets_mid_stream_get) | **GET** /datasets/MID/stream | Market Index Data (MID) stream
*DatasetsApi* | [**datasets_mils_get**](docs/DatasetsApi.md#datasets_mils_get) | **GET** /datasets/MILS | Maximum Import Limit (MILS)
*DatasetsApi* | [**datasets_mils_stream_get**](docs/DatasetsApi.md#datasets_mils_stream_get) | **GET** /datasets/MILS/stream | Maximum Import Limit (MILS) stream
*DatasetsApi* | [**datasets_mnzt_get**](docs/DatasetsApi.md#datasets_mnzt_get) | **GET** /datasets/MNZT | Minimum Non-Zero Time (MNZT)
*DatasetsApi* | [**datasets_mnzt_stream_get**](docs/DatasetsApi.md#datasets_mnzt_stream_get) | **GET** /datasets/MNZT/stream | Minimum Non-Zero Time (MNZT) stream
*DatasetsApi* | [**datasets_mzt_get**](docs/DatasetsApi.md#datasets_mzt_get) | **GET** /datasets/MZT | Minimum Zero Time (MZT)
*DatasetsApi* | [**datasets_mzt_stream_get**](docs/DatasetsApi.md#datasets_mzt_stream_get) | **GET** /datasets/MZT/stream | Minimum Zero Time (MZT) stream
*DatasetsApi* | [**datasets_ndf_get**](docs/DatasetsApi.md#datasets_ndf_get) | **GET** /datasets/NDF | Day and day-ahead National Demand forecast (NDF)
*DatasetsApi* | [**datasets_ndf_stream_get**](docs/DatasetsApi.md#datasets_ndf_stream_get) | **GET** /datasets/NDF/stream | Day and day-ahead National Demand forecast (NDF) stream
*DatasetsApi* | [**datasets_ndfd_get**](docs/DatasetsApi.md#datasets_ndfd_get) | **GET** /datasets/NDFD | 2-14 days ahead National Demand and surplus forecast (NDFD)
*DatasetsApi* | [**datasets_ndfd_stream_get**](docs/DatasetsApi.md#datasets_ndfd_stream_get) | **GET** /datasets/NDFD/stream | 2-14 days ahead National Demand and surplus forecast (NDFD) stream
*DatasetsApi* | [**datasets_ndfw_get**](docs/DatasetsApi.md#datasets_ndfw_get) | **GET** /datasets/NDFW | 2-52 weeks ahead National Demand and surplus forecast (NDFW)
*DatasetsApi* | [**datasets_ndfw_stream_get**](docs/DatasetsApi.md#datasets_ndfw_stream_get) | **GET** /datasets/NDFW/stream | 2-52 weeks ahead National Demand and surplus forecast (NDFW) stream
*DatasetsApi* | [**datasets_ndz_get**](docs/DatasetsApi.md#datasets_ndz_get) | **GET** /datasets/NDZ | Notice to Deviate from Zero (NDZ)
*DatasetsApi* | [**datasets_ndz_stream_get**](docs/DatasetsApi.md#datasets_ndz_stream_get) | **GET** /datasets/NDZ/stream | Notice to Deviate from Zero (NDZ) stream
*DatasetsApi* | [**datasets_netbsad_get**](docs/DatasetsApi.md#datasets_netbsad_get) | **GET** /datasets/NETBSAD | Net Balancing Services Adjustment Data (NETBSAD)
*DatasetsApi* | [**datasets_netbsad_stream_get**](docs/DatasetsApi.md#datasets_netbsad_stream_get) | **GET** /datasets/NETBSAD/stream | Net Balancing Services Adjustment Data (NETBSAD)
*DatasetsApi* | [**datasets_nonbm_get**](docs/DatasetsApi.md#datasets_nonbm_get) | **GET** /datasets/NONBM | Non-BM STOR (NONBM)
*DatasetsApi* | [**datasets_nonbm_stream_get**](docs/DatasetsApi.md#datasets_nonbm_stream_get) | **GET** /datasets/NONBM/stream | Non-BM STOR (NONBM) stream
*DatasetsApi* | [**datasets_nou2_t14_d_get**](docs/DatasetsApi.md#datasets_nou2_t14_d_get) | **GET** /datasets/NOU2T14D | 2 to 14 days ahead generation availability aggregated data (NOU2T14D)
*DatasetsApi* | [**datasets_nou2_t3_yw_get**](docs/DatasetsApi.md#datasets_nou2_t3_yw_get) | **GET** /datasets/NOU2T3YW | 2 to 156 weeks ahead generation availability aggregated data (NOU2T3YW)
*DatasetsApi* | [**datasets_ntb_get**](docs/DatasetsApi.md#datasets_ntb_get) | **GET** /datasets/NTB | Notice to Deliver Bids (NTB)
*DatasetsApi* | [**datasets_ntb_stream_get**](docs/DatasetsApi.md#datasets_ntb_stream_get) | **GET** /datasets/NTB/stream | Notice to Deliver Bids (NTB) stream
*DatasetsApi* | [**datasets_nto_get**](docs/DatasetsApi.md#datasets_nto_get) | **GET** /datasets/NTO | Notice to Deliver Offers (NTO)
*DatasetsApi* | [**datasets_nto_stream_get**](docs/DatasetsApi.md#datasets_nto_stream_get) | **GET** /datasets/NTO/stream | Notice to Deliver Offers (NTO) stream
*DatasetsApi* | [**datasets_ocnmf3_y2_get**](docs/DatasetsApi.md#datasets_ocnmf3_y2_get) | **GET** /datasets/OCNMF3Y2 | 2-156 weeks ahead demand margin forecast (OCNMF3Y2)
*DatasetsApi* | [**datasets_ocnmf3_y2_stream_get**](docs/DatasetsApi.md#datasets_ocnmf3_y2_stream_get) | **GET** /datasets/OCNMF3Y2/stream | 2-156 weeks ahead demand margin forecast (OCNMF3Y2) stream
*DatasetsApi* | [**datasets_ocnmf3_y_get**](docs/DatasetsApi.md#datasets_ocnmf3_y_get) | **GET** /datasets/OCNMF3Y | 2-156 weeks ahead demand surplus forecast (OCNMF3Y)
*DatasetsApi* | [**datasets_ocnmf3_y_stream_get**](docs/DatasetsApi.md#datasets_ocnmf3_y_stream_get) | **GET** /datasets/OCNMF3Y/stream | 2-156 weeks ahead demand surplus forecast (OCNMF3Y) stream
*DatasetsApi* | [**datasets_ocnmfd2_get**](docs/DatasetsApi.md#datasets_ocnmfd2_get) | **GET** /datasets/OCNMFD2 | 2-14 days ahead demand margin forecast (OCNMFD2)
*DatasetsApi* | [**datasets_ocnmfd2_stream_get**](docs/DatasetsApi.md#datasets_ocnmfd2_stream_get) | **GET** /datasets/OCNMFD2/stream | 2-14 days ahead demand margin forecast (OCNMFD2) stream
*DatasetsApi* | [**datasets_ocnmfd_get**](docs/DatasetsApi.md#datasets_ocnmfd_get) | **GET** /datasets/OCNMFD | 2-14 days ahead demand surplus forecast (OCNMFD)
*DatasetsApi* | [**datasets_ocnmfd_stream_get**](docs/DatasetsApi.md#datasets_ocnmfd_stream_get) | **GET** /datasets/OCNMFD/stream | 2-14 days ahead demand surplus forecast (OCNMFD) stream
*DatasetsApi* | [**datasets_pbc_get**](docs/DatasetsApi.md#datasets_pbc_get) | **GET** /datasets/PBC | Procured Balancing Capacity (PBC)
*DatasetsApi* | [**datasets_pbc_stream_get**](docs/DatasetsApi.md#datasets_pbc_stream_get) | **GET** /datasets/PBC/stream | Procured Balancing Capacity (PBC) stream
*DatasetsApi* | [**datasets_pn_get**](docs/DatasetsApi.md#datasets_pn_get) | **GET** /datasets/PN | Physical Notifications (PN)
*DatasetsApi* | [**datasets_pn_stream_get**](docs/DatasetsApi.md#datasets_pn_stream_get) | **GET** /datasets/PN/stream | Physical Notifications (PN) stream
*DatasetsApi* | [**datasets_ppbr_get**](docs/DatasetsApi.md#datasets_ppbr_get) | **GET** /datasets/PPBR | Prices Of Procured Balancing Reserves (PPBR / B1730)
*DatasetsApi* | [**datasets_ppbr_stream_get**](docs/DatasetsApi.md#datasets_ppbr_stream_get) | **GET** /datasets/PPBR/stream | Prices Of Procured Balancing Reserves (PPBR / B1730) stream
*DatasetsApi* | [**datasets_qas_get**](docs/DatasetsApi.md#datasets_qas_get) | **GET** /datasets/QAS | Balancing Services Volume (QAS)
*DatasetsApi* | [**datasets_qas_stream_get**](docs/DatasetsApi.md#datasets_qas_stream_get) | **GET** /datasets/QAS/stream | Balancing Services Volume (QAS) stream
*DatasetsApi* | [**datasets_qpn_get**](docs/DatasetsApi.md#datasets_qpn_get) | **GET** /datasets/QPN | Quiescent Physical Notifications (QPN)
*DatasetsApi* | [**datasets_qpn_stream_get**](docs/DatasetsApi.md#datasets_qpn_stream_get) | **GET** /datasets/QPN/stream | Quiescent Physical Notifications (QPN) stream
*DatasetsApi* | [**datasets_rdre_get**](docs/DatasetsApi.md#datasets_rdre_get) | **GET** /datasets/RDRE | Run Down Rate Export (RDRE)
*DatasetsApi* | [**datasets_rdre_stream_get**](docs/DatasetsApi.md#datasets_rdre_stream_get) | **GET** /datasets/RDRE/stream | Run Down Rate Export (RDRE) stream
*DatasetsApi* | [**datasets_rdri_get**](docs/DatasetsApi.md#datasets_rdri_get) | **GET** /datasets/RDRI | Run Down Rate Import (RDRI)
*DatasetsApi* | [**datasets_rdri_stream_get**](docs/DatasetsApi.md#datasets_rdri_stream_get) | **GET** /datasets/RDRI/stream | Run Down Rate Import (RDRI) stream
*DatasetsApi* | [**datasets_remit_get**](docs/DatasetsApi.md#datasets_remit_get) | **GET** /datasets/REMIT | The Regulation on Wholesale Energy Markets Integrity and Transparency (REMIT)
*DatasetsApi* | [**datasets_remit_stream_get**](docs/DatasetsApi.md#datasets_remit_stream_get) | **GET** /datasets/REMIT/stream | The Regulation on Wholesale Energy Markets Integrity and Transparency (REMIT) stream
*DatasetsApi* | [**datasets_rure_get**](docs/DatasetsApi.md#datasets_rure_get) | **GET** /datasets/RURE | Run Up Rate Export (RURE)
*DatasetsApi* | [**datasets_rure_stream_get**](docs/DatasetsApi.md#datasets_rure_stream_get) | **GET** /datasets/RURE/stream | Run Up Rate Export (RURE) stream
*DatasetsApi* | [**datasets_ruri_get**](docs/DatasetsApi.md#datasets_ruri_get) | **GET** /datasets/RURI | Run Up Rate Import (RURI)
*DatasetsApi* | [**datasets_ruri_stream_get**](docs/DatasetsApi.md#datasets_ruri_stream_get) | **GET** /datasets/RURI/stream | Run Up Rate Import (RURI) stream
*DatasetsApi* | [**datasets_sel_get**](docs/DatasetsApi.md#datasets_sel_get) | **GET** /datasets/SEL | Stable Export Limit (SEL)
*DatasetsApi* | [**datasets_sel_stream_get**](docs/DatasetsApi.md#datasets_sel_stream_get) | **GET** /datasets/SEL/stream | Stable Export Limit (SEL) stream
*DatasetsApi* | [**datasets_sil_get**](docs/DatasetsApi.md#datasets_sil_get) | **GET** /datasets/SIL | Stable Import Limit (SIL)
*DatasetsApi* | [**datasets_sil_stream_get**](docs/DatasetsApi.md#datasets_sil_stream_get) | **GET** /datasets/SIL/stream | Stable Import Limit (SIL) stream
*DatasetsApi* | [**datasets_soso_get**](docs/DatasetsApi.md#datasets_soso_get) | **GET** /datasets/SOSO | SO-SO prices (SOSO)
*DatasetsApi* | [**datasets_soso_stream_get**](docs/DatasetsApi.md#datasets_soso_stream_get) | **GET** /datasets/SOSO/stream | SO-SO prices (SOSO) stream
*DatasetsApi* | [**datasets_syswarn_get**](docs/DatasetsApi.md#datasets_syswarn_get) | **GET** /datasets/SYSWARN | System warnings (SYSWARN)
*DatasetsApi* | [**datasets_syswarn_stream_get**](docs/DatasetsApi.md#datasets_syswarn_stream_get) | **GET** /datasets/SYSWARN/stream | System warnings (SYSWARN) stream
*DatasetsApi* | [**datasets_temp_get**](docs/DatasetsApi.md#datasets_temp_get) | **GET** /datasets/TEMP | Temperature data (TEMP)
*DatasetsApi* | [**datasets_tsdf_get**](docs/DatasetsApi.md#datasets_tsdf_get) | **GET** /datasets/TSDF | Day and day-ahead Transmission System Demand forecast (TSDF)
*DatasetsApi* | [**datasets_tsdf_stream_get**](docs/DatasetsApi.md#datasets_tsdf_stream_get) | **GET** /datasets/TSDF/stream | Day and day-ahead Transmission System Demand forecast (TSDF) stream
*DatasetsApi* | [**datasets_tsdfd_get**](docs/DatasetsApi.md#datasets_tsdfd_get) | **GET** /datasets/TSDFD | 2-14 days ahead Transmission System Demand and surplus forecast (TSDFD)
*DatasetsApi* | [**datasets_tsdfd_stream_get**](docs/DatasetsApi.md#datasets_tsdfd_stream_get) | **GET** /datasets/TSDFD/stream | 2-14 days ahead Transmission System Demand and surplus forecast (TSDFD) stream
*DatasetsApi* | [**datasets_tsdfw_get**](docs/DatasetsApi.md#datasets_tsdfw_get) | **GET** /datasets/TSDFW | 2-52 weeks ahead Transmission System Demand and surplus forecast (TSDFW)
*DatasetsApi* | [**datasets_tsdfw_stream_get**](docs/DatasetsApi.md#datasets_tsdfw_stream_get) | **GET** /datasets/TSDFW/stream | 2-52 weeks ahead Transmission System Demand and surplus forecast (TSDFW) stream
*DatasetsApi* | [**datasets_tudm_get**](docs/DatasetsApi.md#datasets_tudm_get) | **GET** /datasets/TUDM | Trading unit data (S0491_TUDM)
*DatasetsApi* | [**datasets_tudm_stream_get**](docs/DatasetsApi.md#datasets_tudm_stream_get) | **GET** /datasets/TUDM/stream | Trading unit data (S0491_TUDM) stream
*DatasetsApi* | [**datasets_uou2_t14_d_get**](docs/DatasetsApi.md#datasets_uou2_t14_d_get) | **GET** /datasets/UOU2T14D | 2 to 14 days ahead generation availability aggregated by Balancing Mechanism Units (UOU2T14D)
*DatasetsApi* | [**datasets_uou2_t14_d_stream_get**](docs/DatasetsApi.md#datasets_uou2_t14_d_stream_get) | **GET** /datasets/UOU2T14D/stream | 2 to 14 days ahead generation availability aggregated by Balancing Mechanism Units (UOU2T14D) stream
*DatasetsApi* | [**datasets_uou2_t3_yw_get**](docs/DatasetsApi.md#datasets_uou2_t3_yw_get) | **GET** /datasets/UOU2T3YW | 2 to 156 weeks ahead generation availability aggregated by Balancing Mechanism Units (UOU2T3YW)
*DatasetsApi* | [**datasets_uou2_t3_yw_stream_get**](docs/DatasetsApi.md#datasets_uou2_t3_yw_stream_get) | **GET** /datasets/UOU2T3YW/stream | 2 to 156 weeks ahead generation availability aggregated by Balancing Mechanism Units (UOU2T3YW) stream
*DatasetsApi* | [**datasets_watl_get**](docs/DatasetsApi.md#datasets_watl_get) | **GET** /datasets/WATL | Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630)
*DatasetsApi* | [**datasets_watl_stream_get**](docs/DatasetsApi.md#datasets_watl_stream_get) | **GET** /datasets/WATL/stream | Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630) stream
*DatasetsApi* | [**datasets_windfor_get**](docs/DatasetsApi.md#datasets_windfor_get) | **GET** /datasets/WINDFOR | Wind generation forecast (WINDFOR)
*DatasetsApi* | [**datasets_windfor_stream_get**](docs/DatasetsApi.md#datasets_windfor_stream_get) | **GET** /datasets/WINDFOR/stream | Wind generation forecast (WINDFOR) stream
*DatasetsApi* | [**datasets_yafm_get**](docs/DatasetsApi.md#datasets_yafm_get) | **GET** /datasets/YAFM | Year Ahead Forecast Margin (YAFM / B0810)
*DatasetsApi* | [**datasets_yafm_stream_get**](docs/DatasetsApi.md#datasets_yafm_stream_get) | **GET** /datasets/YAFM/stream | Year Ahead Forecast Margin (YAFM / B0810) stream
*DatasetsApi* | [**datasets_yatl_get**](docs/DatasetsApi.md#datasets_yatl_get) | **GET** /datasets/YATL | Year-Ahead Total Load Forecast Per Bidding Zone (YATL / B0650)
*DatasetsApi* | [**datasets_yatl_stream_get**](docs/DatasetsApi.md#datasets_yatl_stream_get) | **GET** /datasets/YATL/stream | Year-Ahead Total Load Forecast Per Bidding Zone (YATL / B0650) stream
*DemandApi* | [**demand_actual_total_get**](docs/DemandApi.md#demand_actual_total_get) | **GET** /demand/actual/total | Actual total load (ATL/B0610)
*DemandApi* | [**demand_get**](docs/DemandApi.md#demand_get) | **GET** /demand | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandApi* | [**demand_outturn_daily_get**](docs/DemandApi.md#demand_outturn_daily_get) | **GET** /demand/outturn/daily | Initial National Demand outturn per day (INDOD)
*DemandApi* | [**demand_outturn_daily_stream_get**](docs/DemandApi.md#demand_outturn_daily_stream_get) | **GET** /demand/outturn/daily/stream | Initial National Demand outturn per day (INDOD) stream
*DemandApi* | [**demand_outturn_get**](docs/DemandApi.md#demand_outturn_get) | **GET** /demand/outturn | Initial National Demand outturn (INDO)
*DemandApi* | [**demand_outturn_stream_get**](docs/DemandApi.md#demand_outturn_stream_get) | **GET** /demand/outturn/stream | Initial National Demand outturn (INDO) stream
*DemandApi* | [**demand_outturn_summary_get**](docs/DemandApi.md#demand_outturn_summary_get) | **GET** /demand/outturn/summary | System demand summary (FUELINST)
*DemandApi* | [**demand_peak_get**](docs/DemandApi.md#demand_peak_get) | **GET** /demand/peak | Peak demand per day (ITSDO)
*DemandApi* | [**demand_peak_indicative_get**](docs/DemandApi.md#demand_peak_indicative_get) | **GET** /demand/peak/indicative | Indicative peak demand per day (S0142, ITSDO, FUELHH)
*DemandApi* | [**demand_peak_indicative_operational_triad_season_get**](docs/DemandApi.md#demand_peak_indicative_operational_triad_season_get) | **GET** /demand/peak/indicative/operational/{triadSeason} | Operational data demand peaks for a Triad season (ITSDO, FUELHH)
*DemandApi* | [**demand_peak_indicative_settlement_triad_season_get**](docs/DemandApi.md#demand_peak_indicative_settlement_triad_season_get) | **GET** /demand/peak/indicative/settlement/{triadSeason} | Settlement data demand peaks for a Triad season (S0142)
*DemandApi* | [**demand_peak_triad_get**](docs/DemandApi.md#demand_peak_triad_get) | **GET** /demand/peak/triad | Triad demand peaks (S0142, ITSDO, FUELHH)
*DemandApi* | [**demand_rolling_system_demand_get**](docs/DemandApi.md#demand_rolling_system_demand_get) | **GET** /demand/rollingSystemDemand | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandApi* | [**demand_stream_get**](docs/DemandApi.md#demand_stream_get) | **GET** /demand/stream | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandApi* | [**demand_summary_get**](docs/DemandApi.md#demand_summary_get) | **GET** /demand/summary | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandApi* | [**demand_total_actual_get**](docs/DemandApi.md#demand_total_actual_get) | **GET** /demand/total/actual | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandForecastApi* | [**forecast_demand_daily_evolution_get**](docs/DemandForecastApi.md#forecast_demand_daily_evolution_get) | **GET** /forecast/demand/daily/evolution | Evolution of the fourteen-day demand forecast over time (NDFD, TSDFD)
*DemandForecastApi* | [**forecast_demand_daily_get**](docs/DemandForecastApi.md#forecast_demand_daily_get) | **GET** /forecast/demand/daily | Fourteen day demand forecast (NDFD, TSDFD)
*DemandForecastApi* | [**forecast_demand_daily_history_get**](docs/DemandForecastApi.md#forecast_demand_daily_history_get) | **GET** /forecast/demand/daily/history | History of the fourteen-day demand forecast (NDFD, TSDFD)
*DemandForecastApi* | [**forecast_demand_day_ahead_earliest_get**](docs/DemandForecastApi.md#forecast_demand_day_ahead_earliest_get) | **GET** /forecast/demand/day-ahead/earliest | Historic view of the earliest forecasted demand (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_earliest_stream_get**](docs/DemandForecastApi.md#forecast_demand_day_ahead_earliest_stream_get) | **GET** /forecast/demand/day-ahead/earliest/stream | Historic view of the earliest forecasted demand (NDF, TSDF) stream
*DemandForecastApi* | [**forecast_demand_day_ahead_evolution_get**](docs/DemandForecastApi.md#forecast_demand_day_ahead_evolution_get) | **GET** /forecast/demand/day-ahead/evolution | Evolution of the day-ahead demand forecast over time (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_get**](docs/DemandForecastApi.md#forecast_demand_day_ahead_get) | **GET** /forecast/demand/day-ahead | Day-ahead demand forecast (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_history_get**](docs/DemandForecastApi.md#forecast_demand_day_ahead_history_get) | **GET** /forecast/demand/day-ahead/history | History of the day-ahead demand forecast (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_latest_get**](docs/DemandForecastApi.md#forecast_demand_day_ahead_latest_get) | **GET** /forecast/demand/day-ahead/latest | Historic view of the latest forecasted demand (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_latest_stream_get**](docs/DemandForecastApi.md#forecast_demand_day_ahead_latest_stream_get) | **GET** /forecast/demand/day-ahead/latest/stream | Historic view of the latest forecasted demand (NDF, TSDF) stream
*DemandForecastApi* | [**forecast_demand_day_ahead_peak_get**](docs/DemandForecastApi.md#forecast_demand_day_ahead_peak_get) | **GET** /forecast/demand/day-ahead/peak | Peak forecasted demand per day (TSDF)
*DemandForecastApi* | [**forecast_demand_total_day_ahead_get**](docs/DemandForecastApi.md#forecast_demand_total_day_ahead_get) | **GET** /forecast/demand/total/day-ahead | Day-ahead total load forecast (DATL/B0620)
*DemandForecastApi* | [**forecast_demand_total_week_ahead_get**](docs/DemandForecastApi.md#forecast_demand_total_week_ahead_get) | **GET** /forecast/demand/total/week-ahead | Week-ahead total load forecast (WATL/B0630)
*DemandForecastApi* | [**forecast_demand_total_week_ahead_latest_get**](docs/DemandForecastApi.md#forecast_demand_total_week_ahead_latest_get) | **GET** /forecast/demand/total/week-ahead/latest | Latest week-ahead total load forecast (WATL/B0630)
*DemandForecastApi* | [**forecast_demand_weekly_evolution_get**](docs/DemandForecastApi.md#forecast_demand_weekly_evolution_get) | **GET** /forecast/demand/weekly/evolution | Evolution of the one-year demand forecast over time  (NDFW, TSDFW)
*DemandForecastApi* | [**forecast_demand_weekly_get**](docs/DemandForecastApi.md#forecast_demand_weekly_get) | **GET** /forecast/demand/weekly | One-year demand forecast (NDFW, TSDFW)
*DemandForecastApi* | [**forecast_demand_weekly_history_get**](docs/DemandForecastApi.md#forecast_demand_weekly_history_get) | **GET** /forecast/demand/weekly/history | History of the one-year demand forecast (NDFW, TSDFW)
*GenerationApi* | [**generation_actual_per_type_day_total_get**](docs/GenerationApi.md#generation_actual_per_type_day_total_get) | **GET** /generation/actual/per-type/day-total | Current snapshot of actual generation by fuel type categories (AGPT/B1620)
*GenerationApi* | [**generation_actual_per_type_get**](docs/GenerationApi.md#generation_actual_per_type_get) | **GET** /generation/actual/per-type | Historic actual generation automatically down-sampled (AGPT/B1620)
*GenerationApi* | [**generation_actual_per_type_wind_and_solar_get**](docs/GenerationApi.md#generation_actual_per_type_wind_and_solar_get) | **GET** /generation/actual/per-type/wind-and-solar | Historic actual or estimated wind and solar power generation (AGWS/B1630)
*GenerationApi* | [**generation_outturn_current_get**](docs/GenerationApi.md#generation_outturn_current_get) | **GET** /generation/outturn/current | Current snapshot of generation by fuel type categories (FUELINST, FUELHH)
*GenerationApi* | [**generation_outturn_fuelinsthhcur_get**](docs/GenerationApi.md#generation_outturn_fuelinsthhcur_get) | **GET** /generation/outturn/FUELINSTHHCUR | This endpoint is obsolete, and this location may be removed with no further notice.
*GenerationApi* | [**generation_outturn_get**](docs/GenerationApi.md#generation_outturn_get) | **GET** /generation/outturn | Total generation outturn (FUELINST)
*GenerationApi* | [**generation_outturn_half_hourly_interconnector_get**](docs/GenerationApi.md#generation_outturn_half_hourly_interconnector_get) | **GET** /generation/outturn/halfHourlyInterconnector | This endpoint is obsolete, and this location may be removed with no further notice.
*GenerationApi* | [**generation_outturn_interconnectors_get**](docs/GenerationApi.md#generation_outturn_interconnectors_get) | **GET** /generation/outturn/interconnectors | Historic half-hourly interconnector flows (FUELINST)
*GenerationApi* | [**generation_outturn_summary_get**](docs/GenerationApi.md#generation_outturn_summary_get) | **GET** /generation/outturn/summary | Historic generation automatically down-sampled (FUELINST)
*GenerationForecastApi* | [**forecast_availability_daily_evolution_get**](docs/GenerationForecastApi.md#forecast_availability_daily_evolution_get) | **GET** /forecast/availability/daily/evolution | Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)
*GenerationForecastApi* | [**forecast_availability_daily_get**](docs/GenerationForecastApi.md#forecast_availability_daily_get) | **GET** /forecast/availability/daily | Fourteen-day generation capacity forecast (FOU2T14D)
*GenerationForecastApi* | [**forecast_availability_daily_history_get**](docs/GenerationForecastApi.md#forecast_availability_daily_history_get) | **GET** /forecast/availability/daily/history | History of the fourteen-day generation capacity forecast (FOU2T14D)
*GenerationForecastApi* | [**forecast_availability_summary14_d_get**](docs/GenerationForecastApi.md#forecast_availability_summary14_d_get) | **GET** /forecast/availability/summary/14D | Down-sampled fourteen-day generation forecast (FOU2T14D)
*GenerationForecastApi* | [**forecast_availability_summary3_yw_get**](docs/GenerationForecastApi.md#forecast_availability_summary3_yw_get) | **GET** /forecast/availability/summary/3YW | Down-sampled three-year generation forecast (FOU2T3YW)
*GenerationForecastApi* | [**forecast_availability_weekly_evolution_get**](docs/GenerationForecastApi.md#forecast_availability_weekly_evolution_get) | **GET** /forecast/availability/weekly/evolution | Evolution of the three-year generation capacity forecast over time (FOU2T3YW)
*GenerationForecastApi* | [**forecast_availability_weekly_get**](docs/GenerationForecastApi.md#forecast_availability_weekly_get) | **GET** /forecast/availability/weekly | Three-year generation capacity forecast (FOU2T3YW)
*GenerationForecastApi* | [**forecast_availability_weekly_history_get**](docs/GenerationForecastApi.md#forecast_availability_weekly_history_get) | **GET** /forecast/availability/weekly/history | History of the three-year generation capacity forecast (FOU2T3YW)
*GenerationForecastApi* | [**forecast_generation_day_ahead_get**](docs/GenerationForecastApi.md#forecast_generation_day_ahead_get) | **GET** /forecast/generation/day-ahead | Day-ahead aggregated generation (DAG/B1430)
*GenerationForecastApi* | [**forecast_generation_wind_and_solar_day_ahead_get**](docs/GenerationForecastApi.md#forecast_generation_wind_and_solar_day_ahead_get) | **GET** /forecast/generation/wind-and-solar/day-ahead | Day-ahead generation forecast for wind and solar (DGWS/B1440)
*GenerationForecastApi* | [**forecast_generation_wind_earliest_get**](docs/GenerationForecastApi.md#forecast_generation_wind_earliest_get) | **GET** /forecast/generation/wind/earliest | Historic view of the earliest forecasted wind generation (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_earliest_stream_get**](docs/GenerationForecastApi.md#forecast_generation_wind_earliest_stream_get) | **GET** /forecast/generation/wind/earliest/stream | Historic view of the earliest forecasted wind generation (WINDFOR) stream
*GenerationForecastApi* | [**forecast_generation_wind_evolution_get**](docs/GenerationForecastApi.md#forecast_generation_wind_evolution_get) | **GET** /forecast/generation/wind/evolution | Evolution of the wind generation forecast over time (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_get**](docs/GenerationForecastApi.md#forecast_generation_wind_get) | **GET** /forecast/generation/wind | Current wind generation forecast (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_history_get**](docs/GenerationForecastApi.md#forecast_generation_wind_history_get) | **GET** /forecast/generation/wind/history | History of the wind generation forecast (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_latest_get**](docs/GenerationForecastApi.md#forecast_generation_wind_latest_get) | **GET** /forecast/generation/wind/latest | Historic view of the latest forecasted wind generation (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_latest_stream_get**](docs/GenerationForecastApi.md#forecast_generation_wind_latest_stream_get) | **GET** /forecast/generation/wind/latest/stream | Historic view of the latest forecasted wind generation (WINDFOR) stream
*GenerationForecastApi* | [**forecast_generation_wind_peak_get**](docs/GenerationForecastApi.md#forecast_generation_wind_peak_get) | **GET** /forecast/generation/wind/peak | Peak wind generation forecast for each day (WINDFOR)
*HealthCheckApi* | [**health_get**](docs/HealthCheckApi.md#health_get) | **GET** /health | Health check
*IndicatedForecastApi* | [**forecast_indicated_day_ahead_evolution_get**](docs/IndicatedForecastApi.md#forecast_indicated_day_ahead_evolution_get) | **GET** /forecast/indicated/day-ahead/evolution | Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
*IndicatedForecastApi* | [**forecast_indicated_day_ahead_get**](docs/IndicatedForecastApi.md#forecast_indicated_day_ahead_get) | **GET** /forecast/indicated/day-ahead | Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
*IndicatedForecastApi* | [**forecast_indicated_day_ahead_history_get**](docs/IndicatedForecastApi.md#forecast_indicated_day_ahead_history_get) | **GET** /forecast/indicated/day-ahead/history | Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_get) | **GET** /balancing/settlement/acceptance/volumes/all/{bidOffer}/{settlementDate} | Acceptance volumes by settlement date (BOAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_settlement_period_get) | **GET** /balancing/settlement/acceptance/volumes/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Acceptance volumes by settlement period (BOAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_acceptances_all_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_acceptances_all_settlement_date_settlement_period_get) | **GET** /balancing/settlement/acceptances/all/{settlementDate}/{settlementPeriod} | Historic acceptances by settlement period (ISPSTACK, BOALF, BOD)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_default_notices_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_default_notices_get) | **GET** /balancing/settlement/default-notices | Default notices (CDN)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_get) | **GET** /balancing/settlement/indicative/cashflows/all/{bidOffer}/{settlementDate} | Indicative period BMU cashflows by settlement date (EBOCF)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_settlement_period_get) | **GET** /balancing/settlement/indicative/cashflows/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Indicative period BMU cashflows by settlement period (EBOCF)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_get) | **GET** /balancing/settlement/indicative/volumes/all/{bidOffer}/{settlementDate} | Indicative volumes by settlement date (DISPTAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_settlement_period_get) | **GET** /balancing/settlement/indicative/volumes/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Indicative volumes by settlement period (DISPTAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_market_depth_settlement_date_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_market_depth_settlement_date_get) | **GET** /balancing/settlement/market-depth/{settlementDate} | Market depth by settlement date (IMBALNGC, BOD, DISEBSP, DISPTAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_market_depth_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_market_depth_settlement_date_settlement_period_get) | **GET** /balancing/settlement/market-depth/{settlementDate}/{settlementPeriod} | Market depth by settlement period (IMBALNGC, BOD, DISEBSP, DISPTAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_messages_settlement_date_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_messages_settlement_date_get) | **GET** /balancing/settlement/messages/{settlementDate} | Settlement messages by settlement date (SMSG)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_messages_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_messages_settlement_date_settlement_period_get) | **GET** /balancing/settlement/messages/{settlementDate}/{settlementPeriod} | Settlement messages by settlement date and period (SMSG)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_stack_all_bid_offer_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_stack_all_bid_offer_settlement_date_settlement_period_get) | **GET** /balancing/settlement/stack/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Settlement bid-offer stacks by settlement period (ISPSTACK)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_summary_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_summary_settlement_date_settlement_period_get) | **GET** /balancing/settlement/summary/{settlementDate}/{settlementPeriod} | Settlement calculation summary (ISPSTACK, DISEBSP, MID, NETBSAD)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_system_prices_settlement_date_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_system_prices_settlement_date_get) | **GET** /balancing/settlement/system-prices/{settlementDate} | Settlement system prices by settlement date (DISEBSP)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_system_prices_settlement_date_settlement_period_get**](docs/IndicativeImbalanceSettlementApi.md#balancing_settlement_system_prices_settlement_date_settlement_period_get) | **GET** /balancing/settlement/system-prices/{settlementDate}/{settlementPeriod} | Settlement system prices by settlement date and period (DISEBSP)
*LegacyApi* | [**interop_message_detail_retrieval_get**](docs/LegacyApi.md#interop_message_detail_retrieval_get) | **GET** /interop/MessageDetailRetrieval | This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
*LegacyApi* | [**interop_message_list_retrieval_get**](docs/LegacyApi.md#interop_message_list_retrieval_get) | **GET** /interop/MessageListRetrieval | This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
*LossOfLoadProbabilityAndDeRatedMarginApi* | [**lolpdrm_forecast_evolution_get**](docs/LossOfLoadProbabilityAndDeRatedMarginApi.md#lolpdrm_forecast_evolution_get) | **GET** /lolpdrm/forecast/evolution | Loss of load probability and de-rated margin forecast (LOLPDRM)
*MarginForecastApi* | [**forecast_margin_daily_evolution_get**](docs/MarginForecastApi.md#forecast_margin_daily_evolution_get) | **GET** /forecast/margin/daily/evolution | Evolution daily margin forecast (OCNMFD2)
*MarginForecastApi* | [**forecast_margin_daily_get**](docs/MarginForecastApi.md#forecast_margin_daily_get) | **GET** /forecast/margin/daily | Daily margin forecast (OCNMFD2)
*MarginForecastApi* | [**forecast_margin_daily_history_get**](docs/MarginForecastApi.md#forecast_margin_daily_history_get) | **GET** /forecast/margin/daily/history | Historical daily margin forecast (OCNMFD2)
*MarginForecastApi* | [**forecast_margin_weekly_evolution_get**](docs/MarginForecastApi.md#forecast_margin_weekly_evolution_get) | **GET** /forecast/margin/weekly/evolution | Evolution daily margin forecast (OCNMFW2, OCNMF3Y2)
*MarginForecastApi* | [**forecast_margin_weekly_get**](docs/MarginForecastApi.md#forecast_margin_weekly_get) | **GET** /forecast/margin/weekly | Weekly margin forecast (OCNMFW2, OCNMF3Y2)
*MarginForecastApi* | [**forecast_margin_weekly_history_get**](docs/MarginForecastApi.md#forecast_margin_weekly_history_get) | **GET** /forecast/margin/weekly/history | Historical weekly margin forecast (OCNMFW2, OCNMF3Y2)
*MarketIndexApi* | [**balancing_pricing_market_index_get**](docs/MarketIndexApi.md#balancing_pricing_market_index_get) | **GET** /balancing/pricing/market-index | Market Index Data (MID) price time series
*NonBMSTORApi* | [**balancing_nonbm_stor_events_get**](docs/NonBMSTORApi.md#balancing_nonbm_stor_events_get) | **GET** /balancing/nonbm/stor/events | Non-BM STOR events (NONBM)
*NonBMSTORApi* | [**balancing_nonbm_stor_get**](docs/NonBMSTORApi.md#balancing_nonbm_stor_get) | **GET** /balancing/nonbm/stor | Non-BM STOR time series (NONBM)
*NonBMVolumesApi* | [**balancing_nonbm_volumes_get**](docs/NonBMVolumesApi.md#balancing_nonbm_volumes_get) | **GET** /balancing/nonbm/volumes | Balancing services volume (QAS)
*REMITApi* | [**remit_get**](docs/REMITApi.md#remit_get) | **GET** /remit | Bulk fetch message details by IDs
*REMITApi* | [**remit_list_by_event_get**](docs/REMITApi.md#remit_list_by_event_get) | **GET** /remit/list/by-event | List messages by event time
*REMITApi* | [**remit_list_by_event_stream_get**](docs/REMITApi.md#remit_list_by_event_stream_get) | **GET** /remit/list/by-event/stream | List messages by event time (stream)
*REMITApi* | [**remit_list_by_publish_get**](docs/REMITApi.md#remit_list_by_publish_get) | **GET** /remit/list/by-publish | List messages by publish time
*REMITApi* | [**remit_list_by_publish_stream_get**](docs/REMITApi.md#remit_list_by_publish_stream_get) | **GET** /remit/list/by-publish/stream | List messages by publish time (stream)
*REMITApi* | [**remit_message_id_get**](docs/REMITApi.md#remit_message_id_get) | **GET** /remit/{messageId} | Fetch message details by ID
*REMITApi* | [**remit_revisions_get**](docs/REMITApi.md#remit_revisions_get) | **GET** /remit/revisions | List all message revisions
*REMITApi* | [**remit_search_get**](docs/REMITApi.md#remit_search_get) | **GET** /remit/search | Fetch message details by mRID
*ReferenceApi* | [**reference_bmunits_all_get**](docs/ReferenceApi.md#reference_bmunits_all_get) | **GET** /reference/bmunits/all | BM Units
*ReferenceApi* | [**reference_fueltypes_all_get**](docs/ReferenceApi.md#reference_fueltypes_all_get) | **GET** /reference/fueltypes/all | Fuel types
*ReferenceApi* | [**reference_interconnectors_all_get**](docs/ReferenceApi.md#reference_interconnectors_all_get) | **GET** /reference/interconnectors/all | Interconnectors
*ReferenceApi* | [**reference_remit_assets_all_get**](docs/ReferenceApi.md#reference_remit_assets_all_get) | **GET** /reference/remit/assets/all | Assets
*ReferenceApi* | [**reference_remit_fueltypes_all_get**](docs/ReferenceApi.md#reference_remit_fueltypes_all_get) | **GET** /reference/remit/fueltypes/all | REMIT fuel types
*ReferenceApi* | [**reference_remit_participants_all_get**](docs/ReferenceApi.md#reference_remit_participants_all_get) | **GET** /reference/remit/participants/all | Participants
*RollingSystemDemandApi* | [**generation_outturn_get**](docs/RollingSystemDemandApi.md#generation_outturn_get) | **GET** /generation/outturn | Total generation outturn (FUELINST)
*SOSOPricesApi* | [**soso_prices_get**](docs/SOSOPricesApi.md#soso_prices_get) | **GET** /soso/prices | SO-SO prices (SOSO)
*SurplusForecastApi* | [**forecast_surplus_daily_evolution_get**](docs/SurplusForecastApi.md#forecast_surplus_daily_evolution_get) | **GET** /forecast/surplus/daily/evolution | Evolution daily surplus forecast (OCNMFD)
*SurplusForecastApi* | [**forecast_surplus_daily_get**](docs/SurplusForecastApi.md#forecast_surplus_daily_get) | **GET** /forecast/surplus/daily | Daily surplus forecast (OCNMFD)
*SurplusForecastApi* | [**forecast_surplus_daily_history_get**](docs/SurplusForecastApi.md#forecast_surplus_daily_history_get) | **GET** /forecast/surplus/daily/history | Historical daily surplus forecast (OCNMFD)
*SurplusForecastApi* | [**forecast_surplus_weekly_evolution_get**](docs/SurplusForecastApi.md#forecast_surplus_weekly_evolution_get) | **GET** /forecast/surplus/weekly/evolution | Evolution weekly surplus forecast (OCNMFW, OCNMF3Y)
*SurplusForecastApi* | [**forecast_surplus_weekly_get**](docs/SurplusForecastApi.md#forecast_surplus_weekly_get) | **GET** /forecast/surplus/weekly | Weekly surplus forecast (OCNMFW, OCNMF3Y)
*SurplusForecastApi* | [**forecast_surplus_weekly_history_get**](docs/SurplusForecastApi.md#forecast_surplus_weekly_history_get) | **GET** /forecast/surplus/weekly/history | Historical weekly surplus forecast (OCNMFW, OCNMF3Y)
*SystemApi* | [**system_demand_control_instructions_get**](docs/SystemApi.md#system_demand_control_instructions_get) | **GET** /system/demand-control-instructions | Demand control instructions (DCI)
*SystemApi* | [**system_frequency_get**](docs/SystemApi.md#system_frequency_get) | **GET** /system/frequency | System frequency (FREQ)
*SystemApi* | [**system_frequency_stream_get**](docs/SystemApi.md#system_frequency_stream_get) | **GET** /system/frequency/stream | System frequency (FREQ) stream
*SystemApi* | [**system_warnings_get**](docs/SystemApi.md#system_warnings_get) | **GET** /system/warnings | System warnings (SYSWARN)
*SystemForecastApi* | [**forecast_system_loss_of_load_get**](docs/SystemForecastApi.md#forecast_system_loss_of_load_get) | **GET** /forecast/system/loss-of-load | Loss of load probability and de-rated margin forecast (LOLPDRM)
*TemperatureApi* | [**temperature_get**](docs/TemperatureApi.md#temperature_get) | **GET** /temperature | Temperature data (TEMP)

## Documentation For Models

 - [InsightsApiLegacyInteroperabilityLegacyRemitDetailBody](docs/InsightsApiLegacyInteroperabilityLegacyRemitDetailBody.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitDetailItem](docs/InsightsApiLegacyInteroperabilityLegacyRemitDetailItem.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitDetailList](docs/InsightsApiLegacyInteroperabilityLegacyRemitDetailList.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitDetailMetadata](docs/InsightsApiLegacyInteroperabilityLegacyRemitDetailMetadata.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse](docs/InsightsApiLegacyInteroperabilityLegacyRemitDetailResponse.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitListItem](docs/InsightsApiLegacyInteroperabilityLegacyRemitListItem.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitListMetadata](docs/InsightsApiLegacyInteroperabilityLegacyRemitListMetadata.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitListResponse](docs/InsightsApiLegacyInteroperabilityLegacyRemitListResponse.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody](docs/InsightsApiLegacyInteroperabilityLegacyRemitListResponseBody.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitOutageProfile](docs/InsightsApiLegacyInteroperabilityLegacyRemitOutageProfile.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitOutageProfileSegment](docs/InsightsApiLegacyInteroperabilityLegacyRemitOutageProfileSegment.md)
 - [InsightsApiLegacyInteroperabilityLegacyRemitResponseList](docs/InsightsApiLegacyInteroperabilityLegacyRemitResponseList.md)
 - [InsightsApiModelsMetadataApiResponseSourceMetadata](docs/InsightsApiModelsMetadataApiResponseSourceMetadata.md)
 - [InsightsApiModelsResponsesBalancingBalancingServicesVolume](docs/InsightsApiModelsResponsesBalancingBalancingServicesVolume.md)
 - [InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse](docs/InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse.md)
 - [InsightsApiModelsResponsesBalancingBidOfferResponse](docs/InsightsApiModelsResponsesBalancingBidOfferResponse.md)
 - [InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse](docs/InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse.md)
 - [InsightsApiModelsResponsesBalancingDatasetRowsBalancingServicesVolumeData](docs/InsightsApiModelsResponsesBalancingDatasetRowsBalancingServicesVolumeData.md)
 - [InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse](docs/InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse.md)
 - [InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse](docs/InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.md)
 - [InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse](docs/InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse.md)
 - [InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData](docs/InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData.md)
 - [InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse](docs/InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse.md)
 - [InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData](docs/InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData.md)
 - [InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse](docs/InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.md)
 - [InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse](docs/InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse.md)
 - [InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData](docs/InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.md)
 - [InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData](docs/InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData.md)
 - [InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData](docs/InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.md)
 - [InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData](docs/InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData.md)
 - [InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData](docs/InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData.md)
 - [InsightsApiModelsResponsesBalancingDynamicDynamicData](docs/InsightsApiModelsResponsesBalancingDynamicDynamicData.md)
 - [InsightsApiModelsResponsesBalancingDynamicRateData](docs/InsightsApiModelsResponsesBalancingDynamicRateData.md)
 - [InsightsApiModelsResponsesBalancingMarketIndexResponse](docs/InsightsApiModelsResponsesBalancingMarketIndexResponse.md)
 - [InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse](docs/InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse.md)
 - [InsightsApiModelsResponsesBalancingNonBmStorResponse](docs/InsightsApiModelsResponsesBalancingNonBmStorResponse.md)
 - [InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData](docs/InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.md)
 - [InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData](docs/InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData.md)
 - [InsightsApiModelsResponsesBalancingPhysicalPhysicalData](docs/InsightsApiModelsResponsesBalancingPhysicalPhysicalData.md)
 - [InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse](docs/InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse.md)
 - [InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs](docs/InsightsApiModelsResponsesBalancingSettlementDerivedDataBidOfferPairs.md)
 - [InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse](docs/InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.md)
 - [InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse](docs/InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.md)
 - [InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse](docs/InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse.md)
 - [InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse](docs/InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse.md)
 - [InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse](docs/InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse.md)
 - [InsightsApiModelsResponsesBalancingSettlementSettlementStackResponse](docs/InsightsApiModelsResponsesBalancingSettlementSettlementStackResponse.md)
 - [InsightsApiModelsResponsesBalancingSettlementSettlementSummaryPrice](docs/InsightsApiModelsResponsesBalancingSettlementSettlementSummaryPrice.md)
 - [InsightsApiModelsResponsesBalancingSettlementSettlementSummaryResponse](docs/InsightsApiModelsResponsesBalancingSettlementSettlementSummaryResponse.md)
 - [InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse](docs/InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingCreditDefaultNoticeResponse.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBalancingServicesVolumeData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBalancingServicesVolumeData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferAcceptanceLevelDatasetResponse.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsBidOfferDatasetResponse.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsCreditDefaultNoticeDatasetResponse.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsDisaggregatedBalancingServicesAdjustmentData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsMarketIndexDatasetResponse.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDatasetRowsNetBalancingServicesAdjustmentData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMaxData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryPeriodMinData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsDeliveryVolumeMaxData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsNoticeData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicDatasetRowsStablePortageLimitData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicRateData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingDynamicRateData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingPhysicalDatasetRowsDeliveryLimitMaxData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesBalancingPhysicalDatasetRowsPhysicalNotificationData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDaily](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDaily.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalWeekly](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalWeekly.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDayAhead](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDayAhead.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsDemandOutturnNational](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsDemandOutturnNational.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsDemandOutturnTransmission](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsDemandOutturnTransmission.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesForecastMarginDatasetRowsForecastMarginDaily](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesForecastMarginDatasetRowsForecastMarginDaily.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesForecastMarginDatasetRowsForecastMarginWeekly](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesForecastMarginDatasetRowsForecastMarginWeekly.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusWeekly](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusWeekly.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitDaily](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitDaily.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityDaily](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityDaily.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsNonBmStorData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsNonBmStorData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedGeneration](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedGeneration.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSoSoPricesDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSoSoPricesDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsTemperatureData](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsTemperatureData.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsActualAggregatedGenerationPerTypeDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsActualAggregatedGenerationPerTypeDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationWindSolarDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationWindSolarDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsActualTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsActualTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsAobeDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsAobeDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsBebDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsBebDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCbsDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCbsDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadAggregatedGenerationDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadAggregatedGenerationDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsFeibDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsFeibDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsIgcpuDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsIgcpuDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsMonthAheadTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsMonthAheadTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsPbcDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsPbcDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsPpbrDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsPpbrDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsWeekAheadTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsWeekAheadTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage](docs/InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage.md)
 - [InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDaily](docs/InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDaily.md)
 - [InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead](docs/InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalDayAhead.md)
 - [InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalWeekly](docs/InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastNationalWeekly.md)
 - [InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily](docs/InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDaily.md)
 - [InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDayAhead](docs/InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionDayAhead.md)
 - [InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly](docs/InsightsApiModelsResponsesDemandForecastDatasetRowsDemandForecastTransmissionWeekly.md)
 - [InsightsApiModelsResponsesDemandForecastDemandForecastDaily](docs/InsightsApiModelsResponsesDemandForecastDemandForecastDaily.md)
 - [InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead](docs/InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)
 - [InsightsApiModelsResponsesDemandForecastDemandForecastPeak](docs/InsightsApiModelsResponsesDemandForecastDemandForecastPeak.md)
 - [InsightsApiModelsResponsesDemandForecastDemandForecastWeekly](docs/InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.md)
 - [InsightsApiModelsResponsesDemandOutturnDatasetRowsDemandOutturnNational](docs/InsightsApiModelsResponsesDemandOutturnDatasetRowsDemandOutturnNational.md)
 - [InsightsApiModelsResponsesDemandOutturnDatasetRowsDemandOutturnTransmission](docs/InsightsApiModelsResponsesDemandOutturnDatasetRowsDemandOutturnTransmission.md)
 - [InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow](docs/InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow.md)
 - [InsightsApiModelsResponsesDemandOutturnDemandOutturn](docs/InsightsApiModelsResponsesDemandOutturnDemandOutturn.md)
 - [InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak](docs/InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.md)
 - [InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak](docs/InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)
 - [InsightsApiModelsResponsesDemandOutturnIndodRow](docs/InsightsApiModelsResponsesDemandOutturnIndodRow.md)
 - [InsightsApiModelsResponsesDemandOutturnRollingSystemDemand](docs/InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.md)
 - [InsightsApiModelsResponsesForecastMarginDatasetRowsForecastMarginDaily](docs/InsightsApiModelsResponsesForecastMarginDatasetRowsForecastMarginDaily.md)
 - [InsightsApiModelsResponsesForecastMarginDatasetRowsForecastMarginWeekly](docs/InsightsApiModelsResponsesForecastMarginDatasetRowsForecastMarginWeekly.md)
 - [InsightsApiModelsResponsesForecastMarginForecastMarginDaily](docs/InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)
 - [InsightsApiModelsResponsesForecastMarginForecastMarginWeekly](docs/InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)
 - [InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily](docs/InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusDaily.md)
 - [InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusWeekly](docs/InsightsApiModelsResponsesForecastSurplusDatasetRowsForecastSurplusWeekly.md)
 - [InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily](docs/InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily.md)
 - [InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly](docs/InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly.md)
 - [InsightsApiModelsResponsesGenerationAggregatedForecast](docs/InsightsApiModelsResponsesGenerationAggregatedForecast.md)
 - [InsightsApiModelsResponsesGenerationAvailabilityDaily](docs/InsightsApiModelsResponsesGenerationAvailabilityDaily.md)
 - [InsightsApiModelsResponsesGenerationAvailabilityWeekly](docs/InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData](docs/InsightsApiModelsResponsesGenerationDatasetRowsAugmentedOutturnData.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitDaily](docs/InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitDaily.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly](docs/InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByBmUnitWeekly.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily](docs/InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeDaily.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly](docs/InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityByFuelTypeWeekly.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityDaily](docs/InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityDaily.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly](docs/InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsNonBmStorData](docs/InsightsApiModelsResponsesGenerationDatasetRowsNonBmStorData.md)
 - [InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast](docs/InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.md)
 - [InsightsApiModelsResponsesGenerationForecastFuelData](docs/InsightsApiModelsResponsesGenerationForecastFuelData.md)
 - [InsightsApiModelsResponsesGenerationGenerationByFuelType](docs/InsightsApiModelsResponsesGenerationGenerationByFuelType.md)
 - [InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn](docs/InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn.md)
 - [InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod](docs/InsightsApiModelsResponsesGenerationOutturnGenerationBySettlementPeriod.md)
 - [InsightsApiModelsResponsesGenerationOutturnGenerationValue](docs/InsightsApiModelsResponsesGenerationOutturnGenerationValue.md)
 - [InsightsApiModelsResponsesGenerationWindGenerationForecast](docs/InsightsApiModelsResponsesGenerationWindGenerationForecast.md)
 - [InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand](docs/InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedDemand.md)
 - [InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedGeneration](docs/InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedGeneration.md)
 - [InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance](docs/InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedImbalance.md)
 - [InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin](docs/InsightsApiModelsResponsesIndicatedForecastDatasetRowsIndicatedMargin.md)
 - [InsightsApiModelsResponsesIndicatedForecastIndicatedForecast](docs/InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)
 - [InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow](docs/InsightsApiModelsResponsesMiscDatasetRowsDemandControlInstructionDatasetRow.md)
 - [InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData](docs/InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData.md)
 - [InsightsApiModelsResponsesMiscDatasetRowsSoSoPricesDatasetRow](docs/InsightsApiModelsResponsesMiscDatasetRowsSoSoPricesDatasetRow.md)
 - [InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency](docs/InsightsApiModelsResponsesMiscDatasetRowsSystemFrequency.md)
 - [InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData](docs/InsightsApiModelsResponsesMiscDatasetRowsSystemWarningsData.md)
 - [InsightsApiModelsResponsesMiscDatasetRowsTemperatureData](docs/InsightsApiModelsResponsesMiscDatasetRowsTemperatureData.md)
 - [InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow](docs/InsightsApiModelsResponsesMiscDatasetRowsTudmDatasetRow.md)
 - [InsightsApiModelsResponsesMiscDemandControlInstructionData](docs/InsightsApiModelsResponsesMiscDemandControlInstructionData.md)
 - [InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse](docs/InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse.md)
 - [InsightsApiModelsResponsesMiscSoSoPrices](docs/InsightsApiModelsResponsesMiscSoSoPrices.md)
 - [InsightsApiModelsResponsesMiscSystemFrequency](docs/InsightsApiModelsResponsesMiscSystemFrequency.md)
 - [InsightsApiModelsResponsesMiscSystemWarningsData](docs/InsightsApiModelsResponsesMiscSystemWarningsData.md)
 - [InsightsApiModelsResponsesMiscTemperatureData](docs/InsightsApiModelsResponsesMiscTemperatureData.md)
 - [InsightsApiModelsResponsesReferenceBmUnitData](docs/InsightsApiModelsResponsesReferenceBmUnitData.md)
 - [InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow](docs/InsightsApiModelsResponsesReferenceDatasetMetadataLatestRow.md)
 - [InsightsApiModelsResponsesReferenceInterconnectorData](docs/InsightsApiModelsResponsesReferenceInterconnectorData.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBalancingServicesVolume.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferAcceptancesResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingBidOfferResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentDetailsResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDisaggregatedBalancingServicesAdjustmentSummaryResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicDynamicData.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingDynamicRateData.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNetBalancingServicesAdjustmentResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNonBmStorResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingNonBmStorResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingPhysicalPhysicalData.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementAcceptanceVolumeResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementHistoricAcceptanceResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeCashflowResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementIndicativeVolumeResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementMarketDepthResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementMessageResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementStackResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSettlementStackResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingSettlementSystemPriceResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDaily.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastDayAhead.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastPeak.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturn.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnDemandOutturnPeak.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndicativeDemandPeak.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnIndodRow.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesDemandOutturnRollingSystemDemand.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginDaily.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastMarginForecastMarginWeekly.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusDaily.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesForecastSurplusForecastSurplusWeekly.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityDaily.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationAvailabilityWeekly.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationHalfHourlyInterconnectorOutturn.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesGenerationWindGenerationForecast.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesIndicatedForecastIndicatedForecast.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSoSoPrices](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSoSoPrices.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscTemperatureData.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualGenerationWindSolar.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.md)
 - [InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone](docs/InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone.md)
 - [InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod](docs/InsightsApiModelsResponsesTransparencyActualGenerationBySettlementPeriod.md)
 - [InsightsApiModelsResponsesTransparencyActualGenerationValue](docs/InsightsApiModelsResponsesTransparencyActualGenerationValue.md)
 - [InsightsApiModelsResponsesTransparencyActualGenerationWindSolar](docs/InsightsApiModelsResponsesTransparencyActualGenerationWindSolar.md)
 - [InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone](docs/InsightsApiModelsResponsesTransparencyActualTotalLoadPerBiddingZone.md)
 - [InsightsApiModelsResponsesTransparencyAgptSummaryData](docs/InsightsApiModelsResponsesTransparencyAgptSummaryData.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsActualAggregatedGenerationPerTypeDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsActualAggregatedGenerationPerTypeDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse](docs/InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationOutputPerGenerationUnitDatasetResponse.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationWindSolarDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsActualGenerationWindSolarDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsActualTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsActualTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsAobeDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsAobeDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsBebDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsBebDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsCbsDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsCbsDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadAggregatedGenerationDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadAggregatedGenerationDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadGenerationForWindAndSolarDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsDayAheadTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsFeibDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsFeibDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsIgcaDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsIgcpuDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsIgcpuDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsMonthAheadTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsMonthAheadTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsPbcDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsPbcDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsPpbrDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsPpbrDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsWeekAheadTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsWeekAheadTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadForecastMarginDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow](docs/InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.md)
 - [InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration](docs/InsightsApiModelsResponsesTransparencyDayAheadAggregatedGeneration.md)
 - [InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar](docs/InsightsApiModelsResponsesTransparencyDayAheadGenerationForWindAndSolar.md)
 - [InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone](docs/InsightsApiModelsResponsesTransparencyDayAheadTotalLoadPerBiddingZone.md)
 - [InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData](docs/InsightsApiModelsResponsesTransparencyRemitDatasetRowsOutageProfileData.md)
 - [InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage](docs/InsightsApiModelsResponsesTransparencyRemitDatasetRowsRemitMessage.md)
 - [InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl](docs/InsightsApiModelsResponsesTransparencyRemitRemitMessageIdentifierWithUrl.md)
 - [InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId](docs/InsightsApiModelsResponsesTransparencyRemitRemitMessageWithId.md)
 - [InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone](docs/InsightsApiModelsResponsesTransparencyWeekAheadTotalLoadPerBiddingZone.md)
 - [InsightsApiModelsServiceDayAheadDemandForecastRow](docs/InsightsApiModelsServiceDayAheadDemandForecastRow.md)
 - [InsightsApiModelsServiceWindGenerationForecastRow](docs/InsightsApiModelsServiceWindGenerationForecastRow.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author



## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://richasharma.co.in/"><img src="https://avatars.githubusercontent.com/u/41283476?v=4?s=100" width="100px;" alt="Richa"/><br /><sub><b>Richa</b></sub></a><br /><a href="https://github.com/openclimatefix/Elexonpy/commits?author=14Richa" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/peterdudfield"><img src="https://avatars.githubusercontent.com/u/34686298?v=4?s=100" width="100px;" alt="Peter Dudfield"/><br /><sub><b>Peter Dudfield</b></sub></a><br /><a href="https://github.com/openclimatefix/Elexonpy/pulls?q=is%3Apr+reviewed-by%3Apeterdudfield" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mduffin95"><img src="https://avatars.githubusercontent.com/u/6598483?v=4?s=100" width="100px;" alt="Matthew Duffin"/><br /><sub><b>Matthew Duffin</b></sub></a><br /><a href="#ideas-mduffin95" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Jacqueline-J"><img src="https://avatars.githubusercontent.com/u/108654780?v=4?s=100" width="100px;" alt="Jacqueline James"/><br /><sub><b>Jacqueline James</b></sub></a><br /><a href="https://github.com/openclimatefix/Elexonpy/commits?author=Jacqueline-J" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!