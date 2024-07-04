import requests

class Post:
    # Initializing our variables
    def __init__(self):
        self.api_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

    # Getting blogs from our api 
    def get_blogs(self):
        response = requests.get(url=self.api_endpoint)
        response.raise_for_status()

        blog_data = response.json()

        return blog_data