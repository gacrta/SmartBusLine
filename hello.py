# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:24:38 2017

@author: gabri
"""

import individuals
import operator
import random
import numpy
import matplotlib.pyplot as plt
import copy

MUTATION_RATE = 0.05

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

def getPopulationStd(popArray):
    return popArray["fitness"].std()

def storePopulationData(dataStorage, population, iteration):
    
    popArray = getPopulationArray(population)
    
    popMean = getPopulationMean(popArray)
    popMax = getPopulationMax(popArray)
    popStd = getPopulationStd(popArray)
    
    dataStorage.append([iteration, popMax, popMean, popStd])

def plotPopulationEvolution(dataStorage):
    dataArray = numpy.array(dataStorage)
    iterations = dataArray[:,0]
    popMax = dataArray[:,1]
    popMean = dataArray[:,2]
    popStd = dataArray[:,3]
    plt.errorbar(iterations, popMean, yerr=popStd)
    plt.plot(iterations, popMax)
    plt.xlabel("Iterations")
    plt.ylabel("Distance (m)")
    plt.title("Best Individual evolution")
    plt.legend(["Mean", "Max"])
    plt.grid()
    plt.savefig("grafics.png")
    #plt.show()

tamPop = 200 # pode ser alterado direto aqui
populacao = []
ind = [] #individuo
routeArray = []

# cria uma populacao
for i in range(tamPop):
    ind = individuals.Individuals(str(i))
    ind.printIndividual()
    populacao.append(ind)

nextGeneration = copy.copy(populacao)
populationData = []

for i in range(20):

    if (i % 2 == 0):
        storePopulationData(populationData, nextGeneration, i)

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

printPopulationStatus(populacao, 20)
printPopulationStatus(nextGeneration, 20)
plotPopulationEvolution(populationData)

print("Done")

# https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# with open("exittest", "w")



# parte para print da saída do programa num arquivo csv, para ser usado em GTFS
"""
# leitura e escrita em Python:
# http://www.pitt.edu/~naraehan/python2/reading_writing_methods.html

import route.RouteGenerator as rg
def printGTFS (generation):
#TODO

# to write a csv file
# https://docs.python.org/2/library/csv.html

# to create a GTFS format 
# https://developers.google.com/transit/gtfs/examples/gtfs-feed?hl=pt-br
    
    # minimum files to create a shapefile in gis (like tutorial below)
    # (http://www.stevencanplan.com/2016/02/converting-a-transit-agencys-gtfs-to-shapefile-and-geojson-with-qgis/)
    
    # create a file stops.txt (save bus stops and its infos)
    # must have points_ID, points_lat, points_lon at least


    stops = open('stops.txt', 'w')
    stops.write("stop_id,stop_name,stop_desc,stop_lat,stop_lon,stop_url,location_type,parent_station\n")
    allNodes = rg.getAllNodes()
    for node in allNodes:
        id = node.getIdx()
        name = node.getLabel()
        latlon = node.getLatLon()
        ...
        string=(str(id)+","+name+","+str(latlon[0])+","+latlon[1]+"\n")
        stops.writelines(string)
    stops.close()

    # create a file shapes.txt (save bus lines and its infos)
    # must have points_ID, points_lat, points_lon at least
    
    shapes = open('shapes.txt', 'w')
    shapes.write("shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled\n")
    for ind in generation:
        for route in ind:
            for node in route:
                id = node.getIdx()
                latlon = node.getLatLon()
                ...
                string=(str(id)+","+str(latlon[0])+","+latlon[1]+"\n")
                stops.writelines(string)    
    shapes.close()    

def printShapefile(generation):
#TODO
# https://glenbambrick.com/2016/01/09/csv-to-shapefile-with-pyshp/

"""
