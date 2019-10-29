import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid ="ec3e5e205b634356b5e4b82496b72dec"
secret = "c4decac528e349c9b17d5662065dcfb5"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

arquivo = json.loads(open("dados.json", "r").read())

for cantor in arquivo[:1]:
    aux = (cantor["Eminem"][1])


aux2 = aux["Alb"]
for alb in aux2:
    artist = alb["artists"]
    for artist in album:
        print(artist)



for album in aux2:
    #print(album["artists"])

    '''for artist in artists:
        print(artist["name"])'''

'''
au = (aux["tracks"])
au = au["items"]


for tag in au:
    artists = tag["artists"]
    for artist in artists:
        print(artist["name"])
'''
