
## Exercice sur la modélisation d'un processus de signature de feuilles de présence
Dans cet exercice, nous allons modéliser le processus de signature de feuilles de présence dans une classe de 22 personnes, disposant de 5 feuilles de présence et de 4 stylos. Chaque personne signe une feuille à la fois et passe ensuite la feuille à son voisin.

### Modélisation par thread :
Nous pouvons modéliser chaque personne, chaque feuille de présence et chaque stylo par des threads. Chaque thread représentera une personne qui signe une feuille de présence.

### Ressources critiques :
Les feuilles de présence sont des ressources critiques car chaque feuille ne peut être signée que par une seule personne à la fois. L'accès concurrent à une même feuille de présence doit être correctement synchronisé pour éviter les conflits.

### Ressources partagées :
Les stylos sont des ressources partagées car ils sont utilisés par différentes personnes pour signer les feuilles de présence. Cependant, chaque personne utilise le stylo puis le passe à son voisin, donc le partage des stylos ne nécessite pas de synchronisation particulière.

### Facteurs limitants :
Les facteurs limitants incluent le nombre de feuilles de présence (5 feuilles) et le nombre de stylos (4 stylos). Le temps nécessaire pour signer une feuille de présence (5 secondes) et pour passer la feuille à un voisin (2 secondes) sont également des facteurs limitants. 

### Temps minimal pour signer les feuilles de présence :
Le temps minimal pour signer toutes les feuilles de présence peut être calculé en additionnant le temps nécessaire pour signer chaque feuille et le temps nécessaire pour passer la feuille à un voisin. Dans ce cas, chaque feuille de présence prend 5 secondes pour être signée et chaque feuille prend 2 secondes pour être passée à un voisin. Par conséquent, le temps minimal pour signer toutes les feuilles de présence est de 35 secondes.
