# -*- coding: utf-8 -*-

import json
import node
import csv
import logging

LOGGING_TAG = "SmartBusLine"
LOGGING_FORMAT = '[%(asctime)-15s] %(name)s:%(levelname)s: %(message)s'
LOGGING_FILE_NAME = "all_events.log"


# method that inits logger machine
# based on: https://docs.python.org/2/howto/logging-cookbook.html
def initLogger():
    logger = logging.getLogger(LOGGING_TAG)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(LOGGING_FILE_NAME, mode='w')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(LOGGING_FORMAT)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)


# method that get a module log for application's classes
def getLogger(mClassName):
    return logging.getLogger(LOGGING_TAG+"."+mClassName)


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
