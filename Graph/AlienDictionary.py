import networkx as nx 
import matplotlib.pyplot as plt
import networkx.drawing
from TopologicalSort import topSort

def createDAGGraph(sortedDict):
    
    g = nx.DiGraph()
    
    for i in range(0, len(sortedDict) - 1):
        w1 = sortedDict[i]
        w2 = sortedDict[i+1]
        for k in range(min(len(w1), len(w2))):
            if w1[k] != w2[k]:
                g.add_node(w1[k])
                g.add_node(w2[k])
                g.add_edge(w1[k], w2[k])
                break

    return g

def alienCharOrder(sortedDict):

    g = createDAGGraph(sortedDict)
    topSorted = topSort(g)
    print(topSorted)


if __name__ == "__main__":

    alienCharOrder(['baa', 'abcd', 'abca', 'cab', 'cad'])
    alienCharOrder(["caa", "aaa", "aab"])
    
    #nx.draw(g, with_labels=True)
    #plt.show()

            
