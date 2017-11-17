# -*- coding: utf-8 -*-

import json
import node


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

import csv
def readCsvFiles():
    filename = "data/csvTest.csv"
    with open(filename, 'rb') as csvfile:
        filereader = csv.reader(csvfile)
        return filereader