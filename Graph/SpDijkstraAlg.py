from GraphModule import Graph, GraphNode
from HeapModule import MinHeap
import math

def bfsUtil(g, source):

    distances = {}
    for v in g.vertices:
        distances[v] = math.inf
    distances[source] = 0

    finalized = set()
    graphNodes = {}
    paths = {}
    
    for v in g.vertices:
        graphNodes[v] = GraphNode(v, distances[v])
        paths[v] = [source]
    
    pqVertices = MinHeap(graphNodes.values())

    while pqVertices.len() > 0:
        node = pqVertices.pop()
        u = node.vertex

        if u not in g.adjList:
            break

        for v in g.adjList[u]:
            if v in finalized:
                continue

            if distances[u] + g.edges[(u,v)] < distances[v]:
                distances[v] = distances[u] + g.edges[(u,v)]
                gnode = graphNodes[v]
                gnode.key = distances[v]
                pqVertices.decreaseKey(gnode, gnode)

                path = paths[u]
                newpath = list(path)
                newpath.append(v)
                paths[v] = newpath

        finalized.add(u)

    return distances, paths

def shortestPath(g, source):
    distances, paths = bfsUtil(g, source)

    print("Shortest distance of all vertices:")
    for v in g.vertices:
        print(f"{source} -> {v}: {distances[v]}")

    print("Shortest paths to all vertices:")
    for v in g.vertices:
        print(f"{source} -> {v}: {paths[v]}")

if __name__ == "__main__":
    g = Graph(is_directed=False)
    g.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8])
    g.add_edges_from([(0,1,4), (0,7,8), (1,2,8), (1,7,11), (2,8,2), (2,3,7), (2,5,4), (3,5,14), (3,4,9), \
        (4,5,10), (5,6,2), (6,7,1), (6,8,6), (7,8,7), (7,0,8)])
    shortestPath(g, 0)