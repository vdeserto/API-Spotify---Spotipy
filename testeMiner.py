import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

cid ="ec3e5e205b634356b5e4b82496b72dec"
secret = "c4decac528e349c9b17d5662065dcfb5"
idAlbum = "3HNnxK7NgLXbDoxRZxNWiR"
arquivo = open('teste.json', 'w')

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


result_json2 = sp.album(idAlbum)

arquivo.writelines(json.dumps(result_json2))