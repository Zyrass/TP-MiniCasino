from random import randint
from ..jeux.machine_a_sous import MachineASous
from ..jeux.roulette import Roulette
from ..utilisateurs import User

def espace():
    """Permet simplement de créer un espace."""
    return print()

def separateur(symbole: str = "-", nombre: int = 100):
    """Fonction permettant de générer des symboles (tirets) pour séparer du contenu.

    Args:
        symbole (str, optional): Le symbole utilisé. Par défaut "-".
        nombre (int, optional): La quantité de symboles répétés. Par défaut 100.

    Returns:
        str: Retourne une chaîne de caractères.
    """
    symbole = symbole.strip()
    nombre = int(nombre)
    return print(f" + {symbole * nombre}")

def bienvenue():
    """Crée un message d'accueil."""
    welcome = """ + TP - D33 (PGR) - MINI CASINO"""
    print(welcome)

def initialisation_scores(file_name="score.txt"):
    """Initialise le fichier score.txt.

    Args:
        file_name (str, optional): Nom du fichier, par défaut score.txt.

    Returns:
        dict: Dictionnaire des scores {username: score}.
    """
    scores = {}
    try:
        with open(file_name, "r") as file:
            for line in file.readlines():
                username, score = line.strip().split(";")
                scores[username] = int(score)
    except FileNotFoundError:
        # Le fichier n'existe pas...
        # Création de celui-ci avec des valeurs par défaut:
        #   GRESSIER;999
        #   GUILLON;777
        default_content_file = "GRESSIER;999\nGUILLON;777\n"
        with open(file_name, "w") as file:
            file.write(default_content_file)
            scores = {
                "GRESSIER": 999,
                "GUILLON": 777
            }
    return scores

def nouveau_scores(username: str, score: int, file_name="score.txt"):
    """Ajoute un nouveau score à la suite.

    Args:
        username (str): Le nom de l'utilisateur.
        score (int): Le score de l'utilisateur.
        file_name (str, optional): Nom du fichier, par défaut score.txt.
    """
    # Chargement des scores existants
    scores = initialisation_scores(file_name)
    scores[username] = score

    with open(file_name, "w") as file:
        for username, score in scores.items():
            file.write(f"{username.upper()};{score}\n")

def afficher_menu(player: User):
    while True:
        separateur("-", 35)
        print(" + MENU - MINI CASINO")
        separateur("-", 35)
        print(" + 1. Machine à sous")
        print(" + 2. Roulette")
        separateur("-", 35)
        print(" + Q. Quitter le mini casino")
        separateur("-", 35)

        choix_utilisateur = input(f"\n{player._name.strip().capitalize()}, veuillez saisir un choix: ")
        espace()

        if choix_utilisateur == "1":
            machine = MachineASous()
            machine.run(player)
        elif choix_utilisateur == "2":
            roulette = Roulette()
            roulette.run(player)
        elif choix_utilisateur.lower() == "q":
            # Sauvegarde de la nouvelle valeur du solde du joueur
            scores[player._name] = player._solde
            nouveau_scores(player._name, player._solde)
            break
        else:
            print("\n Désolé, ce choix est invalide, veuillez réessayer.\n")
            espace()

def check_machine_a_sous(player: User):
    results = [randint(1,6) for _ in range(3)]
    print(f" Résultats : {results}")
    print(f" {player._name.capitalize()}, il te reste actuellement: {player._solde}€")
    
    if results[0] == results[1] == results[2]:
        print(" Félicitations, vous avez gagné 500€")
        player.increment_solde(500)
    else:
        print(" Désolé, vous avez perdu. Essayez encore !")
