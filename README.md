Projet de programmation 2021 à l'UNC
====================================

Page de l'EC de "projet de programmation" en L2 informatique à l'Université de la Nouvelle-Calédonie session 2021.

Introduction
------------

* Semestre : 3
* Intitulé de l'EC : Projet de programmation
* Code l'EC : 27_0196
* Enseignant : [Romuald Thion](mailto:romuald.thion@unc.nc)
* Volume total : 18h TP (12 séances de 1h30)
* Créneau : lundi 14h00-15h30 à partir du 15/02
* Page de l'EC : <https://github.com/romulusFR/unc-s3-projet-2021>
* Canal Discord : `#projet-programmation-python` sur le serveur _Licence Informatique (UNC)_

### Descriptif de l'UE

*Objectifs* : entretenir et approfondir les acquis en programmation autour d'un projet.
Réalisation d'une application en Python permettant de mettre en pratique et d'approfondir les connaissances d'algorithmique et de programmation de première année sur un projet guidé.
Mise en place de bonnes pratiques de programmation dans un environnement collaboratif (Git).

### Modalités de contrôle de connaissances

Le projet est à réaliser **en binôme ou seul**.

L'évaluation sera composée comme suit (les coefficients sont susceptibles de modifications) :

* 50% une démonstration intermédiaire de 5' à 10'
* 50% une démonstration finale de 5' suivie de 10' de questions

La démonstration montre l'état d'avancement du projet en mettant en avant les parties fonctionnelles.

### Changelog

* 2021-03-01 : refonte complète: projet libre et plus Flask
* 2021-02-22 : séance 2 et application de départ
* 2021-02-09 : organisation et jalons du projet
* 2021-02-06 : version de base du sujet

Organisation du projet
----------------------

Le projet consiste en la réalisation d'une petite application web de vote.

### Objectifs pédagogiques détaillés

La réalisation du projet mobilisera les compétences suivantes :

* en programmation et algorithmique Python
* en recherche et utilisation de bibliothèques (standards essentiellement)

Tout ou partie des compétences suivantes :

* en programmation web (HTML, CSS, très peu de JavaScript)
* en interfaces utilisateur
* en bases de données relationnelle

Au delà de la qualité algorithmique, _le projet doit mettre en œuvre les bonnes pratiques de la programmation en Python_.
La réalisation doit avoir un très haut niveau de qualité, ce qui comprend :

* la gestion du code sur une forge avec [Git](https://git-scm.com/), <https://github.com/> ou <https://gitlab.com/>
* la documentation et les commentaires du code, voir <https://docs.python.org/3/library/pydoc.html> ou <https://pdoc3.github.io/pdoc/>,
* le guide de style, dont :
  - les bonnes pratiques de code et le choix des symboles (noms de variables et de fonctions), à vérifier par exemple avec <https://www.pylint.org/>,
  - la mise en forme du code, par exemple avec <https://github.com/psf/black> pour le formattage automatique,
* l'organisation générale du code modulaire, pour la partie Flask notamment

Vous serez donc amenés à découvrir et utiliser des outils de l'écosystème Python qui sont tous intégrés dans [VSCodium](https://vscodium.com/)/[VScode](https://code.visualstudio.com/).

### Jalons / emploi du temps

L'organisation générale du projet est la suivante, avec la réalisation progressive de quatre versions, les liens donnent le travail attendu de chaque séance :

* [15/02, séance #01](seances/SEANCE_01.md) : initialisation,
* [22/02, séance #02](seances/SEANCE_02.md) : présentation d'une appli Flask de départ
* 01/03, séance #03 : changement de sujet projet : passage en projet libre
* 08/03, séance #04 : réalisation version 1
* 15/03, séance #05 : réalisation version 1
* 22/03, ~~pas de séance~~
* 29/03, séance #06 : démonstration intermédiaire de la version 1
* 05/04, ~~lundi de Pâques / vacances~~
* [12/04, séance #07 : réalisation version 2
* [19/04, séance #08 : réalisation version 2
* [16/04, séance #09 : réalisation version 2
* [03/05, séance #10 : réalisation version 3
* [10/05, séance #11 : réalisation version 3
* [17/05, séance #12 : démonstration de la version finale

Cahier des charges
------------------

Le projet consiste en la réalisation d'une petite application **de votre choix**, les exemples sont les suivantes

* une petite application web, voir pour cela le [projet Flask de départ](mini-app/app.py),
* un interpréteur pour "le langage des robots" du TD1 de L1,
* un jeu classique en interface texte puis graphique : serpent, memory, pacman etc,
* la reprise d'un sujet de première année à approfondir,
* un petit outil ligne de commande etc.

Références
----------

Quelques références commentées, complétées au fur et à mesure de l'avancement de l'EC

* La documentation officielle <https://docs.python.org/3/index.html> dont les tutoriaux <https://docs.python.org/3/tutorial/> : _la référence officielle_ un peu aride, mais reste la référence officielle.
* The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/> : _très bon complément à la doc officielle, beaucoup plus orienté pratique_
* [Fluent Python](http://shop.oreilly.com/product/0636920032519.do), extraits de code sur <https://github.com/fluentpython> : _une mine d'or pour aller plus loin dans Python_
* Awesome Python : A curated list of awesome Python frameworks, libraries, software and resources. <https://github.com/vinta/awesome-python> : _un peu en vrac, mais beaucoup de bibliothèques tierces de référence_ **important pour le projet**
* Introduction à la programmation Python pour la biologie à Paris Diderot par Patrick Fuchs et Pierre Poulain : _un très bon cours d'introduction, libre, complet et très accessible, en version HTML et PDF_ <https://python.sdv.univ-paris-diderot.fr/>
* Real Python Tutorials  : _des tutoriaux gratuit de généralement bonne ou très bonne qualité_ <https://realpython.com/>
* A Byte of Python : _très bonne référence introductive, traduite en français_ <https://rgilliotte.gitbook.io/byte-of-python/> ([l'originale en englais ici](https://python.swaroopch.com/))
