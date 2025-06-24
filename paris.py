import folium
from folium.plugins import MarkerCluster
import json
import networkx as nx


stations = {}

def metro(map):

	with open('stations.json') as f:
		metros_json = json.load(f)
		for elem in metros_json['elements']:
			stations[elem["tags"]["name"]] = {
				'name': elem["tags"]["name"],
				'coord': [elem['lat'], elem['lon']],
				'additional': elem
			}


	liste_stations_name = ["Gare d'Austerlitz", "Jussieu", "Cardinal Lemoine", "Maubert - Mutualité", 
						"Cluny-La Sorbonne", "Odéon", "Mabillon", "Sèvres-Babylone", "Vaneau","Duroc", "Ségur",
						"La Motte-Picquet - Grenelle", "Avenue Émile Zola", "Charles Michels", "Javel - André Citroën"]

	metro_add(map, stations, liste_stations_name, "ligne 10")


	liste_stations_name = ["Maison Blanche", "Tolbiac", "Place d'Italie", "Les Gobelins", "Censier - Daubenton", "Place Monge", "Jussieu", "Sully - Morland", "Pont Marie",
							"Châtelet", "Pont Neuf", "Palais Royal - Musée du Louvre", "Pyramides", "Opéra", "Chaussée d'Antin - La Fayette", "Le Peletier", "Cadet", "Poissonnière",
							"Gare de l'Est", "Château Landon", "Louis Blanc", "Stalingrad", "Riquet", "Crimée", "Corentin Cariou", "Porte de la Villette"]

	metro_add(map, stations, liste_stations_name, "ligne 7")

	liste_stations_name = ["Porte de Charenton", "Porte Dorée", "Michel Bizot", "Daumesnil", "Montgallet", "Reuilly — Diderot", "Faidherbe — Chaligny", "Ledru-Rollin", 
							"Bastille", "Chemin Vert", "Saint-Sébastien - Froissart", "Filles du Calvaire", "République", "Strasbourg - Saint-Denis", "Bonne Nouvelle",
							"Grands Boulevards", "Richelieu - Drouot", "Opéra", "Concorde", "Invalides", "La Tour Maubourg", "École Militaire", "La Motte-Picquet - Grenelle",
							"Commerce", "Félix Faure", "Boucicaut", "Lourmel", "Balard"]

	metro_add(map, stations, liste_stations_name, "ligne 8")

	liste_stations_name = ["Porte de Vincennes", "Nation", "Reuilly — Diderot", "Gare de Lyon", "Bastille", "Saint-Paul", "Hôtel de Ville", "Châtelet", "Louvre - Rivoli",
							"Palais Royal - Musée du Louvre", "Tuileries", "Concorde", "Champs-Élysées - Clemenceau", "Franklin D. Roosevelt", "George V", "Charles de Gaulle — Étoile", 
							"Argentine", "Porte Maillot"]

	metro_add(map, stations, liste_stations_name, "ligne 1")

	liste_stations_name = ["Porte de Montreuil", "Maraîchers", "Buzenval", "Nation", "Rue des Boulets", "Charonne", "Voltaire", "Saint-Ambroise", "Oberkampf",
							"République", "Strasbourg - Saint-Denis", "Bonne Nouvelle", "Grands Boulevards", "Richelieu - Drouot", "Chaussée d'Antin - La Fayette", "Havre - Caumartin",
							"Saint-Augustin", "Miromesnil", "Saint-Philippe du Roule", "Franklin D. Roosevelt", "Alma-Marceau", "Iéna", "Trocadéro", "Rue de la Pompe", "La Muette",
							"Ranelagh", "Michel-Ange - Molitor", "Exelmans", "Porte de Saint-Cloud"]

	metro_add(map, stations, liste_stations_name, "ligne 9")



def metro_add(map, metros_json, liste_stations_name, name):
	
	
	coord=[]
	
	for station_name in liste_stations_name:
		elem = stations[station_name]
		folium.Marker(
			location=elem['coord'],
			tooltip=elem['name'],
			popup=name + " - " + elem['name'],
			icon=folium.CustomIcon("metro.png", icon_size=(15, 15)),
		).add_to(map)
		coord.append(elem['coord'])
	

	folium.PolyLine(
		locations=coord,
		color="#FF0000",
		weight=1,
		tooltip=name,
	).add_to(map)
