import matplotlib.pyplot as plt
import networkx as nx
import networkx.drawing

gh = nx.DiGraph()
gh.add_nodes_from([0, 1, 2, 3])
gh.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3)])

nx.draw(gh, with_labels=True)
plt.show()