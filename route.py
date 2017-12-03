# -*- coding: utf-8 -*-

import node
import random
import utils.utils as utils


class Route:
    """ Class that represents the route data and its methods """

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
        self.length = None
        self.string = None
        self.mLogger = utils.getLogger(self.__class__.__name__)

    def __str__(self):
        return "Route object"

    def __repr__(self):
        return "<Route " + self.label + " >"

    # simply append a node to nodes list
    def addNode(self, newNode):
        if isinstance(newNode, node.Node):
            mNode = newNode.cloneNode()
            mNode.setRoute(self)
            self.nodes.append(mNode)
            # self.nodes.append(newNode)
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

    # finds a node at this route's nodes list by idx
    def getNodeById(self, nodeId):
        for aNode in self.nodes:
            if nodeId == aNode.getIdx():
                return aNode

    # returns the lengh of nodes list
    def getNumberOfNodes(self):
        return len(self.nodes)

    def getLabel(self):
        return self.label

    def getLenght(self):
        return self.length

    def setLenght(self, length):
        self.length = length

    def evalRouteDistance(self, startNodeIdx=None, endNodeIdx=None):
        if len(self.nodes) == 0:
            self.mLogger.debug("Route is empty.")
            return 0
        elif startNodeIdx is None:
            # self.mLogger.debug("Evaluating from first node to last node.")
            remainingNodes = self.nodes
        elif endNodeIdx is None:
            # self.mLogger.debug("Evaluating from middle node to last node.")
            startNode = self.getNodeById(startNodeIdx)
            startNodeInnerId = self.nodes.index(startNode)
            remainingNodes = self.nodes[startNodeInnerId:]
        else:
            # self.mLogger.debug("Evaluating from middle node to middle node.")
            startNode = self.getNodeById(startNodeIdx)
            startNodeInnerId = self.nodes.index(startNode)
            endNode = self.getNodeById(endNodeIdx)
            endNodeInnerId = self.nodes.index(endNode)
            remainingNodes = self.nodes[startNodeInnerId:endNodeInnerId+1]
        cDistance = 0
        if len(remainingNodes) > 0:
            cNode = remainingNodes[0]
            for nextNode in remainingNodes[1:]:
                cDistance += cNode.getDistanceOfNode(nextNode)
                cNode = nextNode
        return cDistance

    # evaluates route time from startNode to endNode
    def evalRouteTime(self, startNode, endNode, averageSpeed):
        distance = self.evalRouteDistance(startNode, endNode)

        if distance is not 0:
            # returns time in minutes
            return distance/(60*averageSpeed)
        return 0

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
        invalidNodeIdx = invalidNode.getIdx()
        self.denyInvalidNode(invalidNodeIdx)
        self.mLogger.debug("Node " + invalidNode.getLabel() +
                           " in invalid for route " + self.getLabel())

    def printRouteNodes(self):
        print("Print route  " + self.label)
        for aNode in self.nodes:
            print(aNode.getLabel())

    # returns a string of route nodes
    def getString(self):
        if self.string is None:
            routeString = ""
            for aNode in self.nodes:
                routeString += (str(aNode.getIdx()) + "_")
            self.string = routeString[:len(routeString)-1]
        return self.string

    # returns a list of nodes that this has with otherRoute
    def getCommonNodes(self, otherRoute):
        commonNodes = []
        for mNode in self.nodes:
            mNodeIdx = mNode.getIdx()
            if otherRoute.getNodeById(mNodeIdx) is not None:
                commonNodes.append(mNodeIdx)
        return commonNodes

    # returns true if this route is equal to otherRoute
    def isEqualToRoute(self, otherRoute):
        # TODO
        return False

    def getNodes(self):
        return self.nodes

    def cloneRoute(self):
        rClone = Route()
        rClone.label = self.label
        rClone.nodes = self.nodes
        rClone.invalid = self.invalid
        rClone.length = self.length
        rClone.string = self.string
        return rClone


