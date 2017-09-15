# -*- coding: utf-8 -*-

import node
import random


class Route:
    def __init__(self, label="", nodes=[]):
        self.label = label
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
            key = random.choice(self.nodes[-1].getNeighbors())
            self.addNode(self.getNodeByLabel(key))

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

    def printRouteNodes(self):
        for aNode in self.nodes:
            print aNode.getLabel()
