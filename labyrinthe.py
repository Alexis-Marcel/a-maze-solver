import numpy as np
import random

def generer_labyrinthe(lignes, colonnes, labyrinthe=None, adjacents=None):
    if labyrinthe is None:
        # Initialise toutes les cellules comme des murs
        labyrinthe = np.ones((lignes, colonnes), dtype=int)
        
        # Choix aléatoire d'une cellule de départ et la marque comme chemin
        start_x, start_y = random.randint(0, lignes - 1), random.randint(0, colonnes - 1)
        labyrinthe[start_x][start_y] = 0
        
        # Liste des cellules adjacentes
        adjacents = [(start_x, start_y)]

    if adjacents:
        x, y = random.choice(adjacents)
        adjacents.remove((x, y))
        
        voisins = []
        
        for dx, dy in [(0, -2), (2, 0), (0, 2), (-2, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < lignes and 0 <= ny < colonnes:
                if labyrinthe[nx][ny] == 1:
                    voisins.append((nx, ny))
        
        if voisins:
            nx, ny = random.choice(voisins)
            labyrinthe[nx][ny] = 0
            labyrinthe[nx + (x - nx) // 2][ny + (y - ny) // 2] = 0
            adjacents.append((nx, ny))
            adjacents.append((x, y))
            
    return labyrinthe, adjacents



def trouver_depart_arrivee(labyrinthe):
    # Trouver le point de départ en haut à gauche
    for i in range(labyrinthe.shape[0]):
        for j in range(labyrinthe.shape[1]):
            if labyrinthe[i, j] == 0:
                depart = (i, j)
                labyrinthe[i, j] = 2  # Marquer comme départ
                break
        if 'depart' in locals():
            break

    # Trouver le point d'arrivée en bas à droite
    for i in reversed(range(labyrinthe.shape[0])):
        for j in reversed(range(labyrinthe.shape[1])):
            if labyrinthe[i, j] == 0:
                arrivee = (i, j)
                labyrinthe[i, j] = 3  # Marquer comme arrivée
                break
        if 'arrivee' in locals():
            break
    
    return depart, arrivee