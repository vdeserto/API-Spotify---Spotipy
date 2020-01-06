import os
import json
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid ="34acb700848b455ebc323e943883d059"
secret = "a77e0f95dce246d29405e12cf40a1c88"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

arquivo = open("Adata.json", "w")
arquivo2 = open('cantores.txt', 'r')
arquivo3 = open("Adata.json", "r")

#construir cabeçalho do JSON e gravar informacoes do artista
arquivo.writelines("[")
def info_artist(id):
    #pegar nome do artista
    r = sp.artist(id)
    #Constroi Dicionario do artista
    dic = {r["name"]:''}
    #Constroi Vetor obj do artista
    cab = []
    #Adc o obj info_arts
    cab.append(sp.artist(id))
    aux = show_artist_albums(id)
    #Adc o obj Alb (com todos albuns do artista)
    cab.append(aux)
    #Atribui o vetor de obj ao artist
    dic[r["name"]] = cab
    #Escreve o dic como json no arquivo
    json.dump(dic, arquivo)

def show_artist_albums(id):
    lista = []
    albums = sp.artist_albums(id, album_type='album')
    lista.extend(albums['items'])
    while albums['next']:
    	albums = sp.next(albums)
    	lista.extend(albums['items'])
    unique = set()  # skip duplicate albums
    dic2 = {'Alb':''}
    vet = []
    for album in lista:
        name = album['name'].lower()
        if not name in unique:
            vet.append(info_album(album['id']))
            unique.add(name)
    dic2['Alb'] = vet
    return dic2

def info_album(id):
    result_json2 = sp.album(id)
    return result_json2


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

#Main
inicio = time.time()

x = 0
for cantor in arquivo2:
    if (x != 0):
        arquivo.writelines (", ")
    search(cantor)
    x = x +1

arquivo.writelines("]")
arquivo.close()

fim = time.time()
tf = round(((fim - inicio)/60)/60, 2)
print(tf , "horas")

a = (json.load(arquivo3))
