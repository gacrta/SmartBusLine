# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""
from route import Route
import random


MAX_NUMBER_OF_NODES = 10
ONLY_TERMINAL_ENDING = True

def startNewRandomRoute(nodesList, numberOfNodes):
    newRoute = Route("Random Route")
    newRoute.addNode(random.choice(nodesList))
    for i in range(numberOfNodes-1):
        addRandomNeighborNode(newRoute, nodesList)
    return newRoute

# adds a random neighbor to a given route. returns true if
# succeeds and false otherwise
def addRandomNeighborNode(aRoute):
    neighborList = aRoute.getValidNeighbors()
    if len(neighborList) != 0:
        # picks a random neighbor label from last node
        key = random.choice(neighborList)
        # finds node from database
        node = Route.findNodeByLabel(key)
        aRoute.addNode(node)
        print ("Node " + node.getLabel() + " added to route " + aRoute.getLabel())
        return True
    else:
        # len(neighborList) == 0, no more valid neighbors
        print ("No valid neighbors.")
        return False

def startRandomRouteFromTerminal(newRoute):
    numberOfNodes = newRoute.getNumberOfNodes()
    if (numberOfNodes == 0):
        # Inits route with random terminal
        randomTerminal = random.choice(Route.Terminals)
        newRoute.addNode(randomTerminal)
        print ("Terminal " + randomTerminal.getLabel() + " added to route " + newRoute.getLabel())
    elif (numberOfNodes == MAX_NUMBER_OF_NODES):
        print ("Route " + newRoute.getLabel() + " ended max nodes")
        return False
    wasNodeAdded = addRandomNeighborNode(newRoute)
    if wasNodeAdded:
        if newRoute.isTerminalEnded():
            print ("Route " + newRoute.getLabel() + " ended with terminal " + newRoute.getLastNode().getLabel())
            return True
    else:
        if not ONLY_TERMINAL_ENDING:
            # allows inner node ending
            return True
        else:
            print ("Route " + newRoute.getLabel() + " has no valid end. Deleting " + newRoute.getLastNode().getLabel())
            newRoute.denyLastNode()
    return startRandomRouteFromTerminal(newRoute)

def getNodeByLabel(nodesList, nodeLabel):
    for aNode in nodesList:
        if nodeLabel == aNode.getLabel():
            return aNode
    print ("getNodeByLabel: Node " + nodeLabel + " not found.")

# main program starts here
nodes = Route.Nodes
print (nodes)
terminals = Route.Terminals
print (terminals)
print ("start route array")
routeArray = []
for i in range(10):
    newRoute = Route(str(i+1))
    if startRandomRouteFromTerminal(newRoute):
        routeArray.append(newRoute)
        print ("Route " + routeArray[-1].getLabel() + " is VALID and was added.")
        routeArray[-1].printRouteNodes()
        del(newRoute)
