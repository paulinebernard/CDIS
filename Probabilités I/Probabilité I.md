% Probabilités I

<!-- LaTeX Macros -->
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\B}{\mathcal{B}}

\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}


# Introduction 

Le but de ce cours est de consolider et compléter les connaissances en théorie des probabilités acquises en CPGE mais surtout de permettre d’acquérir le raisonnement probabiliste. En effet, les probabilités peuvent être vues comme un outil de modélisation de phénomènes qui ont la caractéristique d'être aléatoires. L'aléatoire peut intervenir de différentes manières dans ces phénomènes.

 
 * Dans les cas d'école que sont les jeux de pile ou face ou de lancés de dés, la différence entre les résultats, si l’on réitère l’expérience, peut être liée à l’impulsion initiale communiquée au dé et à d'autres facteurs environnementaux comme le vent, la rugosité de la table, etc. Le hasard intervient du fait de la méconnaissance des conditions initiales, car la pièce ou le dé ont des trajectoires parfaitement définies par la mécanique classique.
 * Dans beaucoup de cas de figure, on fait intervenir l'aléatoire dans la modélisation du fait d'une connaissance incomplète des phénomènes. On parle alors de modélisation de l'incertitude. C'est le cas par exemple en sciences du climat, dont nous discutons ci-dessous.
 * Dans certains domaines, tels la physique quantique, l'aléatoire fait intrinsèquement partie de la théorie.

Elles sont aussi un préalable indispensable pour aborder l'analyse statistique des données et les méthodes d'apprentissage automatique.

En CPGE, les probabilités ont été vues dans le cadre de phénomènes aléatoires qui admettent un nombre au plus dénombrable de résultats possibles. Ce cadre restreint est supposé connu. On pourra se reporter au chapitre 3 du cours de @polygarnier ou aux deux premiers chapitres du cours de @polyponts pour une éventuelle mise à niveau.

## Exemple de la modélisation du climat

Les prédictions de la météo et les projections du climat proviennent généralement de modèle numériques qui simulent les différents processus physiques à l'oeuvre. Les incertitudes dans la construction et l'application de ces modèles sont variées et peuvent être réparties en quatre groupes : les conditions initiales (on ne connaît jamais parfaitement l'ensemble des variables climatiques en tout point du globe), les conditions aux limites (par exemple lorsqu'on travaille à l'échelle d'un continent ou d'un pays), les valeurs des paramètres intervenant dans les modèles (constantes issues d'observations diverses), les incertitudes structurelles enfin qui relèvent des choix de modélisation. Pour tenir compte de ces incertitudes, les climatologues effectuent des ensembles de simulations, où les différentes quantités incertaines sont échantillonnées selon des modèles probabilistes (voir en particulier @tebaldi).

L'incertitude sur les conditions initiales est particulièrement influente aux faibles échelles de temps. La météo est un système chaotique, les prévisions sont extrêmement sensibles aux variations des conditions initiales utilisées pour initialiser les modèles. Ces dernières sont en revanche connues de manière imparfaite. Il est ainsi nécessaire de tenir compte de cette incertitude. Ceci est rendu possible par la modélisation probabiliste. Les conditions aux limites font intervenir des **variables continues** (température, pression, vitesse du vent, etc.), ce qui représente la principale nouveauté par rapport au programme de CPGE, et il est nécessaire de caractériser leurs relations de **dépendance**. Il convient par ailleurs de tenir compte des observations (satellites, station de mesure, ...) en incluant cette information dans la modélisation probabiliste. On parle de **conditionnement** aux données. Il s'agit enfin d'en générer les valeurs via des algorithmes de **simulation stochastique**. La validité de l'approche est assurée par les **théorèmes limites**, qui garantissent la représentativité des ensembles générés.

## Plan du cours

Le cours est organisé en 5 amphis et abordera consécutivement les notions évoquées ci-dessus, à savoir les probabilités définies sur $\R$, les variables et vecteurs aléatoires réels, l'indépendance et le conditionnement de variables aléatoires, l'étude des suites de variables aléatoires et, enfin, les méthodes de simulation stochastique.


## Historique 

Avant que l'étude des probabilités soit considérée comme une science, l'observation du hasard dans les événements naturels a amené les philosophes et les scientifiques à réfléchir sur la notion de liens entre événements, causes et conséquences, et lois de la nature. Les jeux de hasard, les situations météorologiques ou les trajectoires des astres ont fait partie des domaines étudiés. Les explications données sont alors liées au destin, à une colère céleste ou à une présence divine.

Il est communément admis que le début de la science des probabilités se situe au XVIe siècle avec l'analyse de jeux de hasard par Jérôme Cardan et au XVIIe siècle avec les discussions entre Pierre de Fermat et Blaise Pascal au sujet de paradoxes issus de ces jeux, notamment posés par Antoine Gombaud, chevalier de Méré. Cette nouvelle théorie est nommée géométrie aléatoire par le chevalier de Méré en 1654, elle est appelée par la suite calcul conjectural, arithmétique politique et plus communément aujourd'hui théorie des probabilités. Cette théorie, dite des probabilités modernes, est alors étudiée par de nombreux penseurs jusqu'au XIXe siècle : Kepler, Galilée, Leibniz, Huygens, Halley, Buffon, les frères Bernoulli, Moivre, Euler, D'Alembert, Condorcet, Laplace, Fourier. Elle est principalement basée sur les événements discrets et la combinatoire.

Des considérations analytiques ont forcé l'introduction de variables aléatoires continues dans la théorie. Cette idée prend tout son essor dans la théorie moderne des probabilités, dont les fondations ont été posées par Andreï Nikolaevich Kolmogorov. Kolmogorov combina la notion d'univers, introduite par Richard von Mises et la théorie de la mesure pour présenter son système d'axiomes pour la théorie des probabilités en 1933. Très vite, son approche devint la base incontestée des probabilités modernes.

Le XXe siècle voit également le développement de l'application de la théorie des probabilités dans plusieurs sciences.

Avec la mécanique newtonienne, la théorie du champ électromagnétique ou la thermodynamique, la physique classique est la théorie utilisée jusqu'à la fin du XIXe siècle. En 1925, Erwin Schrödinger étudie l'équation qui détermine l'évolution d'une onde au cours du temps : l'équation de Schrödinger. Max Born utilise cette équation pour décrire une collision entre des particules telles que des électrons ou des atomes. Les observations de ces expériences l'amènent à supposer que le module de la fonction d'onde est la probabilité que la particule soit détectée en un point de l'espace. C'est le début d'une nouvelle approche de la physique quantique.

En 1900, Louis Bachelier fut un des premiers mathématiciens à modéliser les variations de prix boursiers grâce à des variables aléatoires. « le marché n'obéit qu'à une seule loi : la loi du hasard ». Bachelier utilise alors le calcul stochastique pour étudier les variations boursières au cours du temps. En 1970, Fischer Black et Myron Scholes reprennent les idées de Bachelier pour modéliser les rendements d'une action.

L'utilisation des probabilités en biologie a pris un essor dans les années 1970, notamment dans l'étude de l'évolution des espèces. La reproduction des individus est modélisée par un choix aléatoire des gènes transmis ainsi que des mutations apparaissant de manière aléatoire sur les individus. L'extinction des espèces ou des gènes est alors étudiée en fonction des effets stochastiques.

De nos jours, l’Ecole française de Probabilités est très active. La première Médaille Fields décernée à un probabiliste a été attribuée à Wendelin Werner en 2006. Les probabilités se développent de plus en plus, alimentées en particulier de manière essentielle par la physique, le développement des réseaux de télécommunications, la finance, la biologie, la médecine... Elles permettent de construire des modèles mathématiques, qui peuvent être validés par les données suivant la théorie statistique, et fournissent également des possibilités d’expérimentations fictives dans de multiples domaines d’applications.


Objectifs d'apprentissage
================================================================================

#### Probabilités des événements

   - connaître les définitions de base des probabilités :

      - \zero  espace fondamental $\Omega$
      - \zero  événement $A \subset \Omega$
      - \one  tribu (de parties) 
      - \one  probabilité
      - \one  propriété presque sûre

   - connaître, savoir démontrer et exploiter les résultats suivants :

      - \one  les propriétés élémentaires d'une probabilité 
      - \one  le théorème de continuité monotone

   - indépendance et conditionnement 

      - \one  connaître la définition de la probabilité conditionnelle
      - \one  connaître et savoir exploiter la formule des probabilités totales
      - \one  connaître et savoir exploiter la formule de Bayes
      - \one  connaître la définition de l'indépendance d'événements

#### Variables aléatoires

   - variables aléatoires réelles

      - \four connaître la définition de la tribu borélienne
      - \four savoir manipuler la notion de tribu engendrée
      - \four savoir que la tribu borélienne est engendrée par les intervalles de la forme $]-\infty, x],~ x\in \R$
      - \one connaître la définition d'une variable aléatoire réelle et de sa loi de probabilité
   
   - loi des variables aléatoires réelles
      
      - \one savoir que la fonction de répartition caractérise la loi d'une variable aléatoire réelle
      - \two connaître les propriétes de base de la fonction de répartition
      - \two savoir calculer la fonction de répartition d'une variable aléatoire

   - densité de probabilité

      - \two connaître la définition d'une densité de probabilité
      - \two connaître la définition d'une variable aléatoire réelle à densité 
      - \three savoir identifier si une variable aléatoire admet une densité


# Probabilités des événements 

## Phénomènes aléatoires et événements

L’objet de la théorie des probabilités est l’analyse mathématique de phénomènes dans lesquels le hasard intervient. Les phénomènes aléatoires résultent d'expériences dont le résultat ne peut être prédit à l'avance et qui **peut** varier si on répète l'expérience dans des conditions identiques. 

Il est aisé de trouver des exemples de tels phénomènes.

### Exemples {.example}

 1. Jeu de Pile ou Face
 2. Lancé de dés
 3. Durée de vie d'une ampoule électrique
 4. Température demain à 12h au sommet de la tour Eiffel 
 5. Évolution de la vitesse d’une molécule dans un gaz raréfié sur un intervalle de temps $[t_1,t_2]$

La théorie des probabilités vise à fournir un modèle mathématique pour décrire ces phénomènes. Elle repose sur trois ingrédients essentiels dont on donne ici les définitions.

### L'espace fondamental {.definition}

Noté habituellement $\Omega$, l'*espace fondamental* (ou encore l'*espace d'état* ou *univers*) contient l'ensemble de tous les résultats possibles d'un phénomène aléatoire. Un résultat possible d'une expérience sera noté $\omega \in \Omega$.

Si on reprend les exemples précédents, on peut facilement définir les univers associés.

