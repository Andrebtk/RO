import matplotlib.pyplot as plt
import networkx as nx
import math

from collections import deque

class Graph:
	
	def __init__(self, name):
		self.name = name
		self.list_adjacence = {}


	def add_node(self, name, list):
		#if name not in self.list_adjacence:
		self.list_adjacence[name] = list



	def get(self, station_name):
		return self.list_adjacence[station_name]

	def bfs_shortest_path(self, station_start, station_end):
		station_start_name = station_start.split("|")[0].strip()
		station_start_line = station_start.split("|")[1].strip()

		station_end_name = station_end.split("|")[0].strip()
		station_end_line = station_end.split("|")[1].strip()


		visited = set()
		queue = deque([[station_start]])

		if station_start == station_end:
			return [station_start]

		while queue:
			pass




	def print_graph(self):
		print(self.list_adjacence)

	def plot(self):
		# Build the graph
		G = nx.Graph()
		for name, nbrs in self.list_adjacence.items():
			for nbr in nbrs:
				G.add_edge(name, nbr)

		# Try Graphviz with overlap‐removal & splines
		try:
			A = nx.nx_agraph.to_agraph(G)
			prog = 'sfdp' if len(G) > 200 else 'neato'
			A.layout(prog=prog, args='-Goverlap=prism -Gsplines=true')
			pos = {
				n: tuple(map(float, A.get_node(n).attr['pos'].split(',')))
				for n in G.nodes()
			}
		except Exception:
			k = 1.0 / math.sqrt(len(G))
			pos = nx.spring_layout(G, k=k*2, iterations=200)

		# Dynamic sizing & smaller text
		N = G.number_of_nodes()
		node_size = max(50, 8000 // max(1, N))
		# Now labels are much smaller: between 2 and 12 pts
		font_size = max(2, 12 - int(math.log2(N + 1)))

		plt.figure(figsize=(20, 15))
		nx.draw_networkx_nodes(G, pos,
							node_color='skyblue',
							node_size=node_size,
							alpha=0.8)
		nx.draw_networkx_edges(G, pos,
							edge_color='gray',
							alpha=0.4)
		nx.draw_networkx_labels(G, pos,
								font_size=font_size,
								font_family='sans-serif')

		plt.title(f"Graph: {self.name}", fontsize=font_size + 2)
		plt.axis('off')
		plt.tight_layout()
		plt.show()