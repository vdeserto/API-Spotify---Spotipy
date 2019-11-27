import os
import json
import time
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

cid ="34acb700848b455ebc323e943883d059"

secret = "a77e0f95dce246d29405e12cf40a1c88"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

arquivo = open("dados.json", "w")
arquivo2 = open('cantores.txt', 'r')

arquivo.writelines ("[")

#construir cabeçalho do JSON e gravar informacoes do artista
def info_artist(id):
    #pegar nome do artista
    r = sp.artist(id)
    result_json = sp.artist(id)
    #transforma o return em formato JSON
    result = json.dumps(result_json)
    arquivo.writelines ("{\""+r["name"]+"\": [")
    arquivo.writelines (result)
    arquivo.writelines (", ")
    show_artist_albums(id)


def show_artist_albums(id):
    lista = []
    albums = sp.artist_albums(id, album_type='album')
    lista.extend(albums['items'])
    while albums['next']:
    	albums = sp.next(albums)
    	lista.extend(albums['items'])
    unique = set()  # skip duplicate albums
    arquivo.writelines ("{\"Alb\": [")
    arquivo.writelines("{}")
    for album in lista:
        name = album['name'].lower()
        if not name in unique:
            info_album(album['id'])
            unique.add(name)

    arquivo.writelines ("]}]}")

def info_album(id):
    arquivo.writelines (", ")
    result_json2 = sp.album(id)
    result = json.dumps(result_json2)
    arquivo.writelines (result)


def search(q):
    lista = []
    results = sp.search(q, type='artist')
    results = results['artists']
    lista.extend(results['items'])

    while results['next']:
        results = sp.next(results)
        aux = results['artists']
        lista.extend(aux['items'])
        results = aux

    i = 0
    for artist in lista:
        if(i !=0):
            arquivo.writelines (", ")
        info_artist(artist['id'])
        i = i +1

#Inicio do codigo
#medição de tempo
inicio = time.time()

for cantor in arquivo2:
    search(cantor)


arquivo.writelines ("]")
arquivo.close()

fim = time.time()
tf = round(((fim - inicio)/60)/60, 2)
print(tf , "horas")

arquivo3 = json.loads(open("dados.json", "r").read())

#fim medicao de tempo
