# -*- coding: utf-8 -*-

import node


class Route:
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

    def printRouteNodes(self):
        print "Print route  " + self.label
        for aNode in self.nodes:
            print aNode.getLabel(),
        print ""
