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
import route
import utils.utils as utils

MUTATION_RATE = 0.05
AVERAGE_SPEED = 5.94  # m/s = 21,4 km/h / 3.6
TRANSFER_TIME = 10  # minutes

USE_2_ROUTES = 2
USE_3_ROUTES = 3
USE_4_ROUTES = 4

POPULATION_LENGHT = 80
ITERATION_NUM = 30
MAX_ROUTE_LEN = 40

# constants for evaluation step
K1 = 10.0
xm = 30.0
K2 = 10.0
K3 = 30.0

DATA_FITNESS = "fitness"
DATA_MEAN_TIME = "meanTIme"
DATA_DIRECT = "directly"
DATA_TRANSFER = "transfer"
DATA_UNATTEND = "unattended"


def printPopulationStatus(pop, iteration):
    print("Population Status for " + str(iteration) + " iteration:")
    for ind in pop:
        msg = "Individual %(indLabel)s: %(fitness).2f"%{"indLabel":ind.getLabel(),"fitness":ind.fitness}
        print(msg)


def populationSort(pop):
        return sorted(pop, key=operator.attrgetter("fitness"), reverse=True)


def populationSelect(pop):
    tamPop = len(pop)

    # takes highest half population...
    popOver = sortedPop[:int(tamPop/2)]
    bestInd = popOver.pop(0)
    # ... and pick 0.9 of them
    popOver = random.sample(popOver, int(0.9*(tamPop/2)-1))
    # takes lowest half population...
    popUnder = sortedPop[int(tamPop/2):]
    # ... and pick 0.1 of them
    popUnder = random.sample(popUnder, int(0.1*(tamPop/2)))
    # making a new generation from a half of old pop
    return [bestInd] + popOver + popUnder


def getPopulationArray(population):
    dt = numpy.dtype([("label", numpy.str_, 20),
                      (DATA_FITNESS, numpy.float64, 1),
                      (DATA_MEAN_TIME, numpy.float64, 1),
                      (DATA_DIRECT, numpy.float64, 1),
                      (DATA_TRANSFER, numpy.float64, 1),
                      (DATA_UNATTEND, numpy.float64, 1)])
    tempList = []
    for ind in population:
        tempList.append((ind.label,
                         ind.fitness,
                         ind.data[0],
                         ind.data[1],
                         ind.data[2],
                         ind.data[3]))
    popArray = numpy.array(tempList, dtype=dt)
    return popArray


def getPopulationMean(popArray, dataType):
    return popArray[dataType].mean()


def getPopulationMax(popArray, dataType):
    return popArray[dataType].max()


def getPopulationMin(popArray, dataType):
    return popArray[dataType].min()


def getPopulationStd(popArray, dataType):
    return popArray[dataType].std()


def evalPopulation(population, K1, xm, K2, K3, od_data,
                   transferTime, minimumPath, averageSpeed):
    for ind in population:
        if (not ind.isUpdated()):
            ind.evalFitness3(K1, xm, K2, K3, od_data,
                             transferTime, minimumPath, averageSpeed)


def storePopulationData(dataStorage, popArray, iteration):

    # Fitness
    popFitMean = getPopulationMean(popArray, DATA_FITNESS)
    popFitMax = getPopulationMax(popArray, DATA_FITNESS)
    popFitStd = getPopulationStd(popArray, DATA_FITNESS)

    # Time
    popTimeMean = getPopulationMean(popArray, DATA_MEAN_TIME)
    bestIndTime = popArray[0][DATA_MEAN_TIME]

    # Direct
    popDirectMean = getPopulationMean(popArray, DATA_DIRECT)
    bestIndDirect = popArray[0][DATA_DIRECT]

    # Transfer
    popTransferMean = getPopulationMean(popArray, DATA_TRANSFER)
    bestIndTransfer = popArray[0][DATA_TRANSFER]

    # Unattended
    popUnattended = getPopulationMean(popArray, DATA_UNATTEND)
    bestIndUnattended = popArray[0][DATA_UNATTEND]

    dataStorage.append([iteration, popFitMax, popFitMean, popFitStd,
                        popTimeMean, bestIndTime,
                        popDirectMean, bestIndDirect,
                        popTransferMean, bestIndTransfer,
                        popUnattended, bestIndUnattended])


def plotPopulationEvolution(dataStorage, individualSize):

    # dataStorage = [iteration, popFitMax, popFitMean, popFitStd,
    #                popTimeMean, bestIndTime,
    #                popDirectMean, bestIndDirect,
    #                popTransferMean, bestIndTransfer,
    #                popUnattended, bestIndUnattended]

    indSizeStr = str(individualSize)
    dataArray = numpy.array(dataStorage)
    iterations = dataArray[:, 0]
    popMax = dataArray[:, 1]
    popMean = dataArray[:, 2]
    popStd = dataArray[:, 3]
    plt.figure()
    plt.errorbar(iterations, popMean, yerr=popStd)
    plt.plot(iterations, popMax)
    plt.xlabel("Iterations")
    plt.ylabel("Fitness")
    plt.title("Best Scenario evolution")
    plt.legend(["Max", "Mean"])
    plt.grid()
    plt.savefig("graphics_fitness_" + indSizeStr + ".png")

    bestTime = dataArray[:, 5]
    meanTime = dataArray[:, 4]
    plt.figure()
    plt.plot(iterations, bestTime)
    plt.plot(iterations, meanTime)
    plt.xlabel("Iterations")
    plt.ylabel("Mean Time (min)")
    plt.title("Mean time evolution")
    plt.legend(["Best Scenario", "Population"])
    plt.grid()
    plt.savefig("graphics_mean_time_" + indSizeStr + ".png")

    bestDirect = dataArray[:, 7]
    meanDirect = dataArray[:, 6]
    bestTransf = dataArray[:, 9]
    meanTransf = dataArray[:, 8]
    f, ax = plt.subplots(2, sharex=True)
    ax[0].plot(iterations, bestDirect)
    ax[0].plot(iterations, meanDirect)
    ax[1].plot(iterations, bestTransf)
    ax[1].plot(iterations, meanTransf)
    plt.xlabel("Iterations")
    ax[0].set_ylabel("Direct travels (%)")
    ax[1].set_ylabel("Indirect travels (%)")
    ax[0].set_title("Travel type evolution")
    ax[0].legend(["Best Scenario", "Population"])
    ax[0].grid()
    ax[1].grid()
    plt.savefig("graphics_travels_" + indSizeStr + ".png")

    bestUnattend = dataArray[:, 11]
    meanUnattend = dataArray[:, 10]
    plt.figure()
    plt.plot(iterations, meanUnattend)
    plt.plot(iterations, bestUnattend)
    plt.xlabel("Iterations")
    plt.ylabel("Unnatended demand (%)")
    plt.title("Best Scenario evolution")
    plt.legend(["Best Scenario", "Population"])
    plt.grid()
    plt.savefig("graphics_unattended_" + indSizeStr + ".png")


