# -*- coding: utf-8 -*-
"""
Created on 2017
@author: danier - gabri inspirated
"""
import route
#import random
from utils.utils import nodesFromJsonFile

# main program starts here
[terms, nodes] = nodesFromJsonFile()
print (terms)
print (nodes)
mRoute = route.Route("Test", nodes)
mRoute.printRouteNodes()
print ("test new route")
newRoute = startNewRandomRoute(nodes, 5)
newRoute.printRouteNodes()
# OO eh confuso
