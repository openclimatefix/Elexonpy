# elexonpy
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-7-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


[![tags badge](https://img.shields.io/github/v/tag/openclimatefix/elexonpy?include_prereleases&sort=semver&color=FFAC5F)](https://github.com/openclimatefix/ocf-template/tags)
[![pypi badge](https://img.shields.io/pypi/v/elexonpy?&color=07BCDF)](https://pypi.org/project/elexonpy)
[![ease of contribution: easy](https://img.shields.io/badge/ease%20of%20contribution:%20easy-32bd50)](https://github.com/openclimatefix#how-easy-is-it-to-get-involved) 

**elexonpy** is a Python package that provides a convenient interface to the [ELEXON API](https://developer.data.elexon.co.uk/).

This package is generated using Swagger Codegen, ensuring compatibility and ease of use with the ELEXON API services.


## Installation

You can install the `elexonpy` package via pip from PyPI.

```shell
pip install elexonpy
```

## Examples usage

There are some examples in the `examples` directory that demonstrate how to use the package to retrieve data from the Elexon API.

### Example 1: Demand

This example demonstrates how to use methods from the `DemandApi` to retrieve various types of 
demand data from the Elexon API and format it into a DataFrame.


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

### Example 2: SIP price

This example demonstrates how to use methods from the `IndicativeImbalanceSettlementApi` 
to retrieve settlement system prices data from the Elexon API and format it into a DataFrame.


<details><summary> Example 2 </summary>

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

</details>



### Example 3 : DA Solar and Wind Forecast

This example demonstrates how to use methods from the `GenerationForecastApi` to retrieve 
day-ahead forecast data for wind and solar generation from the Elexon API and format it into a DataFrame.

<details><summary> Example 3 </summary>

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

</details>


## Documentation 

### API Endpoints

Documentation for the API Endpoints can be found [here](./docs/DocApiEndpointsList.md)

### Models
Documentation for the Models can be found [here](./docs/DocModelsList.md)

### Authorization

 All endpoints do not require authorization.


##  FAQ

### How do I get an API key?

You dont need one. The Elexon API does not require an API key for access.

### How do I get a year wroth of data?

You currently have to write a loop yourself. We hope to incorporate this into the package in the future.

## Development

To install the package directly from the GitHub repository, use the following command:

```shell
 pip install git+https://github.com/openclimatefix/Elexonpy.git
```

### Tests

To run the tests use `pytest`

## Contributing and community

[![issues badge](https://img.shields.io/github/issues/openclimatefix/elexonpy?color=FFAC5F)](https://github.com/openclimatefix/elexonpy/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)

- PR's are welcome! See the [Organisation Profile](https://github.com/openclimatefix) for details on contributing
- Find out about our other projects in the [OCF Meta Repo](https://github.com/openclimatefix/ocf-meta-repo)
- Check out the [OCF blog](https://openclimatefix.org/blog) for updates
- Follow OCF on [LinkedIn](https://uk.linkedin.com/company/open-climate-fix)


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
      <td align="center" valign="top" width="14.28%"><a href="http://anaskhan.me"><img src="https://avatars.githubusercontent.com/u/83116240?v=4?s=100" width="100px;" alt="Anas Khan"/><br /><sub><b>Anas Khan</b></sub></a><br /><a href="#maintenance-anxkhn" title="Maintenance">🚧</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
