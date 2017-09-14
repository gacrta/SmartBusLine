# -*- coding: utf-8 -*-

import node


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
        if (type(newNode) is node.Node):
            self.nodes.append(newNode)
        else:
            raise TypeError("The object " + str(type(newNode)) +
                            " is not of type " + str(type(node.Node)))

    def getNumberOfNodes(self):
        return len(self.nodes)

    def evalRouteDistance(self):
        cDistance = 0
        lastNode = self.nodes[0]
        for aNode in self.nodes[1:]:
            cDistance += aNode.getDistanceOfNode(lastNode)
        return cDistance
