# -*- coding: utf-8 -*-

import node
import utils.utils as utils


class Route:
    jsonString = utils.readNodesJsonFile()
    [Nodes, Terminals] = utils.parseJsonString(jsonString)
    del(jsonString)

    # static method that finds a node at data bank
    def findNodeByLabel(nodeLabel):
        allNodes = Route.Nodes + Route.Terminals # concatenates the 2 lists
        for aNode in allNodes:
            if aNode.getLabel() == nodeLabel:
                return aNode

    def __init__(self, label="", nodes=None, deniedNodes=None):
        self.label = label
        # array of route nodes
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
        # array of nodes that results on non terminal ending route 
        if deniedNodes is None:
            self.invalid = []
        else:
            self.invalid = deniedNodes
        # route length: used to rank routes
        self.length = self.evalRouteDistance()

    def __str__(self):
        return "Route object"

    def __repr__(self):
        return "<Route " + self.label + " >"

    # simply append a node to nodes list
    def addNode(self, newNode):
        if isinstance(newNode, node.Node):
            self.nodes.append(newNode)
        else:
            raise TypeError("The object " + str(type(newNode)) +
                            " is not of type " + str(type(node.Node())))

    # returns the route's last node
    def getLastNode(self):
        if len(self.nodes) != 0:
            return self.nodes[-1]

    # finds a node at this route's nodes list
    def getNodeByLabel(self, nodeLabel):
        for aNode in self.nodes:
            if nodeLabel == aNode.getLabel():
                return aNode

    # returns the lengh of nodes list
    def getNumberOfNodes(self):
        return len(self.nodes)
    
    def getLabel(self):
        return self.label

    def evalRouteDistance(self):
        cDistance = 0
        if len(self.nodes) != 0:
            lastNode = self.nodes[0]
            for aNode in self.nodes[1:]:
                cDistance += aNode.getDistanceOfNode(lastNode)
        return cDistance

    # remove the last node and returns it
    def removeLastNode(self):
        if len(self.nodes) != 0:
            return self.nodes.pop()

    # adds a node to invalid list
    def denyInvalidNode(self, invalidNode):
        self.invalid.append(invalidNode)

    # removes and invalidates last node
    def denyLastNode(self):
        invalidNode = self.removeLastNode()
        invalidNodeLabel = invalidNode.getLabel()
        self.denyInvalidNode(invalidNodeLabel)
        print ("Node " + invalidNode.getLabel() + " in invalid for route " + self.getLabel())

    # returns true if route is terminal ended
    def isTerminalEnded(self):
        lastNode = self.getLastNode()
        if lastNode in Route.Terminals:
            return True
        return False

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
            # denys existing inner nodes and invalid ones, but adds a terminal neighbor
            if (((neighborNode is None) or (neighborNode in Route.Terminals)) and (neighbor not in self.invalid)):
                validNodes.append(neighbor)
        return validNodes
