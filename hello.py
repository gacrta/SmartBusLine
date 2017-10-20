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
        #print ("Individual " + ind.getLabel() + ": " + str(ind.evalFitness()))
        msg = "Individual %(indLabel)s: %(fitness).2f"%{"indLabel":ind.getLabel(),"fitness":ind.evalFitness()}
        print (msg)

def populationSort(pop):
        return sorted(pop, key=operator.attrgetter("fitness"), reverse=True)

def populationSelect(pop, tamPop):

    popOver = sortedPop[ : int( tamPop/2 ) ] # takes highest half population...
    bestInd = popOver.pop(0)
    popOver = random.sample( popOver, int( 0.9*( tamPop/2 ) - 1 ) ) #... and pick 0.9 of them
    popUnder = sortedPop[ int( tamPop/2 ) : ] # takes lowest half population...
    popUnder = random.sample( popUnder, int( 0.1*( tamPop ) ) ) #... and pick 0.1 of them
    return [bestInd] + popOver + popUnder # making a new generation from a half of old pop

tamPop = 10 # pode ser alterado direto aqui
populacao = []
ind = [] #individuo
routeArray = []

# cria uma populacao
for i in range(tamPop):
    ind = individuals.Individuals(str(i))
    ind.printIndividual()
    populacao.append(ind)

    nextGeneration = populacao.copy()
for i in range(10):
    printPopulationStatus(nextGeneration, i)
    sortedPop = populationSort(nextGeneration)
    printPopulationStatus(sortedPop, i)
    
    # selects parental generation
    newGeneration = populationSelect(sortedPop, tamPop)
    printPopulationStatus(newGeneration, i)
    
    # completing nextGeneration by reproduction and mutation (inside reproduction)
    nextGeneration = individuals.Individuals.reproduction2(newGeneration)
    printPopulationStatus(nextGeneration, i)
printPopulationStatus(populacao, 10)