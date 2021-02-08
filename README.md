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

### Descriptif de l'UE

*Objectifs* : entretenir et approfondir les acquis en programmation autour d'un projet.
Réalisation d’une application en Python permettant de mettre en pratique et d’approfondir les connaissances d’algorithmique et de programmation de première année sur un projet guidé.
Mise en place de bonnes pratiques de programmation dans un environnement collaboratif (Git).

### Modalités de contrôle de connaissances

L'évaluation sera composée comme suit (les coefficients sont susceptibles de modifications) :

* 20% une démonstration intermédiaire de 5' à 10'
* 50% une démonstration finale de 5' suivie de 10' de questions
* 30% qualité du code et rapport

La démonstration montre l'état d'avancement du projet en mettant en avant les parties fonctionnelles.
Un court rapport complète la remise du code, un modèle est fourni, voir [`RAPPORT.md`](RAPPORT.md).
L'évaluation du code sera en partie automatisée (tests unitaires et exécution de `pylint`).

### Changelog

* 2021-02-06 : version de base du sujet
* 2021-02-09 : reprise des objectifs suite à réalisation correction v0.4

Organisation du projet
----------------------

Le projet consiste en la réalisation d'une petite application web de vote.

### Objectifs pédagogiques détaillés

La réalisation du projet mobilisera les compétences suivantes, par ordre à peu près décroissant d'importance :

* en programmation et algorithmique Python
* en recherche et utilisation de bibliothèques (standards essentiellement)
* en programmation web (HTML, CSS, très peu de JavaScript)
* en interfaces utilisateur
* en bases de données relationnelle

Au delà de la qualité algorithmique, le projet doit mettre en œuvre les bonnes pratiques de la programmation en Python.
La réalisation doit avoir un très haut niveau de qualité, ce qui comprend :

* la gestion du code sur une forge avec [Git](https://git-scm.com/), <https://github.com/> ou <https://gitlab.com/> **obligatoire**,
* la documentation et les commentaires du code, voir <https://docs.python.org/3/library/pydoc.html> ou <https://pdoc3.github.io/pdoc/>,
* le guide de style, dont :
  - les bonnes pratiques de code et le choix des symboles (noms de variables et de fonctions), à vérifier par exemple avec <https://www.pylint.org/>,
  - la mise en forme du code, par exemple avec <https://github.com/psf/black> pour le formattage automatique,
* l'organisation générale du code modulaire, pour la partie Flask notamment

Vous serez donc amenés à découvrir et utiliser des outils de l’écosystème Python qui sont intégré dans [VSCodium](https://vscodium.com/)/[VScode](https://code.visualstudio.com/).

### Jalons / emploi du temps

Emploi du temps _(à finaliser)_.

* [15/02, séance #01](seances/SEANCE_01.md) : introduction, CdC
* [22/02, séance #02](seances/SEANCE_02.md) : mise en place projets, conception
* [01/03, séance #03](seances/SEANCE_03.md)
* [08/03, séance #04](seances/SEANCE_04.md)
* [15/03, séance #05](seances/SEANCE_05.md)
* 22/03, ~~pas de séance~~
* [29/03, séance #06](seances/SEANCE_06.md) : démo intermédiaire
* 05/04, ~~lundi de Pâques / vacances~~
* [12/04, séance #07](seances/SEANCE_07.md)
* [19/04, séance #08](seances/SEANCE_08.md)
* [16/04, séance #09](seances/SEANCE_09.md)
* [03/05, séance #10](seances/SEANCE_10.md)
* 10/05, ~~pas de séance~~
* [17/05, séance #11](seances/SEANCE_11.md)
* [24/05, séance #12](seances/SEANCE_12.md) : démo finale et rendu, **séance double**

Cahier des charges
------------------

Le projet consiste en la réalisation d'une petite application web de vote : deux citations des Simpsons sont présentées à l'utilisateur qui vote pour sa préférée.
Les résultats des duels de citations sont enregistrés et un classement des meilleures citations est calculé à partir des votes.

Le projet est à réaliser en Python 3.8 ou supérieur.

Références
----------

TBD
