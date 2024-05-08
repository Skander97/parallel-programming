# Projet de Traitement d'Images Parallèle

Ce projet vise à démontrer l'efficacité du traitement d'images parallèle en utilisant des threads pour effectuer des opérations de rotation et de détection de contours simultanément sur différentes parties d'une image.

## Objectif

L'objectif principal de ce projet est de comparer les performances du traitement d'images en utilisant des techniques parallèles par rapport à des approches séquentielles. En particulier, nous visons à déterminer si l'utilisation de threads pour traiter différentes parties d'une image simultanément peut entraîner une amélioration significative des performances par rapport à un traitement séquentiel.

## Pourquoi Faire

Le traitement d'images est une tâche intensive en termes de calcul, en particulier lorsqu'il s'agit d'opérations telles que la rotation et la détection de contours. En parallélisant ces opérations et en les exécutant sur plusieurs threads, nous espérons réduire le temps d'exécution total du traitement de l'image. Cela pourrait être particulièrement bénéfique dans des applications où le temps de traitement est critique, telles que le traitement d'images en temps réel dans les applications de vision par ordinateur ou de traitement d'images médicales.

## Ce que Démontrer

Ce projet vise à démontrer plusieurs aspects :

1. **Efficacité du Traitement Parallèle** : Nous voulons montrer que le traitement parallèle des images peut réduire significativement le temps de traitement par rapport à une approche séquentielle, en particulier pour les tâches intensives en calcul telles que la rotation et la détection de contours.

2. **Évolutivité** : Nous voulons également montrer que notre approche parallèle est évolutive, c'est-à-dire qu'elle peut gérer efficacement des images de différentes tailles et des charges de travail variables en répartissant le traitement sur un nombre variable de threads.

## Cas Testés

Le programme est conçu pour diviser une image en plusieurs parties et traiter chaque partie en parallèle. Deux opérations sont effectuées sur chaque partie de l'image :

- Rotation d'Image : Une rotation de 30 degrés est appliquée à chaque partie de l'image.

- Détection de Contours : Les contours sont détectés dans chaque partie de l'image à l'aide de l'algorithme de détection de contours de Canny.

Le temps d'exécution du traitement parallèle est comparé à celui du traitement séquentiel pour évaluer l'efficacité de la parallélisation.
## Exécution

Pour exécuter le programme, assurez-vous d'avoir Python installé sur votre système, ainsi que la bibliothèque OpenCV. Vous pouvez l'installer en utilisant pip :

## Résultats

### Cas 1 : Traitement avec une seule image

Lors de l'exécution du script de transformation géométrique avec une seule image, les résultats suivants ont été obtenus :

- Temps d'exécution (parallèle) : 0.13157129287719727 secondes
- Temps d'exécution (séquentiel) : 0.19551730155944824 secondes

Dans ce cas, la différence de temps entre les deux traitements n'est pas significative, mais le traitement parallèle est légèrement plus rapide que le traitement séquentiel.

### Cas 2 : Traitement avec plusieurs exécutions de la même image

Lors de l'exécution du même script avec la même image mais plusieurs fois, les résultats suivants ont été obtenus :

- Temps d'exécution (parallèle) : 0.3061518669128418 secondes
- Temps d'exécution (séquentiel) : 0.4040093421936035 secondes

Dans ce cas, on observe une différence plus significative entre les temps d'exécution du traitement parallèle et du traitement séquentiel. Le traitement parallèle est plus rapide que le traitement séquentiel, avec une différence d'environ 0.09785747528076172 secondes.
## Auteurs

Ce projet a été développé par :

- Skander LATRACH
- Kelthoum PENOT
- Vincent FABIANO
- Hugo BARBOSA