# method that inits the population list
def initPopulation(indCreator, population=None, popSize=POPULATION_LENGHT):
    willReturn = False
    if population is None:
        population = []
        willReturn = True
    # creates individuals
    for i in range(popSize):
        ind = indCreator.createIndividual(str(i))
        population.append(ind)
    if willReturn:
        return population


# method that mutates random individuals
def mutatePopulation(population, indCreator, mutationRate=MUTATION_RATE):
    # preserves the first individual: elitism
    popmut = random.sample(population[1:],
                           int(len(population)*mutationRate))
    for ind in popmut:
        # mutating indiviuals
        indmut = indCreator.mutation(ind)
        population.remove(ind)
        population.append(indmut)


###################
#  Script Starts  #
###################

utils.initLogger()
mLogger = utils.getLogger("main")
mLogger.info("Script started!")

# sample OD matrix
# [start, end, demand]
mLogger.debug("Parsing OD Matrix from file")
od_data = utils.parseCsvODFile()
mLogger.debug("Parsing OD Matrix done")

mLogger.debug("Init RouteGenerator")
mRouteGenerator = route.RouteGenerator(MAX_ROUTE_LEN)
mLogger.debug("RouteGenerator Created")

mLogger.debug("Init Floyd Mininum Time Matrix")
minimumPath = mRouteGenerator.getFloydMinimumTime(AVERAGE_SPEED)
mLogger.debug("Floyd Mininum Time Matrix created")

mLogger.debug("Init IndividualCreators")
indCreator2 = individuals.IndividualCreator(USE_2_ROUTES, mRouteGenerator)
indCreator3 = individuals.IndividualCreator(USE_3_ROUTES, mRouteGenerator)
indCreator4 = individuals.IndividualCreator(USE_4_ROUTES, mRouteGenerator)
indCreatorList = [indCreator2, indCreator3, indCreator4]
mLogger.debug("IndividualCreators created")

mLogger.debug("Init Population list")
pop2 = initPopulation(indCreator3)
pop3 = initPopulation(indCreator3)
pop4 = initPopulation(indCreator4)
mPopList = [pop2, pop3, pop4]
mLogger.debug("Population list created")

mLogger.debug("Init current USP cenario.")
uspBus = indCreator3.getCurrentIndividual()
mLogger.debug("Evaluating current USP cenario...")
evalPopulation([uspBus], K1, xm, K2, K3, od_data,
               TRANSFER_TIME, minimumPath, AVERAGE_SPEED)
mLogger.debug("Evaluating current USP cenario ended.")

mBestSolutions = []
for pop in mPopList:

    nextGeneration = copy.copy(pop)
    indCreator = indCreatorList[mPopList.index(pop)]
    populationData = []

    mLogger.info("Optimization for population " + str(mPopList.index(pop)) + " started.")
    for i in range(ITERATION_NUM):
        mLogger.info("Starting iteration " + str(i))
        if (i % 2 == 0):
            mLogger.info("Storing data of iteration " + str(i))
            popArray = getPopulationArray(nextGeneration)
            storePopulationData(populationData, popArray, i)

        mLogger.info("Evaluating population at iteration " + str(i))
        evalPopulation(nextGeneration, K1, xm, K2, K3, od_data,
                       TRANSFER_TIME, minimumPath, AVERAGE_SPEED)

        mLogger.info("Sorting population at iteration " + str(i))
        sortedPop = populationSort(nextGeneration)

        # selects parental generation
        mLogger.info("Selecting population at iteration " + str(i))
        newGeneration = populationSelect(sortedPop)

        mLogger.info("Reproducting population at iteration " + str(i))
        # completing nextGeneration by reproduction
        nextGeneration = individuals.Individuals.reproduction2(newGeneration)

        mLogger.info("Mutating population at iteration " + str(i))
        mutatePopulation(nextGeneration, indCreator)

        mLogger.info("End of iteration " + str(i))

    mLogger.info("Optimization for population " + str(mPopList.index(pop)) + " ended.")

    mLogger.debug("Producing graphics for population " + str(mPopList.index(pop)) + "...")
    plotPopulationEvolution(populationData, indCreator.getNumRoutes())
    mLogger.debug("Done producing graphics for population " + str(mPopList.index(pop)))

    mBestSolutions.append(nextGeneration[0])

mLogger.info("Script Finished!")

###################
#   Script Ends   #
###################
