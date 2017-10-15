# -*- coding: utf-8 -*-


class Node:

    def __init__(self, idx=0, label="",
                 neighbors=[], distance=[]):
        self.idx = idx
        self.label = label
        self.neighbors = {}
        size = len(distance)
        for i in range(size):
            self.neighbors.update({neighbors[i]: distance[i]})
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

    def getDistanceOfNode(self, aNode):
        if aNode.getLabel() in self.getNeighbors():
            dist = self.neighbors[aNode.getLabel()]
        elif aNode.getLabel() == self.getLabel():
            dist = 0
        else:
            dist = -1
        return dist

    # returns a clone of this node
    def cloneNode(self):
        mClone = Node()
        mClone.label = self.label
        mClone.idx = self.idx
        mClone.neighbors = self.neighbors
        mClone.mRoute = self.mRoute
        return mClone

    # mRoute setter and getter
    def setRoute(self, mRoute):
        self.mRoute = mRoute

    def getRoute(self):
        return self.mRoute
