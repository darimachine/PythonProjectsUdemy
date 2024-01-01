import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import json
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="51871ca01c1345bab108cc6b74dd9aae",
                                                           client_secret="ee1ca79dcd054f3d95889fe199facca5",
                                                           scope="playlist-modify-private",
                                               redirect_uri="http://example.com",
                                              ))
user_id = sp.current_user()["id"]
print(user_id)
#Web Scraping with BeatifullSoup
year = input("What year would you like to travel YYYY-MM-DD\n")
URl = f"https://www.billboard.com/charts/hot-100/{year}/"
response = requests.get(URl)
response.raise_for_status()
soup = BeautifulSoup(response.text,"html.parser")
musics = soup.find_all("h3",id="title-of-a-story",class_="u-letter-spacing-0021")

top100=[music.text.strip() for music in musics]
top100 = [value for value in top100 if value!="Songwriter(s):" and value!="Producer(s):" and value!="Imprint/Promotion Label:"]
print(top100)
music_uri =[]
for name in top100:
    uri = f"track:{name} year:{year.split('-')[0]}"
    print(uri)
    try:
        musics = sp.search(q=uri,type="track")
        music_uri.append(musics["tracks"]["items"][0]["uri"])
    except:
        print(f"{name} doesn't exist in Spotify. Skipped.")
print(json.dumps(music_uri,indent=3))
name =f"{year} BillBoard 100"
new_playlist = sp.user_playlist_create(user=user_id,name=name,public=False,description="top 100 songs")
print(f" Click to this link to see your playlist made by: Serhan {json.dumps(new_playlist['external_urls']['spotify'],indent=3)} ")
playlist_id = new_playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id,items=music_uri)

#sp.playlist_add_items()

