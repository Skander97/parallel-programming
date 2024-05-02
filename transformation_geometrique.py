import cv2
import numpy as np
import time
import concurrent.futures

# Fonction pour appliquer une transformation géométrique (rotation) à une partie de l'image
def rotation_partielle(image, debut, fin):
    hauteur, largeur = image.shape[:2]
    centre = (largeur // 2, hauteur // 2)
    angle = 30  # Angle de rotation

    rotation_matrix = cv2.getRotationMatrix2D(centre, angle, 1)
    image_rotated = cv2.warpAffine(image[debut:fin], rotation_matrix, (largeur, fin - debut))

    return debut, image_rotated

# Fonction pour détecter les contours à partir d'une partie de l'image
def detection_contours_partielle(image, debut, fin):
    edges = cv2.Canny(image[debut:fin], 100, 200)  # Détection des contours avec l'algorithme Canny
    return debut, edges

# Fonction pour exécuter le traitement parallèle
def traitement_parallele(image, partitions):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        resultats_rotation = [executor.submit(rotation_partielle, image, debut, fin) for debut, fin in partitions]
        resultats_contours = [executor.submit(detection_contours_partielle, image, debut, fin) for debut, fin in partitions]

        for futur_rotation, futur_contours in zip(resultats_rotation, resultats_contours):
            debut, image_rotated = futur_rotation.result()
            _, edges = futur_contours.result()
            edges_single_channel = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            image[debut:debut + image_rotated.shape[0]] = edges_single_channel

# Fonction pour exécuter le traitement séquentiel
def traitement_sequentiel(image, partitions):
    for debut, fin in partitions:
        debut, image_rotated = rotation_partielle(image, debut, fin)
        _, edges = detection_contours_partielle(image, debut, fin)
        edges_single_channel = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        image[debut:debut + image_rotated.shape[0]] = edges_single_channel

# Charger l'image
image = cv2.imread("image.jpg")

# Diviser l'image en parties pour le traitement parallèle
nb_partitions = 12
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
