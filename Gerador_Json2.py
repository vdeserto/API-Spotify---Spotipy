import json
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

cid ="ec3e5e205b634356b5e4b82496b72dec"

secret = "c4decac528e349c9b17d5662065dcfb5"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

arquivo = open("dados.json", "w")
arquivo2 = open('cantores.txt', 'r')


art = '7HGNYPmbDrMkylWqeFCOIQ'
alb = '0bW7duZq6GtoM8nEwtbc6F'


def info_artist(id):
    result_json = sp.album(id)
    result = json.dumps(result_json)
    arquivo.writelines(result)
    print(result)


def search(q):
    lista = []
    results = sp.search(q, type='artist', limit=1)
    results = results['artists']
    results = results['items']
    for artist in results:
    	info_artist(artist['id'])


info_artist(alb)



#arquivo.writelines ("]")
arquivo.close()
arquivo3 = json.loads(open("dados.json", "r").read())


#arquivo3 = json.dumps(open("dados.json", "r").read())
