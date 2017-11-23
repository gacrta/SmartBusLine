# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:23:44 2017

@author: Daniel
"""


#import node
import route
import random
import copy
from node import NodeList as nl

# gera Individuos -> x rotas dentro da USP
# que passem por todos os seus nos e comece/
# termine em algum dos terminais

# http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html
# https://stackoverflow.com/questions/448271/what-is-init-py-for?rq=1

# https://pt.stackoverflow.com/questions/109013/quando-devo-usar-init-em-fun%C3%A7%C3%B5es-dentro-de-classes
# https://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do
# https://stackoverflow.com/questions/8609153/why-do-we-use-init-in-python-classes

class Individuals:
    
    numRoutes = 3 # pode ser alterado direto aqui
    LACKING_NODE_PENALTY = 50
    
    def __init__ (self, label=None, fitness=None, genes=None):
        self.label = label
        if genes is None:
            self.genes = Individuals.createIndividual()
        else:
            self.genes = genes
            #calcula o fitness usando as rotas desse individuo
        #self.fitness = self.evalFitness()
        self.fitness = 0
        # FIM DO GERADOR

    def __str__ (self):
        print ("varias rota")
        
    @staticmethod
    def createIndividual ():
        #allNodes = route.Route.Nodes + route.Route.Terminals # concatenates the 2 lists
        newInd = [] # array de rotas
                
        # assim eh muito mais facil
        for i in range (Individuals.numRoutes):
            # cria Rotas
            newRoute = route.RouteGenerator.getNewRoute( str(i+1) ) 
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

    def getGenes(self):
        return self.genes

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
    def reproduction1 (ind1, ind2):
        individualSon = []
        
        return individualSon
    
    @staticmethod
    def reproduction2 (popList):

        # https://www.python-course.eu/python3_deep_copy.php
        # tutorial copy/deepcopy ~ referencias

        newPopList = copy.copy(popList)
        # this loop shorts indList removing two of its ind by turn, until it 
        # has 0 or 1 (and with 0/1 elem. could not use remove twice) elements
        while (len(popList) > 1):
            ind1 = random.choice(popList)
            popList.remove(ind1)
            ind2 = random.choice(popList)
            popList.remove(ind2)
            rL1, rL2 = ind1.cloneIndGenes(), ind2.cloneIndGenes()
            newInd1, newInd2 = [], []
            for i in range (Individuals.numRoutes):
                r1, r2 = random.choice(rL1), random.choice(rL2)
                if i == 2:
                    newInd1.append( r1 ), newInd2.append( r2 )
                else:
                    newInd1.append( r2 ), newInd2.append( r1 )
                rL1.remove(r1), rL2.remove(r2)
            #newPopList.append( Individuals(ind1.label+ind2.label, None, newInd1) )
            #newPopList.append( Individuals(ind2.label+ind1.label, None, newInd2) )
            newPopList.append( Individuals("", None, newInd1) )
            newPopList.append( Individuals("", None, newInd2) )
        #if len(popList) == 1: newPopList.append (Individuals.mutation(popList.pop()))
        return newPopList
        
		# TODO: COMO SERÁ A MUTAÇÃO? (i) um individuo com uma nova rota ou (ii) uma das rotas do individuo alterada?
		# recebe o individuo a ser mutado
    # estou tomando ind como um array; de array (rotas); de array (nos)
    @staticmethod
    def mutation(ind):
        indMutated = []
        # TODO: foi implementado uma variacao do (i), em q pra cada rota antiga
		  # ha 50% de chance de ela se manter e 50% de entrar um rota nova em seu lugar
        for i, e in enumerate(ind.genes):
            lucky = random.randint(1,2)
            if (lucky == 1):
                indMutated.append(e)
            else:
                newRoute = route.RouteGenerator.getNewRoute( str(i+1) ) 
                indMutated.append(newRoute)
        return Individuals(ind.getLabel() + "M", None, indMutated)
  
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
        # solutions has type [[demand, time], ...]
        for aSolution in solutions:
            sumDemand += aSolution[0]
            demandTimesTime += aSolution[0]*aSolution[1]
        result = demandTimesTime/sumDemand
        #result += self.getLackingNodes()*Individuals.LACKING_NODE_PENALTY
        #print result
        self.fitness = result

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
            else:
                travelTime = self.getTravelTime(startId, originRoutes,
                                                endId, destinationRoutes,
                                                transferTime, averageSpeed)

            solutionsTime.append([demand, travelTime])
        print solutionsTime
        return self.evalFitness2(solutionsTime)

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
                return min(solutions)

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
            return min(solutions)

        # else, the demand is unattended
        return -1

    # method that return individual routes that posses interestNode
    def getRoutesWithNode(self, interestNodeId):
        mRoutesWithNode = []
        for aRoute in self.genes:
            if (aRoute.getNodeById(interestNodeId) is not None):
                mRoutesWithNode.append(aRoute)
        return mRoutesWithNode

    def getLackingNodes(self):
        lenAllPossibleNodes = len(route.RouteGenerator.getAllNodes())
        print(lenAllPossibleNodes)
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
