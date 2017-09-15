# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""
import route
import random

from utils.utils import readNodesJsonFile, parseJsonString


def startNewRandomRoute(nodesList, numberOfNodes):
    newRoute = route.Route("Random Route")
    newRoute.addNode(random.choice(nodesList))
    for i in range(numberOfNodes-1):
        key = random.choice(newRoute.getLastNode().getNeighbors())
        newRoute.addNode(getNodeByLabel(nodesList, key))
    return newRoute


def getNodeByLabel(nodesList, nodeLabel):
    for aNode in nodesList:
        if nodeLabel == aNode.getLabel():
            return aNode

# main program starts here
jsonString = readNodesJsonFile()
nodes = parseJsonString(jsonString)
print nodes
mRoute = route.Route("Test", nodes)
mRoute.printRouteNodes()
print "test new route"
newRoute = startNewRandomRoute(nodes, 5)
newRoute.printRouteNodes()
