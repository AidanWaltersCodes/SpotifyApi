"""Python File for working with the Spotify API"""

#Spotify python import
import spotipy

#dotenv will let me put my tokens in a file that will be ignored by git
from dotenv import load_dotenv

#Load variables created in .env file
load_dotenv()


CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret