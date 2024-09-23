# elexonpy
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

**elexonpy** is a Python package that provides a convenient interface to the [ELEXON API](https://developer.data.elexon.co.uk/).


This package is generated using Swagger Codegen, ensuring compatibility and ease of use with the ELEXON API services.
The package is available on PyPI and can be easily installed via pip.

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


```python
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
df = demand_api.demand_actual_total_get(
    _from=from_date,
    to=to_date,
    settlement_period_from=1,
    settlement_period_to=48,
    format='dataframe'
)

# Print Actual Total Load Data DataFrame
print("\n--- Actual Total Load Data ---")
print(df.head())
```

### Example 2:

This example demonstrates how to use methods from the `IndicativeImbalanceSettlementApi` to retrieve settlement system prices data from the Elexon API and format it into a DataFrame using pandas.

```python
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
```

### Example 3 :

This example demonstrates how to use methods from the `GenerationForecastApi` to retrieve day-ahead forecast data for wind and solar generation from the Elexon API and format it into a DataFrame using pandas.

```python
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
df = forecast_api.forecast_generation_wind_and_solar_day_ahead_get(
    _from=from_date,
    to=to_date,
    process_type='day ahead',
    format='dataframe'
)

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

Documentation for the API Endpoints can be found [here](./docs/DocApiEndpointsList.md)

## Documentation For Models
Documentation for the Models can be found [here](./docs/DocModelsList.md)

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
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yousefsawy"><img src="https://avatars.githubusercontent.com/u/99139949?v=4?s=100" width="100px;" alt="Yousef Elsawy"/><br /><sub><b>Yousef Elsawy</b></sub></a><br /><a href="https://github.com/openclimatefix/Elexonpy/commits?author=yousefsawy" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Sigma-Verma"><img src="https://avatars.githubusercontent.com/u/131307209?v=4?s=100" width="100px;" alt="Utkarsh Verma"/><br /><sub><b>Utkarsh Verma</b></sub></a><br /><a href="#maintenance-Sigma-Verma" title="Maintenance">🚧</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
