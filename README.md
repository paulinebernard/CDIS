

Calcul Différentiel, Intégral et Stochastique
================================================================================

Mines ParisTech, cycle ingénieur civil, unité d'enseignement Mathématiques (UE 11).

:books: Documents 
--------------------------------------------------------------------------------


| Chapitre      | # | E-book | Notebook | Quizz | 
| ------------- | ------: | -----------:  |  :----:  | :-----: |
| Topologie | 1 |  |   | [:grey_question: PDF](https://github.com/paulinebernard/CDIS/raw/main/quizz/Topologie/output/Topologie.pdf) |
| Calcul Différentiel | 1 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Calcul%20Différentiel%20I.pdf) |  | [:grey_question: PDF](https://boisgera.github.io/CDIS/quizz/Calcul%20Différentiel%20I/output/Calcul%20Différentiel%20I.pdf) |
|   | 2 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Calcul%20Différentiel%20II.pdf)  | | [:grey_question: PDF](https://boisgera.github.io/CDIS/quizz/Calcul%20Différentiel%20II/output/Calcul%20Différentiel%20II.pdf) |
| |   3 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Calcul%20Différentiel%20III.pdf) |  | [:grey_question: PDF](https://boisgera.github.io/CDIS/quizz/Calcul%20Différentiel%20III/output/Calcul%20Différentiel%20III.pdf) |
| Equations Différentielles | 1 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Equations%20Différentielles%20I.pdf)  |  [:notebook: IPYNB](https://boisgera.github.io/CDIS/Equations%20Différentielles%20I/Equations%20Différentielles%20I.ipynb) | [:grey_question: PDF](https://boisgera.github.io/CDIS/quizz/Equations%20Différentielles%20I/output/Equations%20Différentielles%20I.pdf)
|  | 2 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Equations%20Différentielles%20II.pdf)|  [:notebook: IPYNB](https://boisgera.github.io/CDIS/Equations%20Différentielles%20II/Equations%20Differentielles%20II.ipynb) |  |
| Calcul Intégral | 1 |  |  |   |
|  | 2 |  |   |    |
| | 3 |   |  |  |
| |  4  | |  |  |
| Probabilités | 1 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Probabilité%20I.pdf)  |   | [:grey_question: PDF](https://boisgera.github.io/CDIS/quizz/Probabilités%20I/output/Probabilités%20I.pdf) |
|  | 2 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Probabilité%20II.pdf)  |   | [:grey_question: PDF](https://boisgera.github.io/CDIS/quizz/Probabilités%20II/output/Probabilités%20II.pdf) |
|  | 3 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Probabilité%20III.pdf)  |   |  |
|  | 4 | [:computer: PDF](https://boisgera.github.io/CDIS/output/Probabilité%20IV.pdf)  |   | [:grey_question: PDF](https://cloud.mines-paristech.fr/index.php/s/xBpxCjhLblwLTDR/download) |
|  | 5 | [:computer: PDF](https://cloud.mines-paristech.fr/index.php/s/GLDwtTAMOJCYk3i/download)  |  [:notebook: IPYNB](https://boisgera.github.io/CDIS/Probabilités%20V/Probabilité%20V.ipynb)  |  |
<!--| ... | ... | ... |-->
  


:calendar: Calendrier 2020-2021
--------------------------------------------------------------------------------

  - :calendar: [interface graphique](https://calendar.google.com/calendar/embed?src=coobt3rgshmvkjsfgpeehgucoc%40group.calendar.google.com&ctz=Europe%2FParis)

  - :link: [lien au format iCal](https://calendar.google.com/calendar/ical/coobt3rgshmvkjsfgpeehgucoc%40group.calendar.google.com/public/basic.ics)


:speech_balloon: Forum
--------------------------------------------------------------------------------

  - [Discourse](https://discourse.mines-paristech.fr) (accès : MINES ParisTech)




:pencil: Développeurs & Contributeurs
--------------------------------------------------------------------------------

### Préliminaire

Installez sur votre ordinateur:

  - un client du système de gestion de version [git](https://git-scm.com/), 

  - un terminal [bash](https://www.gnu.org/software/bash/),

  - une distribution [LaTeX](https://www.latex-project.org/),

  - le gestionnaire de paquetages et d'environnements [conda](https://conda.io/en/latest/).

  - optionnellement, pour modifier les sources du document, 
    [Visual Studio Code](https://code.visualstudio.com/).

### Environnement de travail

Conda est particulièrement important puisqu'il est utilisé pour installer
de nombreux autres outils logiciels dont nous avons besoin, comme Python,
Pandoc, etc. Nos besoins supplémentaires sont décrits dans le fichier 
`environment.yml`.
Pour créer un environnement conda qui soit conforme à ces besoins,
exécuter dans le terminal la commande

    $ conda env create -f environment.yml

Quand vous voudrez travaillez sur le projet, activez l'environnement par la
commande

    $ conda activate CDIS

Référence: [Gestion des environnements Conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

### Génération des documents

Exécutez la commande

    $ ./build

Les documents sont générés dans le répertoire `output`.


--------------------------------------------------------------------------------

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Cette œuvre est mise à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.