### Exemples {.example}

 1. Jeu de Pile ou Face, $\Omega = \{\text{pile}, \text{face}\}$
 2. Lancé de dés,  $\Omega = \{1,2,3,4,5,6\}$
 3. Durée de vie d'une ampoule électrique, $\Omega = [0,+\infty [$ 
 4. Température demain à 12h au sommet de la tour Eiffel (en degrés Kelvin), $\Omega = [0,+\infty [$
 5. Évolution de la vitesse d’une molécule dans un gaz raréfié sur un intervalle de temps $[t_1,t_2]$, $\Omega$ : ensemble des application continues sur $[t_1,t_2]$ à valeurs dans $\R^3$

Cette liste d’exemples montre que l’espace $\Omega$ peut varier énormément dans sa structure, d’une expérience à l’autre. Cela permet de réaliser la richesse de la théorie qu’il faut mettre en place, pour créer un modèle qui englobe tous ces cas. Nous verrons également ultérieurement que le modèle abstrait que nous allons construire permettra de s’affranchir du fait que $\Omega$ décrit précisément tous les résultats possibles de l’expérience.


### Evénement {.definition}
Un *événement* est une propriété qui est vérifiée ou non une fois l'expérience réalisée. On identifie un événement $A$ à un sous-ensemble ou  *partie* de $\Omega$, i.e. $A = \{\omega \in \Omega : A \text{ est vérifiée pour } \omega \}$.

### Exemples {.example}

 1. Jeu de Pile ou Face : $A = \{\text{pile}\}$. 
 2. Lancé de dés :  $A = \{1,3,5\}$.
 3. Durée de vie d'une ampoule électrique : $A = [t_1,t_2] \subset \R_+$.
 4. Température demain à 12h au sommet de la tour Eiffel (en degrés Kelvin) : $A = [T_1,T_2]\cup[T_3,T_4] \subset \R_+$.
 5. Évolution de la vitesse d’une molécule dans un gaz raréfié sur un intervalle de temps $[t_1,t_2] \subset \R_+$ : 
 $A = \{ f \in C([t_1,t_2], \R^3) : \|f-g\|_{\infty} \leq a \}$, où
 $g \in C([t_1,t_2],\R^3)$ et $a \in \R_+$.


Les événements étant des ensembles, les opérations ensemblistes classiques admettent une interprétation probabiliste.

### Correspondance entre opérations logiques et ensemblistes

| Terminologie probabiliste | Terminologie ensembliste | Notation |
|:-:|:-:|:-:|
| événement certain  | ensemble entier  | $\Omega$  |
| événement impossible  |  ensemble vide  | $\varnothing$  |
| événement contraire | complémentaire | $A^c$  |
| événement atomique  |  singleton | $\{\omega\}$  |
| implication | inclusion | $\subset$  |
| et  | intersection  | $\cap$  |
| ou  | réunion | $\cup$ |
| événements incompatibles | ensembles disjoints | $A_1\cap A_2 = \varnothing$  |

On doit maintenant répondre à la question de savoir quels sont les événements dont on va vouloir évaluer la probabilité d'occurence. On va ainsi regrouper les événements en un ensemble $\A$ qui constitue une collection de sous-ensembles de $\Omega$. On va souhaiter en particulier pouvoir combiner des événements au sein de $\A$ par les opérations ensemblistes courantes. 

Ceci conduit à la notion de *tribu de parties* de $\Omega$.

### Tribu {.definition #deftribu}
Une *tribu* (ou *$\sigma$-algèbre*) $\A$ est une collection de sous-ensembles de $\Omega$ tels que :

 1. $\Omega \in \A$,
 2. $A \in \A \Rightarrow A^c \in \A$,
 3. $\forall\, n \in \N, A_n \in \A \Rightarrow \bigcup_n A_n \in \A$.

Le couple $(\Omega, \A)$ est appelé *espace probabilisable*.

### Exemples {.example}
 1. $\A = \{\varnothing,\Omega\}$ est la tribu *grossière* ou *triviale* : c'est la plus petite tribu de $\Omega$.
 2. Dans le cas où $\Omega$ est au plus dénombrable, on choisit systématiquement l'ensemble $\mathcal{P}(\Omega)$ des parties de $\Omega$ dont on vérifie aisément qu'il s'agit d'une tribu ; c'est le cadre étudié en CPGE. On verra plus loin que cette tribu est trop grande dans le cas où $\Omega$ est infini non dénombrable.
 3. Si $\Omega = \R$, on peut le munir de la tribu formée des ensembles mesurables de $\R$, dite *tribu de Lebesgue*.
 4. On verra plus loin qu'il est aisé de définir une tribu sur tout espace topologique.

## Notion de densité de probabilité

Une des nouveautés majeures de ce cours par rapport au programme de CPGE est le cas où l'espace fondamental n'est plus fini ni dénombrable. On va voir ici que les outils développés dans le cours de calcul intégral vont nous permettre de définir une probabilité sur $\R$ muni de la tribu des ensembles mesurables.

Soit $\Omega = \R$ et $f : \Omega \to \R_+$ une fonction intégrable telle que 
$$ \int_\Omega f(x)\, dx =1. $$

Soit $\A$ la collection des ensembles mesurables sur $\Omega$ ;
[les propriétés élémentaires des ensembles mesurables (cf. Calcul Intégral II)](Calcul Intégral II.pdf#pptés-tribu) établissent que $\mathcal{A}$ est une tribu, 
sur laquelle on peut définir

$$ \P(A) = \int_\Omega 1_{A}\, f(x)\, dx = \int_A f(x)\, dx. $$

On vérifie aisément que $\P$ vérifie les 3 propriétés suivantes :

 1. $\forall\, A \in \A$, $\P(A) \in [0,1]$.

 2. $\P(\Omega) = \int_\Omega f(x) dx = 1$.

 3. Si $A_n$ désigne une suite (dénombrable) d'événements **disjoints** de $\A$, on a, en appliquant le [théorème de convergence dominée](Calcul Intégral II.pdf #TCD) à la suite de fonctions $f(x) 1_{\left\{\bigcup_{n=0}^m A_n\right\}}(x) = \sum_{n=0}^m f(x) 1_{A_n}(x)$ ($m \in \N^\ast$), majorée trivialement par $f$ intégrable :
    \begin{align*}
        \P\left(\bigcup_{n\in \N} A_n\right) &= \int_\Omega \lim_{m \to +\infty} 1_{\left\{\bigcup_{n=0}^m A_n\right\}}\, f(x)\, dx\\
                          &= \lim_{m \to +\infty} \int_\Omega \sum_{n=0}^m 1_{A_n}\, f(x)\, dx\\
                          &= \lim_{m \to +\infty} \sum_{n=0}^m \int_\Omega 1_{A_n}\, f(x)\, dx\\
                          &= \lim_{m \to +\infty} \sum_{n=0}^m \P(A_n) \\
                          &= \sum_{n=0}^{+\infty} \P(A_n).                        
    \end{align*}


Ces trois propriétés correspondent aux [axiomes de Kolmogorov](#defproba) qui définissent une probabilité sur un espace probabilisable général. La fonction $f$ est appelée *densité de probabilité*. On verra plus loin que l'on ne peut pas caractériser toutes les probabilités sur $\R$ via cette notion. Celle-ci constitue néanmoins un exemple fondamental que l'on approfondira dans la suite du cours, notamment dans le cadre de l'étude des variables aléatoires.

### Lien avec le cas discret {.remark}

On pourra faire l'analogie entre la densité de probabilité et la loi de probabilité sur un univers discret, dans le sens où elle va "pondérer" les valeurs réelles, en remarquant cependant que :

 * $f(x)$ n'est pas nécessairement inférieure à 1,

 * $\P(\{x\}) = \int_{\{x\}} f(x)\, dx = 0$ et plus généralement, $\P(A) = 0$ si $A$ est négligeable.

## Probabilité

###  Probabilité {.definition #defproba}
Une *probabilité* sur l'espace $(\Omega, \A)$ est une application $\P : \A \rightarrow [0,1]$, telle que :

 1. $\P(\Omega) = 1$,
 2. pour toute suite (dénombrable) $(A_n)_{n\in\N^\star}$ d'éléments de $\A$ **deux à deux disjoints**, on a 
 \begin{equation*}
 \P\left(\bigcup_{n\in\N^\star} A_n\right) = \sum_{n\in\N^\star} \P(A_n).
 \end{equation*}

Le triplet $(\Omega, \A, \P)$ est appelé *espace probabilisé*. La modélisation probabiliste consiste ainsi à décrire une expérience
aléatoire par la donnée d’un espace probabilisé.

La définition suivante est fondamentale en théorie des probabilités. Elle introduit une
notion de “vrai ou faux” qui dépend de la probabilité choisie sur l’espace fondamental.

###  Propriété presque-sûre {.definition}
Soit $(\Omega, \A, \P)$ un espace probabilisé. On dit qu'un événement $A\in\A$ se réalise *$\P$-presque sûrement* (en abrégé $\P$-p.s.) si $\P(A) = 1$. 

###  Propriétés élémentaires {.proposition #elemprop} 
 1. $\forall\, A \in \A$, $\P(A) \in [0,1]$ et $\P(A^c)= 1-\P(A)$.
 2. $\forall\, A,B \in \A$, $A \subset B \Rightarrow \P(A) \leq \P(B)$.
 3. $\forall\, A,B \in \A$, $\P(A \cup B ) = \P(A) + \P(B) - \P(A \cap B)$.
 4. Inégalité de Boole : $\forall\, n \in \N^\ast$, $\forall\, (A_i)_{1 \leq i \leq n} \in \A$, 
 $$\P\left(\bigcup_{i=1}^n A_i\right) \leq \sum_{i=1}^n \P(A_i).$$
 5. Formule de Poincaré : $\forall\, n \in \N^\ast$, $\forall\, (A_i)_{1 \leq i \leq n} \in \A$
 $$ \P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n \P(A_i) - \sum_{1 \leq i < j \leq n} \P(A_i \cap A_j) + \ldots + (-1)^n \P\left(\bigcap_{i=1}^n A_i\right).$$

### Démonstration {.exercise .question .one #propelem}

### Théorème de la continuité monotone {.theorem #continuitemonotone}
Dans le cas d'une suite $(A_n)_{n\in\N^\ast}$ d'éléments de $\A$ croissante, on a 
$$ \P\left(\bigcup_{n\in\N^\ast} A_n\right) = \lim_{n \rightarrow \infty} \P(A_n).$$

### Démonstration {.exercise .question .one #contmon}

### Une définition alternative de la probabilité {.exercise .question .one #altdef}
Soit $(\Omega, \A)$ un espace probabilisable. Supposons que $\P : \A \to [0,1]$ vérifie : 
 
 1. $\P(\Omega) = 1$, 
 2. Pour $A, B \in \A$, tels que $A\cap B = \varnothing$, $\P(A\cup B)= \P(A) + \P(B)$ (additivité),
 3. Pour toute suite $(A_n)_{n\in\N^\ast}$ d'éléments de $\A$ croissante 
    $$\P\left(\bigcup_{n\in\N^\ast} A_n\right) = \lim_{n \rightarrow \infty} \P(A_n).$$

Montrer que $\P$ vérifie la propriété de [$\sigma$-additivité](#defproba).

### Suite décroissante {.remark}
Dans le cas d'une suite décroissante, on a 
$$ \P\left(\bigcap_{n \in \N^\ast} A_n\right) = \lim_{n \rightarrow \infty} \P(A_n).$$

Le second point de la [définition de la probabilité](#defproba) donne la probabilité de la réunion $\cup_n A_n$ en fonction des $\P(A_n)$ lorsque les événements sont deux à deux disjoints. Si ce n'est pas le cas, on a tout de même la majoration suivante :

### Une majoration bien utile {.proposition}
Soit $\P$ une probabilité et soit $(A_n)_{n\in \N^\ast}$ une famille dénombrable d'événements. On a alors
    $$ \P(\cup_n A_n) \leq \sum_{n\in\N^\ast} \P(A_n) $$

### Démonstration {.exercise .question .one #boolinf}


## Probabilité conditionnelle 

La construction d’un modèle probabiliste repose sur l’information connue **a priori** sur l’expérience aléatoire. Ce modèle permet de quantifier les probabilités de réalisation de certains résultats de l’expérience. Il est fondamental de remarquer que si l’information change, les probabilités de réalisation changent. 

### Information a priori {.example}
On cherche pour un lancer de deux dés, la probabilité de l’événement “la somme est supérieure ou égale à 10”.
Elle vaut 1/6 sans information supplémentaire, 1/2 si l’on sait que le résultat d’un des dés est 6, 0 si l’on sait a priori que le résultat d’un des dés est 2. Pour obtenir ces résultats, on a calculé dans chaque cas le rapport du nombre de résultats favorables sur le nombre de cas possibles. Il est ainsi indispensable de bien définir l’espace de probabilité lié à l’expérience munie de l’information a priori. On remarque également que l’information a priori a changé la valeur de la probabilité de l’événement.

L'outil qui va nous permettre d'introduire de l'information est la probabilité conditionnelle dont nous donnons ici la définition.

###  Probabilité conditionnelle {.definition #defprobacond}
Soient $(\Omega, \A, \P)$ un espace probabilisé, $A, B \in \A$ tels que $\P(B)>0$. La *probabilité conditionnelle* de $A$ sachant $B$ est le nombre 
\begin{equation*}
\P(A|B) = \frac{\P(A\cap B)}{\P(B)}.
\end{equation*}

Cela définit une probabilité comme le montre la proposition suivante.

### Conséquences {.proposition}
 1. Soient $(\Omega, \A, \P)$ un espace probabilisé et $B \in \A$ tel que $\P(B)>0$. Alors l’application de $\A$ dans $[0, 1]$ qui à $A$ associe $\P(A|B)$ définit une nouvelle probabilité sur $\Omega$, appelée probabilité conditionnelle sachant $B$.
 2. Si $\P(A) > 0$ et $\P(B) > 0$ , nous avons
$$\P(A|B)\, \P(B) = \P(A \cap B) = \P(B|A)\, \P(A).$$

### Démonstration {.proof}
Il est clair que $0 \leq \P(A|B) \leq 1$. Par ailleurs, les deux propriétés de la [définition de la probabilité](#defproba)
pour $\P(\cdot|B)$ proviennent des mêmes propriétés pour $\P$ et des remarques suivantes :
$\Omega \cap B = B$, et $(\bigcup_{n\in\N^\ast} A_n ) \cap B = \bigcup_{n\in\N^\ast} (A_n \cap B)$. De plus, si $A$ et $C$ sont disjoints, il en est
de même de $A \cap B$ et $C \cap B$. L’assertion 2 est évidente, d'après la définition de la [Probabilité conditionnelle](#defprobacond).

### Formule des probabilités totales {.proposition #formprobatot}

Soit $(B_n)_{n\in\N^\ast}$ une partition finie ou dénombrable d’événements de $\Omega$ (i.e. telle que $\bigcup_{n\in\N^\ast} B_n = \Omega$ et les $B_n$ sont deux-à-deux disjoints), telle que $\P(B_n ) > 0$ pour tout $n\in\N^\ast$. Pour tout $A \in \A$, on a alors
\begin{equation*}
P(A) = \sum_{n\in\N^\ast} P(A \cap B_n ) = \sum_{n\in\N^\ast} P(A|B_n)\, P(B_n).
\end{equation*}

### Démonstration {.proof}
Nous avons $A = \bigcup_{n\in\N^\ast} (A\cap B_n)$. Par hypothèse, les ensembles $(A\cap B_n)$ sont deux-à-deux disjoints et de plus $\P(A\cap B_n) = \P(A|B_n)\,\P(B_n)$. Le résultat découle du deuxième point de la [définition de la probabilité](#defproba). 

### Formule de Bayes {.proposition #bayes}
Selon les mêmes hypothèses que ci-dessus et si $\P(A) > 0$, on a 

\begin{equation*}
\forall\, i \in \{1,\dots,n\},\  \P(B_i | A) = \dfrac{\P(A | B_i)\, \P(B_i)}{\sum_{n\in\N^\ast} \P(A | B_n)\, \P(B_n)}.
\end{equation*}

### Démonstration {.proof}
Le dénominateur vaut $\P(A)$ d'après la [Formule des probabilités totales](#formprobatot). La définition de la [probabilité conditionnelle](#defprobacond) implique :
\begin{equation*}
\P(B_i | A) = \dfrac{\P(A \cap B_i)}{\P(A)} = \dfrac{\P(A | B_i) \P(B_i)}{\P(A)}.
\end{equation*}

### Remarque {.remark}
La formule de Bayes, simple conséquence des axiomes et de la définition de la probabilité conditionnelle, tient une place à part dans le calcul des probabilités en raison de son importance pratique considérable et des controverses auxquelles son application pratique a donné lieu : elle est à la base de toute une branche de la statistique appelée statistique bayésienne.

### Test {.exercise .question .one #test}
Un individu est tiré au hasard dans une population où l’on trouve une proportion $10^{-4}$ de séropositifs. On lui fait passer un test de détection de la
séropositivité. Par ailleurs, des expérimentations antérieures ont permis de savoir que les probabilités d’avoir un résultat positif lors de l’application du test si l’individu est séropositif, ou s’il ne l’est pas, sont respectivement égales à 0,99 (c’est la sensibilité du test) et à 0,001 (0,999 = 1 - 0,001 est la spécificité du test). Sachant que le test donne un résultat positif, quelle est la probabilité pour que l’individu soit effectivement séropositif ?


## Indépendance des événements 
La notion d’indépendance est absolument fondamentale en probabilités et nous verrons
par la suite toutes ses implications dans la modélisation de l’aléatoire.

Intuitivement, deux événements $A$ et $B$ sont indépendants si le fait de savoir que $A$ est
réalisé ne donne aucune information sur la réalisation de $B$ et réciproquement.

Si $B$ est un événement de probabilité strictement positive, $A$ sera dit indépendant de $B$ si
$$\P(A | B) = \frac{\P(A\cap B)}{\P(B)} = \P(A)$$
On remarque que cette formule se symétrise et la notion d’indépendance se définit
finalement comme suit.

###  Indépendance de deux événements {.definition}
Deux événements $A$ et $B$ sont *indépendants* si et seulement si 
\begin{equation*}
\P(A\cap B) = \P(A)\, \P(B).
\end{equation*}

### Remarques {.remark}

 * La probabilité de voir $A$ réalisé ne dépend pas de la réalisation de $B$, et réciproquement.
 * Cette notion est liée au choix de la probabilité $\P$ et n’est pas une notion ensembliste. Cela n’a en particulier rien à voir avec le fait que $A$
    et $B$ soient disjoints ou non.
 * Si $\P(A)>0$ et $\P(B)>0$, alors 
    \begin{equation*}
    \P(A\cap B) = \P(A)\, \P(B) \Leftrightarrow \P(A) = \P(A|B) \Leftrightarrow \P(B) = \P(B|A).
    \end{equation*}

### Proposition {.proposition}
Si les événements $A$ et $B$ sont indépendants, alors il en est de même des couples $(A^c,B)$, $(A,B^c)$ et $(A^c,B^c)$.

### Démonstration {.exercise .question .one #indep}

### Auto-indépendant ?{.exercise .question .one #autoindep}
À quelle condition un événement $A$ est-il indépendant de lui-même ?

### Exemples {.example}

 1. On lance 3 fois un dé. Si $A_i$ est un événement qui ne dépend que du $i^\text{ème}$ lancer, alors $A_1$ , $A_2$ , $A_3$ sont indépendants.
 2. On tire une carte au hasard dans un jeu de 52 cartes. Soit $A$ = \{la carte est une dame\} et $B$ = \{la carte est un coeur\}. 
 Il est facile de voir que $\P(A) = 4/52$ et $\P(B) = 13/52$ et $\P(A \cap B) = \P( \{\text{la carte est la dame de coeur}\} ) = 1/52 = \P(A) \P(B)$.
 Ainsi, les événements $A$ et $B$ sont indépendants pour la probabilité uniforme $\P$.
 3. On suppose maintenant que le jeu de cartes soit trafiqué. Soit $\widetilde{\P}$ la nouvelle probabilité correspondant au tirage de cartes. On suppose également que
    $$ \widetilde{\P}(\{\text{As de trèfle}\} ) = \frac{1}{2}, \,\,\,\,\, \widetilde{\P}(\{\text{autre carte}\}) = \frac{1}{2} \frac{1}{51} = \frac{1}{102},$$
 alors 
    $$\widetilde{\P}(A \cap B) = \frac{1}{102} \neq \widetilde{\P}(A)\widetilde{\P}(B) = \frac{2}{51}\frac{13}{102}.$$
 Les événements $A$ et $B$ ne sont pas indépendants sous la probabilité $\widetilde{\P}$.
 
### Indépendance de $n$ événements {.definition}
$n$ événements $A_1, \dots, A_n$ sont *indépendants* si et seulement si pour toute partie $I \subset \lbrace 1,\dots, n\rbrace$
\begin{equation*}
\P(\cap_{i\in I} A_i) = \prod_{i\in I} \P(A_i).
\end{equation*}

### Remarque {.remark}
 Attention, l'indépendance des évènements deux à deux ne suffit pas pour l'indépendance mutuelle de tous les évènements.

## Remarque : réflexion sur le concept de probabilité 

La théorie mathématiques des probabilités ne dit pas quelle loi de probabilité choisir sur un espace $(\Omega,\A)$ parmi l'infinité de lois possibles. Ce problème qui concerne ceux qui veulent appliquer le calcul des probabilités, renvoie à la nature "physique" du concept de probabilité qui formalise et quantifie le sentiment d'incertitude vis-à-vis d'un événement. Ce problème d'ordre conceptuel oppose deux écoles de pensée, la conception objectiviste et la conception subjectiviste.

Pour les tenants du premier point de vue, la probabilité d'un événement peut être déterminée de manière unique. Dans la vision dite classique, héritée des jeux de hasard, $\Omega$ est fini et on donne à chaque événement élémentaire la même probabilité. Le calcul des probabilités se résume alors à un problème de dénombrement et la probabilité d'un événement est le rapport du nombre de cas favorables sur le nombre de cas possibles. Dans le cas infini, la vision fréquentiste repose sur la loi des grands nombres : si on répète un grand nombre de fois l'expérience, la proportion de fois où un événement sera réalisé va converger vers la probabilité de cet événement. Dans ce cadre, il est impossible de donner une valeur et même un sens à un événement non répétable comme "pleuvra-t-il demain ?". En outre, la répétition à l'infini d'une même expérience étant physiquement irréalisable, la loi des grands nombres étant un résultat qui suppose défini le concept de probabilité, la vision fréquentiste est logiquement intenable.

Dans la conception subjectiviste, la probabilité objective d'un événement n'existe pas et n'est donc pas une grandeur mesurable analogue à la masse d'un corps, par exemple. C'est simplement une mesure d'incertitude qui reflète un degré de croyance pouvant varier avec les circonstances et l'observateur, donc subjective, la seule exigence étant qu'elle satisfasse aux axiomes du calcul des probabilités. Des méthodes ont alors été proposées pour passer d'un simple pré-ordre sur les événements, à une probabilité. Puisque la répétition n'est plus nécessaire, on peut probabiliser des événements non répétables et étendre ainsi le domaine d'application du calcul des probabilités, notamment pour orienter des prises de décisions. On notera que la [formule de Bayes](#bayes) permet d'intégrer facilement de l'information a priori, dans la mesure où celle-ci est probabilisée.

On arrête ici ces quelques remarques sans prendre parti dans une querelle qui dure encore. L'un ou l'autre point de vue sera adopté selon les ouvrages rencontrés. Dans tous les cas, les outils mathématiques développés dans ce cours seront adaptés. On rappelle tout de même que la modélisation probabiliste a prouvé son efficacité dans de nombreuses applications mais que, comme tout modèle, ce n'est qu'une représentation simplificatrice de la réalité et que ses hypothèses doivent être mises à l'épreuve des faits. À ce titre, on citera Georges Matheron qui dans son essai sur la pratique des probabilités Estimer et Choisir (@matheron) écrit fort justement : "Il n'y a pas de probabilités en soi. Il n'y a que des modèles probabilistes".

# Variables aléatoires

En théorie moderne des probabilités, on préfère prendre un point de vue fonctionnel plutôt qu’ensembliste, et utiliser les variables aléatoires plutôt que les événements. Une variable aléatoire est une grandeur qui dépend du résultat de l’expérience. Par exemple,

 * le nombre de 6 obtenus dans un lancer de 3 dés,
 * le nombre d’appels dans un central téléphonique pendant une heure,
 * la distance du point d’atteinte d’une flèche au centre de la cible,
 * la valeur maximale d’un prix d’actif sur un intervalle de temps donné,
 
sont des variables aléatoires.

La définition formelle d'une variable aléatoire fait intervenir des éléments de la théorie de la mesure qui nous font pour l'instant défaut. On s'intéressera dans un premier temps au cas d'une variable réelle dont on donne une définition partielle : 

Soit $\Omega$ l'espace fondamental muni de sa tribu $\A$. Une *variable aléatoire* $X$ est une application de $(\Omega,\A)$ dans un ensemble $E$,
\begin{equation*}
\omega \in \Omega \mapsto X(\omega) \in E
\end{equation*}

En pratique, l’ensemble $E$ pourra être un ensemble fini ou dénombrable ou $\R$ ou $\R^d$ ou encore un espace plus sophistiqué tel que l’ensemble $C(\R_+ , \R^d)$ des fonctions continues de $\R_+$ dans $\R^d$.

### Vocabulaire {.remark}
La terminologie, consacrée par l'usage, peut être trompeuse. Une variable aléatoire n'est pas une variable (au sens de l'analyse) mais une fonction. Cette terminologie est apparentée à la notion de variable en physique ou en sciences humaines où on désigne volontiers par "variable" la valeur prise par une fonction de l'état du système étudié.

L'intérêt principal de travailler avec des variables aléatoires est de pouvoir substituer à l'espace abstrait $\Omega$ des résultats de l'expérience l'espace $E$, mieux connu dans la pratique. Ainsi, grâce à une variable aléatoire $X$, nous pouvons transporter la structure abstraite du modèle probabiliste $(\Omega, \A, \P)$ sur l'espace d'arrivée $E$, en posant pour $B \subset E$
$$\P_X (B) = \P(X^{-1}(B)) = \P(\{\omega, X(\omega)\in B\})$$

Cette formule définit une nouvelle probabilité, notée $\P_X$ et définie sur $E$, qui s'appelle la *loi de la variable* $X$.

### Notation {.remark}
Il est usuel de noter l'ensemble $X^{-1}(B) = \{\omega \in \Omega, X(\omega) \in B\}$ par $\{X \in B\}$, ce qui allège les écritures. On se rappelera néanmoins que cette notation désigne un sous-ensemble de $\Omega$.

Comme $\P(A)$ n'est définie que pour les $A$ de la tribu $\A$, la formule ci-dessus ne permet de définir $\P_X(B)$ que pour les ensembles $B$ tels que $X^{-1}(B) \in \A$, d’où l’importance de la proposition suivante :

### Loi d'une variable aléatoire {.proposition #propva.tribu}

 a) La famille $\E$ des parties $B$ de $E$ telles que $X^{-1}(B) \in \A$ est une tribu de $E$.
 b) L'application $\P_X$ définie pour $B \in \E$ par 
 $$ \P_X (B ) = \P(X^{-1}(B)) $$ 
 définit une probabilité sur le couple $(E,\E)$.

### Démonstration {.proof}
Les 3 propriétés de la [définition d'une tribu](#deftribu) pour $\E$ ainsi que les deux propriétés de la [définition de la probabilité](#defproba) pour $\P_X$ découlent immédiatement des mêmes propriétés pour $\A$ et $\P$, une fois remarquées les propriétés élémentaires suivantes :
\begin{align*}
& X^{-1}(\varnothing) = \varnothing, X^{-1}(E) = \Omega, X^{-1}(B^c) = X^{-1}(B)^c \\
& X^{-1}(\cap_i A_i) = \cap_i X^{-1}(A_i), X^{-1}(\cup_i A_i) = \cup_i X^{-1}(A_i)
\end{align*}

### {.anonymous}

$\P_X$ sera plus facile à caractériser que $\P$ puisque $E$ est un ensemble connu (on pourra en particulier utiliser ses propriétés topologiques) alors que $\Omega$ est un espace abstrait. Les variables que nous rencontrerons dans ce cours seront soit à valeurs dans un ensemble dénombrable, soit à valeurs dans $\R$ ou dans $\R^d$. Nous les appellerons respectivement des variables aléatoires discrètes, réelles ou des vecteurs aléatoires. Leurs lois seront alors des probabilités respectivement sur un ensemble dénombrable, sur $\R$ ou sur $\R^d$. Le cas discret est considéré connu. 

## Variables aléatoires réelles

La [proposition ci-dessus](#propva.tribu) implique que l'ensemble $X^{-1}(B)$ soit un évènement, pour tout $B$ dans $\E$. Dans le cas où $E = \R$, on  a déjà vu que la collection des ensembles mesurables forment une tribu. Cependant, en probabilité, on travaille généralement avec la *tribu des boréliens*, que l'on notera $\B(\R)$, qui est très utile comme on le verra pour identifier les lois de probabilité. Avant de l'introduire, on a toutefois besoin de la notion de tribu engendrée.

### Tribu engendrée {.definition #tribu-engendrée}
Si $C \subset \mathcal{P}(\Omega)$, on appelle tribu engendrée par $C$ la plus petite tribu contenant $C$. Elle existe toujours, car d’une part $\mathcal{P}(\Omega)$ est une tribu contenant $C$, et d’autre part l’intersection d’une famille quelconque de tribus est une tribu. Ainsi, la tribu
engendrée par $C$ est l’intersection de toutes les tribus contenant $C$.

### Tribus engendrées {.example}

- La tribu engendrée par un ensemble $A \subset \Omega$ est ${\varnothing, A, A^c , \Omega}$.
- si $(A_i )_{i \in I}$ est une partition finie ou dénombrable de $\Omega$ (i.e. les $A_i$ sont deux-à-deux disjoints et leur réunion est $\Omega$), la tribu engendrée par $\{A_i , i \in I\}$ est l’ensemble des réunions $B_J = \cup_{i \in J} A_i$, où $J$ décrit la classe de toutes les parties
de I.

### Tribu borélienne sur $\R$ {.definition #bor}
Si $\Omega = \R$, on appelle tribu borélienne, que l'on note $\B(\R)$, la tribu engendrée par la classe des ouverts de $\R$.

À titre d’exercice de maniement des tribus, on donne en détail la démonstration du résultat suivant :

### Définition alternative {.proposition #altbor} 
La tribu borélienne de $\R$ est la tribu engendrée par les intervalles de la forme $] - \infty, a]$ pour $a \in \Q$.

### Démonstration {.proof}
On rappelle que toute tribu est stable par passage au complémentaire, par réunion ou intersection dénombrable.

Soit $C_1$ la classe des intervalles ouverts de $\R$, $C_2$ la classe des intervalles  $] - \infty, a]$ pour $a \in \Q$ et $\B(\R)$ la tribu borélienne.

Tout ouvert $A$ est réunion dénombrable d'intervalles ouverts, en effet, on a $A = \cup_{(q,n)\in B} ]q -\frac{1}{n}, q -\frac{1}{n}[$, où $B$ est l'ensemble (dénombrable) des couples $(q,n)$ avec $q \in \Q$, $n \in \N$ et $]q -\frac{1}{n}, q -\frac{1}{n}[ \in A$. La tribu engendrée par les intervalles ouverts est donc identique à la tribu borélienne par la stabilité par réunion dénombrable et le fait que $C_1 \subset \B(\R)$.

Réciproquement, soit $]x, y[$ un intervalle ouvert de $\R$. Soit $(x_n)_n$ une suite de rationnels décroissant vers $x$ et $(y_n)_n$
une suite de rationnels croissant strictement vers y. On a :
$$ ]x, y[= \bigcup_n (] - \infty, y_n ]\bigcap ] - \infty, x_n ]^c ).$$
Donc $C_1$ et par conséquent $\B(\R)$ sont inclus dans la tribu engendrée par $C_2$. Finalement, comme tout fermé est dans $\B(\R)$ par complémentarité, on a aussi $C_2 \subset \B(\R)$, d’où le résultat.

### {.post}

On peut maintenant définir une variable aléatoire réelle :

### Variable aléatoire réelle {.definition #defvar}
Soit l'espace d'état $\Omega$ muni de la tribu $\A$ des évènements. Une application $X$ de $\Omega$ dans $\R$ est une *variable aléatoire réelle* si $X^{-1}(B) \in \A$ pour tout $B \in \B(\R)$.

### Loi d'une variable aléatoire réelle {.definition #defloivar}
La probabilité $\P_X$, définie sur $(\R,\B(\R))$ par $\P_X (B) = \P(X^{-1}(B))$ pour $B \in \B(\R)$ est appelée *loi de la variable $X$*, ou *distribution* de $X$.

On peut voir $\P_X$ comme une transposition de $\P$ sur $\R$. On a alors le résultat très utile suivant :

### Composition {.proposition #composition}
Si $X_1, \ldots, X_n$ sont des variables aléatoires réelles et si $g$ est une fonction continue de $\R^n$ dans $\R$, alors $Y = g(X_1,\ldots,X_n)$ est une variable aléatoire réelle.

### Démonstration {#proof}

1. On montre d'abord que si $X : \Omega \to \R$ est une application telle que $\forall a \in \R$, $\{\omega ; X(\omega) \leq a \} = X^{-1}(]-\infty,a]) \in \mathcal{A}$, alors $X$ est une variable aléatoire réelle. Soit $\mathcal{R}$, l'ensemble des $B \in \B(\R)$ tels que $X^{-1}(B) \in \mathcal{A}$. $\mathcal{R}$ est une tribu, comme vu plus haut, et $\mathcal{R}$ contient tous les ensembles de la forme $]-\infty,a]$ par [la proposition](#altbor), on a $\mathcal{R} = \B(\R)$.

2. Soit $a \in \R$, on va montrer que $\{Y \leq a\} \in \mathcal{A}$ ou plutôt, de manière équivalente $\{Y >a\} \in \mathcal{A}$.
$g$ étant continue, l'ensemble $A = \{x\in R^n ; g(x)>a\}$ est un ouvert. On peut donc l'écrire comme l'union dénombrable $A = \cup_{i \in \N^\star} A_i$, où les $A_i$ sont des pavés ouverts de la forme $A_i = \prod_{j=1}^n ]x_{ij},y_{ij}[$ et on a :
\begin{align*}
\{Y>a\} &= \{(X_1,\ldots,X_n) \in A\} \\
&= \bigcup_{i \in \N^\star}\{(X_1,\ldots,X_n) \in A_i\} \\
&= \bigcup_{i \in \N^\star}\bigcap_{j=1}^n \{x_{ij} < X_i < y_{ij}\}
\end{align*}
Puisque les $X_i$ sont des variables aléatoires réelles, $\{x_{ij} < X_i < y_{ij}\} \in \mathcal{A}$ et donc $\{Y>a\} \in \mathcal{A}$.


### {.post}
Comme application de ce résultat, on a les propriétés suivantes :

### Conséquences {.proposition}

Soient $X$, $Y$ et $(X_n)_{n \in \N^\star}$ des variables aléatoires réelles. On a 

 1. $X + Y$, $XY$, $\frac{X}{Y}$ si $Y \neq 0$, sont des variables aléatoires.
 
 2. $\sup_{1\leq p \leq n} X_p$, $\inf_{1\leq p \leq n} X_p$, sont des variables aléatoires.

 3. $\sup_{n\geq 1} X_n$, $\inf_{n\geq 1} X_n$, sont des variables aléatoires.
        
 4. Si $X_n(\omega) \xrightarrow[n \to \infty]{} Z(\omega)$, $\forall \omega$, alors la limite $Z$ est une variable aléatoire.

 5. $Z = 1_A$ est une variable aléatoire $\Leftrightarrow$ $A \in \A$.


## Loi des variables aléatoires réelles

Nous avons vu précédemment la définition générale d'une probabilité $\P$ sur un espace quelconque $\Omega$ muni d'une tribu $\A$. Un problème fondamental est de construire et de caractériser ces probabilités. La résolution de ce problème lorsque $\Omega$ est fini ou dénombrable est connu.
Le cas général est décrit dans le cadre de la théorie de la mesure et sera évoqué ultérieurement.

Puisque les variables aléatoires réelles sont définies sur $\R$, nous allons étudier leur loi de probabilité $\P_X$ définie sur $\R$ muni de la tribu $\B(\R)$.

###  Fonction de répartition {.definition #deffdr}
Soit $X$ une variable aléatoire réelle et $\P_X$ sa loi.
La *fonction de répartition* de $X$ est la fonction
\begin{equation*}
F_X(x) = \P_X(\left]-\infty, x\right]) = \P(X \leq x),\ x \in \R.
\end{equation*}

