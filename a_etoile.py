from heapq import heappop, heappush

def heuristique_de_manhattan(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def voisins(noeud, grille):
    x, y = noeud
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # haut, droite, bas, gauche
    voisins = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]): # Vérifiez que le voisin est dans la grille
            if grille[nx][ny] == 0 or grille[nx][ny] == 3:  # Vérifiez que le voisin est un chemin ou un point d'arrivée
                voisins.append((nx, ny))
                

    return voisins


def a_etoile(depart, arrivee, grille):
    ouvert = [(heuristique_de_manhattan(depart, arrivee), 0, depart)]  # file de priorité (f, g, noeud)
    ferme = set()
    parents = {depart: None}
    g_costs = {depart: 0}  # coûts de déplacement du départ à chaque nœud
    

    while ouvert:
        f, g, noeud_courant = heappop(ouvert)  # retire le nœud avec le plus bas coût f
        ferme.add(noeud_courant)
        print(parents)

        if noeud_courant == arrivee:
            # Trouvé un chemin
            chemin = reconstruire_chemin(parents, arrivee)
            return chemin
        
        for voisin in voisins(noeud_courant, grille):
            if voisin in ferme:
                continue
            
            # Calcul du nouveau coût g pour le voisin
            nouveau_g = g + 1  # coût pour aller du nœud courant au voisin (1 dans ce cas)
            
            if voisin not in g_costs or nouveau_g < g_costs[voisin]:
                g_costs[voisin] = nouveau_g  # mettre à jour le coût g pour le voisin
                nouveau_f = nouveau_g + heuristique_de_manhattan(voisin, arrivee)  # mettre à jour le coût f pour le voisin

                heappush(ouvert, (nouveau_f, nouveau_g, voisin))
                parents[voisin] = noeud_courant
    
    return []  # Retourne un chemin vide si aucun chemin n'est trouvé


def reconstruire_chemin(came_from, current):
    chemin = []
    while current in came_from:
        chemin.append(current)
        current = came_from[current]
        if current is None:  
            break
    return chemin[::-1]  # Inverser pour avoir le chemin du début à la fin

