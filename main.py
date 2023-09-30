import pygame
from labyrinthe import generer_labyrinthe, trouver_depart_arrivee
from graphique import initialiser_fenetre, dessiner_labyrinthe, dessiner_joueur, dessiner_chemin
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
fenetre = initialiser_fenetre(LARGEUR, HAUTEUR)

# Variables pour la génération du labyrinthe
labyrinthe = None
adjacents = None
labyrinthe_genere = False

# Boucle principale
execution = True
while execution:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execution = False
        if event.type == pygame.KEYDOWN and labyrinthe_genere:
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

    if not labyrinthe_genere:
        labyrinthe, adjacents = generer_labyrinthe(
            N_LIGNES, N_COLONNES, labyrinthe, adjacents)
        labyrinthe_genere = not bool(adjacents)

        dessiner_labyrinthe(fenetre, labyrinthe,
                            CELLULE_LARGEUR, CELLULE_HAUTEUR)

        # pygame.time.delay(10)

    else:

        # Initialize le joueur et les positions de départ et d'arrivée
        if 'joueur_pos' not in locals():
            depart, arrivee = trouver_depart_arrivee(labyrinthe)
            print(depart, arrivee)
            joueur_pos = j.init_joueur(depart)

        if 'chemin' not in locals():
            chemin = a_etoile(depart, arrivee, labyrinthe)
            print(chemin)

        
        # Dessiner le joueur et le labyrinthe
        dessiner_labyrinthe(fenetre, labyrinthe,
                            CELLULE_LARGEUR, CELLULE_HAUTEUR)

        dessiner_chemin(fenetre, chemin, CELLULE_LARGEUR, CELLULE_HAUTEUR)
        dessiner_joueur(fenetre, joueur_pos, CELLULE_LARGEUR, CELLULE_HAUTEUR)

        coord_texte = f'X: {joueur_pos[0]}, Y: {joueur_pos[1]}'
        texte_surface = ma_police.render(
            coord_texte, True, (0, 0, 0))
        # Position en haut à droite
        fenetre.blit(texte_surface, (LARGEUR - 120, 10))

    pygame.display.update()

pygame.quit()
