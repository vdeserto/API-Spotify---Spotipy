import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials



cid ="ec3e5e205b634356b5e4b82496b72dec"
secret = "c4decac528e349c9b17d5662065dcfb5"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

arquivo = open('cantores.txt', 'r')
arquivo2 = open('dados.txt', 'w')


def info_album(id):
	album = sp.album(id)
	arquivo2.writelines(str(album))

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

def info_artist(id):
    artist = sp.artist(id)
    arquivo2.writelines(str(artist))
    show_artist_albums(id)


def search(q):
    lista = []
    results = sp.search(q, type='artist', limit=1)
    results = results['artists']
    results = results['items']
    for artist in results:
    	info_artist(artist['id'])


for cantor in arquivo:
	search(cantor)
