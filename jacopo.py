# %% [markdown]
# # **Data scraping of spotify artists data**

# %%
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tqdm as tqdm
load_dotenv() # Loads variables from .env files

# %%
api_key = os.getenv("SPOTIFY_API_KEY")
client_id = os.getenv("SPOTIFY_CLIENT_ID")
redirect_uri = "https://github.com/Jacopo00811/socialgraphs2025-project"

# %%
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=api_key)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print(f"{i + 1 + playlists['offset']:4d} {playlist['uri']} {playlist['name']}")
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

# %%
# get the artists in the top 50 global playlist
playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
results = sp.playlist_items(playlist_id, additional_types=['track'], market='US')


