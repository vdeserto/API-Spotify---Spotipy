import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid ="ec3e5e205b634356b5e4b82496b72dec"
secret = "c4decac528e349c9b17d5662065dcfb5"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

arquivo = json.loads(open("dados.json", "r").read())


for cantor in arquivo:
    for item in cantor:
        aux = (cantor[item][1])
        aux = (aux["Alb"])
        for album in aux[1:]:
            #ja consigo imprimir o nome dos albuns
            
