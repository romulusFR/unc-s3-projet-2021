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
* créer un dépôt **privé** nommé `unc-s3-projet-2021`
  - donner les droits au binôme et à <https://github.com/romulusFR>
  - cloner le dépôt sur vos postes
  - (optionnel) ajouter le présent projet en upstream pour faire "fork privé", [voir l'annexe](#création-du-fork-privé).
* installer [VScode](https://code.visualstudio.com/) ou [VSCodium](https://vscodium.com/)

### Raffinement des spécifications

Rémplacé par [la démonstration](#démonstration)

* ~~dessiner une esquisse _wireframe_ des différents écrans web~~
* ~~pour chacun donner son URL~~

### Démonstration

En guise de conclusion, la version _finale attendue_ que le client voudrait, voir [la vidéo YouTube](https://youtu.be/89NNkLoDkfk).

Annexes
-------

### Création du fork privé

Procédure expliquée ici <https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274>, voir [duplicating a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository) sur la documentation officielle.Voir aussi si besoin [le tutorial officiel](https://www.atlassian.com/git/tutorials/syncing/git-fetch).

```bash
# on clone temporairement le dépôt d'origine
git clone --bare  git@github.com:romulusFR/unc-s3-projet-2021.git
cd unc-s3-projet-2021.git/

# ici on créer le nouveau projet PRIVE sur github, "le fork privé"

# on push le projet d'origine sur le fork
git push --mirror git@github.com:romulusFR/unc-s3-projet-2021-fork.git

# on supprime le projet d'origine
cd ..
rm unc-s3-projet-2021.git/

# on peut maintenant récupérer le "fork privé"
git clone git@github.com:romulusFR/unc-s3-projet-2021-fork.git

# on ajoute le dépôt d'origine pour pouvoir suivre ses modifications mais en interdisant les écritures
git remote add upstream git@github.com:romulusFR/unc-s3-projet-2021.git
git remote set-url --push upstream DISABLE

# synthèse avec
git remote -v

# pour télécharger les mise à jour sur le dépôt d'origine et les intégrer
git pull upstream master
```
