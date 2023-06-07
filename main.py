#!/usr/bin/env python3

from utilisateur import Utilisateur
from jeux.machine_a_sous import MachineASous
from jeux.roulette import Roulette
from utils.fichier_score import FichierScore
from utils.menu import Menu
from utils.separateur import Separateur
from os import system



def main():
    fichier_scores: FichierScore = FichierScore("scores", "txt")
    
    print("\n")
    main_separateur: Separateur = Separateur("-", 69, "+ ")
    main_separateur.afficher_separateur()
    print("""+ TP - D33 (PGR) - MINI CASINO""")
    main_separateur.afficher_separateur()

    nom_joueur = input("+ Veuillez saisir votre nom pour accéder au mini casino : ").upper()

    print("\n")
    scores = fichier_scores.initialisation_scores()
    if nom_joueur in scores:
        joueur = Utilisateur(nom_joueur, scores[nom_joueur])
    else:
        joueur = Utilisateur(nom_joueur)
        scores[joueur.get_nom()] = joueur._solde
        fichier_scores.enregistrer_score(joueur, joueur._solde)

    print(f"\nBienvenue {joueur.get_nom()}, votre solde est de {joueur._solde}€")
    print("Petite précision, le score est lié directement à ton solde actuel.\n")
    
    fichier_scores.afficher_scores("scores.txt")
    print()
    
    menu = Menu()
    menu.afficher_menu(joueur)
        
if __name__ == "__main__":
    main()
