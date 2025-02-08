import os
import json
import requests

class Skyscanner:
    def __init__(self):
        self.name = "Skyscanner"
        self.session_token = None
        self.headers = {
        'x-rapidapi-key': os.getenv('RAPIDAPI_API_KEY',''),
        'x-rapidapi-host': os.getenv('RAPIDAPI_HOST','sky-scanner3.p.rapidapi.com')
        }


    # def get_flights(self, origin, destination, date):
    #     """
    #     Get flights from origin to destination on a specific date.

    #     Example:
    #     get_flights("San franciso", "New york", "2022-12-31")
    #     Args:
    #         origin (str): Origin of the flight
    #         destination (str): Destination of the flight
    #         date (str): Date of the flight in the format "YYYY-MM-DD"
    #     Returns:
    #         str: The API response of getting flights from Skyscanner or an error message if the flights could not be fetched    
    #     """
    #     url = f"https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/{self.api_key}/US/USD/en-US/{origin}/{destination}/{date}"
    #     response = requests.get(url)
    #     return response.content
    
    def get_cheapest_flight(self, origin, destination, date):
        """
        Get the cheapest flight from origin to destination on a specific date.

        Example:
        get_cheapest_flight("SFO", "JFK", 
        )
        Args:
            origin (str): Origin of the flight
            destination (str): Destination of the flight
            date (str): Date of the flight in the format "YYYY-MM-DD"
        Returns:
            str: The API response of getting the cheapest flight from Skyscanner or an error message if the flight could not be fetched    
        """
        url = "https://sky-scanner3.p.rapidapi.com/flights/cheapest-one-way"

        querystring = {"fromEntityId":origin,"toEntityId":destination,"departDate":date}
        response = requests.get(url, headers=self.headers, params=querystring)

        data = response.json()
        return json.dumps(data['data'])
    
