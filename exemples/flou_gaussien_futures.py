import cv2
import numpy as np
import time
import concurrent.futures

# Fonction pour appliquer le filtre de flou gaussien à une partie de l'image
def flou_gaussien_partiel(image, debut, fin):
    resultat_partiel = cv2.GaussianBlur(image[debut:fin], (5, 5), 0)
    return debut, resultat_partiel

# Fonction principale
if __name__ == "__main__":
    # Charger l'image
    image = cv2.imread("image.jpg")

    # Diviser l'image en parties pour le traitement parallèle
    nb_partitions = 12
    taille_partition = image.shape[0] // nb_partitions
    partitions = [(i * taille_partition, (i + 1) * taille_partition) for i in range(nb_partitions)]

    # Début du chronomètre
    debut_chrono = time.time()

    # Créer un pool de threads pour exécuter les tâches en parallèle
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Appliquer le filtre de flou gaussien à chaque partition de l'image en parallèle
        resultats = [executor.submit(flou_gaussien_partiel, image, debut, fin) for debut, fin in partitions]

        # Récupérer les résultats une fois terminés
        for futur in concurrent.futures.as_completed(resultats):
            debut, resultat_partiel = futur.result()
            image[debut:debut + resultat_partiel.shape[0]] = resultat_partiel

    # Fin du chronomètre
    fin_chrono = time.time()

    # Calcul du temps d'exécution
    temps_execution = fin_chrono - debut_chrono
    print(f"Temps d'exécution : {temps_execution} secondes")

    # Afficher l'image floue résultante
    cv2.imshow("Image floue (parallèle)", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()