from .separateur import Separateur

def creer_separateur_tirets_x100_avec_decorateur_plus() -> Separateur:
    return Separateur("-", 100, " + ")

def creer_separateur_tirets_x35_avec_decorateur_plus() -> Separateur:
    return Separateur("-", 35, " + ")
