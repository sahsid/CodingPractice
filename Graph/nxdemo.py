import networkx as nx 

if __name__ == "__main__":
    g = nx.Graph()
    g.add_nodes_from([1,2,3])
    g.add_weighted_edges_from([(1,2,5), (2,3,7)])
    print(g.edges.data())