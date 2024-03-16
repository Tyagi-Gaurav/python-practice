import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth

LAB_CLIENT_ID = "938963804a9746dc8ee190a909f83a4f"
LAB_CLIENT_SECRET = "b758565724c54d8b844f8d44d3af43ea"

requested_date = "1979-05-24"  # input("Which year would you like to travel to? Type date in YYYY-MM-DD format: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{requested_date}/")
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

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
    playist_id = found_playlists[0]["id"]
else:
    playlist_creation_response = sp.user_playlist_create(user_id, requested_date, description="Test playlist")
    print(playlist_creation_response)
    playist_id = playlist_creation_response["id"]

for song in song_names:
    track_response = sp.search(q=f"year:1975-1980 track:{song   }", limit=1)
    if (len(track_response["tracks"]["items"])) > 0:
        track_url = track_response["tracks"]["items"][0]["external_urls"]["spotify"]
        add_response = sp.playlist_add_items(playist_id, items=[track_url])
        print(add_response)
