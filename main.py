from joueur import Joueur
from utils.fichier_score import FichierScore
from utils.menu import Menu
from utils.separateur import Separateur
from os import system


def main():
    fichier_scores = FichierScore()

    separateur_principal = Separateur("-", 69, "+ ")

    system("clear")
    print()
    separateur_principal.afficher_separateur()
    print("""+ 👨‍🎓 - TP - D33 (PGR) - MINI CASINO""")
    separateur_principal.afficher_separateur()
    print()
    
    nom_joueur = input(
        "🖊️ - Veuillez saisir votre nom pour accéder au mini casino : ").upper()

    system("clear")
    print("\nℹ️  - Rappel des scores :\n")
    scores = fichier_scores.lire_scores()
    fichier_scores.afficher_scores(scores)
    
    if nom_joueur in scores:
        solde_joueur = scores[nom_joueur]
        joueur = Joueur(nom_joueur, solde_joueur)
    else:
        joueur = Joueur(nom_joueur)
        scores[joueur.nom] = joueur.solde
        fichier_scores.enregistrer_nouveau_score(joueur.nom, joueur.solde)

    print(f"\nBienvenue {joueur.nom}, votre solde est de {joueur.solde}€")
    print("Petite précision, le score est lié directement à ton solde actuel.")
    print("Je te souhaite vraiment de gagner un maximum d'argent... mais aussi d'en perdre soyons réaliste 🤪")
    print("🔞 - Le jeu d'argent est dangereux pour la santé, veuillez faire très attention.\n")

    menu = Menu()
    menu.afficher_menu(joueur, fichier_scores)

if __name__ == "__main__":
    main()
