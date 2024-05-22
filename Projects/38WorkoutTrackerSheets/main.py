import requests
import os 
from dotenv import load_dotenv

# loading the .env file to access our environment variables
load_dotenv()

lang_for_exercise_endpoint = "/v2/natural/exercise"

# defining headers to auth our api request
header = {
    "x-app-id": os.environ.get("app_id"),
    "x-app-key": os.environ.get("api_key")
}