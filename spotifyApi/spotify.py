"""Python File for working with the Spotify API"""

#Spotify python import
import spotipy

#dotenv will let me put my tokens in a file that will be ignored by git
from dotenv import load_dotenv

#This will allow me to grab my keys from the env file
import os 

#Load variables created in .env file
load_dotenv()


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

