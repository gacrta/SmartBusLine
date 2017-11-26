# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""

import individuals
import operator, random, numpy, copy
import matplotlib.pyplot as plt
from route import RouteGenerator as rg

MUTATION_RATE = 0.01
AVERAGE_SPEED = 7.22  # m/s = 26 km/h / 3.6
TRANSFER_TIME = 10  # minutes


def printPopulationStatus(pop, iteration):
    print("Population Status for " + str(iteration) + " iteration:")
    for ind in pop:
        #print ("Individual " + ind.getLabel() + ": " + str(ind.evalFitness()))
        msg = "Individual %(indLabel)s: %(fitness).2f"%{"indLabel":ind.getLabel(),"fitness":ind.fitness}
        print (msg)

def populationSort(pop):
        return sorted(pop, key=operator.attrgetter("fitness"), reverse=True)

def populationSelect(pop, tamPop):

    popOver = sortedPop[ : int( tamPop/2 ) ] # takes highest half population...
    bestInd = popOver.pop(0)
    popOver = random.sample( popOver, int( 0.9*( tamPop/2 ) - 1 ) ) #... and pick 0.9 of them
    popUnder = sortedPop[ int( tamPop/2 ) : ] # takes lowest half population...
    popUnder = random.sample( popUnder, int( 0.1*( tamPop/2 ) ) ) #... and pick 0.1 of them
    return [bestInd] + popOver + popUnder # making a new generation from a half of old pop

def getPopulationArray(population):
    dt = numpy.dtype([("label", numpy.str_, 20), ("fitness", numpy.float64, 1)])
    #popArray = numpy.array(dtype=dt)
    tempList = []
    for ind in population:
        tempList.append((ind.label, ind.fitness))
        #popArray.put((ind.label, ind.fitness))
    popArray = numpy.array(tempList, dtype = dt)
    return popArray

def getPopulationMean(popArray):
    return popArray["fitness"].mean()

def getPopulationMax(popArray):
    return popArray["fitness"].max()

def getPopulationMin(popArray):
    return popArray["fitness"].min()

def getPopulationStd(popArray):
    return popArray["fitness"].std()

def evalPopulation(population, K1, xm, K2, K3, od_data,
                   transferTime, minimumPath, averageSpeed):
    for ind in population:
        ind.evalFitness3(K1, xm, K2, K3, od_data,
                         transferTime, minimumPath, averageSpeed)

def storePopulationData(dataStorage, population, iteration):

    popArray = getPopulationArray(population)

    popMean = getPopulationMean(popArray)
    popMax = getPopulationMax(popArray)
    popStd = getPopulationStd(popArray)

    dataStorage.append([iteration, popMax, popMean, popStd])

def plotPopulationEvolution(dataStorage):
    dataArray = numpy.array(dataStorage)
    iterations = dataArray[:, 0]
    popMax = dataArray[:, 1]
    popMean = dataArray[:, 2]
    popStd = dataArray[:, 3]
    plt.errorbar(iterations, popMean, yerr=popStd)
    plt.plot(iterations, popMax)
    plt.xlabel("Iterations")
    plt.ylabel("Fitness")
    plt.title("Best Individual evolution")
    plt.legend(["Max", "Mean"])
    plt.grid()
    plt.savefig("grafics.png")
    #plt.show()

tamPop = 80  # pode ser alterado direto aqui
populacao = []
ind = []  # individuo
routeArray = []

# sample OD matrix
# start, end, demand
od_data = [[0, 25, 200],
           [9, 18, 30],
           [0, 18, 50],
           [0, 19, 30],
           [0, 35, 45],
           [0, 36, 60]]

# constants of eval
K1 = 10.0
xm = 30.0
K2 = 10.0
K3 = 10.0
minimumPath = rg.getFloydMinimumTime(AVERAGE_SPEED)

# cria uma populacao
for i in range(tamPop):
    ind = individuals.Individuals(str(i))
    #ind.printIndividual()
    populacao.append(ind)

nextGeneration = copy.copy(populacao)
populationData = []

for i in range(25):

    if (i % 2 == 0):
        storePopulationData(populationData, nextGeneration, i)

    evalPopulation(nextGeneration, K1, xm, K2, K3, od_data,
                   TRANSFER_TIME, minimumPath, AVERAGE_SPEED)

    #printPopulationStatus(nextGeneration, i)
    sortedPop = populationSort(nextGeneration)
    #printPopulationStatus(sortedPop, i)

    # selects parental generation
    newGeneration = populationSelect(sortedPop, tamPop)
    #printPopulationStatus(newGeneration, i)

    # completing nextGeneration by reproduction and mutation (inside reproduction)
    nextGeneration = individuals.Individuals.reproduction2(newGeneration)

    popmut = random.sample(nextGeneration, int(len(nextGeneration)*MUTATION_RATE))
    for ind in popmut:
        indmut = individuals.Individuals.mutation(ind)
        nextGeneration.remove(ind)
        nextGeneration.append(indmut)

    #printPopulationStatus(nextGeneration, i)

#printPopulationStatus(populacao, 20)
#printPopulationStatus(nextGeneration, 20)
plotPopulationEvolution(populationData)

print("Done")


"""
# minimum gtfs files to create a shapefile in gis (like tutorial below)
# (http://www.stevencanplan.com/2016/02/converting-a-transit-agencys-gtfs-to-shapefile-and-geojson-with-qgis/)

# https://glenbambrick.com/2016/01/09/csv-to-shapefile-with-pyshp/

import shapefile, csv
def getWKT_PRJ (epsg_code):
 import urllib
 wkt = urllib.urlopen("http://spatialreference.org/ref/epsg/{0}/prettywkt/".format(epsg_code))
 remove_spaces = wkt.read().replace(" ","")
 output = remove_spaces.replace("\n", "")
 return output

def printShapefile(generation):
#TODO
usp_shp = shapefile.Writer()

"""
