import networkx as nx
import matplotlib.pyplot as plt


'''
CRIAR GRAFO E ADICIONAR NÓS 
'''
# G = nx.Graph()
# G.add_edge(1,2)
# G.add_edge(2,3, weight=0.9)
# G.add_edge("A", "B")
# G.add_edge("B", "B")
# G.add_node("C")
# G.add_node(print)
# G.add_node("Lícia")



'''
CRIAR NÓS A PARTIR DE UMA LISTA
'''
# edge_list = [(1,2), (2,3), (3,4), (3,5), (4,6), (6,7)]
# G = nx.from_edgelist(edge_list)

# # Ou outra forma
# G = nx.Graph()
# G.add_edges_from(edge_list)

'''MOSTRAR GRAFO'''
# No final sempre mostre gráfico com esses comandos
# Substitua G pelo nome do grafo
nx.draw_spring(G, with_labels=True)
plt.show()