#!/usr/bin/env python3

from utilisateur import Utilisateur
from jeux.machine_a_sous import MachineASous
from jeux.roulette import Roulette
from utils.fichier_score import FichierScore
from utils.menu import Menu
from utils.common import creer_separateur_tirets_x35_avec_decorateur_plus
from utils.separateur import Separateur


def main():
    fichier_scores: FichierScore = FichierScore("scores", "txt")
    
    separateur_tirets_x35_avec_decorateur_plus: Separateur = creer_separateur_tirets_x35_avec_decorateur_plus()
    separateur_tirets_x35_avec_decorateur_plus.afficher_separateur()
    print(""" + TP - D33 (PGR) - MINI CASINO""")
    separateur_tirets_x35_avec_decorateur_plus.afficher_separateur()

    nom_joueur = input(" + Veuillez saisir votre nom pour jouer : ").upper()

    scores = fichier_scores.initialisation_scores()
    if nom_joueur in scores:
        joueur = Utilisateur(nom_joueur, scores[nom_joueur])
    else:
        joueur = Utilisateur(nom_joueur)
        scores[joueur.get_nom()] = joueur._solde
        fichier_scores.enregistrer_score(joueur, joueur._solde)

    print(f"\nBienvenue {joueur.get_nom()}, votre solde est de {joueur._solde}\n")
    
    menu = Menu()
    menu.afficher_menu(joueur)

if __name__ == "__main__":
    main()
