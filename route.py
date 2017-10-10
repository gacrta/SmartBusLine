# -*- coding: utf-8 -*-

import node
import utils.utils as utils


class Route:
    jsonString = utils.readNodesJsonFile()
    [Nodes, Terminals] = utils.parseJsonString(jsonString)
    del(jsonString)

    def __init__(self, label="", nodes=None):
        self.label = label
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
        self.length = self.evalRouteDistance()

    def __str__(self):
        return "Route object"

    def __repr__(self):
        return "<Route " + self.label + " >"

    def addNode(self, newNode):
        if isinstance(newNode, node.Node):
            self.nodes.append(newNode)
        else:
            raise TypeError("The object " + str(type(newNode)) +
                            " is not of type " + str(type(node.Node())))

    def getLastNode(self):
        if len(self.nodes) != 0:
            return self.nodes[-1]

    def getNodeByLabel(self, nodeLabel):
        for aNode in self.nodes:
            if nodeLabel == aNode.getLabel():
                return aNode

    def getNumberOfNodes(self):
        return len(self.nodes)

    def evalRouteDistance(self):
        cDistance = 0
        if len(self.nodes) != 0:
            lastNode = self.nodes[0]
            for aNode in self.nodes[1:]:
                cDistance += aNode.getDistanceOfNode(lastNode)
        return cDistance

    def removeLastNode(self):
        if len(self.nodes) != 0:
            return self.nodes.pop()

    def printRouteNodes(self):
        print ("Print route  " + self.label)
        for aNode in self.nodes:
            print (aNode.getLabel()),
        print ("")

    # returns a list of available nodes of last neighbor
    def getValidNeighbors(self):
        validNodes = [];
        lastNode = self.getLastNode()
        neighborhood = lastNode.getNeighbors()
        for neighbor in neighborhood:
            neighborNode = self.getNodeByLabel(neighbor)
            # denys existing inner nodes, but adds a terminal neighbor
            if ((neighborNode is None) or (neighborNode in Route.Terminals)):
                validNodes.append(neighbor)
        return validNodes
