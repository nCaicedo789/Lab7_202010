"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    rgraph = g.newGraph(111353,compareByKey)
    prime = 111353 * 2
    catalog = {'delayGraph':rgraph, 'visitedMap':None}
    catalog['visitedMap'] = map.newMap(capacity=prime, maptype='PROBING',comparefunction=compareByKey)
    return catalog




def addReviewNode (catalog, row):
    """
    Adiciona un nodo para almacenar un libro o usuario 
    """
    if not g.containsVertex(catalog['delayGraph'], row['SOURCE']):
        g.insertVertex (catalog['delayGraph'], row['SOURCE'])
    if not g.containsVertex(catalog['delayGraph'], row['DEST']):
        g.insertVertex (catalog['delayGraph'], row['DEST'])

def addReviewEdge (catalog, row):
    """
    Adiciona un enlace para almacenar una revisión
    """
    g.addEdge (catalog['delayGraph'], row['SOURCE'], row['DEST'], row['ARRIVAL_DELAY'])


def countNodesEdges (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de revisiones
    """
    nodes = g.numVertex(catalog['delayGraph'])
    edges = g.numEdges(catalog['delayGraph'])

    return nodes,edges

def depth_first_search(catalog,node):
    valor={'nodo':node, 'stado':True, 'predecesor':None}
    map.put(catalog['visitedMap'],valor['nodo'],valor)
    list_ad=g.adjacents(catalog['delayGraph'],node)
    for i in range (1,lt.size(list_ad)+1):
        li_node=lt.getElement(list_ad,i)
        if not map.contains(catalog['visitedMap'],li_node):
            record={'nodo':li_node, 'stado':True, 'predecesor':node}
            map.put(catalog['visitedMap'],record['nodo'],record)
            depth_first_search(catalog,li_node)
            

def countConnectedComponents (catalog):
    """
    Retorna la cantidad de componentes conectados del grafo de revisiones
    """
    counter=0
    list_nodes=g.vertices(catalog['delayGraph'])
    for i in range(1,lt.size(list_nodes)+1):
        node=lt.getElement(list_nodes,i)
        if not map.contains(catalog['visitedMap'],node):
            depth_first_search(catalog,node)
            counter+=1
    return counter




# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

