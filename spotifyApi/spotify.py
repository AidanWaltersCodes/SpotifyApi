"""Python File for working with the Spotify API"""

#Spotify python import
import spotipy
#dotenv will let me put my tokens in a file that will be ignored by git
from dotenv import load_dotenv
#This will allow me to grab my keys from the env file
import os 
from spotipy.oauth2 import SpotifyOAuth

#Load variables created in .env file
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")


scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])



