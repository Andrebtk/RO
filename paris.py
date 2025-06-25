import folium
from folium.plugins import MarkerCluster
import json
import networkx as nx

from graph import Graph


stations = {}


class Metro:

	def __init__(self, map):

		self.graph =  Graph("metros")

		with open('stations.json') as f:
			metros_json = json.load(f)
			for elem in metros_json['elements']:
				stations[elem["tags"]["name"]] = {
					'name': elem["tags"]["name"],
					'coord': [elem['lat'], elem['lon']],
					'additional': elem
				}
		
		self.lines = {}

		list_ligne_10 = ["Gare d'Austerlitz", "Jussieu", "Cardinal Lemoine", "Maubert - Mutualité", 
							"Cluny-La Sorbonne", "Odéon", "Mabillon", "Sèvres-Babylone", "Vaneau","Duroc", "Ségur",
							"La Motte-Picquet - Grenelle", "Avenue Émile Zola", "Charles Michels", "Javel - André Citroën"]

		self.metro_add(map, stations, list_ligne_10, "ligne 10")
		self.lines["ligne 10"] = list_ligne_10
		
		list_ligne_7 = ["Maison Blanche", "Tolbiac", "Place d'Italie", "Les Gobelins", "Censier - Daubenton", "Place Monge", "Jussieu", "Sully - Morland", "Pont Marie",
								"Châtelet", "Pont Neuf", "Palais Royal - Musée du Louvre", "Pyramides", "Opéra", "Chaussée d'Antin - La Fayette", "Le Peletier", "Cadet", "Poissonnière",
								"Gare de l'Est", "Château Landon", "Louis Blanc", "Stalingrad", "Riquet", "Crimée", "Corentin Cariou", "Porte de la Villette"]

		self.metro_add(map, stations, list_ligne_7, "ligne 7")
		self.lines["ligne 7"] = list_ligne_7
		
		list_ligne_8 = ["Porte de Charenton", "Porte Dorée", "Michel Bizot", "Daumesnil", "Montgallet", "Reuilly — Diderot", "Faidherbe — Chaligny", "Ledru-Rollin", 
								"Bastille", "Chemin Vert", "Saint-Sébastien - Froissart", "Filles du Calvaire", "République", "Strasbourg - Saint-Denis", "Bonne Nouvelle",
								"Grands Boulevards", "Richelieu - Drouot", "Opéra", "Concorde", "Invalides", "La Tour Maubourg", "École Militaire", "La Motte-Picquet - Grenelle",
								"Commerce", "Félix Faure", "Boucicaut", "Lourmel", "Balard"]

		self.metro_add(map, stations, list_ligne_8, "ligne 8")
		self.lines["ligne 8"] = list_ligne_8
		
		list_ligne_1 = ["Porte de Vincennes", "Nation", "Reuilly — Diderot", "Gare de Lyon", "Bastille", "Saint-Paul", "Hôtel de Ville", "Châtelet", "Louvre - Rivoli",
								"Palais Royal - Musée du Louvre", "Tuileries", "Concorde", "Champs-Élysées - Clemenceau", "Franklin D. Roosevelt", "George V", "Charles de Gaulle — Étoile", 
								"Argentine", "Porte Maillot"]

		self.metro_add(map, stations, list_ligne_1, "ligne 1")
		self.lines["ligne 1"] = list_ligne_1


		list_ligne_9 = ["Porte de Montreuil", "Maraîchers", "Buzenval", "Nation", "Rue des Boulets", "Charonne", "Voltaire", "Saint-Ambroise", "Oberkampf",
								"République", "Strasbourg - Saint-Denis", "Bonne Nouvelle", "Grands Boulevards", "Richelieu - Drouot", "Chaussée d'Antin - La Fayette", "Havre - Caumartin",
								"Saint-Augustin", "Miromesnil", "Saint-Philippe du Roule", "Franklin D. Roosevelt", "Alma-Marceau", "Iéna", "Trocadéro", "Rue de la Pompe", "La Muette",
								"Ranelagh", "Michel-Ange - Molitor", "Exelmans", "Porte de Saint-Cloud"]

		self.metro_add(map, stations, list_ligne_9, "ligne 9")
		self.lines["ligne 9"] = list_ligne_9
		

	def metro_add(self, map, metros_json, liste_stations_name, line_name_arg):
		
		last_station_name = ""
		coord=[]
		
		for station_name in liste_stations_name:
			elem = stations[station_name]
			folium.Marker(
				location=elem['coord'],
				tooltip=elem['name'],
				popup=line_name_arg + " - " + elem['name'],
				icon=folium.CustomIcon("metro.png", icon_size=(15, 15)),
			).add_to(map)
			coord.append(elem['coord'])


			list_adj = []
			if last_station_name != "":
				list_adj=[last_station_name]

			# Add to graph
			#Check if connected to another station
			for line_name, list_line in self.lines.items():
				if line_name != line_name_arg and stations[station_name]['name'] in list_line:
					print(stations[station_name]['name'], line_name, line_name_arg)
					list_adj.append(stations[station_name]['name'] + " | " + line_name)

			n = station_name + " | " + line_name_arg

			


			self.graph.add_node(n, list_adj)
			last_station_name=n

		

		folium.PolyLine(
			locations=coord,
			color="#FF0000",
			weight=1,
			tooltip=line_name_arg,
		).add_to(map)


	def plot_graph(self):
		self.graph.plot()


	def shortest_path(self, station1, station2):
		pass