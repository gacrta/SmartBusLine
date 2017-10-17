# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""

import individuals
import operator
import random

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

# cria uma populacao
for i in range(tamPop):
    ind = individuals.Individuals(str(i))
    ind.printIndividual()
    populacao.append(ind)

printPopulationStatus(populacao, 0)
sortedPop = populationSort(populacao)
printPopulationStatus(sortedPop, 0)

    #print ("Route " + routeArray[-1].getLabel() + " is VALID and was added.")
    #routeArray[-1].printRouteNodes()

# selects parental generation
popOver = sortedPop[ : int( tamPop/2 ) ] # takes highest half population...
popOver = random.sample( popOver, int( 0.9*( tamPop/2 ) ) ) #... and pick 0.9 of them
popUnder = sortedPop[ int( tamPop/2 ) : ] # takes lowest half population...
popUnder = random.sample( popUnder, int( 0.1*( tamPop ) ) ) #... and pick 0.1 of them
newGeneration = popOver + popUnder # making a new generation from a half of old pop
printPopulationStatus(newGeneration, 0)

# completing nextGeneration by reproduction and mutation


