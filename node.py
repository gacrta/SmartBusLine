# -*- coding: utf-8 -*-

# https://www.tutorialspoint.com/python/python_classes_objects.htm
class Node:

  def __init__(self, idx=0, label="", neighbors=[], distance=[]):
    # https://www.tutorialspoint.com/python/python_lists.htm
    self.idx = idx
    self.label = label
    self.neighbors = {}
    # https://stackoverflow.com/questions/19184335/is-there-a-need-for-rangelena
    size = len(distance)
    for i in range(size):
      self.neighbors.update( { neighbors[i]: distance[i] } )
    # http://www.bogotobogo.com/python/python_hash_tables_hashing_dictionary_associated_arrays.php
                
  # https://stackoverflow.com/questions/3691101/what-is-the-purpose-of-str-and-repr-in-python
  def __str__(self):
    return "Node " + self.label

  def __repr__(self):
    return "<Node " + str(self.idx) + " label: " + self.label + ">"

  def getIdx(self):
    return self.idx

  def getLabel(self):
    return self.label
    
    # https://docs.python.org/2/tutorial/datastructures.html#dictionaries
  def getNeighbors(self):
    return self.neighbors.keys()

  def getDistanceOfNode(self, aNode):
    dist = 0
    if aNode.getLabel() in self.getNeighbors():
      dist = self.neighbors[aNode.getLabel()]
    # caso em que o nó passado nao é vizinho e nem ele mesmo, tem q ser erro
    # ou fazer alguma maneira de achar algum caminho entre eles (dijkstra?)
    """
    elif aNode.getLabel() == self.getLabel():
      dist = 0
    else:
      #dist = -1
      return "nao eh vizinho"
    """
    return dist
