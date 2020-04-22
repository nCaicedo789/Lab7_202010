import config as cf
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime




def depth_first_search(Graph, Mapa_de_marcar, node):
    valor={'nodo':node, 'stado':True, 'predecesor':None}
    map.put(Mapa_de_marcar,valor['nodo'],valor)
    list_ad=g.adjacents(Graph,node)
    for i in range (1,lt.size(list_ad)+1):
        li_node=lt.getElement(list_ad,i)
        if not map.contains(Mapa_de_marcar,li_node):
            record={'nodo':li_node, 'stado':True, 'predecesor':node}
            map.put(Mapa_de_marcar,record['nodo'],record)
            depth_first_search(Graph, Mapa_de_marcar, li_node)
            

def countConnectedComponents (Graph, Mapa_de_marcar):
    """
    Retorna la cantidad de componentes conectados del grafo de revisiones
    """
    counter=0
    list_nodes=g.vertices(Graph)
    for i in range(1,lt.size(list_nodes)+1):
        node=lt.getElement(list_nodes,i)
        if not map.contains(Mapa_de_marcar, node):
            depth_first_search(Graph, Mapa_de_marcar, node)
            counter+=1
    return counter