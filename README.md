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

## Résultats

### Cas 1 : Traitement avec une seule image

Lors de l'exécution du script de transformation géométrique avec une seule image, les résultats suivants ont été obtenus :

- Temps d'exécution (parallèle) : 0.13157129287719727 secondes
- Temps d'exécution (séquentiel) : 0.19551730155944824 secondes

Dans ce cas, la différence de temps entre les deux traitements n'est pas significative, mais le traitement parallèle est légèrement plus rapide que le traitement séquentiel.

Dans ce cas, le traitement parallèle peut offrir des avantages en termes de vitesse d'exécution, car les différentes parties de l'image peuvent être traitées simultanément par différents threads.
Cependant, les gains de performance peuvent être limités si la taille de l'image est petite ou si le traitement est relativement rapide, car il y a un certain surcoût lié à la gestion des threads.
La comparaison des temps d'exécution montre que le traitement parallèle peut être légèrement plus lent dans ce cas en raison du surcoût lié à la parallélisation.

### Cas 2 : Traitement avec plusieurs exécutions de la même image

Lors de l'exécution du même script avec la même image mais plusieurs fois, les résultats suivants ont été obtenus :

- Temps d'exécution (parallèle) : 0.3061518669128418 secondes
- Temps d'exécution (séquentiel) : 0.4040093421936035 secondes

Dans ce cas, on observe une différence plus significative entre les temps d'exécution du traitement parallèle et du traitement séquentiel. Le traitement parallèle est plus rapide que le traitement séquentiel, avec une différence d'environ 0.09785747528076172 secondes.

Lorsque plusieurs images différentes sont traitées de manière séquentielle, le traitement parallèle peut encore offrir des avantages en termes de vitesse, car chaque image peut être traitée simultanément par un thread distinct.
Cependant, si les images sont de tailles différentes ou nécessitent des quantités variables de travail, il peut y avoir des déséquilibres de charge entre les threads, ce qui peut entraîner une utilisation inefficace des ressources de calcul.
Dans ce cas, le temps d'exécution parallèle peut être comparable ou légèrement plus lent que le traitement séquentiel en raison des déséquilibres de charge ou du surcoût lié à la gestion des threads.


### Cas 3 : Traitement avec plusieurs images différentes 

Lors de l'exécution du même script avec les différents images les résultats suivants ont été obtenus :

-  Temps d'exécution (parallèle) : 0.5613892078399658 secondes
-  Temps d'exécution (séquentiel) : 0.40071266174316406

Dans ce cas, on observe une différence plus significative entre les temps d'exécution du traitement parallèle et du traitement séquentiel. Le traitement parallèle est plus rapide que le traitement séquentiel, avec une différence d'environ 0.09785747528076172 secondes.

Lorsque plusieurs images différentes sont traitées simultanément de manière parallèle, il peut y avoir des opportunités significatives pour l'exploitation du parallélisme, car chaque image peut être traitée indépendamment des autres.
Si les images sont de tailles similaires et nécessitent des quantités similaires de travail, le traitement parallèle peut fournir des gains de performance significatifs en répartissant la charge de travail sur plusieurs threads.
Cependant, si les images sont de tailles très différentes ou nécessitent des quantités variables de travail, il peut y avoir des déséquilibres de charge entre les threads, ce qui peut affecter les performances globales.
Dans ce cas, le temps d'exécution parallèle peut être considérablement plus court que le traitement séquentiel, en particulier lorsque les images sont suffisamment nombreuses et que la charge de travail est équilibrée entre les threads.

## Conclusion

Dans l'ensemble, le traitement parallèle peut offrir des avantages significatifs en termes de vitesse d'exécution lors du traitement de plusieurs images différentes, surtout si les images sont de tailles similaires et nécessitent des quantités similaires de travail. Cependant, il est important de surveiller et de gérer les déséquilibres de charge pour optimiser les performances parallèles.

## Auteurs

Ce projet a été développé par :

- Skander LATRACH
- Kelthoum PENOT
- Vincent FABIANO
- Hugo BARBOSA

