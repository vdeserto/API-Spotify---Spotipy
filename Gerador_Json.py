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

arquivo.writelines ("[")

def info_artist(id):
    r = sp.artist(id)
    result_json = sp.artist(id)
    result = json.dumps(result_json)
    arquivo.writelines ("{\""+r["name"]+"\": [")
    arquivo.writelines (result)
    show_artist_albums(id)


def show_artist_albums(id):
    lista = []
    albums = sp.artist_albums(id, album_type='album')
    lista.extend(albums['items'])
    while albums['next']:
    	albums = sp.next(albums)
    	lista.extend(albums['items'])
    unique = set()  # skip duplicate albums
    for album in lista:
        name = album['name'].lower()
        if not name in unique:
            info_album(album['id'])
            unique.add(name)
    arquivo.writelines ("]}")

def info_album(id):
    arquivo.writelines (", ")
    result_json2 = sp.album(id)
    result = json.dumps(result_json2)
    arquivo.writelines (result)


def search(q):
    lista = []
    results = sp.search(q, type='artist', limit=1)
    results = results['artists']
    results = results['items']
    for artist in results:
        info_artist(artist['id'])



i = 0
for cantor in arquivo2:
    if(i !=0):
        arquivo.writelines (", ")
    search(cantor)
    i = i + 1


arquivo.writelines ("]")
arquivo.close()
arquivo3 = json.loads(open("dados.json", "r").read())
print(arquivo3[0])

#arquivo3 = json.dumps(open("dados.json", "r").read())
