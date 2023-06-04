# Gestion des scores (score.txt) - partie 1/2
def initialisation_scores(file_name: str = "score.txt") -> object:
    """Création d'une première méthode pour initialiser le fichier score.txt

    Args:
        file_name (str, optional): Nom du fichier par défaut score.txt

    Returns:
        object: {username;score}
    """
    scores = {}
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file.readlines():
                username, score = line.strip().split(";")
                scores[username] = int(score)
    except FileNotFoundError:
        # Le fichier n'existe pas...
        # Création de celui-ci avec des valeurs par défaut:
        #   GRESSIER;999
        #   GUILLON;777
        default_content_file: str = "GRESSIER;999\nGUILLON;777\n"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(default_content_file)
            scores = {
                "GRESSIER": 999,
                "GUILLON": 777
            }
            
    # test affichage réussi [X]
    # print(scores)
    return scores

# Gestion des scores (score.txt) - partie 2/2
def nouveau_scores(username: str, score: int, file_name: str = "score.txt") -> None:
    """Création d'une seconde méthode pour ajouter à la suite un nouveau score.

    Args:
        username (str): Le nom de l'utilisateur
        score (int): Le score de l'utilisateur
        file_name (str, optional): Nom du fichier par défaut score.txt
    """
    if score >= 0:
        with open(file_name, "a+") as file:
            file.write(f"{username};{score}\n")
