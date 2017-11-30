# -*- coding: utf-8 -*-

class Node:

    def __init__(self, idx=0, label="",
                 neighbors=[], distance=[],
                 latlong=[], neighbors_latlong=[]):
        self.idx = idx
        self.label = label
        self.neighbors = {}
        self.neighbors_latlong = {}
        size = len(distance)
        for i in range(size):
            self.neighbors.update({neighbors[i]: distance[i]})
            self.neighbors_latlong.update({neighbors[i]: neighbors_latlong[i]})
        self.latlong = latlong
        self.mRoute = None

    def __str__(self):
        return "Node " + self.label

    def __repr__(self):
        return "<Node " + str(self.idx) + " label: " + self.label + ">"

    def getIdx(self):
        return self.idx

    def getLabel(self):
        return self.label

    def getNeighbors(self):
        return list(self.neighbors.keys())

    def getLatLong(self):
        return self.latlong

    def getDistanceOfNode(self, aNode):
        if aNode.getIdx() in self.getNeighbors():
            dist = self.neighbors[aNode.getIdx()]
        else:
            dist = 0 # if aNode == self OR aNode not a neighbor
        return dist
    
    def getNeighborsLatLong(self, aNode):
        if aNode.getIdx() in self.getNeighbors():
            neighborsList = self.neighbors_latlong[aNode.getIdx()]
        else:
            neighborsList = []
        return neighborsList

    # returns a clone of this node
    def cloneNode(self):
        mClone = Node()
        mClone.label = self.label
        mClone.idx = self.idx
        mClone.neighbors = self.neighbors
        mClone.latlong = self.latlong
        mClone.mRoute = self.mRoute
        mClone.neighbors_latlong = self.neighbors_latlong
        return mClone

    # mRoute setter and getter
    def setRoute(self, mRoute):
        self.mRoute = mRoute

    def getRoute(self):
        return self.mRoute


class NodeList:
    """ Static Class for methods that works on node lists """

    # returns a list of strings of nodes of nodeList
    @staticmethod
    def getNodesLabelList(nodeList):
        nodeLabelList = []
        for aNode in nodeList:
            if aNode.getLabel() not in nodeList:
                nodeLabelList.append(aNode.getLabel())
        return nodeLabelList

    # returns a lisf of strings of unique nodes of passed lists
    @staticmethod
    def getUniqueNodesFromLists(*lists):
        uniqueNodes = None
        if lists is not None:
            lists = lists[0]
            uniqueNodes = []
            for aList in lists:
                if len(uniqueNodes) == 0:
                    uniqueNodes = NodeList.getNodesLabelList(aList)
                else:
                    for aNode in aList:
                        aNodeLabel = aNode.getLabel()
                        if not (aNodeLabel in uniqueNodes):
                            uniqueNodes.append(aNodeLabel)
        return uniqueNodes