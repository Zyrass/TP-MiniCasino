from random import randint
from jeux.roulette import Roulette
from user import User
from jeux.machine_a_sous import MachineASous
from .common import espace, séparateur

def bienvenue():
    """Création d'un message d'accueil"""
    welcome: str = """ + TP - D33 (PGR) - MINI CASINO"""
    return print(welcome)

def initialisation_scores(file_name="score.txt"):
    """Création d'une première méthode pour initialiser le fichier score.txt

    Args:
        file_name (str, optional): Nom du fichier par défaut score.txt

    Returns:
        dict: {username: score}
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
    """Création d'une seconde méthode pour ajouter à la suite un nouveau score.

    Args:
        username (str): Le nom de l'utilisateur
        score (int): Le score de l'utilisateur
        file_name (str, optional): Nom du fichier par défaut score.txt
    """
    # Chargement des scores existants
    scores = initialisation_scores(file_name)
    scores[username] = score

    with open(file_name, "w") as file:
        for username, score in scores.items():
            file.write(f"{username.upper()};{score}\n")

def afficher_menu(player: User):
    while True:
        séparateur("-", 35)
        print(" + MENU - MINI CASINO")
        séparateur("-", 35)
        print(" + 1. Machine à sous")
        print(" + 2. Roulette")
        séparateur("-", 35)
        print(" + Q. Quitter le mini casino")
        séparateur("-", 35)

        choix_utilisateur: str = input(f"\n{player._name.strip().capitalize()}, veuillez saisir un choix: ")
        espace()

        if choix_utilisateur == "1":
            machine = MachineASous()
            machine.run(player)
        elif choix_utilisateur == "2":
            roulette = Roulette()
            roulette.run(player)
        elif choix_utilisateur.lower() == "q":
            break
        else:
            print("\n Désolé, ce choix est invalide, veuillez réessayer.\n")
            espace()

def check_machine_a_sous(player: User):
    results = [randint(1,6) for _ in range(3)]
    print(f" Résultats : {results}")
    print(f" {player._name.capitalize()}, il te reste actuellement: {player._solde}€")
    
    if results[0] == results[1] == results[2]:
        print(" Félicitation vous avez gagné 500€")
        player.increment_solde(500)
    else:
        print(" Désolé, vous avez perdu. Essayez encore !")
