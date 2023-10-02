import pygame
from labyrinthe import generer_labyrinthe, trouver_depart_arrivee
from graphique import initialiser_fenetre, dessiner_labyrinthe, dessiner_joueur, dessiner_chemin, dessiner_etats, dessiner_bouton, dessiner_labyrinthe_generation
from a_etoile import a_etoile
import joueur as j

# Initialise Pygame
pygame.init()
pygame.font.init()
ma_police = pygame.font.SysFont('Arial', 14)

# Constantes
LARGEUR, HAUTEUR = 500, 500
N_LIGNES, N_COLONNES = 25, 25
CELLULE_LARGEUR, CELLULE_HAUTEUR = LARGEUR // N_LIGNES, HAUTEUR // N_COLONNES

# Initialiser la fenêtre
fenetre = initialiser_fenetre(LARGEUR, HAUTEUR+100)

bouton_labyrinthe = (50, 550, 150, 50)
bouton_a_etoile = (250, 550, 150, 50)

# Variables pour la génération du labyrinthe
labyrinthe = None
joueur_pos = None
depart, arrivee = None, None
chemin = None

# Boucle principale
execution = True
while execution:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execution = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if bouton_labyrinthe[0] <= x <= bouton_labyrinthe[0] + bouton_labyrinthe[2] and bouton_labyrinthe[1] <= y <= bouton_labyrinthe[1] + bouton_labyrinthe[3]:
                chemin = None
                joueur_pos = None
                labyrinthe = None
                labyrinthe, depart, arrivee = generer_labyrinthe(
            N_LIGNES, N_COLONNES,dessiner_labyrinthe_generation, fenetre, CELLULE_LARGEUR, CELLULE_HAUTEUR)
            
            if bouton_a_etoile[0] <= x <= bouton_a_etoile[0] + bouton_a_etoile[2] and bouton_a_etoile[1] <= y <= bouton_a_etoile[1] + bouton_a_etoile[3]:
                if labyrinthe is not None:
                    chemin = a_etoile(depart, arrivee, labyrinthe, dessiner_etats, fenetre, CELLULE_LARGEUR, CELLULE_HAUTEUR)

        if event.type == pygame.KEYDOWN and labyrinthe is not None:
            if event.key == pygame.K_LEFT:
                joueur_pos = j.deplacer_joueur(
                    joueur_pos, j.Action.GAUCHE, labyrinthe)
            elif event.key == pygame.K_RIGHT:
                joueur_pos = j.deplacer_joueur(
                    joueur_pos, j.Action.DROITE, labyrinthe)
            elif event.key == pygame.K_UP:
                joueur_pos = j.deplacer_joueur(
                    joueur_pos, j.Action.HAUT, labyrinthe)
            elif event.key == pygame.K_DOWN:
                joueur_pos = j.deplacer_joueur(
                    joueur_pos, j.Action.BAS, labyrinthe)
                
    dessiner_bouton(fenetre, 'Générer Labyrinthe', *bouton_labyrinthe, (0, 128, 255))
    dessiner_bouton(fenetre, 'Lancer A*', *bouton_a_etoile, (0, 255, 0))

    if labyrinthe is not None:
        # Initialize le joueur et les positions de départ et d'arrivée
        if not joueur_pos:
            joueur_pos = j.init_joueur(depart)
        
        #if chemin:
        #    dessiner_chemin(fenetre, chemin, CELLULE_LARGEUR, CELLULE_HAUTEUR)
        
        dessiner_labyrinthe(fenetre, labyrinthe, CELLULE_LARGEUR, CELLULE_HAUTEUR)
        
        dessiner_joueur(fenetre, joueur_pos, CELLULE_LARGEUR, CELLULE_HAUTEUR)

    pygame.display.update()
   

pygame.quit()