class RouteGenerator:
    """ Class used to create Route objects """

    def __init__(self, maxNumberOfNodes, isOnlyTerminalEnd=True):
        self.maxNumberOfNodes = maxNumberOfNodes
        self.isOnlyTerminalEnd = isOnlyTerminalEnd
        jsonString = utils.readNodesJsonFile()
        [self.nodes, self.terminals] = utils.parseJsonString(jsonString)
        self.allNodes = self.terminals + self.nodes
        del(jsonString)
        self.mLogger = utils.getLogger(self.__class__.__name__)

    # method that finds a node at data bank
    def findNodeByLabel(self, nodeLabel):
        for aNode in self.allNodes:
            if aNode.getLabel() == nodeLabel:
                return aNode

    # method that finds a node at data bank by idx
    def findNodeById(self, nodeId):
        for aNode in self.allNodes:
            if aNode.getIdx() == nodeId:
                return aNode

    # returns true if a interest node is in a interest list of nodes
    def isNodeOnList(self, interestNode, interestList):
        for aNode in interestList:
            if aNode.getIdx() == interestNode.getIdx():
                return True
        return False

    # returns true if route is terminal ended
    def isRouteTerminalEnded(self, aRoute):
        lastRouteNode = aRoute.getLastNode()
        if self.isNodeOnList(lastRouteNode, self.terminals):
            return True
        return False

    # returns a list of available nodes of route's last node
    def getRouteValidNeighbors(self, aRoute):
        validNodes = []
        lastNode = aRoute.getLastNode()
        neighborhood = lastNode.getNeighbors()
        for neighbor in neighborhood:
            neighborNode = aRoute.getNodeById(neighbor)
            # denys existing inner nodes and invalid ones, but adds a terminal neighbor
            if (((neighborNode is None) or
                 (self.isNodeOnList(neighborNode, self.terminals))) and
                 (neighbor not in aRoute.invalid)):
                validNodes.append(neighbor)
        return validNodes

    # returns all nodes list
    def getAllNodes(self):
        return self.allNodes

    # returns a route composed by a list of node ids
    def getRouteFromNodeList(self, routeLabel, nodeIdList):
        newRoute = Route(routeLabel)
        for aNodeId in nodeIdList:
            thisNode = self.findNodeById(aNodeId)
            if len(newRoute.nodes) == 0:
                if (thisNode in self.terminals):
                    newRoute.addNode(thisNode)
                else:
                    raise ValueError("The node " + thisNode.getLabel() +
                                     " is not a Terminal.")
            elif(aNodeId != nodeIdList[-1]):
                validNeighbors = self.getRouteValidNeighbors(newRoute)
                if (aNodeId in validNeighbors):
                    newRoute.addNode(thisNode)
                else:
                    raise ValueError("The node " + thisNode.getLabel() +
                                     " is not a valid neighbor of " +
                                     newRoute.getLastNode().getLabel())
            else:
                validNeighbors = self.getRouteValidNeighbors(newRoute)
                if ((aNodeId in validNeighbors) and (thisNode in self.terminals)):
                    newRoute.addNode(thisNode)
        return newRoute

    # adds a random neighbor to a given route. returns true if
    # succeeds and false otherwise
    def addRandomNeighborNode(self, aRoute):
        neighborList = self.getRouteValidNeighbors(aRoute)
        if len(neighborList) != 0:
            # picks a random neighbor label from last node
            key = random.choice(neighborList)
            # finds node from database
            aNode = self.findNodeById(key)
            aRoute.addNode(aNode)
            self.mLogger.debug("Node " + aNode.getLabel() + " added to route "
                               + aRoute.getLabel())
            return True
        else:
            # len(neighborList) == 0, no more valid neighbors
            self.mLogger.debug("No valid neighbors.")
            return False

    # receives a route and returns true if a valid route is created
    def startRandomRouteFromTerminal(self, newRoute):
        numberOfNodes = newRoute.getNumberOfNodes()
        if (numberOfNodes == 0):
            # Inits route with random terminal
            randomTerminal = random.choice(self.terminals)
            newRoute.addNode(randomTerminal)
            self.mLogger.debug("Terminal " + randomTerminal.getLabel() +
                               " added to route " + newRoute.getLabel())
        elif (numberOfNodes == self.maxNumberOfNodes):
            self.mLogger.debug("Route " + newRoute.getLabel() +
                               " ended max nodes")
            return False
        wasNodeAdded = self.addRandomNeighborNode(newRoute)
        if wasNodeAdded:
            if self.isRouteTerminalEnded(newRoute):
                self.mLogger.debug("Route " + newRoute.getLabel() +
                                   " ended with terminal " +
                                   newRoute.getLastNode().getLabel())
                return True
        else:
            if not self.isOnlyTerminalEnd:
                # allows inner node ending
                return True
            else:
                self.mLogger.debug("Route " + newRoute.getLabel() +
                                   " has no valid end. Deleting " +
                                   newRoute.getLastNode().getLabel())
                newRoute.denyLastNode()
        return self.startRandomRouteFromTerminal(newRoute)

    # method that returns a valid route
    def getNewRoute(self, label=""):
        if (label == ""):
            label = "sample route"
        routeDone = False
        newRoute = None
        while not routeDone:
            if newRoute is not None:
                self.mLogger.debug("An invalid route was created and abbandoned.")
                del(newRoute)
            newRoute = Route(label)
            routeDone = self.startRandomRouteFromTerminal(newRoute)
        self.mLogger.debug("Route " + label + " is VALID.")
        newRoute.setLenght(newRoute.evalRouteDistance())
        return newRoute

    # method that returns the minimum path matrix
    def getFloydMinimumTime(self, averageSpeed):
        inf = 100000  # value bigger than any distance

        # init matrix with all neighbors distance
        minDistMatrix = []
        for rowNode in self.allNodes:
            line = []
            for columnNode in self.allNodes:
                dist = rowNode.getDistanceOfNode(columnNode)
                # if dist = -1, the nodes are not neighbors
                if dist == -1:
                    dist = inf
                line.append(dist/(60*averageSpeed))
            minDistMatrix.append(line)

        # evaluate floyd minimum path
        N = len(self.allNodes)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    innerDist = minDistMatrix[i][k]+minDistMatrix[k][j]
                    if minDistMatrix[i][j] > innerDist:
                        minDistMatrix[i][j] = innerDist
        return minDistMatrix


class RouteList:
    """ Static class used handle lists of routes """
    # compare two route lists element wise by their string elements
    # returns common routes
    @staticmethod
    def getCommonListElements(listA, listB):
        commonRoutes = []
        for a in listA:
            for b in listB:
                stringA = a.getString()
                stringB = b.getString()
                if stringA == stringB:
                    commonRoutes.append(a)
        return commonRoutes