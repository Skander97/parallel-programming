import cv2
import numpy as np
import time
import multiprocessing
import logging

# Configuration des logs
logging.basicConfig(level=logging.DEBUG)

# Fonction pour appliquer le filtre de flou gaussien à une partie de l'image
def flou_gaussien_partiel(image, debut, fin, resultat):
    logging.debug(f"Traitement de la partie de l'image de {debut} à {fin}")
    resultat_partiel = cv2.GaussianBlur(image[debut:fin], (5, 5), 0)
    resultat.put((debut, resultat_partiel))
    logging.debug(f"Traitement de la partie de l'image de {debut} à {fin} terminé")

# Fonction principale
if __name__ == "__main__":
    # Charger l'image
    image = cv2.imread("image.jpg")

    # Diviser l'image en parties pour le traitement parallèle
    nb_partitions = 1
    taille_partition = image.shape[0] // nb_partitions
    partitions = [(i * taille_partition, (i + 1) * taille_partition) for i in range(nb_partitions)]
    logging.debug(f"Partitions de l'image : {partitions}")

    # Créer un objet Queue pour stocker les résultats partiels
    resultat_partiel = multiprocessing.Queue()

    # Créer et démarrer les processus parallèles
    processus = [multiprocessing.Process(target=flou_gaussien_partiel, args=(image, debut, fin, resultat_partiel)) for debut, fin in partitions]
    for p, (debut, fin) in zip(processus, partitions):
        logging.debug(f"Démarrage du processus pour la partie de l'image de {debut} à {fin}")
        p.start()

   # Attendre la fin de tous les processus avec une limite de temps
    for p, (debut, fin) in zip(processus, partitions):
        p.join(timeout=10)  
        if p.is_alive():
            logging.error(f"Le processus pour la partie de l'image de {debut} à {fin} n'a pas pu se terminer dans le délai imparti.")
            p.terminate()  # Forcer l'arrêt du processus si nécessaire
        else:
            logging.debug(f"Le processus pour la partie de l'image de {debut} à {fin} s'est terminé avec succès.")


    # Rassembler les résultats partiels dans une nouvelle image
    image_floue = np.zeros_like(image)
    while not resultat_partiel.empty():
        debut, resultat_partiel = resultat_partiel.get()
        logging.debug(f"Récupération du résultat partiel pour la partie de l'image de {debut} à {debut + resultat_partiel.shape[0]}")
        image_floue[debut:debut + resultat_partiel.shape[0]] = resultat_partiel

    # Afficher l'image floue résultante
    cv2.imshow("Image floue (parallèle)", image_floue)
    cv2.waitKey(0)
    cv2.destroyAllWindows()