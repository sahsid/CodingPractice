class GraphNode:
    def __init__(self, vertex, key):
        self.vertex = vertex
        self.key = key

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key
    
    def __str__(self):
        return str(self.vertex) + ': ' + str(self.key)

class Graph:
    def __init__(self, is_directed=True):
        self.vertices = set()
        self.adjList = {}
        self.edges = {}
        self.directed = is_directed

    def add_node(self, vertex):
        self.vertices.add(vertex)

    def add_nodes_from(self, arr):
        for item in arr:
            self.add_node(item)

    def _addEdge(self, end1, end2, weight):
        if end1 not in self.adjList:
            self.adjList[end1] = set()
        
        self.adjList[end1].add(end2)     
        self.edges[(end1, end2)] = weight

    def add_edge(self, end1, end2, weight=None):
        if end1 not in self.vertices or end2 not in self.vertices:
            print("Error: One or both of the vertices of this edge is not present in Graph.")
            return       

        self._addEdge(end1, end2, weight) 

        if not self.directed:
            self._addEdge(end2, end1, weight)

        

    def add_edges_from(self, arr):
        for edge in arr:
            if len(edge) == 2:
                e1, e2 = edge
                self.add_edge(e1, e2)
            else:
                e1, e2, w = edge
                self.add_edge(e1, e2, w)

    def delete_node(self, vertex):
        if vertex not in self.vertices:
            print("Error: Vertex not present in this Graph")
        
        #First remove the edges connected to this vertex
        if vertex in self.adjList:
            del self.adjList[vertex]

        for edges in self.adjList.values():
            if vertex in edges:
                edges.remove(vertex)

        edgesToDelete = []
        for edge in self.edges:
            if vertex in edge:
                edgesToDelete.append(edge)

        for e in edgesToDelete:
            del self.edges[e]

        #At the end, remove the vertex
        self.vertices.remove(vertex)

    def _delEdge(self, end1, end2):
        if end1 in self.adjList:
            self.adjList[end1].remove(end2)

        if (end1, end2) in self.edges:
            del self.edges[(end1, end2)]
                
    def delete_edge(self, end1, end2):

        self._delEdge(end1, end2)

        if not self.directed:
            self._delEdge(end2, end1)

    def copy(self):

        g = Graph()
        g.vertices = self.vertices
        g.adjList = self.adjList
        g.edges = self.edges

        return g

    def __str__(self):
        graphStr = ""

        for u, edges in g.adjList.items():
            graphStr += "{} ---> {} \n".format(u, edges)
            
        for edge, w in g.edges.items():
            if w != None:
                graphStr += "{} : {} \n".format(edge, w)
        
        return graphStr

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    g = Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from([(1,2,4), (1,3,8), (2, 5, 10), (3, 5, 2), (4,5,1)])
    print(g)

