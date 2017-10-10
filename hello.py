# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""
import route
import random


def startNewRandomRoute(nodesList, numberOfNodes):
    newRoute = route.Route("Random Route")
    newRoute.addNode(random.choice(nodesList))
    for i in range(numberOfNodes-1):
        addRandomNeighborNode(newRoute, nodesList)
    return newRoute


def addRandomNeighborNode(aRoute, nodeList):
    neighborList = aRoute.getValidNeighbors()
    if len(neighborList) != 0:
        # picks a random neighbor label from last node
        key = random.choice(neighborList)
        # gets the node from nodeList
        node = getNodeByLabel(nodeList, key)
        if node is not None:
            if aRoute.getNodeByLabel(key) is None:
                aRoute.addNode(node)
                print ("Node " + key + " added to route " + aRoute.label)
                return key
            else:
                print ("Node " + key + " already present " + "at route " + aRoute.label)
        else:
            print ("Node " + key + " not found.")


def startRandomRouteFromTerminal(nodesList, terminalsList, routeLabel=""):
    newRoute = route.Route(routeLabel)
    # Inits route with random terminal
    newRoute.addNode(random.choice(terminalsList))
    addRandomNeighborNode(newRoute, nodesList)
    while 1:
        if not addRandomNeighborNode(newRoute, nodesList):
            if addRandomNeighborNode(newRoute, terminalsList):
                return newRoute
            else:
                # TODO
                print ("[startRandomRouteFromTerminal]: node duplicated")
                return


def getNodeByLabel(nodesList, nodeLabel):
    for aNode in nodesList:
        if nodeLabel == aNode.getLabel():
            return aNode
    print ("getNodeByLabel: Node " + nodeLabel + " not found.")

# main program starts here
nodes = route.Route.Nodes
print (nodes)
terminals = route.Route.Terminals
print (terminals)
print ("start route array")
routeArray = []
for i in range(10):
    routeArray.append(startRandomRouteFromTerminal(nodes, terminals, str(i)))
    routeArray[-1].printRouteNodes()
