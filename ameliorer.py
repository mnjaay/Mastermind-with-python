import random


def comparaison(tab1, tab2):
    for i in range(len(tab1)):
        if tab1[i] in tab2:
            for j in range(len(tab2)):
                if tab1[i] == tab2[j]:
                    if i == j:
                        print(f'{i + 1}. Bonne Couleur - Bien Placée')
                    else:
                        print(f'{i + 1}. Bonne Couleur - Mal Placée')
        else:
            print(f'{i + 1}. Mauvaise Couleur')


def comp(tab1, tab2):
    return tab1 == tab2


def main():
    couleurs = ['jaune', 'bleu', 'blanc', 'noir', 'vert', 'orange']
    random.shuffle(couleurs)
    resultat = couleurs[:4]

    nombre_de_tentatives = 10
    nombre_actuel = 1

    while nombre_actuel <= nombre_de_tentatives:
        print(f'Nombre de tentative : {nombre_actuel}')

        while True:
            couleur_input = input(f' Veuillez saisir vos couleurs (ex : rouge, vert, blanc, noir) {nombre_actuel} : ')
            resultat_user = couleur_input.split()
            if len(resultat_user) == 4 and all(couleur in couleurs for couleur in resultat_user):
                break
            else:
                print("Entrée invalide. Assurez-vous de saisir exactement 4 couleurs parmi les suivantes :")
                print(", ".join(couleurs))

        comparaison(resultat_user, resultat)

        if comp(resultat_user, resultat):
            print("Bravo, vous avez gagné!!")
            break

        nombre_actuel += 1

    if nombre_actuel > nombre_de_tentatives:
        print(f'Vous avez épuisé toutes vos tentatives. Le résultat était : {resultat}')


if __name__ == "__main__":
    main()
