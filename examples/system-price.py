from elexonpy.api_client import ApiClient
from swagger_client.api.system_api import SystemApi

# Initialize ApiClient and SystemApi
api_client = ApiClient()
system_api = SystemApi(api_client)


try:
    response = system_api.system_frequency_get(_from='2024-01-01T00:00:00Z', to='2024-01-02T00:00:00Z')
    print("Response type:", type(response))
    print(response)
except Exception as e:
    print(f"Error: {str(e)}")
