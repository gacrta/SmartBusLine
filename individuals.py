# -*- coding: utf-8 -*-

import route
import random
import copy
from node import NodeList as nl

class Individuals:

    numRoutes = 3 # number of genes(routes) to each individual
    LACKING_NODE_PENALTY = 5

    def __init__(self, label=None, fitness=None, genes=None):
        self.label = label
        if genes is None:
            self.genes = Individuals.createIndividual()
        else:
            self.genes = genes
        self.fitness = 0
        # boolean that indicates if fitness need to be evaluated
        self.updated = False
        # list of useful data for plotting purposes
        # [meanTime, %direct, %withTransf, %unattended]
        self.data=[0,0,0,0]
        # FIM DO GERADOR

    def __str__(self):
        print ("Ind: " + self.getLabel())

    @staticmethod
    def createIndividual ():
        #allNodes = route.Route.Nodes + route.Route.Terminals # concatenates the 2 lists
        newInd = []
        while len(newInd) != (Individuals.numRoutes):
            # cria Rotas
            newRoute = route.RouteGenerator.getNewRoute("")
            newRouteIsUnique = True
            for aRoute in newInd:
                if aRoute.getString() == newRoute.getString():
                    newRouteIsUnique = False
            if (newRouteIsUnique):
                newInd.append( newRoute )
        return newInd

    # method to easily read individual contents
    def printIndividual(self):
        print("Printing Individual " + self.label)
        for aRoute in self.genes:
            aRoute.printRouteNodes()
            print(" - Route lenght: " + str(aRoute.getLenght()))
            print("")

    def getLabel(self):
        return self.label

    def getFitness(self):
        if self.fitness is None:
            self.fitness = self.evalFitness()
        return self.fitness

    def getUsefulData(self):
        return self.data

    def getGenes(self):
        return self.genes

    def isUpdated(self):
        return self.updated

    # takes an ind and return a list of cloned routes
    def cloneIndGenes(self):
        genes = self.getGenes()
        routeList = []
        for gene in genes:
            clonedRoute = gene.cloneRoute()
            routeList.append(clonedRoute)
        return routeList

    @staticmethod
    def reproduction2(popList):


        newPopList = copy.copy(popList)
        # this loop shorts indList removing two of its ind by turn, until it
        # has 0 or 1 (and with 0/1 elem. could not use remove twice) elements
        while (len(popList) > 1):

            ind1 = random.choice(popList)
            ind2 = random.choice(popList)
            while (ind1 == ind2):
                ind1 = random.choice(popList)
                ind2 = random.choice(popList)
            rL1, rL2 = ind1.cloneIndGenes(), ind2.cloneIndGenes()
            newInd1, newInd2 = [], []
            indReproductionDone = False
            i = 0
            while(not indReproductionDone):
                r1, r2 = random.choice(rL1), random.choice(rL2)
                if r1.getString() != r2.getString():
                    if i % 2 == 0:
                        newInd1.append( r1 ), newInd2.append( r2 )
                    else:
                        newInd1.append( r2 ), newInd2.append( r1 )
                    rL1.remove(r1), rL2.remove(r2)
                elif (len(rL1) == 1):
                    break
                if (len(rL1) == 0):
                    indReproductionDone = True
                i+=1
            if (indReproductionDone):
                #newPopList.append( Individuals(ind1.label+ind2.label, None, newInd1) )
                #newPopList.append( Individuals(ind2.label+ind1.label, None, newInd2) )
                popList.remove(ind1)
                popList.remove(ind2)
                newPopList.append( Individuals("", None, newInd1) )
                newPopList.append( Individuals("", None, newInd2) )
            else:
                del(newInd1)
                del(newInd2)
        #if len(popList) == 1: newPopList.append (Individuals.mutation(popList.pop()))
        return newPopList

    @staticmethod
    def mutation(ind):
        indMutated = []
        for i, e in enumerate(ind.genes):
            lucky = random.randint(1,2)
            if (lucky == 1):
                indMutated.append(e)
            else:
                newRoute = route.RouteGenerator.getNewRoute( str(i+1) ) 
                indMutated.append(newRoute)
        return Individuals(ind.getLabel() + "M", None, indMutated)

    # sample method to evaluate fitness
    # returns the simple median of the lenght of individual routes
    def evalFitness(self):
        sumLenght = 0
        for aRoute in self.genes:
            sumLenght += aRoute.evalRouteDistance()
        sumLenght -= self.getLackingNodes()*Individuals.LACKING_NODE_PENALTY
        return sumLenght/Individuals.numRoutes

    def evalFitness2(self, solutions):
        sumDemand = 0
        demandTimesTime = 0
        unnatendedDemand = 0
        # solutions has type [[demand, time], ...]
        for aSolution in solutions:
            sumDemand += aSolution[0]
            if aSolution[1] != -1:
                demandTimesTime += aSolution[0]*aSolution[1]
            else:
                unnatendedDemand += aSolution[0]
        result = demandTimesTime/sumDemand
        result += self.getLackingNodes()*Individuals.LACKING_NODE_PENALTY
        result += unnatendedDemand
        self.fitness = result

    # method that evaluates fitness as CHAKROBORTY
    def evalFitness3(self, K1, xm, K2, K3,
                     ODmatrix, transferTime, minimumPath, averageSpeed):
        solutions = self.evalIVT(ODmatrix, transferTime, averageSpeed)

        F1 = self.evalF1(solutions, K1, xm, minimumPath, averageSpeed)
        F2 = self.evalF2(solutions, K2)
        F3 = self.evalF3(solutions, K3)

        self.fitness = F1+F2+F3
        self.updated = True

    # evaluetes the time part of fitness
    def evalF1(self, solutions, K1, xm, minimumPath, averageSpeed):
        attendedDemand = 0
        acumulatedF = 0
        acumulatedTime = 0
        # -K1/xm <= b1 <= 0
        b1 = -K1/(2*xm)

        for aSolution in solutions:
            i = aSolution[0]
            j = aSolution[1]
            demand = aSolution[2]
            time = aSolution[3]
            if time != -1:
                attendedDemand += demand
                acumulatedTime += time*demand
                x = time - minimumPath[i][j]
                if x <= xm:
                    f = -(b1/xm + K1/(xm**2))*x**2 + b1*x + K1
                else:
                    f = 0
                acumulatedF += f*demand

        if attendedDemand == 0:
            return 0
        self.data[0] = acumulatedTime/attendedDemand
        return acumulatedF/attendedDemand

    # evaluetes the transfer part of fitness
    def evalF2(self, solutions, K2):
        a = 3
        b = 1
        # K2/a <= b2 <= 2*K2/a
        b2 = 3*K2/(2*a)
        attendedDirectly = 0
        attendedWithTransfer = 0

        for aSolution in solutions:
            demand = aSolution[2]
            time = aSolution[3]
            transfer = aSolution[4]
            if time != -1:
                if transfer is False:
                    attendedDirectly += demand
                else:
                    attendedWithTransfer += demand

        totalDemand = float(attendedDirectly + attendedWithTransfer)
        if totalDemand == 0:
            return 0
        self.data[1] = float(attendedDirectly)/totalDemand
        self.data[2] = float(attendedWithTransfer)/totalDemand
        dT = (a*attendedDirectly + b*attendedWithTransfer)/totalDemand
        return ((K2 - b2*a)/(a**2))*(dT**2) + b2*dT

    # evaluetes the unattended demand part of fitness
    def evalF3(self, solutions, K3):
        # - K3 <= b3 <= 0
        b3 = -K3/2
        unAttendedDemand = 0
        totalDemand = 0

        for aSolution in solutions:
            demand = aSolution[2]
            time = aSolution[3]
            if time == -1:
                unAttendedDemand += demand
            totalDemand += demand

        dUn = float(unAttendedDemand)/totalDemand
        self.data[3] = dUn
        return -(b3 + K3)*(dUn**2) + b3*dUn + K3

    # evaluates the In Vehicle Travel time for each OD pair
    def evalIVT(self, ODmatrix, transferTime, averageSpeed):
        solutionsTime = []
        # Suppose that ODmatrix = [[startId, endId, demand], ...]
        for line in ODmatrix:
            startId = line[0]
            endId = line[1]
            demand = line[2]

            # for each node pair of OD matrix, find [Ro] and [Rd]
            # important: the OD matrix must be ordered equally to allNodes list
            originRoutes = self.getRoutesWithNode(startId)
            destinationRoutes = self.getRoutesWithNode(endId)

            lenghtOR = len(originRoutes)
            lenghtDR = len(destinationRoutes)
            # if individual is not guaranteed to have all nodes,
            # the demand could be unattended
            if lenghtOR == 0 or lenghtDR == 0:
                travelTime = -1
                transfer = False
            else:
                [travelTime, transfer] = self.getTravelTime(startId,
                                                            originRoutes,
                                                            endId,
                                                            destinationRoutes,
                                                            transferTime,
                                                            averageSpeed)

            solutionsTime.append([startId, endId, demand, travelTime, transfer])
        return solutionsTime

    def getTravelTime(self, originNode, originRouteList,
                      destinationNode, destinationRouteList,
                      transferTime, averageSpeed):

        solutions = []  # list that contains solutions

        # searches for common routes between [Ro] and [Rd]
        commonRoutes = route.RouteList.getCommonListElements(originRouteList,
                                                             destinationRouteList)
        if len(commonRoutes) != 0:
            for solutionRoute in commonRoutes:
                time = solutionRoute.evalRouteTime(originNode, destinationNode,
                                                   averageSpeed)
                if time > 0:
                    # if time = 0, it is a unatended demand
                    solutions.append(time)
            if len(solutions) > 0:
                return [min(solutions), False]

        # otherwise, search for common nodes between each element of [Ro]
        # and [Rd]
        for originRoute in originRouteList:
            for destinationRoute in destinationRouteList:
                commonNodes = originRoute.getCommonNodes(destinationRoute)
                for transferNode in commonNodes:
                    time = self.evalTransitTimeWithTransfer(transferNode,
                                                            transferTime,
                                                            originNode,
                                                            originRoute,
                                                            destinationNode,
                                                            destinationRoute,
                                                            averageSpeed)
                    solutions.append(time)

        # if a transfer node is found, return the smallest time
        if len(solutions) != 0:
            return [min(solutions), True]

        # else, the demand is unattended
        return [-1, False]

    # method that return individual routes that posses interestNode
    def getRoutesWithNode(self, interestNodeId):
        mRoutesWithNode = []
        for aRoute in self.genes:
            if (aRoute.getNodeById(interestNodeId) is not None):
                mRoutesWithNode.append(aRoute)
        return mRoutesWithNode

    def getLackingNodes(self):
        lenAllPossibleNodes = len(route.RouteGenerator.getAllNodes())
        return lenAllPossibleNodes - len(self.getAllNodes())

    # returns a list of all nodes of this individual, without repetition
    def getAllNodes(self):
        mNodes = []
        mNodesList = []
        for gene in self.genes:
            mNodesList.append(gene.getNodes())
        mNodes = nl.getUniqueNodesFromLists(mNodesList)
        return mNodes

    # eval transit time with one transfer
    def evalTransitTimeWithTransfer(self, transferNodeId, transferTime,
                                    originNodeId, originRoute,
                                    destinationNodeId, destinationRoute,
                                    averageSpeed):

        time1 = originRoute.evalRouteTime(originNodeId,
                                          transferNodeId, averageSpeed)
        time2 = destinationRoute.evalRouteTime(transferNodeId,
                                               destinationNodeId, averageSpeed)

        if time1 is not None and time1 is not None:
            return time1+time2+transferTime
        return None