import pandas as pd
import spotipy
sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials
cid ="xxxxx"
secret = "xxxx"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False


uri = 'spotify:user:spotify:playlist:37i9dQZF1DX5EkyRFIV92g'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

results = sp.user_playlist(username, playlist_id)
print json.dumps(results, indent=4)
