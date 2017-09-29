# -*- coding: utf-8 -*-

import node
import random

class Route:
  def __init__(self, label="", nodes=[]):
    self.label = label
    self.nodes = nodes
    self.length = self.evalRouteDistance()

  def __str__(self):
    return "Route object"

  def __repr__(self):
    return "<Route " + self.label + " >"

  def printRouteNodes(self):
    for aNode in self.nodes:
        print ( aNode.getLabel() )

  def addNode(self, newNode):
    if isinstance(newNode, node.Node):
      self.nodes.append(newNode)
    else:
      raise TypeError("The object " + str(type(newNode)) +
                      " is not of type " + str(type(node.Node())))
      # https://stackoverflow.com/questions/13957829/how-to-use-raise-keyword-in-python
      # https://docs.python.org/3.3/tutorial/errors.html

  def getLastNode(self):
    if len(self.nodes) != 0:
      return self.nodes[-1]
    key = random.choice(self.nodes[-1].getNeighbors())
    self.addNode(self.getNodeByLabel(key))

  def getNodeByLabel(self, nodeLabel):
    
    for aNode in self.nodes:
      if nodeLabel == aNode.getLabel():
        return aNode
            
  def getNumberOfNodes(self):
    return len(self.nodes)

  def evalRouteDistance(self):
    cDistance = 0
    # nodes tem q ter pelo menos dois nos para ter alguma dist
    # se len() == 1, só tem 1 nó (n tem dist), e se len() == 0 n tem o q calc
    if len(self.nodes) > 1:
        for i in range( 1, len(self.nodes) ):
            cDistance += self.nodes[i].getDistanceOfNode(self.nodes[i-1])
    return cDistance

  def genRoute(source, sink, nodesList):
    newRoute = Route("Random Route")
		newRoute.addNode(source)
		newRoute.addNode(random.choice(source.getNeighbors())) # garantindo que entre no loop
    while ( newRoute.getLastNode() != sink ):
			key = random.choice(newRoute.getLastNode().getNeighbors())
      newRoute.addNode( nodesList.getNodeByLabel( key ) )
    return newRoute
