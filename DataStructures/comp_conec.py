import config as cf
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime




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