import cv2
import time
import concurrent.futures


# Fonction pour appliquer une transformation géométrique (rotation) à une partie de l'image
def rotation_partielle(image, debut, fin):
    hauteur, largeur = image.shape[:2]
    
    # Vérifier si la taille de la partie de l'image est valide 
    if debut >= fin or debut < 0 or fin > hauteur:
        return debut, None
    
    centre = (largeur // 2, hauteur // 2)
    angle = 30  # Angle de rotation

    rotation_matrix = cv2.getRotationMatrix2D(centre, angle, 1)
    image_rotated = cv2.warpAffine(image[debut:fin], rotation_matrix, (largeur, fin - debut))
    
    # Vérifier si l'image a été correctement transformée
    if image_rotated is None:
        return debut, None

    return debut, image_rotated

# Fonction pour détecter les contours à partir d'une partie de l'image
def detection_contours_partielle(image, debut, fin):
    edges = cv2.Canny(image[debut:fin], 100, 200)  # Détection des contours avec l'algorithme Canny
    return debut, edges

# Fonction pour exécuter le traitement parallèle sur une seule image
def traitement_image_parallele(image, partitions):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        resultats_rotation = [executor.submit(rotation_partielle, image, debut, fin) for debut, fin in partitions]
        resultats_contours = [executor.submit(detection_contours_partielle, image, debut, fin) for debut, fin in partitions]

        for futur_rotation, futur_contours in zip(resultats_rotation, resultats_contours):
            debut, image_rotated = futur_rotation.result()
            _, edges = futur_contours.result()
            edges_single_channel = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            image[debut:debut + image_rotated.shape[0]] = edges_single_channel

# Fonction pour traiter une liste d'images en parallèle
def traitement_images_parallele(images, partitions):
    for image in images:
        traitement_image_parallele(image, partitions)

# Fonction pour exécuter le traitement séquentiel sur une seule image
def traitement_image_sequentiel(image, partitions):
    for debut, fin in partitions:
        debut, image_rotated = rotation_partielle(image, debut, fin)
        _, edges = detection_contours_partielle(image, debut, fin)
        edges_single_channel = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        image[debut:debut + image_rotated.shape[0]] = edges_single_channel

# Fonction pour traiter une liste d'images séquentiellement
def traitement_images_sequentiel(images, partitions):
    for image in images:
        traitement_image_sequentiel(image, partitions)

# Charger une liste d'images
images = [cv2.imread("images/image1.jpg"), cv2.imread("images/image2.jpg"), cv2.imread("images/image2.jpg")]

# Diviser les images en parties pour le traitement
nb_partitions = 12
taille_partition = images[0].shape[0] // nb_partitions
partitions = [(i * taille_partition, (i + 1) * taille_partition) for i in range(nb_partitions)]

# Mesurer le temps d'exécution pour le traitement parallèle des images
debut_chrono = time.time()
traitement_images_parallele(images, partitions)
temps_execution_parallele = time.time() - debut_chrono

# Mesurer le temps d'exécution pour le traitement séquentiel des images
debut_chrono = time.time()
traitement_images_sequentiel(images, partitions)
temps_execution_sequentiel = time.time() - debut_chrono

print(f"Temps d'exécution (parallèle) : {temps_execution_parallele} secondes")
print(f"Temps d'exécution (séquentiel) : {temps_execution_sequentiel} secondes")
