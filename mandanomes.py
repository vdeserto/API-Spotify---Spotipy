import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

cid ="34acb700848b455ebc323e943883d059"

secret = "a77e0f95dce246d29405e12cf40a1c88"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

arquivo2 = open('names.txt', 'r')
arquivo = open("nom.txt", "w")
id  = "3HNnxK7NgLXbDoxRZxNWiR"


result_json2 = sp.album(id)
print(result_json2)
for i in range(10):
    print(i)

result = json.dumps(result_json2)
