import cv2
import numpy as np
import time
import concurrent.futures

# Fonction pour appliquer le filtre de flou gaussien à une partie de l'image
def flou_gaussien_partiel(image, debut, fin):
    resultat_partiel = cv2.GaussianBlur(image[debut:fin], (15, 15), 0)
    return debut, resultat_partiel

# Fonction pour exécuter le traitement parallèle
def traitement_parallele(image, partitions):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        resultats = [executor.submit(flou_gaussien_partiel, image, debut, fin) for debut, fin in partitions]
        for futur in concurrent.futures.as_completed(resultats):
            debut, resultat_partiel = futur.result()
            image[debut:debut + resultat_partiel.shape[0]] = resultat_partiel

# Fonction pour exécuter le traitement séquentiel
def traitement_sequentiel(image, partitions):
    for debut, fin in partitions:
        debut, resultat_partiel = flou_gaussien_partiel(image, debut, fin)
        image[debut:debut + resultat_partiel.shape[0]] = resultat_partiel

# Charger l'image
image = cv2.imread("image.jpg")

# Diviser l'image en parties pour le traitement parallèle
nb_partitions = 8
taille_partition = image.shape[0] // nb_partitions
partitions = [(i * taille_partition, (i + 1) * taille_partition) for i in range(nb_partitions)]

# Mesurer le temps d'exécution pour le traitement parallèle
debut_chrono = time.time()
traitement_parallele(image.copy(), partitions)
temps_execution_parallele = time.time() - debut_chrono

# Mesurer le temps d'exécution pour le traitement séquentiel
debut_chrono = time.time()
traitement_sequentiel(image.copy(), partitions)
temps_execution_sequentiel = time.time() - debut_chrono

print(f"Temps d'exécution (parallèle) : {temps_execution_parallele} secondes")
print(f"Temps d'exécution (séquentiel) : {temps_execution_sequentiel} secondes")