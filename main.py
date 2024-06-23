import random

# Liste des couleurs possibles
COULEURS = ['jaune', 'bleu', 'blanc', 'noir', 'vert', 'orange']
NOMBRE_DE_TENTATIVES = 10

# Fonction pour comparer un élément à un autre dans une position donnée
def comparaison(tab1, tab2):
    resultats = []
    for i in range(len(tab1)):
        if tab1[i] in tab2:
            for j in range(len(tab2)):
                if tab1[i] == tab2[j]:
                    if i == j:
                        resultats.append(f'{i + 1}. Bonne Couleur - Bien Placée')
                    else:
                        resultats.append(f'{i + 1}. Bonne Couleur - Mal Placée')
        else:
            resultats.append(f'{i + 1}. Mauvaise couleur')
    return resultats

# Fonction pour vérifier si les deux listes sont identiques
def comp(tab1, tab2):
    return tab1 == tab2

# Fonction pour obtenir les entrées de l'utilisateur
def obtenir_entree_utilisateur():
    while True:
        couleur = input('Veuillez saisir vos couleurs (ex : rouge, vert, blanc, noir) : ')
        resultat_user = couleur.split()
        if len(resultat_user) == 4 and all(c in COULEURS for c in resultat_user):
            return resultat_user
        else:
            print("Entrée invalide. Assurez-vous de saisir quatre couleurs valides séparées par des espaces.")

# Initialisation du jeu
def jouer():
    random.shuffle(COULEURS)
    resultat = COULEURS[:4]
    nombre_de_fois = 1

    while nombre_de_fois <= NOMBRE_DE_TENTATIVES:
        print(f'Nombre de tentative : {nombre_de_fois}')
        resultat_user = obtenir_entree_utilisateur()
        resultats = comparaison(resultat_user, resultat)
        for res in resultats:
            print(res)

        if comp(resultat_user, resultat):
            print("Bravo, vous avez gagné!!")
            break

        nombre_de_fois += 1
        if nombre_de_fois > NOMBRE_DE_TENTATIVES:
            print(f'Vous avez épuisé toutes vos tentatives. Le résultat était : {resultat}')

# Démarrer le jeu
if __name__ == "__main__":
    jouer()
