# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""
import route

routeArray = []
for i in range(10):
    newRoute = route.RouteGenerator.getNewRoute()
    routeArray.append(newRoute)
    print ("Route " + routeArray[-1].getLabel() + " is VALID and was added.")
    routeArray[-1].printRouteNodes()