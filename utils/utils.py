# -*- coding: utf-8 -*-

import json
import node
import csv


def readNodesJsonFile():
    """ read data/nodes.json file from this project """
    fileName = "data/nodes.json"
    with open(fileName, "r") as f:
        jsonString = f.read()
        return jsonString


def parseJsonString(jsonString):
    """ creates nodes list from jsonString """
    nodes = []
    terminals = []
    jsonStruct = json.loads(jsonString)
    for jsonNode in jsonStruct['network']['nodes']:
        nodes.append(node.Node(jsonNode['id'],
                               jsonNode['label'],
                               jsonNode['neighbors'],
                               jsonNode['distance'],
                               jsonNode['latlong']))

    for jsonNode in jsonStruct['network']['terminals']:
        terminals.append(node.Node(jsonNode['id'],
                                   jsonNode['label'],
                                   jsonNode['neighbors'],
                                   jsonNode['distance'],
                                   jsonNode['latlong']))
    return [nodes, terminals]


""" TODO - deixar apto p ler um csv de uma API, p. ex. """

# (Python2) https://docs.python.org/2/library/csv.html
# (Python3) https://docs.python.org/3/library/csv.html
# http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
# https://pymotw.com/2/csv/

# method that reads OD info from .csv file
def parseCsvODFile():
    od_matrix = "data/matriz_od_fake.csv"
    with open(od_matrix, 'rb') as csvfile:
        filereader = csv.reader(csvfile)
        destinations = filereader.next()
        demandMatrix = []
        for row in filereader:
            origin = row[0]
            tam = len(row)
            for i in range(1, tam):
                dest = row[i]
                if dest != "" and dest != "EOT" and dest != "0":
                    demandMatrix.append([int(origin), int(destinations[i]),
                                         int(dest)])
        return demandMatrix
