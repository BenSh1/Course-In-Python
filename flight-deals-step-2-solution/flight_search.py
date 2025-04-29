import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "X7rRxWYZ-yrXXM0SKIO_B4E3K1xQk3_s"


class FlightSearch:

    def __init__(self,city_name):
        #self.destination_data = {}
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey":TEQUILA_API_KEY}
        query = {"term":city_name , "location_types":"city"}
        response = requests.get(url=location_endpoint,headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code


    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code
