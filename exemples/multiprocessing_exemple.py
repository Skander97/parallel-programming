import multiprocessing

# Fonction pour calculer la somme des nombres dans une liste
def calculer_somme(liste, resultat):
    somme = sum(liste)
    resultat.put(somme)

if __name__ == "__main__":
    # Liste de nombres à traiter
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Créer un objet Queue pour stocker le résultat
    resultat = multiprocessing.Queue()

    # Créer et démarrer le processus parallèle
    p = multiprocessing.Process(target=calculer_somme, args=(nombres, resultat))
    p.start()

    # Attendre la fin du processus
    p.join()
    # Récupérer le résultat
    somme = resultat.get()
    print("La somme des nombres est :", somme)