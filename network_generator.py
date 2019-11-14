import json
import spotipy
import networkx as nx
from spotipy.oauth2 import SpotifyClientCredentials

cid ="ec3e5e205b634356b5e4b82496b72dec"
secret = "c4decac528e349c9b17d5662065dcfb5"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

arquivo = json.loads(open("dados.json", "r").read())

G = nx.MultiGraph()

for cantor in arquivo:
    lista = []
    for item in cantor:
        aux = (cantor[item][1])
        aux = (aux["Alb"])
        for album in aux[1:]:
            #ja consigo imprimir o nome dos albuns
            track = (album["tracks"])
            track = track["items"]
            for item in track:
                artists = (item["artists"])
                for name in artists:
                    lista.append(name["name"])
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    lista2.sort()

print(arquivo[0])
#G.add_node()
