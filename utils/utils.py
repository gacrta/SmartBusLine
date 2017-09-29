# -*- coding: utf-8 -*-

import json
import node

def nodesFromJsonFile():
    
    terms = [] # array of objs Nodes containing terminals nodes
    nodes = [] # array of objs Nodes containing simple nodes
    
    fileName = "data/nodes.json"
    with open(fileName, "r") as f:
        jsonString = f.read()
    
    jsonStruct = json.loads(jsonString)
    for field in jsonStruct['network']['terminals']:
        terms.append(node.Node(field['id'], field['label'],
                           field['neighbors'], field['distance']))
    for jsonNode in jsonStruct['network']['nodes']:
        nodes.append(node.Node(jsonNode['id'], jsonNode['label'],
                           jsonNode['neighbors'], jsonNode['distance']))
    return [terms, nodes]

"""
def readNodesJsonFile():
    # read data/nodes.json file from this project
    fileName = "data/nodes.json"
    with open(fileName, "r") as f:
        jsonString = f.read()
        return jsonString

def parseJsonString(jsonString):
    nodes = []
    jsonStruct = json.loads(jsonString)
    for jsonNode in jsonStruct['network']['nodes']:
        nodes.append(node.Node(jsonNode['id'], jsonNode['label'],
                               jsonNode['neighbors'], jsonNode['distance']))
    return nodes
"""

"""
def dijkstraUSP(nodes, ):
    # a ideia eh se caso precise, ja esta na mao uma
    # versao do dijkstra adaptado para nosso problema de rotas
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm
    
    # possiveis implementacoes
    # https://gist.github.com/econchick/4666413 - olhando por cima, achei a mais facil de adaptar
    # http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
    # https://www.ics.uci.edu/~eppstein/161/python/dijkstra.py

def yenUSP():
    # a ideia eh se caso precise, ja esta na mao uma
    # versao do 'Yen's k shortest path' adaptado para nosso problema de rotas
    # https://en.wikipedia.org/wiki/Yen%27s_algorithm
    
    # ainda tem uma versao que permite as k menores rotas com repeticoes nos nós (Yen nao permite)
    # https://stackoverflow.com/questions/12870122/eppsteins-algorithm-and-yens-algorithm-for-k-shortest-paths
    # o link acima tem links para os trabalhos do Yen e do Eppstein
    
    # possiveis implementacoes
    # https://stackoverflow.com/questions/15878204/k-shortest-paths-implementation-in-igraph-networkx-yens-algorithm
    # https://github.com/Pent00/YenKSP - link acima direciona pra esse/esse tb eh um dos 1os retornos do google
    # https://stackoverflow.com/questions/26054468/yens-k-shortest-algorithm-python-implementation-for-a-10-node-all-connected-g
    # https://gist.github.com/ALenfant/5491853
"""