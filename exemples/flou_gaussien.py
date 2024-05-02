import cv2
import numpy as np
import time

# Fonction pour appliquer le filtre de flou gaussien à l'image
def flou_gaussien(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

# Fonction principale
if __name__ == "__main__":
    # Charger l'image
    image = cv2.imread("image.jpg")

    # Calculer le temps d'exécution pour le traitement séquentiel
    debut_sequentiel = time.time()
    image_floue_sequentielle = flou_gaussien(image)
    fin_sequentiel = time.time()
    temps_sequentiel = fin_sequentiel - debut_sequentiel

    # Afficher le temps d'exécution séquentiel
    print("Temps d'exécution séquentiel :", temps_sequentiel, "secondes")

    # Afficher l'image originale et l'image floue
    cv2.imshow("Image originale", image)
    cv2.imshow("Image floue (séquentielle)", image_floue_sequentielle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()