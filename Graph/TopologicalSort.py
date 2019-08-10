import networkx as nx 
import matplotlib.pyplot as plt
import networkx.drawing

def dfsUtil(g, start, visited, time, depTime, arrTime):
    visited.append(start)
    arrTime[start] = time[0]

    if start in g.adj:
        for v in g.adj[start].keys():
            if v not in visited:
                time[0] += 1
                dfsUtil(g, v, visited, time, depTime, arrTime)

    depTime[start] = time[0]
    time[0] += 1

def topSort(g):
    start = 5
    time = [0]
    depTime = {}
    arrTime = {}
    visited = []

    for start in g:
        if start not in visited:
            dfsUtil(g, start, visited, time, depTime, arrTime)
    
    topSorted = [k for k in sorted(depTime, key=lambda x: depTime[x], reverse=True)]
    return topSorted

if __name__ == "__main__":

    gh = nx.DiGraph()
    gh.add_nodes_from([0, 1, 2, 3, 4, 5])
    gh.add_edges_from([(5, 2), (5, 0), (4, 0), (4, 1), (2,3), (3,1)])

    print(topSort(gh))

    #nx.draw(gh, with_labels=True)
    #plt.show()