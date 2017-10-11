# -*- coding: utf-8 -*-

import node
import route
import random

# gera Individuos -> x rotas dentro da USP
# que passem por todos os seus nos e comece/
# termine em algum dos terminais

# http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html
# https://stackoverflow.com/questions/448271/what-is-init-py-for?rq=1

# https://pt.stackoverflow.com/questions/109013/quando-devo-usar-init-em-fun%C3%A7%C3%B5es-dentro-de-classes
# https://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do
# https://stackoverflow.com/questions/8609153/why-do-we-use-init-in-python-classes

class Individuals:
    
    def __init__ (self, label="", routes=[]):
        self.label = label
        self.routes = routes
    
	def __str__ (self):
		print ("varias rota")
		
    def createIndividual (termNodes, simpleNodes):
        individuo = [] # array de rotas
				
		#numOfNodes = 0
        #allNodes = FALSE
		#while (!allNodes):
		# se tiver que passar por todos os nos da rede para sair do loop gerador de individuo
		# sera algo assim, com "switch(allNodes)" e um contador de nos/
		# ou armazena cada no novo num array a parte e depois compara
				
		# assim eh muito mais facil
		for i in range (3):
			(tIni, tEnd) = ( random.choice(termNodes), random.choice(termNodes) )
			# como saber qdo o individuo nasceu (i.e. parar de gerar rotas pro individ): 
			# qdo passar por todos nos? qdo atingir um random number entre 1 e x?

			# tem q chamar a gera rotas com um term inicio e fim - (termIni, termFim, array de nos)
			# (se for o mesmo, seria uma rota circular)
			routeGene = route.Route.genRoute( tIni, tEnd, simpleNodes )
			individuo.append(routeGene)
        return individuo

# escolhe dois individuos diferentes e escolhe
# de cada um, aleatoriamente, umas das suas rotas
 
# pode receber uma matriz de individuos como parametro
# ou receber direto dois individ para acasalarem
# ou dar um "get"/gerar dentro da propria funcao

# passa uma lista de individuos p/ poder escolher RANDOM qual ind dara qual rota
    def reproduction (indList):
        individualSon = []
		for i in range(3):
			ind = random.choice(indList) # usa random para escolher individ (2x se usar matriz)
			gene = random.choice(ind) # usa random para dar um "getRoutes" de um individ (pra ser rand a rota pega)
			individualSon.append(gene) # usa random para escolher até qual nó a rota vai ser preservada e appendada a outra
    	# da maneira que esta, ha o risco de formar um filho igual um pai
		# pode se atacar isso comparando individuos ou soh deixando ele sofrer pressao seletiva igual
        return individualSon
    
	# recebe o individuo a ser mutado
	# estou tomando ind como um array; de array (rotas); de array (nos)
    def mutation(ind, ):
        individualMutated = []
        # como fazer a mutacao? alterando uma rota dentro do indiv(1)? tirar uma das rotas e colocar outra nova(2)?
		# (1)
		route = random.choice(ind)
		newLastNodeIndex = randint(1, len(route))
		for i in range(newLastNodeIndex):
			individualMutated.append(route[i])
		tEnd = random.choice(termNodes)
		routeGene = route.Route.genRoute( route[newLastNodeIndex - 1], tEnd, simpleNodes )
		individualMutated.extend(routeGene)
			
		"""
		# (2)
		for i in ind:
			lucky = random.choice(1,2)
			if (lucky == 1):
				individualMutated.append(i)
			else:
				routeGene = route.Route.genRoute( tIni, tEnd, simpleNodes )
				individuo.append(routeGene)
        """
        return individualMutated

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
