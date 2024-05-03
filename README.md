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

Nous testons notre approche sur plusieurs cas d'utilisation représentatifs, notamment :

1. Images de Tailles Variables : Nous testons notre programme sur des images de différentes tailles pour évaluer sa capacité à gérer des images de grande taille.

2. Charges de Travail Variables : Nous testons le programme avec différentes charges de travail pour évaluer sa capacité à s'adapter à des scénarios où le nombre de parties de l'image à traiter peut varier.

## Exécution

Pour exécuter le programme, assurez-vous d'avoir Python installé sur votre système, ainsi que la bibliothèque OpenCV. Vous pouvez l'installer en utilisant pip :

## Résultats

Le programme affichera les temps d'exécution du traitement parallèle et séquentiel. Les résultats seront comparés pour évaluer l'efficacité de la parallélisation dans le traitement d'images.

## Auteurs

Ce projet a été développé par :

- Skander LATRACH
- Kelthoum PENOT
- Vincent FABIANO
- Hugo BARBOSA

