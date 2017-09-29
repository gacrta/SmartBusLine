# -*- coding: utf-8 -*-

import node
import random

# gera Individuos -> x rotas dentro da USP
# que passem por todos os seus nos e comece/
# termine em algum dos terminais

class Individuals:
	
	def __init__ (self, label="", routes=[]):
		self.label = label
		self.routes = routes
		
	def createIndividual ():
		individuo = [] # array de rotas
		
		
			
		return individuo

# escolhe dois individuos diferentes, escolhe
# de cada um, aleatoriamente, uma das suas rotas,
# escolhe (aleat.) um ponto de cada rota para quebrar
# e juntar elas

# pode receber uma matriz de individuos como parametro
# ou receber direto dois individ para acasalarem
# ou dar um "get"/gerar dentro da propria funcao
	def reproduction ():
	
	# usa random para escolher individ (2x se usar matriz)
	# usa random para dar um "getRoutes" de um individ (pra ser rand a rota pega)
	# usa random para escolher até qual nó a rota vai ser preservada e appendada a outra
	
		return individualSon
	
	def mutation():
		
		
		
		return individualMutated

	

# criando individuos usando a "startNewRandomRoute"

def individuos (nodesList):
  individuos = []
	#termArray = getTermNodesFrom(nodesList) 							# array soh com os term
	#nodeArray = getNodesFrom(nodesList) 									# array sem os term
	#termInitial = random.choice(termArray) 	# pega um terminal pra ser o inicio da rota
	#termEnding = random.choice(termArray) 	# pega um terminal pra ser o fim da rota (se for = init, rota circular)
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
