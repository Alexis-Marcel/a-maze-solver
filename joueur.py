# Logique pour gérer le joueur dans le labyrinthe
from enum import Enum

class Action(Enum):
    GAUCHE = 1
    DROITE = 2
    HAUT = 3
    BAS = 4
    
def init_joueur(depart):
    return list(depart)
            
def deplacer_joueur(pos, action, labyrinthe):
    
    dx, dy = 0, 0
    if action == Action.GAUCHE:
        dx = -1
    elif action == Action.DROITE:
        dx = 1
    elif action == Action.HAUT:
        dy = -1
    elif action == Action.BAS:
        dy = 1
        
    if cellule_is_valide((pos[0] + dy, pos[1] + dx), labyrinthe):
        return (pos[0] + dy, pos[1] + dx)

    return pos
    

def cellule_is_valide(pos, labyrinthe):
    x, y = pos
    return 0 <= x < len(labyrinthe) and 0 <= y < len(labyrinthe[0]) and labyrinthe[x][y] != 1
