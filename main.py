#!/usr/bin/env python3

from utilisateur import Utilisateur
from jeux.machine_a_sous import MachineASous
from jeux.roulette import Roulette
from random import randint
from utils.fichier_score import FichierScore
from utils.menu import Menu
from utils.common import *



# PROGRAMME PRINCIPAL
def main():
    fichier_scores: FichierScore = FichierScore("scores", "txt")
    
    print("\n")
    separateur_tirets_x35_avec_decorateur_plus.afficher_separateur()
    print(""" + TP - D33 (PGR) - MINI CASINO""")
    separateur_tirets_x35_avec_decorateur_plus.afficher_separateur()

    nom_joueur = input(" + Veuillez saisir votre nom pour jouer : ").upper()

    scores = {}
    if nom_joueur in scores:
        joueur = Utilisateur(nom_joueur, scores[nom_joueur])
    else:
        joueur = Utilisateur(nom_joueur)
        scores[joueur.get_nom()] = joueur.get_solde()
        fichier_scores.enregistrer_score(joueur, joueur.get_solde())

    # Message d'accueil
    print(f"\nBienvenue {joueur.get_nom()}, votre solde est de {joueur.get_solde()}\n")
    
    menu = Menu()
    print(menu.afficher_menu(joueur))

# INITIALISATION DU PROGRAMME PRINCIPAL
try:
    main()
except UnboundLocalError:
    scores = FichierScore().initialisation_scores()
    main()
