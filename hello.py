# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""
import route
import node

from utils.utils import readNodesJsonFile, parseJsonString

# main program starts here
jsonString = readNodesJsonFile()
nodes = parseJsonString(jsonString)
print nodes
mRoute = route.Route("Test", nodes)
print mRoute
mRoute.addNode(node.Node())
