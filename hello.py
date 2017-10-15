# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""

import individuals
import operator

def printPopulationStatus(pop, iteration):
    print("Population Status for " + str(iteration) + " iteration:")
    for ind in pop:
        print ("Individual " + ind.getLabel() + ": " + str(ind.evalFitness()))

def populationSort(pop):
        return sorted(pop, key=operator.attrgetter("fitness"), reverse=True)

tamPop = 10 # pode ser alterado direto aqui
populacao = []
ind = [] #individuo
routeArray = []

for i in range(tamPop):
    ind = individuals.Individuals(str(i))
    ind.printIndividual()
    populacao.append(ind)

printPopulationStatus(populacao, 0)
sortedPop = populationSort(populacao)
printPopulationStatus(sortedPop, 0)

    #print ("Route " + routeArray[-1].getLabel() + " is VALID and was added.")
    #routeArray[-1].printRouteNodes()