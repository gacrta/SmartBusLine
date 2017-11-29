# -*- coding: utf-8 -*-

import json
import node
import io
import csv



def readNodesJsonFile():
    """ read data/nodes.json file from this project """
    fileName = "data/nodes.json"
    with open(fileName, "r") as f:
        jsonString = f.read()
        return jsonString


def parseJsonString(jsonString):
    """ creates nodes list from jsonString """
    nodes = []
    terminals = []
    jsonStruct = json.loads(jsonString)
    for jsonNode in jsonStruct['network']['nodes']:
        nodes.append(node.Node(jsonNode['id'],
                               jsonNode['label'],
                               jsonNode['neighbors'],
                               jsonNode['distance'],
                               jsonNode['latlong'],
                               jsonNode['neighbors_latlong']))

    for jsonNode in jsonStruct['network']['terminals']:
        terminals.append(node.Node(jsonNode['id'],
                                   jsonNode['label'],
                                   jsonNode['neighbors'],
                                   jsonNode['distance'],
                                   jsonNode['latlong'],
                                   jsonNode['neighbors_latlong']))
    return [nodes, terminals]


""" TODO - deixar apto p ler um csv de uma API, p. ex. """

# (Python2) https://docs.python.org/2/library/csv.html
# (Python3) https://docs.python.org/3/library/csv.html
# http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
# https://pymotw.com/2/csv/

import csv
def readCsvFiles():
    filename = "data/csvTest.csv"
    with open(filename, 'rb') as csvfile:
        filereader = csv.reader(csvfile)
        return filereader
    
# parte para print da saída do programa num arquivo csv, para ser usado em GTFS

# leitura e escrita em Python:

# http://www.pitt.edu/~naraehan/python2/reading_writing_methods.html
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

def print_GTFS (generation):
    
    jsonStr = readNodesJsonFile()
    [Nodes, Terminals] = parseJsonString(jsonStr)
    allNodes = Terminals + Nodes
    print_gtfs_stops_file(generation, allNodes)
    print_gtfs_shapes_file(generation, allNodes)

# to create a GTFS format 
# https://developers.google.com/transit/gtfs/examples/gtfs-feed?hl=pt-br
# http://gtfs.org/best-practices/
       
# create a file stops.txt (save bus stops and its infos)
# must have points_ID, points_lat, points_lon at least
def print_gtfs_stops_file(generation, allNodes):
    stops = open("data/stops.txt","w")
    stops.write("stop_id,\"stop_name\",\"stop_desc\",stop_lat,stop_lon,stop_url,location_type,parent_station\n")
    for a_node in allNodes:
        id, name, latlon = a_node.getIdx(), a_node.getLabel(), a_node.getLatLong()
        prtname = "\"%s\"" % name
        string = (str(id)+","+prtname+","+","+str(latlon[0])+","+str(latlon[1])+","+","+","+"\n")
        stops.writelines(string)
    stops.close()

# create a file shapes.txt (save bus lines and its infos)
# must have points_ID, points_lat, points_lon at least
def print_gtfs_shapes_file(generation, allNodes):
    routeIndex = 0
    shapes = open('data/shapes.txt', 'w')
    shapes.write("shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled\n")
    for individual in generation:
        routeList = individual.getGenes()
        for rt in routeList:
            nodeList = rt.getNodes()
            routeIndex+=1
            nodeSeq, distAcc = 0, 0
            last_node=""
            for i, a_node in enumerate(nodeList):
                # first node doesn't need distance
                if (i != 0):
                    distAcc+= last_node.getDistanceOfNode(a_node)
                    # last node doesn't have neighbor ahead
                    if ( i < len(nodeList) ):
                        nll = last_node.getNeighborsLatLong(a_node) #neighbor_latlon_list
                        for j in range (0, len(nll), 2):
                            nodeSeq+=1
                            string=(str(routeIndex)+","+str(nll[j])+","+str(nll[j+1])+","+str(nodeSeq)+","+"\n")
                            shapes.writelines(string)
                latlon = a_node.getLatLong()
                nodeSeq+=1
                string=(str(routeIndex)+","+str(latlon[0])+","+str(latlon[1])+","+str(nodeSeq)+","+str(distAcc)+"\n")
                last_node = a_node
                shapes.writelines(string)
    shapes.close()
    

def read_sptrans_files(filename):
    
    f = io.open("data/sptrans_gtfs/"+filename, 'r', encoding='utf-8').readlines()
    matrix, array = [], []
    str = ""
    for ind in f:
        for char in ind:
            if (char == ",") or (char == '\n'):
                array.append(str)
                str = ""
            else: str+=char
        matrix.append(array)
        array = []
    return matrix

def gtfs_sptrans():
    
    mat_stops = read_sptrans_files("stops.txt")
    mat_stoptimes = read_sptrans_files("stop_times.txt")
    mat_trips = read_sptrans_files("trips.txt")
    mat_shapes = read_sptrans_files("shapes.txt")
    
    #lists of interest
    shapes_USP, trips_USP, stoptimes_USP, stops_USP = [], [], [], []
    
    # trips
    trips_USP.append(mat_trips[0])
    for line in mat_trips:
        for col in line:
            if (col == "\"8012-10\"") or (col == "\"8022-10\""):
                trips_USP.append(line)
    
    #shapes
    shapes_USP.append(mat_shapes[0])
    for line in mat_shapes:
        for col in line:
            if (col == trips_USP[1][5]) or (col == trips_USP[2][5]):
                shapes_USP.append(line)

""" test function - read only terms and only nodes

import json
def readTerms():
    with open("terms.txt", "r") as f:
        jsonString = f.read()
        terminals = []
        jsonStruct = json.loads(jsonString)
        for jsonNode in jsonStruct['network']['terminals']:
            terminals.append(node.Node(jsonNode['id'],
                                   jsonNode['label'],
                                   jsonNode['neighbors'],
                                   jsonNode['distance'],
                                   jsonNode['latlong'],
                                   jsonNode['neighbors_latlong']))
        return terminals

import json
def readNos():
    with open("nos.txt", "r") as f:
        jsonString = f.read()
        nodes = []
        jsonStruct = json.loads(jsonString)
        for jsonNode in jsonStruct['network']['nodes']:
            nodes.append(node.Node(jsonNode['id'],
                                   jsonNode['label'],
                                   jsonNode['neighbors'],
                                   jsonNode['distance'],
                                   jsonNode['latlong'],
                                   jsonNode['neighbors_latlong']))
        return nodes
        
"""
# method that reads OD info from .csv file
def parseCsvODFile():
    od_matrix = "data/matriz_od_fake.csv"
    with open(od_matrix, 'rb') as csvfile:
        filereader = csv.reader(csvfile)
        destinations = filereader.next()
        demandMatrix = []
        for row in filereader:
            origin = row[0]
            tam = len(row)
            for i in range(1, tam):
                dest = row[i]
                if dest != "" and dest != "EOT" and dest != "0":
                    demandMatrix.append([int(origin), int(destinations[i]),
                                         int(dest)])
        return demandMatrix
