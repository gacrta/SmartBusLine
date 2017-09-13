# -*- coding: utf-8 -*-


class Node:

    def __init__(self, idx=0, label="",
                 neighbors=None, distance=None):
        self.idx = idx
        self.label = label
        self.neighbors = neighbors
        self.distance = distance

    def __str__(self):
        return "Node " + self.label

    def __repr__(self):
        return "<Node " + self.idx + " label: " + self.label + ">"
