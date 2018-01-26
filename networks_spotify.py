import networkx as nx
import matplotlib.pyplot as plt 

G = nx.read_edgelist('/Users/andrescarvallo/Desktop/recsys_spotify/spotify_song_graph.csv', delimiter=';')

#print(nx.info(G))

#print(nx.number_of_nodes(G))
#print(nx.number_of_edges(G))

nx.draw_spring(G)
plt.show()