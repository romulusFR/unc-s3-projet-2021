Projet de programmation 2021 à l'UNC
====================================

Description de la séance #01 du 15/02/21.

Objectif
--------

* installer l'environnement de travail collaboratif
* raffiner le CdC en posant des questions

Travail à faire
---------------

### Briser la glace

### Préparation de l'environnement

* constituer les binômes
* créer, si ce n'est pas déjà fait, un compte <https://github.com/>
* créer un projet **privé** nommé `unc-s3-projet-2021`
  - donner les droits au binôme et à <https://github.com/romulusFR>
  - cloner le projet sur vos postes
  - (optionnel) ajouter le présent projet en upstream pour faire "fork privé"
* installer [VScode](https://code.visualstudio.com/) ou [VSCodium](https://vscodium.com/)

### Raffinement des spécifications

* dessiner une esquisse _wireframe_ des différents écrans web
* pour chacun donner son URL

### Outillage qualité

* pour chacun des outils suivants, expliquer en une ligne ce qu'il fait
  - <https://pdoc3.github.io/pdoc/>
  - <https://www.pylint.org/>
  - <https://github.com/psf/black>
  - <https://coverage.readthedocs.io/>
  - <https://flake8.pycqa.org/>
  - <https://github.com/google/yapf>
  - <https://pdoc3.github.io/pdoc/>
  - <https://docs.pytest.org/>
  - <https://docs.python.org/3/library/pydoc.html>
  - <https://docs.python.org/3/library/unittest.html>
* regroupper les outils précédents en catégories

Notes en séance
---------------

### Discussion

* Ouverture d'un serveur Discord ?

### Démonstration

En guise de conclusion, la version _finale attendue_ que le client voudrait.

Annexes
-------

### Création du fork privé

Procédure expliquée ici <https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274>, voir [duplicating a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository) sur la documentation officielle.

```bash
git clone --bare  git@github.com:romulusFR/unc-s3-projet-2021.git
cd unc-s3-projet-2021.git/
git push --mirror git@github.com:romulusFR/unc-s3-projet-2021-fork.git
cd ..
rm unc-s3-projet-2021.git/

git clone git@github.com:romulusFR/unc-s3-projet-2021-fork.git
```
