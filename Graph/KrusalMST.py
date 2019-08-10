import networkx as nx 
import matplotlib.pyplot as plt
import networkx.drawing

def hasCycle(g):
    cycleFound = False
    try:
        nx.find_cycle(g)
        cycleFound = True
    except nx.NetworkXNoCycle:
        pass

    return cycleFound


def KrusalMST(g):

    mstVertices = set()
    mstEdges = set()
    mst = nx.Graph()

    #Sort all the edges of the graph by increasing weight
    #edges =  [e for e,d in sorted(g.edges.items(), key=lambda x,y:y['weight'])]
    edges = sorted([(e, data['weight']) for e, data in g.edges.items()], key=lambda x:x[1])
    
    while len(mstVertices) != len(g):
        e, w = edges.pop(0)
        v1, v2 = e

        if e in mstEdges:
            continue

        if v1 not in mstVertices:
            mstVertices.add(v1)
            mst.add_node(v1)
        if v2 not in mstVertices:
            mstVertices.add(v2)
            mst.add_node(v2)

        mst.add_edge(v1, v2, weight=w)

        if hasCycle(mst):
            #discard the edge
            mst.remove_edge(v1, v2)
            continue

        mstEdges.add(e)

    return mst


if __name__ == "__main__":
    g = nx.Graph()
    g.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8])
    g.add_weighted_edges_from([(0,1,4), (0,7,8), (1,2,8), (1,7,11), (2,8,2), (2,3,7), (2,5,4), (3,5,14), (3,4,9), \
        (4,5,10), (5,6,2), (6,7,1), (6,8,6), (7,8,7), (7,0,8)])
    mst = KrusalMST(g)
    nx.draw(mst, with_labels=True)
    plt.show()
