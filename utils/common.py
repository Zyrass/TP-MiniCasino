def espace():
    """Permet de simplement créer un espace"""
    return print()

def séparateur(symbole: str = "-", nombre: int = 100):
    """fonction permettant de générer des symboles (tirets) pour séparer du contenu

    Args:
        symbole (str, optional): Le symbole utilisé. Par défaut "-".
        nombre (int, optional): La quantité de symbole répété. Par défaut 100.

    Returns:
        _type_: Retourne une chaîne de caractères.
    """
    symbole: str = symbole.strip()
    nombre: int = int(nombre)
    return print(f" + {symbole * nombre}")
