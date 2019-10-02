# -*- coding: utf-8 -*-
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

cid ="ec3e5e205b634356b5e4b82496b72dec"
secret = "c4decac528e349c9b17d5662065dcfb5"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

art = '7dGJo4pcD2V6oG8kP0tJRR'
art2 = 'spotify:artist:3fMbdgg4jU18AjLCKBhRSm'
tra = 'spotify:track:4xkOaSrkexMciUUogZKVTS'
alb = 'spotify:album:1ATL5GLyefJaxhQzSPVrLX'

arquivo = open('dados.txt', 'w')

'''Métodos usados com Tracks'''
def info_track(id):
    track = sp.track(id)
    print (track)

def track_popularity(id):
    pop = sp.track(id)
    print(pop['popularity'])


def artist_name(id):
    track  = sp.track(id)
    for name in track['artists']:
        print(name['name'])

def available_markets(id):
    track = sp.track(id)
    print(track['available_markets'])

def albums_name(id):
    track = sp.track(id)
    track2 = track['album']
    print(track2['name'])



'''Métodos usados com artistas'''
def info_artist(id):
    artist = sp.artist(id)
    arquivo.writelines(str(artist))
    print(artist)

def top_musicas(id):
    musics = sp.artist_top_tracks(id)
    for track in musics['tracks'][:10]:
        print ('track : ' + track['name'])

def followers(id):
    follow = sp.artist(id)
    qtd = follow['followers']
    print(qtd)
    print(qtd["total"])

def genre(id):
    genre = sp.artist(id)
    for name in genre['genres']:
        print(name)

def artist_popularity(id):
    pop = sp.artist(id)
    print(pop['popularity'])

def artist_type(id):
    type = sp.artist(id)
    print(type['type'])


def show_album_tracks(id):
    album = sp.album_tracks(id)
    for track in album['items']:
        print("musicas: " + track['name'])

def info_album(id):
    album = sp.album(id)
    print(album)

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
            print("Album: " + name)
            unique.add(name)
            show_album_tracks(album['id'])


def search(q):
    lista = []
    results = sp.search(q, type='artist')
    results2 = results['artists']
    lista.extend(results2['items'])

    while results2['next']:
        results2 = sp.next(results2)
        aux = results2['artists']
        lista.extend(aux['items'])
        results2 = aux
    i = 0
    for artist in lista[:20]:
        i = i + 1
        print(i, artist['name'])
        print(artist['popularity'], "\n")

search("Eliana")

arquivo.close()
