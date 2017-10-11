# -*- coding: utf-8 -*-
"""
Created on 2017
@author: danier - gabri inspirated
"""
#import route
#import random
from utils.utils import nodesFromJsonFile
import individuals

# main program starts here
[terms, nodes] = nodesFromJsonFile()
"""
# teste para as primeiras funcoes
# p ver se objetos nos e rotas estao
# sendo criados certos
print (terms)
print (nodes)
mRoute = route.Route("Test", nodes)
mRoute.printRouteNodes()
print ("test new route")
newRoute = route.Route.startNewRandomRoute(nodes, 5)
newRoute.printRouteNodes()
# OO eh confuso
"""
numDeRotas = 3 # pode ser alterado direto aqui
tamDaPop = 100 # pode ser alterado direto aqui
populacao = []
ind = [] #individuo
# num de iteracoes definira a pop inicial
# e as populacoes seguintes
for index in range (tamDaPop):
    # https://stackoverflow.com/questions/3289601/null-object-in-python
    ind = individuals.Individuals(index, None) # para passar um NULL em Python, usa-se None
