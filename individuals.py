# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:23:44 2017

@author: Daniel
"""


#import node
import route
#import random

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
    
    def __init__ (self, label=None, fitness=None, genes=None):
        self.label = label
        if genes is None:
            self.genes = Individuals.createIndividual()
        else:
            print ("ruim")
            #calcula o fitness usando as rotas desse individuo
        self.fitness = self.evalFitness()
        # FIM DO GERADOR

    def __str__ (self):
        print ("varias rota")
        
    # recebe num de rotas que um individuo deve ter
    # recebe mais coisas?
    def createIndividual ():
        
        allNodes = route.Route.Nodes + route.Route.Terminals # concatenates lists
        
        routeArray = []
        # loop below append numRoutes routes in an individual and find nodes
        # that no routes pass by
        lackingLabelNodes = []
        for i in range (Individuals.numRoutes):
            # create Routes
            newRoute = route.RouteGenerator.getNewRoute( str(i+1) )
            # get labels from route
            routeNodes = newRoute.getNodes()
            
            for j in allNodes:
                flag = 1 # flag to identify if j node label is in newRoute
                
                for k in routeNodes:
                    
                    # if this label is already in lackingNodes, 
                    # this means that it is not a lackingNode anymore
                    if k.getLabel() in lackingLabelNodes:
                        lackingLabelNodes.remove(k.getLabel())
                    
                    # if some route label is equal to some label in allNodes
                    # this route label shuold not go in lackingNodes list
                    elif k.getLabel() == j.getLabel():
                        flag= 0
                    
                if flag == 1:
                    lackingLabelNodes.append(j.getLabel())
            
            routeArray.append( newRoute )
        
        distArray = []
        
        for someLabelNode in lackingLabelNodes:
            
            for someRoute in routeArray:
                # call method that finds distance between a lacking node and
                # its the closest node in this route
                dist = someRoute.getDistanceRouteNode(someLabelNode)
                distArray.append( dist )
            
            
            lackingLabelNodes.pop()
            
        
        # uma vez q o array de rotas esta criado, precisa verificar se ele esta adequado
        

        return routeArray

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

    # escolhe dois individuos diferentes e escolhe
    # de cada um, aleatoriamente, umas das suas rotas
     
    # pode receber uma matriz de individuos como parametro
    # ou receber direto dois individ para acasalarem
    # ou dar um "get"/gerar dentro da propria funcao
    """
    # passa uma lista de individuos p/ poder escolher RANDOM qual ind dara qual rota
        def reproduction (indList):
            individualSon = []
            for i in range(3):
                ind = random.choice(indList)
                gene = random.choice(ind)
                individualSon.append(gene)
        
        # usa random para escolher individ (2x se usar matriz)
        # usa random para dar um "getRoutes" de um individ (pra ser rand a rota pega)
        # usa random para escolher até qual nó a rota vai ser preservada e appendada a outra
        
            # da maneira que esta, ha o risco de formar um filho igual um pai
            # pode se atacar isso comparando individuos ou soh deixando ele sofrer pressao seletiva igual
            return individualSon
        
            # recebe o individuo a ser mutado
            # estou tomando ind como um array; de array (rotas); de array (nos)
        def mutation(ind, ):
            individualMutated = []
            
            # como fazer a mutacao? alterando uma rota dentro do indiv(1)? tirar uma das rotas e colocar outra nova(2)?
            # (2) eh mais facil
                    
            for i in ind:
                lucky = random.choice(1,2)
                if (lucky == 1):
                    individualMutated.append(i)
                else:
                    routeGene = route.Route.genRoute( tIni, tEnd, simpleNodes )
                    individuo.append(routeGene)
            
            return individualMutated
    
    """    
    """
    
    # criando individuos usando a "startNewRandomRoute" (logica antiga)
    
        def individuos (nodesList):
            individuos = []
        #termArray = getTermNodesFrom(nodesList)                             # array soh com os term
        #nodeArray = getNodesFrom(nodesList)                                     # array sem os term
        #termInitial = random.choice(termArray)     # pega um terminal pra ser o inicio da rota
        #termEnding = random.choice(termArray)     # pega um terminal pra ser o fim da rota (se for = init, rota circular)
        #numRandomNode = random.randint(1,length(nodeArray)) # num aleatorio pra definir tamanho da rota que vai p newRandomRoute
        
            return individuos
    
    # qtos individuos serao criados por turno?
    # e qtos filhos?
    # filhos serao sempre dois a dois? ou pode ter uns partos frutos de orgia?
    # se dois a dois, repr recebe como parametro ind1, ind2, certo? ou faz um rand dentro de uma matriz
    # de individuos e vai pegando e transando-os?
    
            def reproduction ():
        
        #ind1 = getind() 
        #ind2 = getind()
        #cromossomo1 = random.choice(ind1) # pega alguma rota do individuo 1
        #cromossomo2 = random.choice(ind2) # pega alguma rota do individuo 2
        # dada uma rota de N nos, pensei em usar um x=randint pra pegar um trecho de rota com x nos, 
        # e outra com N-x nos, e depois ligar elas -> sendo obrigadas a fazerem sentido ou nao? (i.e.,
        # o ultimo no de uma tem q ser vizinho do primeiro da outra?) 
        # se nao fizer sentido, isso pode ser cortado na hora dos pesos/selecao (~fitness)
        
        # como a rota (cromossomo) eh um array, da pra criar o gene pegando esse array ateh o elemento x
        #gene = []
            #for i in random.randint(1,lentgh(cromossomo1)) 
            #gene.append(cromossomo1[i])
        #N = lentgh(cromossomo2)
        #n = random.randint(1,N)
        #for j in n
            # gene.append(cromossomo2[N-n+j])
        
        
        # newIndividual = gene1.extend(gene2)
        
                return newIndividual
    """
    # sample method to evaluate fitness
    # returns the simple median of the lenght of individual routes
    def evalFitness(self):
        sumLenght = 0
        for aRoute in self.genes:
            sumLenght += aRoute.evalRouteDistance()
        return sumLenght/Individuals.numRotas
    
    # evaluates the In Vehicle Travel time for each OD par
    def evalIVT(self, ODmatrix, transferTime):
        solutionsTime = []
        for line in ODmatrix:
            for i in line:
                for j in line:
                    if i != j:
                        # for each node pair of OD matrix, find [Ro] and [Rd]
                        # important: the OD matrix must be ordered equally to allNodes list
                        originNode = route.RouteGenerator.findNodeByLabel(i)
                        originRoutes = self.getRoutesWithNode(originNode)
                        destinationNode = route.RouteGenerator.findNodeByLabel(j)
                        destinationRoutes = self.getRoutesWithNode(destinationNode)
    
                        lenghtOR = len(originRoutes)
                        lenghtDR = len(destinationRoutes)
                        # if individual is not guaranteed to have all nodes, the demand
                        # could be unattended
                        if lenghtOR == 0 or lenghtDR == 0:
                            return -1
    
                        # searches for common routes between [Ro] and [Rd]
                        commonRoutes = route.RouteList.getCommonListElements(originRoutes, destinationRoutes)
                        for solutionRoute in commonRoutes:
                            solutionsTime.append(solutionRoute.evalRouteDistance())
    
                        # if a common route is found, return the smallest time
                        if len(solutionsTime) != 0:
                            return min(solutionsTime)
    
                        # otherwise, search for common nodes between each element of [Ro] and [Rd]
                        commonNodes = route.RouteList.getCommonNodes(originNode, destinationNode)
                        for nodeList in commonNodes:
                            for aNode in nodeList:
                                # Todo - Finish common nodes
                                return None
    
                        # if there are common nodes, get all possible times
                        for solutionNode in commonNodes:
                            solutionsTime.append()

# method that return individual routes that posses interestNode
def getRoutesWithNode(self, interestNode):
    # TODO
    return None