### La fonction de répartition caractérise la probabilité {.theorem #carac}
La fonction de répartition $F$ caractérise la probabilité $\P_X$ sur ($\R,\B(\R)$).

### Démonstration {.proof}

D'après [la définition de la fonction de répartition](#deffdr), on a $\P_X(]x,y]) = F(y)-F(x)$ pour tous $x< y$. Par conséquent, si $B = \cup_{i=1}^n ]x_i,y_i]$, avec $x_i < y_i < x_{i+1}$, on a 
$$\P_X(B) = \sum_{i=1}^n \P_X(]x_i,y_i]) = \sum_{i=1}^n F(y_i)-F(x_i),$$
car les intervalles sont disjoints. Puisque $\P_X(]x,+ \infty[) = 1-F(x)$, nous en déduisons finalement que $F$ caractérise la restriction de $\P_X$ à l'ensemble de toutes les réunions finies d'intervalles disjoints de la forme $]x,y]$ ou $]x,+ \infty[$. Cet ensemble contient $\R$, $\varnothing$ et est stable par passage au complémentaire et par réunion finie (on dit que c'est une algèbre). Un résultat difficile de théorie de la mesure (voir @Jacod pour une preuve) montre que la connaissance de $\P_X$ sur cette algèbre suffit à déterminer entièrement $\P_X$ sur la tribu engendrée par cette algèbre. Mais [la proposition vu précédemment](#altbor) nous indique que cette tribu est la tribu borélienne.

### Caractérisation de la fonction de répartition {.theorem #theofdr}
Une fonction $F$ est la fonction de répartition d'une unique probabilité $\P_X$ sur $(\R,\B(\R))$ si et seulement si elle vérifie les trois conditions suivantes :

 1. elle est croissante,
 2. elle est continue à droite,
 3. $\lim\limits_{x \to -\infty} F(x) = 0, \lim\limits_{x \to +\infty} F(x) = 1$.

### Démonstration {.proof}

La première assertion est immédiate d'après la [définition](#deffdr). Pour la seconde, on remarque que si $x_n$ décroît vers $x$, alors $]-\infty,x_n]$ décroît vers $]-\infty,x]$ et donc $F(x_n)$ décroît vers $F(x)$ par le [théorème de la continuité monotone](#continuitemonotone). La troisième assertion se montre de manière analogue  en remarquant que $]-\infty,x]$ décroît vers $\varnothing$ (resp. croît vers $\R$) lorsque $x$ décroît vers $-\infty$ (resp. croît vers $+\infty$).

Pour la réciproque, on se reportera à @Jacod.

### Quelques propriétés {.remark}
 Comme $F$ est croissante, elle admet une limite à gauche en chaque point notée $F(x^-)$. En remarquant que $]-\infty,y[\, = \lim\limits_{n \to +\infty}]-\infty,y_n[$ si $y_n$ tend vers $y$ par valeurs décroissantes, on obtient pour $x < y$ : 

  * $\P_X(]x,y]) = \P( x < X \leq y) = F(y) - F(x)$
  * $\P_X(]x,y[) = \P( x < X < y) = F(y-) - F(x)$
  * $\P_X([x,y]) = \P( x \leq X \leq y) = F(y) - F(x^-)$
  * $\P_X([x,y[) = \P( x \leq X < y) = F(y-) - F(x^-)$

En particulier, $\P_X(\{x\}) = F(x) - F(x^-)$ est le **saut** de la fonction $F$ au point $x$. On a donc $\P_X(\{x\}) = 0$ pour tout $x$ si et seulement si $F$ est continue en tout point.

### Nécessité des tribus {.remark} 
Le [théorème ci-dessus](#carac) explique pourquoi, d’un point de vue strictement mathématique, il est nécessaire d’introduire les tribus en probabilités, malgré la complexité que cela engendre. 

Plus concrètement, considérons l'exemple suivant : soit $\Omega = [0,1]$ et $\P$ telle que $\P(]a,b]) = b-a$ pour $0\leq a\leq b\leq 1$ (il s'agit de la loi uniforme sur [0,1]). C'est une probabilité naturelle qui assigne à tout intervalle sa longueur comme probabilité. Supposons maintenant que l'on souhaite étendre de manière unique $\P$ aux $2^{[0,1]}$ éléments de $\mathcal{P}([0,1])$ de manière à ce que $\P(\Omega) =1$ et $\P\left(\cup_{n\in\N^\star} A_n\right) = \sum_{n\in\N^\star} \P(A_n)$ pour toute suite $(A_n)_{n\in\N^\star}$ tels que $\A_n\cap A_m = \varnothing$ pour $n \neq m$. On peut prouver qu'un tel $\P$ n'existe pas. $\mathcal{P}([0,1])$ est trop "grand" pour définir un tel $\P$. Il contient en particulier des ensembles non mesurables.

Si l'on voulait travailler avec la tribu $\A = \mathcal{P}(\R)$, il n'existerait que très peu de probabilités sur $\R$, à savoir les probabilités discrètes que l'on décrit rapidement ci-dessous.

### Probabilités discrètes {.example #ex.discret}

 1. Les masses de Dirac (ou **mesures** de Dirac).  
 
    $X$ est identiquement égale à $a \in \R$. Alors sa loi est la mesure de Dirac en $a$, la probabilité $\P_X$ sur $\R$ qui vérifie pour $A \in \mathcal{P}(\R)$
    \begin{equation*}
        \P_X(A) = \left\{ \begin{array}{ll}
        1  &\text{si } a \in A, \\
        0 &\text{sinon.}
        \end{array}
        \right.
    \end{equation*}
    Sa fonction de répartition est $F(x) = 1_{[a,+\infty[}(x)$.

 2. Les probabilités portées par $\N$.

    $X$ est à valeurs dans $\N$. Comme $\N$ est une partie de $\R$, toute probabilité sur $\N$ peut être considérée comme une probabilité sur $\R$ qui ne "charge" que $\N$. Plus précisément, si $Q$ est la loi de probabilité de $X$ sur $\N$, on définit son "extension" $\P_X$ à $\R$ en posant $\P_X(A) = Q(A\cap \N)$. Si $q_n = Q(\{n\})$ pour $n \in \N$, la fonction de répartition $F$ de $\P_X$ est 
    \begin{equation*}
    F(x) = \left\{ \begin{array}{ll}
    0  &\text{si } x <0, \\
    \sum_{i=0}^{\lfloor x \rfloor} q_i &\text{sinon,}
    \end{array}
    \right.
    \end{equation*}
    où $\lfloor \cdot \rfloor$ désigne la partie entière.
    A titre d'exemple, on représente ci-dessous les fonctions de répartitions de la loi binomiale et de la loi de Poisson.
        ![fonction de répartition de la loi binomiale](images/CdfBinom.tex)
        ![fonction de répartition de la loi de Poisson](images/CdfPoisson.tex)

 3. Les probabilités discrètes.

    Plus généralement, si $X$ prend ses valeurs dans une partie finie ou dénombrable $E$ de $\R$, la loi $\P_X$ de $X$ est caractérisée pour tout $i \in E$ par $q_i = \P_X({i}) = \P(X=i)$. La fonction de répartition $F$ de $X$ est alors 
    $$F(x) = \sum_{\substack{i \in E \\ i \leq x}} q_i,$$
    avec la convention qu'une somme "vide" vaut 0. On retrouve bien l'exemple 2 si $E = \N$. On voit que $F$ est **purement discontinue** au sens où elle est complètement caractérisée par ses sauts $\triangle F(x) = F(x) - F(x^-)$ :
    $$F(x) = \sum_{y\leq x} \triangle F(y).$$
    
Il existe bien d’autres probabilités, non discrètes, sur $\R$. Le paragraphe suivant est consacré à un exemple très important, celui des variables aléatoires dont la loi admet une densité.

## Variables aléatoires réelles à densité

### Densité de probabilité {.definition #defdens}
Une fonction réelle $f$ sur $\R$ est une *densité de probabilité* (ou plus simplement une *densité*) si elle est positive, intégrable et vérifie 
$$\int_\R f(x)\, dx = 1.$$ 

Si $f$ est une densité, la fonction 
   $$F(x) =\int_{-\infty}^x f(y)\, dy$$ 
est la fonction de répartition d'une probabilité sur $\R$. 

### Variable aléatoire réelle à densité {.definition #va.densité}
Soit $X$ une variable aléatoire. On dit que $X$ a une *loi de densité $f$* (ou par abus de language "est de densité $f$"), si $\P_X$ admet la densité $f$ et donc si pour tout réel $x$, 
$$ \P(X\leq x) = \int_{-\infty}^x f(y) dy.$$

### Fonction de répartition d'une variable aléatoire à densité {.proposition #fdr-va-dens}
Soit $X$ de loi de densité $f$.

   1. Sa fonction de répartition $F$ est continue, de sorte que 
      $$\P(X=x) = 0,~~~\forall x \in \R.$$
   2. La fonction $F$ est dérivable en tout point $x$ où $f$ est continue et
      $$F'(x) = f(x).$$
   3. A l'inverse, si la fonction de répartition $F$ de $X$ est dérivable, ou seulement continue partout et dérivable par morceaux, alors $X$ admet la densité
      $$F'(x) = f(x).$$



Il existe bien sûr des variables aléatoires qui n'ont pas de densité : c'est le cas des variables discrètes données en exemple [ci-dessus]{#ex.discret}. Il existe des cas "mixtes" : soient d'une part $f$ une fonction positive, intégrable et d'intégrale strictement positive et d'autre part une partie finie ou dénombrable $E$ de $\R$ et des poids $p_i>0$ indexés par $i \in E$, tels que :
    $$ \int_\R f(x)\, dx + \sum_{i\in E} p_i = 1.$$
Alors la fonction 
    $$ F(x) = \int_{-\infty}^x f(x)\, dx + \sum_{\substack{i\in E \\ i \leq x}} p_i$$
est une fonction de répartition, et la probabilité associée $\P_X$ n'admet pas de densité et n'est pas non plus discrète.

### Remarques {.remark}

<!-- le "f(x) +1" me perturbe un peu ... comme si ce choix particulier avait un
     rôle spécial ; bien sûr ça n'est pas le cas ! Est-ce qu'on peut éviter ce
     "red herring" ? j'ai ajouté un "par exemple" et j'y ferai gaffe en amphi !
  -->

 1. La fonction de répartition est entièrement déterminée par la probabilité $\P$. Il n'en est pas de même de la densité lorsqu'elle existe : si en effet on a $F(x) =\int_{-\infty}^x f(y)\, dy$ et si on pose $g(x) = f(x)$ si $x \notin E$ et $g(x) =f(x)+1$ (par exemple) si $x\in E$, où $E$ est un ensemble négligeable, alors $g$ est encore une densité de $\P$.

 2. Une interprétation intuitive de la densité $f$ de $\P$ : si $dx$ est un petit accroissement de la variable $x$, on a (si du moins $f$ est continue en $x$) :
 $$ f(x) \sim \frac{\P([x,x+dx])}{dx}.$$   


### Durée de fonctionnement {.exercise .one #ex.expo}

On suppose que la durée de fonctionnement, en heures, d'un ordinateur avant sa première panne est une variable aléatoire positive de loi exponentielle de paramètre 1/100, de densité donnée par 

$$f(x) = \left\{ \begin{array}{ll}
        \frac{1}{100}\exp\left(-\frac{x}{100}\right) & x \geq 0, \\
        0 & x < 0.
        \end{array}
        \right.$$

1. Calculer la probabilité que cette durée de fonctionnement $X$ soit comprise entre 50 et 150 heures.
2. Calculer la probabilité que l'ordinateur fonctionne moins de 100 heures.
3. Calculer la probabilité que l'ordinateur fonctionne exactement 100 heures avant sa première panne.

### Précipitation {.exercise .one #ex.pluie}
On souhaite modéliser la hauteur de précipitation (en mm) tombée sur Paris en une journée par une variable aléatoire $X$. On considère que cette hauteur suit une loi exponentielle de paramètre $1/10$ lorsqu'il pleut et qu'il pleut en moyenne un jour sur deux.

1. Donner la Fonction de répartition de $X$.
2. $X$ admet-elle une densité ?



### Quelques lois à densités {.example #exampledens}

 1. La *loi uniforme* sur $[a,b]$, avec $a,b \in \R$ tels que $a < b$, notée $\mathcal{U}_{[a,b]}$, est la probabilité $\P$ qui admet la densité
    $$f(x) = \left\{\begin{array}{ll}
            \frac{1}{b-a} & \text{si } a \leq x \leq b,\\
            0 & \text{sinon}.
            \end{array}\right.$$
    ![Densité de probabilité de la loi uniforme](images/PdfUnif.tex)
    En vertu de la remarque 1. ci-dessus, on aurait pu choisir $f(a) = f(b) = 0$. Au vu de l'interprétation 2. ci-dessus, le fait que $f$ soit constante sur $[a, b]$ exprime que si on choisit un point selon la probabilité uniforme, on a “autant de chances” de tomber au voisinage de chaque point de l’intervalle $[a, b]$. Cela explique le nom “uniforme”. On remarque aussi que $\P(\{x\}) = 0$ pour tout $x$ (comme pour toutes les probabilités à densité). On a donc une probabilité nulle de tomber exactement en un point $x$ fixé à l’avance.
    On vérifie aisément que sa fonction de répartition est
    $$F(x) = \left\{\begin{array}{ll}
            0 & \text{si } x < a,\\
            \frac{x-a}{b-a} & \text{si } a \leq x \leq b,\\
            1 & \text{si } x > b.
            \end{array}\right.$$
    ![fonction de répartition de la loi uniforme](images/CdfUnif.tex)

 2. La *loi exponentielle* de paramètre $\theta$, notée $\mathcal{E}_\theta$, est la loi de densité
    $$f(x) = \left\{\begin{array}{ll}
            0 & \text{si } x < 0,\\
            \theta e^{-\theta x} & \text{sinon}.
            \end{array}\right.$$
    ![Densité de probabilité de la loi exponentielle](images/PdfExp.tex)
    et de fonction de répartition 
    $$F(x) = \left\{\begin{array}{ll}
            0 & \text{si } x < 0,\\
            1 - e^{-\theta x} & \text{sinon}.
            \end{array}\right.$$
    ![fonction de répartition de la loi exponentielle](images/CdfExp.tex)
    Dans la pratique, on utilise fréquemment la loi exponentielle pour modéliser une durée de vie ou le temps d’attente avant l’arrivée d’un événement spécifique. Par exemple la durée de vie d’une bactérie, d'un composant électronique, la durée d’une conversation téléphonique ou le temps qui nous sépare du prochain tremblement de terre peuvent être considérées comme des variables aléatoires de loi exponentielle.
    
 3. La *loi normale* (ou de *Gauss* ou encore *gaussienne*) de paramètres $\mu$ et $\sigma^2$, notée $\mathcal{N}(\mu,\sigma^2)$, est la loi de densité
    
    $$f(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$
    ![Densité de probabilité de la loi normale](images/PdfGauss.tex)
    Lorsque $\mu = 0$ et $\sigma^2 = 1$, on l'appelle la loi normale *centrée réduite* pour des raisons que nous expliciterons au prochain chapitre.

    La distribution normale fut introduite par De Moivre en 1733. Celui-ci l’utilisa pour approximer une variable aléatoire binomiale quand le paramètre $n$ de celle-ci était grand. Ce résultat fut ensuite progressivement généralisé par Laplace et d’autres confrères pour devenir le théorème connu sous le nom de théorème de la limite centrale, qui sera démontré au Chapitre 4. Ce théorème est l’un des plus importants de la théorie des probabilités et prouve que de très nombreux phénomènes aléatoires suivent approximativement une loi normale. On peut citer à titre d’exemple la taille d’un individu choisi au hasard, les composantes de la vitesse d’une molécule de gaz ou l’erreur de mesure d’une quantité physique.

    Il est difficile de faire des calculs avec la loi normale car sa densité n’admet pas de primitive explicite. Aussi des tables numériques ont-elles été construites pour permettre aux utilisateurs d’obtenir très rapidement des valeurs numériques. Elles sont disponibles dans la plupart des logiciels et permettent entre autre de représenter sa fonction de répartition.
    
    ![fonction de répartition de la loi normale](images/CdfGauss.tex)

Nous aurons l'occasion de voir par la suite un grand nombre d'autres exemples de probabilités à densité.

Exercices complémentaires
================================================================================

## Indépendance et conditionnement

### Question 1 {.question #ic-1}
Dans quelles circonstances particulières deux événements $A$ et $B$ tels que $A\cup B$ soit presque sûr sont-ils indépendants ?

### Question 2 {.question #ic-2}
Soit $A$, $B$ et $C$ trois événements indépendants **2 à 2**, avec $\P(C)>0$. Donner une condition nécessaire et suffisante sur $A$, $B$ et $C$ pour que $A$ et $B$ soient indépendants relativement à la probabilité conditionnelle $\P(\,\,|C)$, à la place de $\P$. 

### Question 3 {.question #ic-3}
Etablir que deux événements $A$ et $B$ sont indépendants ssi 
$$ \P(A\cap B)\P(A^c \cap B^c) = \P(A \cap B^c)\P(A^c\cap B)$$

## Problème de Monty Hall {.question #mh}
Dans un jeu télévisé, vous êtes confrontés au problème suivant : devant vous se trouvent 3 portes fermées. Derrière l'une d'entre elle se trouve une voiture, derrière chacune des deux autres, une chèvre. Vous désignez au hasard l'une d'entre elle. Le présentateur, qui sait où se trouve la voiture, ouvre alors une porte, qui n'est ni celle que vous avez choisie, ni celle qui cache la voiture. Il vous offre alors la possibilité de réviser votre choix. Que choisissez-vous ?

Calculer la probabilité de remporter la voiture selon les deux stratégies (changer ou non son choix de porte).

## Queues de distributions

Soit une densité $f$ sur $\R$ telle que la fonction $h: x \in \R \mapsto x\,f(x)$ est intégrable. Cette hypothèse sera appelée $(\mathcal{H})$. On note $F$ la fonction de répartition correspondante sur la droite réelle achevée. Nous allons montrer que[^o]
$$\left|\begin{array}{rl} 1-F(x) \underset{x\to+\infty}{=} o\left(\dfrac{1}{x}\right), & (1)\\[1em] F(x) \underset{x\to-\infty}{=} o\left(\dfrac{1}{x}\right).& (2) \end{array} \right. $$ 

### Etude en $+\infty$ {.question #dlfdr-pi}

1. Vérifier que pour tout $u > 0$, $$\int_{-\infty}^{+\infty} h(x)\,dx \geq \int_{-\infty}^u h(x)\,dx + u\,\left(1-F(u)\right).$$

2. En déduire $(1)$.

[^o]: Soient $a \in [-\infty,+\infty]$ et $f$ et $g$ deux fonctions définies sur un même voisinage $I$ de $a$. On dit que $f$ est *négligeable* par rapport à $g$ (ou que $g$ est *prépondérante* par rapport à $f$) au voisinage de $a$ et on note note $f(x) \underset{x\to a}{=} o(g(x))$ s'il existe une fonction $\epsilon$ définie sur $I$ telle que $\epsilon(x) \xrightarrow[x\to a]{} 0$ et $f = \epsilon \times g$.

### Etude en $-\infty$ {.question #dlfdr-mi}

3. En vous inspirant du raisonnement précédent, montrer $(2)$.

### Interprétation {.question #dlfdr-interpret}

4. Proposez une interprétation de ce résultat.

### Etude de la réciproque {.question #dlfdr-reciproque}

Considérons maintenant la fonction de répartition 
$$ F: x \in \R \mapsto \left|\begin{array}{ll} 1 - \dfrac{e}{x\,\ln(x)} & \text{si } x \geq e,\\ 0 & \text{si } x <e, \end{array}\right. $$
que l'on étend à la droite réelle achevée en posant $F(-\infty) = 0$ et $F(+\infty) = 1$.

5. Vérifier que cette fonction possède bien une densité $f$ et l'expliciter.

6. A-t-on les développements asymptotiques $(1)$ et $(2)$ ? 

7. La fonction $h$ correspondante est-elle absolument intégrable ?

8. Qu'en concluez-vous ?

### Liens entre les développements asymptotiques {.question #dlfdr-liensdl}

Soient les fonctions de répartition $$F: x\in\R \mapsto \left|\begin{array}{ll} 1 - \dfrac{1}{\ln(x)} & \text{si } x \geq e,\\ 0 & \text{sinon,}\end{array}\right.$$ et $G : x\in\R \mapsto 1 - F(-x)$, toutes deux étendues à la droite réelle achevée en posant $\lim\limits_{x\to-\infty} F(x) = \lim\limits_{x\to-\infty} G(x) = 0$ et $\lim\limits_{x\to+\infty} F(x) = \lim\limits_{x\to+\infty} G(x) = 1$.

9. Que peut-on dire sur les éventuels liens entre $(1)$ et $(2)$ à l'aide de ces deux fonctions ?


## Densité et fonction de répartition d'une loi Normale

On considère la densité d'une loi Normale centrée réduite : $$f : x\in \R \mapsto \dfrac{1}{\sqrt{2\,\pi}}\,\exp\left\{-\dfrac{x^2}{2}\right\},$$
où $f(-\infty) := \lim\limits_{x\to-\infty} f(x)$ et $f(+\infty) := \lim\limits_{x\to+\infty} f(x)$.

### Propriétés générales {.question #fdrgaussprop}

1. Faire l'étude de $f$ (domaine, parité, limites aux bornes, dérivabilité, variations, convexité/concavité).

2. Donner la définition de la fonction de répartition $F$ associée à $f$. En donner une expression faisant apparaître la *fonction d'erreur* (qui est une fonction spéciale) $$\text{erf} : x\in\R \mapsto \dfrac{2}{\sqrt{\pi}}\,\int_{0}^x e^{-u^2}\,du.$$

### Encadrement de $1 - F(x)$ pour tout $x > 0$ {.question #fdrgaussenca}

Nous allons maintenant démontrer la propriété suivante : $\forall\,x > 0$ $$ \dfrac{x}{1+x^2}\,f(x) \leq 1 - F(x) \leq \dfrac{f(x)}{x}. $$

3. En observant que $u\geq x >0$ implique $\dfrac{u}{x} \geq 1$, montrer l'inégalité de droite.

4. En observant que $u\geq x > 0$ implique $u^{-2} \leq x^{-2}$, montrer que $\forall\,x>0$, $$\left(1+\dfrac{1}{x^2}\right)\,\left(1-F(x)\right) \geq \dfrac{f(x)}{x}.$$ En déduire l'inégalité de gauche.

### Equivalent de $1-F(x)$ quand $x\to+\infty$. {.question #fdrgaussequi}

5. Déduire de l'encadrement prédédent un équivalent de $1-F(x)$ lorsque $x\to+\infty$. 

### Ratio de Mills {.remark} 
Pour $x\in\R$, le rapport $\dfrac{1-F(x)}{f(x)}$ est appelé *ratio de Mills*. Il est beaucoup utilisé en statistique, en particulier pour l'analyse des modèles de régression en présence de biais de sélection.

6. Comparer ce résultat à celui de l'exercice sur les développements limités pour les fonctions de répartition. En particulier, $h:x\in[-\infty,+\infty] \mapsto x\,f(x)$ est-elle intégrable ?

### Loi Normale générale. {.question #fdrgaussgen}

Considérons maintenant la densité plus générale $$g(x) = \dfrac{1}{\sqrt{2\,\pi}\,\sigma}\, \exp\left\{-\dfrac{(x-\mu)^2}{2\,\sigma^2} \right\},$$
où $\mu \in \R$ et $\sigma^2 > 0$. On note $G$ sa fonction de répartition associée.

7. En réécrivant $g$ en fonction de $f$, déduire des questions précédentes un équivalent de $1-G(x)$ lorsque $x\to+\infty$.


---


# Solutions

Exercices essentiels
--------------------------------------------------------------------------------

### Propriétés élémentaires {.answer #answer-propelem}

 1. $\P(A) \in [0,1]$ est donné par la définition. Par ailleurs, on a $\Omega = A \cup A^c$ et $A\cap A^c = \varnothing$. En considérant la suite $A_1 = A$, $A_2 = A^c$ et $A_n = \varnothing$ pour $n > 2$, le point 2. de la définition nous donne $1 = \P(\Omega) = \P(A) + \P(A^c)$.

 2. Puisque $A \subset B$, on a l'union disjointe $B = (B\cap A) \cup (B\cap A^c) = A \cup (B\cap A^c)$. Comme $\P(B\cap A^c) \geq 0$ par définition, on en déduit le résultat.

 3. On a $(A\cup B) = B \cup (A\cap B^c)$, avec $B \cap (A\cap B^c) =\varnothing$ ainsi que $A = (A\cap B^c) \cup (A\cap B)$, où $(A\cap B^c) \cap (A\cap B) = \varnothing$. On en déduit $\P(A\cup B) = \P(B) + \P(A\cap B^c)$ et $\P(A) = \P(A\cap B^c) + \P(A\cap B)$, d'où le résultat.

 4. Par récurrence. On a déjà vu que $\P(A\cup B) \leq \P(A) + \P(B)$. Notant $B = \bigcup_{i=1}^n A_i$, alors $\P(\bigcup_{i=1}^{n+1} A_i) \leq \P(B) + \P(A_{n+1})$, et l'hypothèse de récurrence nous indique $\P\left(\bigcup_{i=1}^n A_i\right) \leq \sum_{i=1}^n \P(A_i)$, d'où le résultat.

 5. Par récurrence. On a déjà vu que $\P(A \cup B ) = \P(A) + \P(B) - \P(A \cap B)$. Notant $B = \bigcup_{i=1}^n A_i$, alors 
    \begin{align*}
        \P(\bigcup_{i=1}^{n+1} A_i) =& \P(B \cup A_{n+1}) \\
                                    =& \P(B) + \P(A_{n+1}) - \P(B \cap A_{n+1}) \\
                                    =& \sum_{i=1}^n \P(A_i) - \sum_{1 \leq i < j \leq n} \P(A_i \cap A_j) + \ldots + (-1)^n \P\left(\bigcap_{i=1}^n A_i\right) \\
                                     &+ \P(A_{n+1})\\
                                     &-\sum_{i=1}^n \P(A_i\cap A_{n+1}) + \sum_{1 \leq i < j \leq n} \P(A_i \cap A_j) + \ldots + (-1)^{n+1} \P\left(\bigcap_{i=1}^n A_i\cap A_{n+1}\right)\\
                                     =& \sum_{i=1}^{n+1} \P(A_i) - \sum_{1 \leq i < j \leq n +1 } \P(A_i \cap A_j) + \ldots + (-1)^{n+1} \P\left(\bigcap_{i=1}^{n+1} A_i\right).
    \end{align*}


### Continuité monotone {.answer #answer-contmon}
On définit une suite $(B_n)_{n\in \N^\ast}$ telle que $B_1 = A_1$ et $B_n = A_n \setminus A_{n-1}$, pour $n\geq 2$. Les $B_n$ ainsi définis sont deux à deux disjoints et $\cup B_n = \cup A_n$, donc :
$$ \P\left(\bigcup_{n\in\N^\ast} A_n\right) = \sum_n \P(B_n) = \lim_{n \to \infty} \sum_{p=1}^n \P(B_p) = \lim_{n \to \infty} \P(A_n).$$

### Une définition alternative de la probabilité {.answer #answer-altdef}

Soit $A_n$ une suite d'éléments de $\A$ deux-à-deux disjoints. On définit $B_n = \cup_{p \leq n} A_n$ et $B = \cup_n A_n$. Comme $\P$ est additive, on a $\P(B_n) = \sum_{p \leq n} \P(A_n)$ qui croît vers $\sum_n \P(A_n)$ et aussi vers $\P(B)$ d'après le point 3.

En considérant les résultats de ces deux exercices, on obtient une définition alternative de la probabilité en substituant la [continuité monotone](#contmon) et l'additivité à la propriété de [$\sigma$-additivité](#defproba).

### Inégalité {.answer #answer-boolinf}
On a déjà vu le cas fini avec [l'inégalité de Boole](#propelem). On pose $B_n = \cup_{i=1}^n A_i$, qui croît vers l'ensemble $C = \cup_n A_n$.
D'après [l'inégalité de Boole](#propelem), on a 
   $$\P(B_n) \leq \sum_{i=1}^n \P(A_i)$$
Mais $\P(B_n) \to_{n \to \infty} \P(C)$ d'après le [théorème de continuité monotone](#contmon), tandis que $\sum_{i=1}^n \P(A_i) \to_{n \to \infty} \sum_{n\in\N^\ast} \P(A_n)$. En passant à la limite, on obtient donc le résultat.



### Test {.answer #answer-test}
On considère les événements $A$ “l’individu est séropositif”, et $B$ “le test de détection donne un résultat positif”. Les données ci-dessus nous indiquent $P(A) = 10^{-4}$ d’où $\P(A^c) = 0,9999$ , $\P(B|A) = 0,99$ et $\P(B|A^c) = 0,001$. Nous trouvons alors
\begin{align*}
\P(A|B) &= \frac{\P(A \cap B)}{\P(B)}\\
        &= \frac{\P(B |A ) \P(A)}{\P(B |A)\P(A) + \P(B|A^c)\P(A^c)}\\
        &= \frac{0,99 \times 10^{-4}}{0,99 \times 10^{-4} + 0,001 \times 0,9999}\\
        &\approx 0,09.
\end{align*}
On remarque que contrairement à l’intuition, cette probabilité est faible.

### Démonstration {.answer #answer-indep}
Pour $(A^c,B)$, si $\P(B) = 0$, alors $\P(A^c \cap B) = 0 = \P(B)\P(A^c)$. Sinon, $\P(A^c \cap B) = \P(B)\P(A^c|B) = \P(B)(1-\P(A|B)) = \P(B)(1-\P(A))=\P(B)\P(A^c)$.

Pour $(A,B^c)$, on inverse les rôles de $A$ et $B$ ci-dessus.

Pour $(A^c,B^c)$, on remarque que $A^c \cap B^c = (A \cup B)^c$, d'où $\P(A^c \cap B^c) = 1-\P(A \cup B) = 1-\P(A) - \P(B) +\P(A)\P(B) = (1-\P(A))(1-\P(B)) = \P(A^c)\P(B^c)$

### Auto-indépendant ?{.answer #answer-autoindep}
$A$ est indépendant de lui-même ssi $\P(A) = \P(A \cap A) = \P(A)\P(A)$, autrement dit si $\P(A) = 0$ ou si $\P(A) = 1$.

### Durée de fonctionnement {.answer #answer-ex.expo}
1. $\P(X \in [50,150]) = \int_{50}^{150} \frac{1}{100}\exp\left(-\frac{x}{100}\right) dx = \exp(-1/2)-\exp(-3/2) \approx 0,38.$
2. $\P(X \leq 100) = \int_{0}^{100} \frac{1}{100}\exp\left(-\frac{x}{100}\right) dx = 1-e^{-1} \approx 0,63.$
3. $\P(X = 100) = 0$

### Précipitations {.answer #answer-ex.pluie}
1. $$F(x) = \left\{ \begin{array}{ll}
   0 & \text{si } x < 0 \\
   1/2 & \text{si } x = 0 \\ 
   1/2 + 1/2 \int_0^x \frac{1}{10}\exp\left(-\frac{x}{10}\right) & \text{si } x > 0 
   \end{array} \right.$$
   
2. $F$ n'est pas continue, $X$ n'admet donc pas de densité ([voir la proposition](#fdr-va-dens)).

## Indépendance et conditionnement

### Question 1 {.answer #answer-ic-1}

On a $1 = \P(A\cup B) = \P(A) + \P(B) - \P(A\cap B)$, donc $1 = \P(A) + \P(B) - \P(A)\P(B)$ si et seulement si $A$ et $B$ sont indépendants. Cette égalité se réécrit $(1-\P(A))(1-\P(B))=0$, qui est vérifiée ssi $A$ ou $B$ est presque sûr.

### Question 2 {.answer #answer-ic-2}

Par définition, on a $A$ et $B$ indépendants relativement à $\P(\,\,|C)$ ssi
$$\P(A\cap B |C) = \P(A|C)\P(B|C) = \P(A)\P(B),$$
car $A$ et $B$ sont chacun indépendants de $C$, d'où 
$$\frac{\P(A\cap B \cap C)}{\P(C)} = \P(A)\P(B)$$ 
par [définition](#defprobacond) ; et comme $A$, $B$ et $C$ sont indépendants 2 à 2, 
$$\P(A\cap B \cap C) = \P(A)\P(B)\P(C)$$ 
équivaut à $A$, $B$ et $C$ sont mutuellement indépendants.

### Question 3 {.answer #answer-ic-3}

On a $\P(A^c\cap B^c) = \P((A \cup B)^c) = 1 - \P(A) - \P(B) + \P(A\cap B)$, donc
$$\P(A\cap B)\P(A^c \cap B^c) = \P(A\cap B) - \P(A\cap B)(\P(A) + \P(B) + \P(A\cap B))$$
Par ailleurs, on a 
$$\left\{ \begin{array}{ll}
        \P(A \cap B^c)  & = \P(A \setminus (A\cap B)) = \P(A) - \P(A\cap B) \\
        \P(A^c \cap B)  &=  \P(B \setminus (A\cap B)) = \P(B) - \P(A\cap B)
        \end{array}
        \right.$$
Donc
$$ \P(A \cap B^c)\P(A^c\cap B) = \P(A)\P(B) -\P(A\cap B)(\P(A) + \P(B)- \P(A\cap B))$$
On a donc bien l'égalité ssi $\P(A)\P(B) = \P(A\cap B)$

## Problème de Monty Hall {.answer #answer-mh}
Considérons les événements $A$ = 'la porte choisie en premier est la bonne' et $B$ = 'la dernière porte est la bonne'.

On a évidemment $\P(A) = \frac{1}{3}$, puisque le choix initial se fait uniformément parmi les 3 portes.

Pour $B$, on doit tenir compte de l'information donnée par le présentateur. On a par [la formule des probabilités totales](#formprobatot)
$$\P(B) = \P(B|A)\P(A) + \P(B|A^c)\P(A^c) = 0.\frac{1}{3} + 1.\frac{2}{3} = \frac{2}{3}$$
En effet $\P(B|A^c) = 1$ car si la porte choisie initialement n'est pas la bonne, c'est nécessairement la dernière.

Il convient donc de changer son choix compte tenu de la nouvelle information. 
Pour se convaincre du résultat, on peut refaire le calcul avec disons 100 portes et le présentateur qui ouvre 98 autres portes après le choix du candidat.


## Queues de distributions

### Etude en $+\infty$ {.answer #answer-dlfdr-pi}

1. Soit $u>0$. Comme $h$ est intégrable, on peut écrire
\begin{align*}
\int_{-\infty}^{+\infty} h(x)\,dx = \int_{-\infty}^{+\infty} x\,f(x)\,dx & = \int_{-\infty}^{u} x\,f(x)\,dx + \int_{u}^{+\infty} x\,f(x)\,dx\\
&\geq \int_{-\infty}^{u} x\,f(x)\,dx + u\,\int_{u}^{+\infty} f(x)\,dx\\
&= \int_{-\infty}^{u} h(x)\,dx + u\,\left(1- F(u)\right).
\end{align*}

<!-- On peut justifier que pour $f,g : \R \to \R$ intégrables telles que $f < g$ on a $\int f < \int g$ en utilisant la positivité et la linéarité de l'intégrale (qui sont vraies quand on passe à $[-\infty,+\infty]$ même si ce n'est pas explicitement mentionné dans le cours de calcul intégral 1 pour la positivité). En effet, dans ce cadre $g-f$ est intégrable par linéarité, positive ($g > f$) et on a donc $\int g - f = \int g - \int f > 0$. -->

2. Soit toujours $u>0$. Toute fonction de répartition étant à valeurs dans $[0,1]$, on a $u\,\left(1-F(u)\right) \geq 0$. En utilisant la question précédente on obtient donc l'encadrement
\begin{align*}
0 \leq u\,\left(1-F(u)\right) & \leq \int_{-\infty}^{+\infty} h(x)\,dx - \int_{-\infty}^u h(x)\,dx\\
&= \int_{u}^{+\infty} h(x)\,dx = \int_{-\infty}^{+\infty} h(x)\,1_{[u,+\infty]}(x)\,dx.
\end{align*}
Or pour tout $x\in \R$ on a $\left|h(x)\,1_{[u,+\infty]}(x)\right| \leq \left|h(x)\right|$, qui est intégrable. On peut donc appliquer le [théorème de convergence dominée](Calcul Intégral II.pdf #TCD), qui nous donne :
\begin{align*}
\lim_{u\to+\infty} u\,(1-F(u)) & = \int_{-\infty}^{+\infty} h(x)\,\lim_{u\to+\infty} 1_{[u,+\infty]}(x)\,dx\\
& = \int_{-\infty}^{+\infty} h(x)\,1_{\varnothing}(x)\,dx = 0.
\end{align*}
On en conclut que $1-F(x) = o\left(\dfrac{1}{x}\right)$ lorsque $x\to+\infty$.

### Etude en $-\infty$ {.answer #answer-dlfdr-mi}

3. Prenons maintenant $u<0$. Comme $h$ est intégrable, on peut écrire
\begin{align*}
\int_{-\infty}^{+\infty} h(x)\,dx = \int_{-\infty}^{+\infty} x\,f(x)\,dx & = \int_{-\infty}^{u} x\,f(x)\,dx + \int_{u}^{+\infty} x\,f(x)\,dx\\
&\leq u\, \int_{-\infty}^{u} f(x)\,dx + \int_{u}^{+\infty} x\,f(x)\,dx\\
&= u\,F(u) + \int_{u}^{+\infty} h(x)\,dx.
\end{align*}
Or, comme $F$ prend ses valeurs dans $[0,1]$, $u\,F(u) \leq 0$. On obtient donc
\begin{align*}
0 \geq u\,F(u) & \geq \int_{-\infty}^{+\infty} h(x)\,dx - \int_{u}^{+\infty} h(x)\,dx\\
&= \int_{-\infty}^{u} h(x)\,dx = \int_{-\infty}^{+\infty} h(x)\,1_{[-\infty,u]}(x)\,dx.
\end{align*}
Comme précédemment, cette dernière fonction sous l'intégrale est dominée par $-\left|h\right|$ (à gauche) et $\left|h\right|$ (à droite), toutes deux intégrables, donc d'après le [théorème de convergence dominée](Calcul Intégral II.pdf #TCD)
\begin{align*}
\lim_{u\to-\infty} u\,F(u) & = \int_{-\infty}^{+\infty} h(x)\,\lim_{u\to-\infty} 1_{[-\infty,u]}(x)\,dx\\
& = \int_{-\infty}^{+\infty} h(x)\,1_{\varnothing}(x)\,dx = 0.
\end{align*}
On a donc bien $F(x) = o\left(\dfrac{1}{x}\right)$ lorsque $x\to-\infty$.

### Interprétation {.answer #answer-dlfdr-interpret}

4. L'hypothèse que $h$ est  intégrable nous donne une indication sur la vitesse de convergence de $1-F(x)$ et $F(x)$ lorsque $x$ tend respectivement vers $+\infty$ et $-\infty$ : elles convergent vers $0$ au moins aussi vite que $\dfrac{1}{x}$. On dit que les queues de la distribution sont "relativement" fines.

Pour mieux comprendre l'impact de ce résultat, prenons un exemple pratique. Considérons un phénomène aléatoire comme la concentration en polluant dans l'air, modélisé par une loi de probabilité sur $\R$ de densité $f$ nulle sur $\R_-^\ast$. Etre capable de déterminer la probabilité que la concentration dépasse un seuil critique $x$ est alors très important pour les organismes de contrôle de la qualité de l'air. Or cet événement correspond mathématiquement à l'événement $[x,+\infty]$. Dans ce cas, $1 - F(x)$ nous donne cette probabilité selon le modèle considéré. Le résultat nous indique que si l'on choisit un modèle tel que $h$ est intégrable, alors cette probabilité décroît plus rapidement que $\dfrac{1}{x}$ lorsque le seuil $x$ augmente. En d'autres termes, les événements extrêmes (quand $x$ est grand) restent "assez" rares. L'impact du choix de modèle n'est donc pas négligeable : si on prend une distribution à queues trop fines alors que les pics de pollution ne sont en réalité pas si rares que ça, $1-F(x)$ risque de sous-estimer le risque réel de dépassement du seuil !

### Etude de la réciproque {.answer #answer-dlfdr-reciproque}

5. La fonction $F$ considérée est continue et dérivable par morceaux sur $\R$ ; le seul point où $F$ n'est pas dérivable est $e$ (le taux d'accroissement n'a pas les mêmes limites à gauche et à droite). Elle possède donc [une densité](#fdr-va-dens) qui s'obtient en dérivant chaque morceau : pour tout $x\in\R$, $$f(x) = \left|\begin{array}{ll} e\,\dfrac{\ln(x) + 1}{x^2\,\ln(x)^2} & \text{si } x \geq e,\\ 0 & \text{sinon.}\end{array}\right.$$
<!-- Ici on peut leur montrer qu'on aurait pu prendre n'importe quelle valeur pour f en e, et ça marcherait quand même (idée qu'on n'a pas forcément une unique densité, mais qu'elles sont toutes égales p.p.) -->
On peut l'étendre à la droite réelle achevée en posant $f(\pm\infty) = \lim\limits_{x\to\pm\infty}f(x) = 0$.

6. On remarque que pour tout $x\geq e$, $x\,\left(1-F(x)\right) = \dfrac{e}{\ln(x)} \xrightarrow[x\to+\infty]{} 0$, donc le développement asymptotique $(1)$ est bien vérifié. En outre, comme $x\,F(x) = 0$ pour tout $x < e$, le développement asymptotique $(2)$ est aussi bien respecté.

7. Pour tout $x\in\R$, $$ h(x) = \left|h(x)\right| = \left|\begin{array}{ll} e\,\dfrac{\ln(x) + 1}{x\,\ln(x)^2} & \text{si } x \geq e,\\ 0 & \text{sinon,} \end{array}\right.$$ et on pose $h(\pm\infty) = \lim\limits_{x\to\pm\infty}h(x) = 0$.
Par conséquent, $h$ est clairement  intégrable sur $[-\infty,e]$, où elle est égale presque partout (partout sauf en $e$) à la fonction nulle. Pour savoir si $h$ est  intégrable sur toute la droite réelle achevée, il nous faut donc regarder si elle l'est sur $[e,+\infty]$. Pour cela, nous allons utiliser le [théorème de Hake](Calcul Intégral I.pdf #hake), qui nous dit de vérifier que $h$ est intégrable sur tout segment $[a,b] \subsetneq [e,+\infty]$, puis que $\lim\limits_{t\to+\infty} \int_e^t h(x)\,dx$ existe et est finie. Remarquons d'abord que $h$ est continue, donc elle est intégrable sur tout segment strictement inclus dans $[e,+\infty]$; le premier point est vérifié. On remarque en outre que pour tout $x\geq e$, $$h(x) \geq \dfrac{1}{x\,\ln(x)}. $$ Par conséquent, pour tout $t > e$ on a:
$$\int_{e}^t h(x)\,dx \geq \int_e^t \dfrac{1}{x\,\ln(x)}\,dx = \left[\ln(\ln(x))\right]_e^t = \ln(\ln(t)).$$
Or cette dernière quantité tend vers $+\infty$ quand $t\to+\infty$. Donc $\int_{e}^t h(x)\,dx$ n'a pas de limite finie quand $t\to+\infty$. On en conclut que $h$ n'est pas  intégrable.

8. La fonction de répartition $F$ considérée respecte bien les développements asymptotiques $(1)$ et $(2)$, mais la fonction $h$ associée n'est pas  intégrable. Nous avons donc montré que la réciproque de la propriété est fausse.

### Liens entre les développements asymptotiques {.answer #answer-dlfdr-liensdl}

9. On remarque que $F$ satisfait $(2)$ mais pas $(1)$, tandis que $G$ satisfait $(1)$ mais pas $(2)$. On en conclut que $(1)$ n'implique pas $(2)$ et inversement.


## Densité et fonction de répartition d'une loi Normale

### Propriétés générales {.answer #answer-fdrgaussprop}

1. Faisons l'étude de $f$.

* **Domaine.** $f : \R \to \R^+$.
* **Parité.** On remarque que $f$ est paire : $\forall\,x\in\R$, $f(x) = f(-x)$.
* **Limites aux bornes.** $\lim\limits_{x\to-\infty} f(x) = \lim\limits_{x\to+\infty} f(x) = 0$. Ainsi, la parité est aussi vraie aux bornes.
* **Dérivabilité.** $f$ est continue sur $\R$ et infiniment dérivable sur $\R$ en tant que composée de fonctions infiniment dérivables. Pour tout $x\in\R$ sa dérivée première s'écrit $f^\prime(x) = -x\,f(x)$ et a dérivée seconde $f^{\prime\prime}(x) =(x^2 - 1)\,f(x)$. Ces deux dernières fonctions peuvent être étendues à la droite réelle achevée en posant $f^\prime(\pm\infty) := \lim\limits_{x\to\pm\infty} f^\prime(x) = 0$ et $f^{\prime\prime}(\pm\infty) := \lim\limits_{x\to\pm\infty} f^{\prime\prime}(x) = 0$.
* **Variations.**  $f^\prime$ est strictement positive (resp. négative) ssi $-\infty < x < 0$ (resp. $+\infty > x > 0$). Elle est nulle en $0$, $+\infty$ et $-\infty$. Ainsi, $f$ est strictement croissante sur $]-\infty,0[$, vaut $\left(2\,\pi\right)^{-1/2}$ en $0$, puis est strictement décroissante sur $]0,+\infty[$. 
* **Convexité/Concavité.** $f^{\prime\prime}$ est strictement positive (resp. négative) sur $\R\backslash\,]-1,1[$ (resp. $]-1,1[$). $f$ est donc convexe sur $\R\backslash\,]-1,1[$ et concave sur $]-1,1[$.

2. Par définition, pour tout $x\in\R$ $$ F(x) = \int_{-\infty}^x \dfrac{1}{\sqrt{2\,\pi}}\,\exp\left\{-\dfrac{u^2}{2}\right\}\,du.$$ On pose $F(+\infty) = 1$ et $F(-\infty) = 0$. Lorsque $x = 0$, comme $f$ est paire et que son intégrale sur $[-\infty,+\infty]$ vaut $1$ (c'est [une densité](#defdens)), son intégrale sur $[-\infty,0]$ (i.e. $F(0)$) vaut $\dfrac{1}{2}$. Lorsque $x > 0$, en décomposant l'intégrale puis en utilisant un [changement de variable](Calcul Intégral I.pdf #changement-de-variable)  on obtient 
$$F(x) = \dfrac{1}{2} + \int_{0}^x \dfrac{1}{\sqrt{2\,\pi}}\,\exp\left\{-\dfrac{u^2}{2}\right\}\,du = \dfrac{1}{2} + \int_{0}^{\frac{x}{\sqrt{2}}} \dfrac{1}{\sqrt{\pi}}\,e^{-v^2}\,dv = \dfrac{1}{2} + \dfrac{1}{2}\,\text{erf}\left(\dfrac{x}{\sqrt{2}}\right).$$
Lorsque $x<0$, on peut procéder de la même manière avec $1 - F(x)$ et obtenir la même égalité que ci-dessus.

### Encadrement de $1 - F(x)$ pour tout $x > 0$ {.answer #answer-fdrgaussenca}

3. Soit $x>0$. Par définition,
$$1 - F(x) = \int_{-\infty}^{+\infty} f(u)\,du - \int_{-\infty}^x f(u)\,du = \int_{x}^{+\infty} \dfrac{1}{\sqrt{2\,\pi}}\,\exp\left\{-\dfrac{u^2}{2}\right\}\,du. $$
Or pour tout $u\geq x$ on a $u/x \geq 1$, donc 
$$1 - F(x) \leq \dfrac{1}{\sqrt{2\,\pi}}\,\int_{x}^{+\infty} \dfrac{u}{x}\, \exp\left\{-\dfrac{u^2}{2}\right\}\,du = \dfrac{-1}{x}\,\int_{x}^{+\infty} f^\prime(u)\,du. $$
Or $f^\prime$ a pour primitive $f$ donc d'après [le théorème fondamental du calcul (extension)](Calcul Intégral I.pdf #TFC) on a 
$$1-F(x) \leq -\dfrac{f(+\infty) - f(x)}{x} = \dfrac{f(x)}{x}. $$


4. Soit $x>0$. Par définition, $$\left(1 + \dfrac{1}{x^2}\right)\,\left(1-F(x)\right) = \int_x^{+\infty} \left(1 + \dfrac{1}{x^2} \right)\,f(u)\,du.$$
Or pout tout $u \geq x$ on a $\dfrac{1}{u^2} \leq \dfrac{1}{x^2}$, d'où
$$\left(1 + \dfrac{1}{x^2}\right)\,\left(1-F(x)\right) \geq \int_{x}^{+\infty} \left( 1 + \dfrac{1}{u^2} \right)\,f(u)\,du.$$
Remarquons maintenant que d'après la question 1, $\left(\dfrac{f(x)}{x} \right)^\prime = \dfrac{-x^2\,f(x) - f(x)}{x^2} = -\left(1+\dfrac{1}{x^2}\right)\,f(x)$. En d'autres termes, $A : x\in\R \mapsto -\dfrac{f(x)}{x}$ est une primitive de $x\in\R \mapsto \left(1+\dfrac{1}{x^2}\right)\,f(x)$. On peut étendre ses valeurs à la droite réelle achevée en posant $A(\pm\infty) = \lim\limits_{x\to\pm\infty} A(x) = 0$. On obtient alors par [le théorème fondamental du calcul (extension)](Calcul Intégral I.pdf #TFC)
$$\left(1 + \dfrac{1}{x^2}\right)\,\left(1-F(x)\right) \geq - \left(A(+\infty) - A(x)\right) = A(x) = \dfrac{f(x)}{x}.$$
On en déduit directement l'inégalité de gauche :
$$ 1-F(x) \geq f(x)\,\dfrac{x^2}{(x^2+1)\,x} = f(x)\,\dfrac{x}{x^2+1}. $$

### Equivalent de $1-F(x)$ quand $x\to+\infty$. {.answer #answer-fdrgaussequi}

5. Soit $x>0$. L'encadrement que nous avons démontré peut être réécrit
$$ \dfrac{x^2}{1+x^2} \leq \dfrac{1-F(x)}{\dfrac{f(x)}{x}} \leq 1, $$
et comme $\dfrac{x^2}{1+x^2} \to 1$ lorsque $x\to+\infty$, on obtient que $1-F(x) \sim \dfrac{f(x)}{x}$ quand $x\to+\infty$.

6. Pour tout $x \in [-\infty,+\infty]$ on a $\left|h(x)\right| = \left|x\,f(x)\right| = |x|\,f(x)$ puisque $f\geq 0$. Lorsque $x \in [0,+\infty]$, $\left|h(x)\right| = h(x)$, or d'après la question 1, $h$ admet pour primitive $-f$, qui vaut $0$ en $+\infty$ et $-\infty$ puis $(2\,\pi)^{-1/2}$ en $0$. Par conséquent, (d'après l'extension du [théorème fondamental du calcul](Calcul Intégral I.pdf #TFC)) l'intégrale de $\left|h\right|$ sur $[0,+\infty]$ existe, et vaut $(2\,\pi)^{-1/2}$. Or $\left|h\right|$ est paire, son intégrale sur $[-\infty,0]$ existe donc aussi et vaut $(2\,\pi)^{-1/2}$. On en conclut que $h$ est bien absolument intégrable sur $[-\infty,+\infty]$. En remarquant qu'elle est impaire, on obtient immédiatement que son intégrale vaut $0$.

On est donc bien dans le cadre de l'exercice sur les queues de distributions. L'équivalent que nous avons trouvé implique bien que $1-F(x) = o\left(\dfrac{1}{x} \right)$ lorsque $x\to+\infty$. Il nous donne juste plus de précisions quant au comportement de $1-F(x)$ lorsque $x\to+\infty$ dans le cas spécifique de la loi Normale centrée réduite : on connaît sa vitesse de convergence.

### Loi Normale générale. {.answer #answer-fdrgaussgen}

7. Soit $x\in\R$. On remarque que $g(x) = \dfrac{1}{\sigma}\,f\left(\dfrac{x-\mu}{\sigma} \right)$. Cela implique en particulier que $$G(x) =  \int_{-\infty}^x \dfrac{1}{\sigma}\,f\left(\dfrac{u-\mu}{\sigma} \right)\,du = \int_{-\infty}^{\frac{x-\mu}{\sigma}} f(u)\,du = F\left(\dfrac{x-\mu}{\sigma}\right).$$
On obtient alors l'encadrement suivant, pour tout $x>\mu$ :
$$ \dfrac{x-\mu}{1 + \dfrac{(x-\mu)^2}{\sigma^2}}\,g(x) \leq 1 - G(x) \leq \dfrac{\sigma^2\,g(x)}{x-\mu}.  $$

On en déduit que $1-G(x) \sim \dfrac{\sigma^2\,g(x)}{x-\mu} \sim \sigma^2\,\dfrac{g(x)}{x}$ lorsque $x\to+\infty$.


Références
================================================================================
