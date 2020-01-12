import json
import networkx as nx
import matplotlib.pyplot as plt
from random import random

arquivo = open("Hdata.json", "r")
arquivo = (json.load(arquivo))

G = nx.MultiGraph()
#Extrair nome dos cantores secundarios
for cantor in arquivo:
    lista = []
    for item in cantor:
        aux = (cantor[item][1])
        aux = (aux["Alb"])
        for album in aux:
            #ja consigo imprimir o nome dos albuns
            track = (album["tracks"])
            track = track["items"]
            for tag in track:
                artists = (tag["artists"])
                for name in artists:
                    lista.append(name["name"])
#armazenar os cantores secundarios em uma lista sem repetição
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    lista2.sort()
#extrair o nome do cantor principal
    pivo = item
#Construcao do grafo
    G.add_node(pivo)
    for item in lista2:
        # if verificacao para nao por 2 nós repitidos
        G.add_node(item)
        G.add_edge(item, pivo)

nx.write_gexf(G, "G.gexf")
