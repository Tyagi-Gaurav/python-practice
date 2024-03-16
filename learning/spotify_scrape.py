from jproperties import Properties
import spotipy
from bs4 import BeautifulSoup
import requests
import os
from spotipy.oauth2 import SpotifyOAuth

configs = Properties()

with open(f"{os.getenv('HOME')}/.secrets", 'rb') as config_file:
    configs.load(config_file)

LAB_CLIENT_ID = configs.get("SPOTIFY_LAB_CLIENT_ID").data
LAB_CLIENT_SECRET = configs.get("SPOTIFY_LAB_CLIENT_SECRET").data

requested_date = input("Which year would you like to travel to? Type date in YYYY-MM-DD format: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{requested_date}/")
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=LAB_CLIENT_ID,
                                               client_secret=LAB_CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read,playlist-modify-private,playlist-modify-public"))

user_id = sp.current_user()["id"]
# print(user_id)
playlists = sp.user_playlists(user_id, limit=10)
found_playlists = [item for item in playlists["items"] if item['name'] == requested_date]
if len(found_playlists) > 0:
    print("Playlist already exists")
    playlist_id = found_playlists[0]["id"]
else:
    playlist_creation_response = sp.user_playlist_create(user_id, requested_date, description="Test playlist")
    print(playlist_creation_response)
    playlist_id = playlist_creation_response["id"]

for song in song_names:
    track_response = sp.search(q=f"year:1975-1980 track:{song}", limit=1)
    if (len(track_response["tracks"]["items"])) > 0:
        track_url = track_response["tracks"]["items"][0]["external_urls"]["spotify"]
        add_response = sp.playlist_add_items(playlist_id, items=[track_url])
        print(f"Adding {song} to playlist {requested_date}")
