import json
import requests


class PostcodeApi:
    def __init__(self):
        pass

    def get_postcode(self, postcode):

        try:
            response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}'.format(postcode=postcode))
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"error found: {e}")
            return None


print(PostcodeApi().get_postcode('SW112RG'))
