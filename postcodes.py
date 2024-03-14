import json
import requests


class PostcodeApi:
    def __init__(self):
        pass

    def get_postcode(self, postcode):

        try:
            response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}', )
            if response.status_code == 200 or response.status_code == 201:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"error found: {e}")
            return None

    def post_request_postcode(self, postcode_input):
        """
        :put in postcodes in a list format as postcode_input
        """
        response = requests.post(f'https://api.postcodes.io/postcodes',json={'postcodes': postcode_input})
        return response.json()

post_code_api = PostcodeApi()

print(post_code_api.post_request_postcode())


#print(PostcodeApi().get_postcode('SW112RG'))
# '.format(postcode=postcode
