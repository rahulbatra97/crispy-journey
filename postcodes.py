import json
import requests

# def get_json_data(url):               #retrieving data from a URL specified pn postcodes/docs
#
#     try:
#         response = requests.get(url)
#         json_data = response.json()
#         return json_data
#
#         return json_data
#     except requests.exceptions.RequestException as e:
#         print(f"error found: {e}")
#         return None
#
# postcode_api_url = "https://api.postcodes.io"
# json_data = get_json_data(postcode_api_url)
#
#
#
#
# if json_data:
#     # Process the JSON data as needed
#     print(json_data)


response = requests.get('https://api.postcodes.io')

if response.status_code == 200:

    print(response.text)

else:
    print(f"error found: {e}")

# convert to a python dictionary
