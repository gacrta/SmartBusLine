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
    nodes = []
    jsonStruct = json.loads(jsonString)
    for jsonNode in jsonStruct['network']['nodes']:
        nodes.append(node.Node(jsonNode['id'], jsonNode['label'],
                               jsonNode['neighbors'], jsonNode['distance']))
    return nodes
