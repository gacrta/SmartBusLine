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
