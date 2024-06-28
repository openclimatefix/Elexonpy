""" File to get all the routes of the api """
import json
import requests
import pandas as pd
import sys

# returns JSON object as
# a dictionary
with open(
    "prod-insol-insights-api.json",
) as f:
    data = json.load(f)

# Note on date availability
base_url = 'https://data.elexon.co.uk/bmrs/api/v1'

# Function to automatically generate functions to retrieve data from API
def generate_function_from_openapi(openapi_json):
    path_items = openapi_json.get("paths", {})

    # Iterate over each path
    for path, methods in path_items.items():
        # Iterate through each method and extract details
        for method, details in methods.items():
            # Generate function name
            function_name = details.get("operationId", "retrieve_data_from_elexon_api").replace("-", "_")
            # Generate list of parameters to be used in the call function
            parameters = details.get("parameters", [])
            param_name_list = [param["name"] for param in parameters if param["name"]]
            param_str = ', '.join(param_name_list)
            param_str = param_str.replace("format", "json").replace("from", "date_from").replace("to", "date_to")
            print("")

            # Print the function signature
            print(f"def {function_name}({param_str}):")
            print("")

            # Construct the docstring
            print(f"    \"\"\"")
            print(f"    Get the {details.get('summary', 'No summary provided')}")
            print(f"    This function requests data from the '{path}' endpoint")
            path_lookup = path.replace('/', '-')
            print(f"    See https://developer.data.elexon.co.uk/api-details#api=prod-insol-insights-api&operation=get{path_lookup} for more information")
            print("")
            print(f"    Args:")
            # Format the parameter descriptions to appear in the docstring
            for param in parameters:
                # Get the parameter name
                param_name = param["name"]
                # Get the description for the parameter
                param_desc = param.get("description", "")
                # Get the valid options for the parameter
                format_enum = param["schema"].get("enum", [])
                # Convert the list of parameter options into a string
                format_enum_str = f" Use {', '.join(format_enum)}." if format_enum else ""
                # Create the string to be used as the description of each parameter
                final_desc = f"{param_name}: {param_desc}{format_enum_str}"
                # Rename "from" and "to" to avoid conflicts with reserved keywords
                # Rename 'format' to 'json' to control the choice of data format
                final_desc_renamed = final_desc.replace("format", "'json'").replace("from", "date_from").replace("to", "date_to")
                print(f"        {final_desc_renamed}")

            print("")
            print(f"    Raises:")
            print(f"        Exception: If the request fails or returns a non-200 status code.")
            print(f"    \"\"\"")
            print("")

            # Generate the base URL and the request URL
            url = f"{base_url}{path}"
            print(f"    url = '{url}'")
            print("")

            # Generate the parameter dictionary
            print("    params = {")
            for param_name in param_name_list:
                # Rename values to avoid conflicts with reserved keywords, and to define the format
                renamed_param_name = param_name.replace("from", "date_from").replace("to", "date_to").replace("format", "'json'")
                # Print the original parameter name for API recognition and re-formatted names for Python compatibility
                print(f"        '{param_name}': {renamed_param_name},")
            print("    }")
            print("")

            # Run the API request
            print("    # Run the API request")
            print("    response = requests.get(url, params=params)")
            print("")
            print("    if response.status_code == 200:")
            print("        data = response.json()")
            print("        # Convert JSON output to DataFrame")
            print("        df = json_to_dataframe_with_metadata(data)")
            print("    else:")
            print("        raise Exception(f'Error: {response.status_code}')")
            print("")
            print("    return df")
            print("")
            print("")

# Redirect stdout to the file
with open("openapi_functions.py", "w") as f:
    original_stdout = sys.stdout  # Save a reference to the original standard output
    sys.stdout = f  # Redirect stdout to the file

    try:
        # Call the function to capture the print messages
        generate_function_from_openapi(data)
    finally:
        sys.stdout = original_stdout  # Restore stdout to its original state
