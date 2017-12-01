# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:23:44 2017

@author: Daniel
"""


import route
import random
import copy
from node import NodeList as nl

# http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html
# https://stackoverflow.com/questions/448271/what-is-init-py-for?rq=1

# https://pt.stackoverflow.com/questions/109013/quando-devo-usar-init-em-fun%C3%A7%C3%B5es-dentro-de-classes
# https://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do
# https://stackoverflow.com/questions/8609153/why-do-we-use-init-in-python-classes

class Individuals:
    """

    gera Individuos -> x rotas dentro da USP
    que passem por todos os seus nos e comece/
    termine em algum dos terminais

    """

    numRoutes = 3 # pode ser alterado direto aqui
    LACKING_NODE_PENALTY = 5

    def __init__(self, label=None, fitness=None, genes=None):
        self.label = label
        self.genes = genes
        self.fitness = 0
        # boolean that indicates if fitness need to be evaluated
        self.updated = False
        # list of useful data for plotting purposes
        # [meanTime, %direct, %withTransf, %unattended]
        self.data=[0, 0, 0, 0]
        # FIM DO GERADOR

    def __str__(self):
        print ("varias rota")

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

    # passa uma lista de individuos p/ poder escolher RANDOM qual ind dara qual rota
    # filhos serao sempre dois a dois? ou pode ter uns partos frutos de orgia?
    # TODO: PENSAR MELHOR EM COMO FAZER A REPRODUCAO
	 # 1. (i) se o metodo recebe um par de pais ou (ii) se recebe a lista com todos
    # 2. (i) se appenda parte uma rota de um pai na de outro ou (ii) se pega uma rota de cada pai
	 # 3. (i) retorna um unico filho ou (ii) retorna a lista com a proxima geracao direto
    @staticmethod
    def reproduction1(ind1, ind2):
        individualSon = []

        return individualSon

    @staticmethod
    def reproduction2(popList):

        # https://www.python-course.eu/python3_deep_copy.php
        # tutorial copy/deepcopy ~ referencias

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

		# TODO: COMO SERÁ A MUTAÇÃO? (i) um individuo com uma nova rota ou (ii) uma das rotas do individuo alterada?
		# recebe o individuo a ser mutado
    # estou tomando ind como um array; de array (rotas); de array (nos)

    """   
  
  # se dois a dois, repr recebe como parametro ind1, ind2, certo? ou faz um rand dentro de uma matriz
  # de individuos e vai pegando e transando-os?
	
    # dada uma rota de N nos, pensei em usar um x=randint pra pegar um trecho de rota com x nos, 
    # e outra com N-x nos, e depois ligar elas -> sendo obrigadas a fazerem sentido ou nao? (i.e.,
    # o ultimo no de uma tem q ser vizinho do primeiro da outra?) 
    # se nao fizer sentido, isso pode ser cortado na hora dos pesos/selecao (~fitness)
    
    # como a rota (cromossomo) eh um array, da pra criar o gene pegando esse array ateh o elemento x
    #gene = []
    #for i in random.randint(1,lentgh(cromossomo1)):
    	#gene.append(cromossomo1[i])
    #N = lentgh(cromossomo2)
    #n = random.randint(1,N)
    #for j in n:
      #gene.append(cromossomo2[N-n+j])
    
    #newIndividual = gene1.extend(gene2)
    
    return newIndividual
    """

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


class IndividualCreator:

    def __init__(self, numRoutes, routeGenerator):
        self.mNumRoutes = numRoutes
        self.mRouteGenerator = routeGenerator

    # method that returns a full individual
    def createIndividual(self, label):
        routeArray = []  # a route array
        newIndividual = Individuals(label)

        while len(routeArray) != (self.mNumRoutes):
            # cria Rotas
            newRoute = self.mRouteGenerator.getNewRoute("")
            newRouteIsUnique = True
            for aRoute in routeArray:
                if aRoute.getString() == newRoute.getString():
                    newRouteIsUnique = False
            if (newRouteIsUnique):
                routeArray.append(newRoute)
        newIndividual.genes = routeArray
        return newIndividual

    # method that counts nodes not attended by individual
    def getLackingNodes(self, aIndividual):
        lenAllPossibleNodes = len(self.mRouteGenerator.getAllNodes())
        return lenAllPossibleNodes - len(aIndividual.getAllNodes())

    # method that gets a individual and may return a mutated one
    def mutation(self, ind):
        indMutated = []
        for i, e in enumerate(ind.genes):
            lucky = random.randint(1, 2)
            if (lucky == 1):
                indMutated.append(e)
            else:
                newRoute = self.mRouteGenerator.getNewRoute(str(i+1))
                indMutated.append(newRoute)
        return Individuals(ind.getLabel() + "M", None, indMutated)

    # method that creates current USP bus situation
    def getCurrentIndividual(self):
        uspBus = Individuals(label="Current USP", genes=[])
        circ1List = [0, 4, 33, 26, 24, 22, 20, 19, 46, 48, 50, 52,
                     54, 61, 56, 58, 43, 45, 59, 57, 16, 15, 27, 29,
                     30, 28, 12, 11, 9, 7, 5, 3, 0]
        circ2List = [0, 4, 6, 8, 10, 13, 14, 60, 17, 18, 21, 23, 25, 35, 36,
                     38, 40, 55, 61, 53, 51, 49, 47, 44, 42,
                     41, 39, 37, 34, 31, 32, 5, 3, 0]
        circ1 = self.mRouteGenerator.getRouteFromNodeList("Circ1", circ1List)
        circ2 = self.mRouteGenerator.getRouteFromNodeList("Circ2", circ2List)
        uspBus.genes.append(circ1)
        uspBus.genes.append(circ2)
        return uspBus
