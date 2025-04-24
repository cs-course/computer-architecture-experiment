import networkx as nx
import matplotlib.pyplot as plt

from icn_functions import *

# 创建一个包含8个节点的空图
G = nx.Graph()

# 添加8个节点
G.add_nodes_from([n for n in range(16)])

# 将节点分为两部分
part1 = [n for n in range(8)]
part2 = [(n+8) for n in part1]

# 使用互连函数将两部分节点连接
for i in range(len(part1)):
    G.add_edge(part1[i], part2[identity(i)])
#    G.add_edge(part1[i], part2[switch(i, 0)])
#    G.add_edge(part1[i], part2[shuffle_sub(i, 3)])
#    G.add_edge(part1[i], part2[shuffle_sup(i, 2, 3)])
#    G.add_edge(part1[i], part2[butterfly_sub(i, 2)])
#    G.add_edge(part1[i], part2[butterfly_sub(i, 1)])
#    G.add_edge(part1[i], part2[butterfly_sup(i, 1, 3)])

# 绘制二部图
pos = nx.bipartite_layout(G, part1)
nx.draw_networkx_nodes(G, pos, nodelist=part1, node_color='r')
nx.draw_networkx_nodes(G, pos, nodelist=part2, node_color='b')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
plt.axis('off')
plt.show()
