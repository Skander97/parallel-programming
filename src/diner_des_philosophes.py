import threading
import time

class Fourchette:
    def __init__(self, index):
        self.index = index
        self.semaphore = threading.Semaphore(1)  # Sémaphore pour gérer l'accès à la fourchette
        self.is_used = False  # Indicateur pour savoir si la fourchette est utilisée
    
    def prendre(self):
        self.semaphore.acquire()  # Acquérir le sémaphore pour prendre la fourchette
        self.is_used = True  # Marquer la fourchette comme utilisée
    
    def poser(self):
        self.is_used = False  # Marquer la fourchette comme non utilisée
        self.semaphore.release()  # Libérer le sémaphore pour poser la fourchette

class Philosophe(threading.Thread):
    def __init__(self, index, fourchette_gauche, fourchette_droite):
        super().__init__()
        self.index = index
        self.fourchette_gauche = fourchette_gauche
        self.fourchette_droite = fourchette_droite
    
    def run(self):
        while True:
            # Penser
            print(f"Philosophe {self.index} pense.")
            time.sleep(1)
            
            # Prendre les fourchettes
            print(f"Philosophe {self.index} veut prendre les fourchettes.")
            self.fourchette_gauche.prendre()
            print(f"Philosophe {self.index} a pris la fourchette gauche.")
            self.fourchette_droite.prendre()
            print(f"Philosophe {self.index} a pris la fourchette droite.")
            
            # Manger
            print(f"Philosophe {self.index} mange.")
            time.sleep(2)
            
            # Poser les fourchettes
            print(f"Philosophe {self.index} pose les fourchettes.")
            self.fourchette_gauche.poser()
            self.fourchette_droite.poser()
            print(f"Philosophe {self.index} a posé les fourchettes.")

# Créer les fourchettes
nb_philosophes = 5
fourchettes = [Fourchette(i) for i in range(nb_philosophes)]

# Créer les philosophes
philosophes = [Philosophe(i, fourchettes[i], fourchettes[(i + 1) % nb_philosophes]) for i in range(nb_philosophes)]

# Démarrer les threads des philosophes
for philosophe in philosophes:
    philosophe.start()

# Attendre que tous les philosophes aient fini de manger
for philosophe in philosophes:
    philosophe.join()