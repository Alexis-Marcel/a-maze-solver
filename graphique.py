import pygame

def initialiser_fenetre(LARGEUR, HAUTEUR):
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Labyrinthe")
    return fenetre

def dessiner_labyrinthe(fenetre, labyrinthe, CELLULE_LARGEUR, CELLULE_HAUTEUR):
    for i in range(labyrinthe.shape[0]):
        for j in range(labyrinthe.shape[1]):
            if labyrinthe[i, j] == 1:
                couleur = (128, 128, 128)  # Gris pour les murs
            elif labyrinthe[i, j] == 0:
                couleur = (255, 255, 255) # Blanc pour les chemins
            elif labyrinthe[i, j] == 2:
                couleur = (0, 255, 0)  # Vert pour le point de départ
            elif labyrinthe[i, j] == 3:
                couleur = (255, 0, 0)  # Rouge pour le point d'arrivée
            pygame.draw.rect(fenetre, couleur, (j * CELLULE_LARGEUR, i * CELLULE_HAUTEUR, CELLULE_LARGEUR, CELLULE_HAUTEUR))

def dessiner_joueur(fenetre, pos, CELLULE_LARGEUR, CELLULE_HAUTEUR):
    x, y = pos
    largeur, hauteur = CELLULE_LARGEUR - 2, CELLULE_HAUTEUR - 2
    couleur = (0, 0, 255)  # Bleu pour le joueur
    pygame.draw.rect(fenetre, couleur, (y * CELLULE_LARGEUR + 1, x * CELLULE_HAUTEUR + 1, largeur, hauteur))
  

def dessiner_chemin(fenetre, chemin, CELLULE_LARGEUR, CELLULE_HAUTEUR):
    largeur, hauteur = CELLULE_LARGEUR- 15, CELLULE_HAUTEUR - 15
    couleur = (255, 255, 0)  # Jaune pour le chemin
    for pos in chemin:
        
        pygame.draw.rect(fenetre, couleur, (pos[1] * CELLULE_LARGEUR, pos[0] * CELLULE_HAUTEUR, largeur, hauteur))
