import networkx as nx 
import matplotlib.pyplot as plt
import networkx.drawing
import math

def addToMst(g, v, mstVertices, primKeys):
    mstVertices.add(v)
    for adj_v in g.adj[v].keys():
        primKeys[adj_v] = min(g.edges[v, adj_v]['weight'], primKeys[adj_v])

def minKeyAdjVertex(g, mstVertices, primKeys):
    minKeyNode = None
    minSourceNode = None
    minKey = math.inf

    for v in mstVertices:
        for adj_v in g.adj[v].keys():
            if adj_v not in mstVertices and primKeys[adj_v] < minKey:
                minKey = primKeys[adj_v]
                minKeyNode = adj_v
                minSourceNode = v

    return minSourceNode,minKeyNode


def primsMST(g, start):

    mstVertices = set()
    mst = nx.Graph()

    #initialize the key of all the vertices
    primKeys = {}
    for v in g:
        primKeys[v] = math.inf

    primKeys[start] = 0
    addToMst(g, start, mstVertices, primKeys)
    mst.add_node(start)


    while len(mstVertices) != len(g):
        #Iterate through all the vertices in MSTSet and find the adjacent node with min key
        sv, tv = minKeyAdjVertex(g, mstVertices, primKeys)
        # add the minkeyNode to MST Set
        addToMst(g, tv, mstVertices, primKeys)
        mst.add_node(tv)
        mst.add_edge(sv, tv)

    return mst

if __name__ == "__main__":
    g = nx.Graph()
    g.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8])
    g.add_weighted_edges_from([(0,1,4), (0,7,8), (1,2,8), (1,7,11), (2,8,2), (2,3,7), (2,5,4), (3,5,14), (3,4,9), \
        (4,5,10), (5,6,2), (6,7,1), (6,8,6), (7,8,7), (7,0,8)])

    mst = primsMST(g, 0)
    nx.draw(mst, with_labels=True)
    plt.show()
        

    