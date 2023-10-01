import pygame

def initialiser_fenetre(LARGEUR, HAUTEUR):
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Labyrinthe")
    return fenetre

def dessiner_labyrinthe(fenetre, labyrinthe, CELLULE_LARGEUR, CELLULE_HAUTEUR):
    for i in range(labyrinthe.shape[0]):
        for j in range(labyrinthe.shape[1]):
            if labyrinthe[j, i] == 1:
                couleur = (128, 128, 128)  # Gris pour les murs
            elif labyrinthe[j, i] == 0:
                couleur = (255, 255, 255) # Blanc pour les chemins
            elif labyrinthe[j, i] == 2:
                couleur = (0, 255, 0)  # Vert pour le point de départ
            elif labyrinthe[j, i] == 3:
                couleur = (255, 0, 0)  # Rouge pour le point d'arrivée
            pygame.draw.rect(fenetre, couleur, (i * CELLULE_LARGEUR, j * CELLULE_HAUTEUR, CELLULE_LARGEUR, CELLULE_HAUTEUR))

def dessiner_joueur(fenetre, pos, CELLULE_LARGEUR, CELLULE_HAUTEUR):
    x, y = pos
    largeur, hauteur = CELLULE_LARGEUR - 2, CELLULE_HAUTEUR - 2
    couleur = (0, 0, 255)  # Bleu pour le joueur
    pygame.draw.rect(fenetre, couleur, (x * CELLULE_LARGEUR + 1, y * CELLULE_HAUTEUR + 1, largeur, hauteur))
  

def dessiner_chemin(fenetre, chemin, CELLULE_LARGEUR, CELLULE_HAUTEUR):
    largeur, hauteur = CELLULE_LARGEUR- 15, CELLULE_HAUTEUR - 15
    couleur = (255, 255, 0)  # Jaune pour le chemin
    for i in range(len(chemin)):
        pos = chemin[i]
        next_pos = chemin[i + 1] if i + 1 < len(chemin) else None
        
        if next_pos:
            x, y = pos
            next_x, next_y = next_pos
            if x == next_x:
                pygame.draw.rect(fenetre, couleur, (x * CELLULE_LARGEUR + 7, y * CELLULE_HAUTEUR + 7, largeur, CELLULE_HAUTEUR - 15))
            elif y == next_y:
                pygame.draw.rect(fenetre, couleur, (x * CELLULE_LARGEUR + 7, y * CELLULE_HAUTEUR + 7, CELLULE_LARGEUR - 15, hauteur))
