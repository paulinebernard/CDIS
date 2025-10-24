% Probabilités V

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\B}{\mathcal{B}}
\renewcommand{\L}{\mathcal{L}}
\newcommand{\Esp}{\mathbb{E}}
\newcommand{\V}{\mathbb{V}}
\newcommand{\cov}{\text{Cov}}
\renewcommand{\No}{\mathcal{N}}

\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}



Objectifs d'apprentissage
================================================================================

Cette section s'efforce d'expliciter et de hiérarchiser
les acquis d'apprentissages associés au chapitre. 
Ces objectifs sont organisés en paliers :

(\zero) Prérequis (\one) Fondamental (\two) Standard (\three) Avancé
(\four) Expert

Sauf mention particulière, la connaissance des démonstrations du document 
n'est pas exigible[^hp] 

[^hp]: l'étude des démonstrations du cours peut toutefois 
contribuer à votre apprentissage, au même titre que la résolution 
d'exercices.

#### Intégrale de Monte Carlo

- \one connaître le principe de l'intégration par la méthode Monte Carlo
- \one savoir que cette approche se justifie par la loi des grands nombres
- \one savoir que l'approximation fournie par le TCL offre un contrôle de l'erreur

#### Génération de nombres pseudo-aléatoires

- \one connaître le principe de la génération de nombres pseudo-aléatoires par la méthode des congruences

#### Méthodes de simulation de v.a.

- \one connaître et savoir implémenter en python la méthode d'inversion
- \one connaître et savoir implémenter en python la méthode de rejet
- \one connaître la méthode de Box-Muller
- \one connaître et savoir implémenter la simulation de vecteurs gaussien par la méthode de Cholesky

#### Echantillonnage d'importance

- \one connaître la définition de la méthode d'échantillonnage d'importance
- \one savoir qu'un bon choix de densité instrumentale permet de minimiser la variance d'estimation


# Intégrale de Monte-Carlo

Les méthodes de Monte-Carlo ont été développées initialement par des physiciens dans les années 1950 (notamment par les travaux de Metropolis, Ulam, Hastings,
Rosenbluth) pour calculer des intégrales (déterministes) à partir de méthodes probabilistes numériquement assez économiques. Le nom a été donné en référence
au célèbre casino du fait du caractère aléatoire de ces méthodes.

Les méthodes de simulation sont basées sur la production de nombres aléatoires, distribués selon une certaine loi de probabilité. 
Dans de nombreuses applications, pour une certaine fonction $h$, on souhaite calculer, pour une variable aléatoire $X$ de loi $\P_X$
$$\mathcal{I}=\Esp\left(h(X)\right)=\int h(x)\, \P_X(dx).$$

En général, même si on sait évaluer $h$ en tout point, on ne peut pas calculer formellement l'intégrale $\mathcal{I}$. Le calcul d'intégrale par la méthode Monte-Carlo consiste dans sa version la plus simple à générer un *échantillon* $(X_1,\ldots,X_n) \sim_{i.i.d.}\P_X$, et à
estimer $\mathcal{I}$ par la moyenne empirique 
$$M_n(h)=\frac{1}{n}\sum_{i=1}^{n}h(X_i),$$
où i.i.d signifie indépendant et identiquement distribué. En effet, d'après la [loi forte des grands nombres](Probabilité III.pdf #lfgn), si $h(x)$ est $\P_X$-intégrable, on a l'assurance que quand $n \to +\infty$,
$$M_n(h) \rightarrow \int h(x)\P_X(dx) \text{ p.s.}$$
Si de plus $h(X)^2$ est intégrable, la vitesse de convergence de $M_n(h)$ peut être évaluée,
puisque la variance
$$\V(M_n(h)) = \frac{1}{n} \int \left(h(x)-\mathcal{I}\right)^2 \P_X(dx)$$
peut également être estimée à partir de l'échantillon
$(X_1,\ldots,X_n)$ par la quantité
$$\sigma_n^2=\frac{1}{n}\sum_{i=1}^{n}\left( h(X_i)-M_n(h)\right)^2.$$
Le [théorème central limite](Probabilité III.pdf #TCL) assure alors que pour $n$ grand,
$$\frac{M_n(h)-\mathcal{I}}{\sigma_n}$$
suit approximativement une loi $\No(0,1)$[^foot1]. Cette propriété conduit à la construction de tests de convergence et de bornes de
confiance asymptotiques pour $M_n(h)$. Par exemple, on aura
$$\P\left(\mathcal{I} \in \left[M_n(h) - 1.96 \sigma_n,M_n(h) + 1.96 \sigma_n\right]\right) \approx 0.95,$$
où $1.96 \approx \Phi^{-1}(0,975)$ avec $\Phi$ la fonction de répartition de la loi normale centrée réduite.

En outre, cette propriété indique que la vitesse de convergence de $M_n(h)$ est de l'ordre de $\sqrt{n}$, et ce indépendamment de la dimension du problème. Cela explique la supériorité de cette méthode par rapport aux méthodes d'intégration numérique déterministes dont les vitesses de convergence décroissent rapidement (exponentiellement) avec la dimension du problème.

[^foot1]: ce résultat sera démontré dans le cours de science des données au second semestre.

### Calcul numérique d'une probabilité {.exercise .question .two #mc1}
Calculer une estimation de la probabilité de l’événement $\sin(X) > 1/2$ pour $X$ de loi $\No (0, 1)$.

Indication : si x est un vecteur, `y=(np.sin(x)>1/2)` désigne le vecteur de booléens dont les coordonnées valent `True` ou `False` selon que les coordonnées correspondantes de `np.sin(x)` soient ou non > 1/2. Par ailleurs, les vecteurs de booléens se convertissent naturellement en vecteurs de 0 et de 1 si on leur applique une fonction dont les arguments sont des nombres (ex : `np.mean`).


# Génération de nombres pseudo-aléatoires

Les ordinateurs sont des machines déterministes. Il peut sembler paradoxal de leur demander de générer des nombres aléatoires[^vn]. En réalité, les algorithmes de génération de nombres aléatoires vont produire des séquences de nombres déterministes qui vont avoir l'aspect de l'aléatoire. On s'intéresse ici à la génération de nombres uniformes sur $]0,1[$ (on exclut les bornes par commodité), puisque, comme on le verra dans la suite, il s'agit de l'ingrédient de base de toutes les méthodes de simulation stochastique.

[^vn]:Von Neumann (1951) résume ce problème très clairement : "Any one who considers arithmetical methods of reproducing random digits is, of course, in
a state of sin. As has been pointed out several times, there is no such thing as a random number --- there are only methods of producing random numbers, and a
strict arithmetic procedure of course is not such a method. "

### Générateur de nombres uniformes pseudo-aléatoires {.definition} 
Un *générateur de nombres uniformes pseudo-aléatoires* est un algorithme qui étant donné une valeur initiale $u_0$ et une transformation $T$ produit une séquence $u_i=T^i(u_0)$, $i \in\N^\ast$, de valeurs dans $]0,1[$. 

Pour tout $n\in\N^\ast$, les valeurs $(u_1,\ldots,u_n)$ reproduisent le comportement d'une suite de variables aléatoires $(V_1,\ldots,V_n)$ i.i.d de loi uniforme sur ]0,1[, lorsqu'on les compare au travers d'un ensemble de tests statistiques[^diehard], vérifiant par exemple que la corrélation entre deux nombres successifs est suffisamment faible.

[^diehard]: Par exemple, la suite de tests [Die Hard](https://en.wikipedia.org/wiki/Diehard_tests), due à Marsaglia.

### la méthode des congruences {.example}
Cet algorithme, dû à @Lehmer, est l'un des premiers à avoir été proposé et implémenté. Il repose sur 2 paramètres :
 
 - le multiplicateur $a\in\N^\ast$,
 - le modulo $m\in\N^\ast$.

Etant donné un entier $k_0$ tel que $1 \leq k_0 \leq m-1$, la séquence de nombres est générée par la transformation suivante : pour tout $n\in\N^\ast$ on définit l'entier $k_{n+1} = a\,k_n\,\mathrm{\,mod\,} m$ puis on pose
$$u_{n+1} = \frac{k_{n+1}}{m},\hspace{1em} u_0 = \frac{k_0}{m}.$$

On peut remarquer que l'algorithme va produire une séquence de valeurs qui sera périodique, c'est-à-dire qu'après un certain nombre d'itérations, la suite se répétera, et qu'il pourra fournir au plus $m-1$ valeurs différentes. Ce trait est commun à tous les générateurs de nombre aléatoires et est lié aux limitations matérielles des ordinateurs (on ne peut représenter qu'un nombre fini de nombres). Le choix des valeurs de $a$ et $m$ est par conséquent crucial. Il existe des critères qui permettent de s'assurer du bon comportement de cette suite :

 * $m$ est un nombre premier (le plus grand possible),
 * $p = (m-1) /2$ est un nombre premier,
 * $a^p = -1 \mathrm{\,mod\,} m$.

Ce critère assure une période pleine et donc que tous les nombres $(1/m,\ldots,(m-1)/m)$ seront générés. Cependant, les nombres générés ne sont pas indépendants, pas même non corrélés. On peut montrer que la corrélation entre 2 nombres successifs vaut approximativement $1/a$. Il convient donc de choisir $a$ suffisamment grand pour que celle-ci devienne négligeable. Par exemple, en prenant $a=1000$ et $m=2001179$, on obtient une période de $2001178$ et une corrélation de l'ordre de $10^{-3}$.

Ce générateur de nombres uniformes pseudo-aléatoires, bien que rudimentaire, a ouvert la voie à des générateurs plus sophistiqués, toujours basés sur des opérations arithmétiques. Le plus couramment utilisé à ce jour est l'algorithme de [Mersenne-Twister](https://en.wikipedia.org/wiki/Mersenne_Twister). Il s'agit du générateur par défaut de la plupart des logiciels tels que Python, R, MATLAB, Julia, MS Excel,... Il passe notamment avec succès toute la batterie de tests Die Hard. En particulier, sa période vaut $2^{19937} - 1$.

Pour certains usages, cet algorithme n'est cependant pas recommandé du fait de sa prédictibilité. C'est notamment un défaut rédhibitoire pour les applications en cryptographie. Il existe des variantes mieux adaptées à ce cas de figure. On notera enfin qu'il existe des générateurs de nombres aléatoires basés sur des phénomènes physiques comme un bruit électrique ou des phénomènes quantiques et donc parfaitement imprévisibles.

# Méthodes de simulation de variables aléatoires réelles

On a vu au chapitre II du cours de Probabilités que l'on pouvait transformer des variables aléatoires réelles suivant certaines lois pour en obtenir de nouvelles. Par exemple, si $X_1,\dots,X_n$ sont $n\in\N^\ast$ variables gaussiennes centrées réduites indépendantes, alors $X_1^2+\dots,X_n^2$ suit une loi du $\chi^2$ à $n$ degrés de liberté. Dans le même esprit, on va voir ici comment simuler des v.a.r. de lois diverses à partir de la simulation de variables uniformes sur $]0,1[$. On introduit une notation qui sera utile dans la suite : pour spécifier que deux v.a.r. $X$ et $Y$ ont même loi, on écrira $X \overset{\L}{=} Y$.

## Méthode d'inversion

L'objectif de ce paragraphe est de définir quand et comment il est possible de simuler une variable aléatoire réelle $X$ de fonction de répartition (f.d.r.) $F_X$ en transformant la simulation d'une variable aléatoire $U$ de loi uniforme sur $]0,1[$. En d'autres termes, on cherche à déterminer les conditions sous lesquelles il est possible d'identifier une fonction borélienne $\psi :\,]0,1[ \to \R$ telle que $X \overset{\L}{=} \psi(U)$.

Commençons par un cadre simple, où $F_X$ est **bijective** d'un intervalle non vide de $\R$ sur $]0,1[$.

### Cas où $F_X$ est bijective {.proposition #invbij}
Soient $X$ une variable aléatoire réelle de fonction de répartition $F_X$ et $U$ une variable uniforme sur $]0,1[$. S'il existe un intervalle non vide $]a,b[ \subset \R$ tel que $F_X :\, ]a,b[ \to \,]0,1[$ est bijective, de bijection réciproque $F_X^{-1} :\, ]0,1[ \to ]a,b[$, alors $F_X^{-1}(U) \overset{\L}{=} X$ et $F_X(X) \overset{\L}{=} U$.

### Démonstration {.proof}
Le premier résultat est immédiat : pour tout $x\in\R$, par croissance de $F_X$ et donc de $F_X^{-1}$, on a
$$\P\left(F_X^{-1}(U)\leq x\right) = \P\left(U \leq F_X(x) \right) = F_X(x).$$
Concernant le second, notons $G$ la fonction de répartition de la variable aléatoire $F_X(X)$. La croissance de $F_X$ garantit que $\P\left(F_X(X) \in\, ]0,1[\right) = 1$. Ainsi, pour tout $x\in\R$ on a bien
$$G(x) = \left|\begin{array}{ll} 1 & \text{si } x \geq 1,\\ \P\left(F_X(X)\leq x\right) = \P\left( X \leq F_X^{-1}(x) \right) = x & \text{si } 0 < x < 1,\\ 0 & \text{sinon.}\end{array}\right.$$

### Exemples d'application 1 {.exercise .question .one #exemples1}
Donner un algorithme de simulation d'une v.a.r. $X$ suivant une loi

* uniforme sur un intervalle $I \subset \R$,
* Exponentielle de paramètre $\lambda \in \R_+^\ast$,
* de Cauchy, de densité $x\in\R \mapsto \left(\pi\left(1+x^2\right)\right)^{-1}$,
* de Laplace de paramètres $\mu \in \R$ et $s\in\R_+^\ast$, de densité $x\in\R \mapsto \frac{1}{2s}\,\exp\left\{-\frac{|x-\mu|}{s}\right\}$,
* Logistique de paramètres $\mu \in \R$ et $s\in\R_+^\ast$, de fonction de répartition $x\in\R \mapsto \left(1 + \exp\left\{-\frac{x-\mu}{s} \right\}\right)^{-1}$ ?

### {.anonymous}

Dans cette situation idéale, $\psi = F_X^{-1}$ est une solution à notre problème. Que se passe-t-il en revanche si $F_X$ n'est pas bijective ? 

### Pile ou face {.exercise .question .one #pf}
Proposer une méthode pour simuler un tir à pile ou face à partir de la simulation d'une variable uniforme sur $]0,1[$.

### {.anonymous}

On a déjà vu au chapitre II que les fonctions de répartition de v.a.r. possèdent un nombre au plus dénombrable de points de discontinuité. Sur chaque intervalle où elles sont continues, on peut alors considérer qu'elles sont bijectives, quitte à réduire les zones de palier à un point. Cela permet de généraliser la notion de bijection réciproque pour ces fonctions.

### Réciproque généralisée {.definition #defrecgen}
Soit $F$ une fonction de répartition. On définit sa *réciproque généralisée* (aussi appelée *inverse généralisée* ou *pseudo-inverse*) comme la fonction
$$F^{-} : u \in\, ]0,1[\, \mapsto \inf\left\{ x \in \R : F(x) \geq u \right\} \in \R.$$

### Conséquences {.remark} 

* Cette fonction est bien définie sur tout $]0,1[$, car quel que soit $u$ dans cet intervalle, l'ensemble $\left\{ x \in \R : F(x) \geq u \right\}$ est non vide et minoré. S'il était vide ou non minoré pour un certain $u_0\in\,]0,1[$, pour tout $x \in \R$ on aurait dans le premier cas $F(x) < u_0 < 0$ et dans le second $F(x) \geq u_0 > 1$. L'une comme l'autre de ces inégalités est impossible pour une fonction de répartition.
* La réciproque généralisée de la f.d.r. $F_X$ d'une v.a.r. $X$ est aussi appelée *fonction quantile*. On pourra notamment remarquer que $F_X^{-}\left(\frac{1}{2}\right)$ est la médiane de $X$.
* Lorsque $F$ réalise une bijection d'un intervalle non vide $I\subset \R$ sur $]0,1[$, sa réciproque généralisée coïncide avec sa bijection réciproque.

On a alors le résultat suivant, qui stipule que $\psi = F_X^-$ est une solution universelle à notre problème. La preuve détaillée est donnée en Annexe.

### Méthode d'inversion {.theorem #invgen}
Soient $U$ une variable uniforme sur $]0,1[$ ainsi que $X$ une variable aléatoire réelle de fonction de répartition $F_X$ et de réciproque généralisée $F_X^-$. Alors $F_X^-(U) \overset{\L}{=} X$. 

### Exemples d'application 2 {.exercise .question .one #exemples2}

Donner un algorithme de simulation d'une v.a.r. $X$ suivant une loi

* Binomiale de paramètres $n\in\N^\ast$ et $p \in\, ]0,1[$,
* Uniforme sur l'union de deux segments non vides et disjoints $[a,b], [c,d]\subset\R$, de densité $x\in\R \mapsto (b-a + d-c)^{-1}\,1_{[a,b]\cup[c,d]}(x)$ ?

### Limitations 
La méthode d'inversion peut sembler universelle pour simuler une v.a.r. $X$ à partir de $U \sim \mathcal{U}_{]0,1[}$. Cependant, elle nécessite en pratique de disposer d'une expression analytique de $F_X$ pour en déduire sa réciproque généralisée. Ce n'est typiquement pas le cas de nombreuses lois usuelles comme la loi Normale. On va donc déterminer d'autres procédures pour simuler des variables suivant de telles lois.

## Méthode de rejet

La méthode de rejet est une alternative populaire à la méthode d'inversion, lorsque cette dernière ne peut être utilisée directement et que **la loi cible possède une densité**. On la doit à @vonNeumann. Pour en comprendre le fondement, il nous faut d'abord introduire une généralisation naturelle de la loi uniforme dans $\R$ à tout $\R^d$ ($d\in\N^\ast$). On notera $\lambda$ la mesure de Lebesgue sur $\R^d$.

### Loi uniforme sur un borélien {.definition}
La loi uniforme sur un borélien $A\subset\R^d$ de volume $\lambda(A) > 0$ est une loi de probabilité admettant pour densité $$f : x\in\R^d \mapsto \dfrac{1_A(x)}{\lambda(A)}.$$

### Loi uniforme sur un pavé {.exercise .question .one #unipave}
Comment simuler un vecteur aléatoire $(U_1,\dots,U_d)$ de loi uniforme sur un pavé non vide $[a_1,b_1]\times\dots\times[a_d,b_d] \subset \R^d$ ?

### {.anonymous}

Une propriété fondamentale de cette loi est qu'elle reste stable par conditionnement, dans le sens suivant.

### Stabilité par conditionnement {.proposition #stabunif}
Soit $U$ un vecteur aléatoire de loi uniforme sur un borélien $A\subset\R^d$ de volume $\lambda(A) > 0$. Alors pour tout borélien $B \subset A$ de volume $\lambda(B) > 0$, la loi conditionnelle $\P_{U\mid U\in B}$ de $U$ sachant que $U \in B$ est uniforme sur $B$.

### Démonstration {.exercise .question .one #unicond}

### Simulation {.exercise .question .one #simunibor}
Déduire de la [proposition précédente](#stabunif) une méthode pour simuler un vecteur aléatoire de loi uniforme sur un borélien $B \subset \R^d$ **borné** et de volume $\lambda(B) > 0$.

### {.anonymous}

Il est aussi possible de simuler un vecteur aléatoire de loi uniforme sur certains boréliens non vides et non bornés, comme l'établit la proposition ci-dessous.

### Loi uniforme sur le sous-graphe d'une densité {.proposition #simunifdens} 
Soient une densité $f : \R \to \R$, une v.a.r. $X$ et une variable $U$ uniforme sur $]0,1[$, indépendante de $X$. On note $A_f := \left\{ (x,y) \in \R \times \R_+ : f(x) \geq y \right\}$ le domaine limité par le graphe de $f$ et l'axe des abscisses (souvent appelé sous-graphe de $f$). Si $X$ est de densité $f$, alors le couple $(X,Uf(X))$ suit une loi uniforme sur $A_f$. 

### Démonstration {.proof}
Commençons par remarquer que $\lambda(A_f) = 1$. Quel que soit $(z,v)\in\R^2$, par indépendance de $X$ et $U$ et par Fubini on a 
\begin{align*}
\P\left( X \leq z, Uf(X) \leq v \right) &= \int_\R \int_\R 1_{]-\infty,z]}(x)\,1_{]-\infty,v]}(uf(x))\,1_{]0,1[}(u)\,f(x)\,du\,dx\\
&= \int_{-\infty}^z \left(\int_\R 1_{]-\infty,v]\cap ]0,f(x)[}(uf(x))\,f(x)\,du\right)\,dx\\
&= \int_{-\infty}^z \int_{-\infty}^v 1_{]0,f(x)[}(u)\,du\,dx\\
& = \int_{-\infty}^z \int_{-\infty}^v 1_{A_f}(x,u)\,du\,dx.
\end{align*}
Ainsi, $(X,Uf(X))$ admet pour densité $1_{A_f}$, qui correspond bien à celle d'une loi uniforme sur $A_f$.

### {.anonymous}

Pour simuler un vecteur uniforme $(X,Y)$ sur un ensemble $A_f$ tel que défini à la proposition précédente, il suffit donc de simuler une v.a.r. $X$ de densité $f$, puis une variable $U$ uniforme sur $]0,1[$, et de poser $Y = f(X)U$.

En combinant les résultats précédents, on obtient la méthode de rejet, illustrée sur la figure ci-dessous, où $A_Y := \left\{ (x,y) \in \R \times \R_+ : y \leq f_Y(x) \right\}$.

### Méthode de rejet
On souhaite simuler une variable aléatoire réelle $X$ de densité $f_X$. Supposons que l'on sait simuler une variable $U$ uniforme sur $]0,1[$, ainsi qu'une v.a.r. $Y$ (par exemple avec la méthode d'inversion) de densité $f_Y$ telle qu'il existe un réel $a > 0$ pour lequel on a $\forall x \in \R$ : $f_X(x) \leq a\,f_Y(x)$. Il suffit alors de suivre l'algorithme suivant :

1. simuler $Y$ et $U$,

2. si $aUf_Y(Y) > f_X(Y)$, recommencer à l'étape 1.

3. poser $X = Y$.

![Méthode de rejet](images/MetRej.tex)

### Limitations 
La méthode de rejet a l'avantage de permettre de simuler des variables aléatoires à densité dont la fonction de répartition n'a pas de forme analytique, rendant la méthode d'inversion inapplicable. Néanmoins, pour pouvoir l'appliquer il faut connaître une densité auxiliaire qui, multipliée par un réel positif, majore la densité cible, et que l'on sait simuler. Le taux de rejet, c'est-à-dire la probabilité de l'événement $\{aUf_Y(Y) > f_X(Y)\}$, peut parfois être élevé, notamment lorsque la dimension de $X$ est grande, ce qui limite l'efficacité de la méthode.

### Taux de rejet {.exercise .two .question #tauxrej}
Calculer le taux de rejet de la méthode proposée ci-dessus.

## Simulation de variables aléatoires gaussiennes : Box-Muller

On a vu que la méthode d'inversion est inappropriée pour simuler une variable gaussienne, puisqu'elle requiert l'expression analytique de la fonction de répartition cible. Il existe des méthodes basées sur une intégration numérique de la densité gaussienne puis une inversion de cette approximation de la f.d.r. mais elle ne sont pas optimales en temps de calcul. La méthode de rejet est quant à elle sous-optimale, dans le sens où toutes les variables uniformes générées ne sont pas directement utilisées (une partie, potentiellement grande, est rejetée). La loi normale étant fondamentale en probabilité, il est plus que souhaitable de pouvoir en trouver une méthode de simulation exacte et efficace.

George E. P. Box et Mervin E. Muller ont proposé en 1958 une telle méthode (@BoxMuller). Elle exploite la propriété d'invariance par rotation de la densité d'un couple de variables gaussiennes indépendantes centrées réduites.

### Proposition {.proposition #boxmuller}
Soient $U$ et $V$ deux variables indépendantes, de loi uniforme sur $]0,1[$. Alors les variables aléatoires $X = \sqrt{-2\ln(U)}\cos\left(2\pi V\right)$ et $Y = \sqrt{-2\ln(U)}\sin\left(2\pi V\right)$ sont indépendantes et suivent toutes deux une loi normale centrée réduite.

### Démonstration {.proof}

On considère $(\widetilde{X},\widetilde{Y})$ un vecteur aléatoire dont les deux composantes sont indépendantes, de loi normale centrée réduite. On note ses coordonnées polaires aléatoires $\widetilde{R}$ et $\widetilde{\Theta}$. On a vu dans le cours de Probabilités II que dans ce cas, $\widetilde{R}$ et $\widetilde{\Theta}$ sont indépendantes, la première de densité $f_{\widetilde{R}} : r \in \R \mapsto r\,e^{-\frac{r^2}{2}} 1_{\R_+^\ast}(r)$ et la seconde de loi uniforme sur $]0,2\pi]$.

$X$ et $Y$ sont les coordonnées cartésiennes obtenues à partir d'un rayon et d'un angle : en posant $R = \sqrt{-2\ln(U)}$ et $\Theta = 2\pi V$ on obtient $X =R\cos(\Theta)$ et $Y = R\sin(\Theta)$. Par indépendance de $U$ et $V$, $R$ et $\Theta$ sont indépendantes. Pour que le vecteur $(X,Y)$ ait la même distribution que $(\widetilde{X},\widetilde{Y}) = \left(\widetilde{R}\cos(\widetilde{\Theta}),\widetilde{R}\sin(\widetilde{\Theta})\right)$, il suffit de montrer que $R \overset{\L}{=} \widetilde{R}$ et $\Theta \overset{\L}{=} \widetilde{\Theta}$.

* Commençons par étudier la loi de $R$, de fonction de répartition $F_R$. On remarque que la fonction $u\in\, ]0,1[ \mapsto \sqrt{-2\ln(u)} \in \R_+^\ast$ est bijective, strictement décroissante. Ainsi, pour tout $r\in\R_-$ on a $\P\left(R \leq r \right) = 0$ et pour tout $r \in \R_+^\ast$ on a
$$\P(R \leq r) = \P\left(\sqrt{-2\ln(U)} \leq r \right) = \P\left(U \geq e^{-\frac{r^2}{2}} \right) = 1 - e^{-\frac{r^2}{2}}.$$
qui correspond à la fonction de répartition associée à la densité $f_{\widetilde{R}}$.
$$\int_{-\infty}^r f_{\widetilde{R}}(x)\,dx = \left|\begin{array}{ll}\displaystyle \int_0^r x\,e^{-\frac{x^2}{2}}\,dx = \left[-e^{-\frac{x^2}{2}} \right]_0^r = 1 - e^{-\frac{r^2}{2}}  & \text{si } r>0,\\[1em] 0 & \text{sinon.} \end{array}\right.$$

* En ce qui concerne la loi de $\Theta$, de fonction de répartition $F_\Theta$, puisque la fonction $v \in\, ]0,1[\, \mapsto 2\pi v \in\, ]0,2\pi[$ est bijective strictement croissante, on a que pour tout $\theta \in \R$
$$F_\Theta(\theta) = \left|\begin{array}{ll} 1 & \text{si } \theta \geq 2\pi,\\ \P\left(V\leq \frac{\theta}{2\pi} \right) = \dfrac{\theta}{2\pi} & \text{si } \theta \in\, ]0,2\pi[,\\ 0 & \text{si } \theta \leq 0,\end{array}\right.$$
qui est bien la fonction de répartition d'une loi uniforme sur $]0,2\pi[$.

### {.anonymous}

Cette méthode permet de simuler directement deux variables gaussiennes centrées réduites indépendantes à partir de deux variables uniformes indépendantes. Pour simuler une variable gaussienne d'espérance $m \in \R$ et de variance $\sigma^2 \in \R_+^\ast$ quelconques, on se rappelera que si $X$ suit une loi normale centrée réduite, alors $\sigma X + m$ suit une loi normale d'espérance $m$ et de variance $\sigma^2$.

# Simulation d'un vecteur gaussien à densité
On souhaite simuler un vecteur gaussien $X = (X_1,\ldots,X_d)$ à valeurs dans $\R^d$ d'espérance $m$ et de matrice de covariance $C$ définie positive (et donc inversible) données. 

Puisque la matrice $C$ est définie positive, elle admet une racine carrée, c'est-à-dire qu'il existe une matrice $N$ telle que $C = N\,N^t$. En effet, on peut par exemple décomposer $C$ de la manière suivante :
$$C = V\,D\,V^t,$$
où $V$ est une matrice orthogonale et $D$ est la matrice diagonale dont les termes diagonaux sont les valeurs propres (toutes strictement positives) de $C$. Il suffit alors de prendre $N = V\,D^{1/2}$, où $D^{1/2}$ est la matrice diagonale dont les termes diagonaux sont les racines carrées des valeurs propres. 

En pratique, il est coûteux numériquement d'effectuer le calcul des valeurs propres et des vecteurs propres de $C$. On va plutôt calculer sa [*décomposition* ou *factorisation de Cholesky*](https://fr.wikipedia.org/wiki/Factorisation_de_Cholesky) qui permet d'écrire
$$C = L\,L^t$$
avec $L$ une matrice triangulaire inférieure [^chol].

[^chol]: Cette décomposition est très utile dans la résolution de systèmes linéaires de la forme $A\,x = b$, où $b$ est connu, $x$ inconnu et $A$ est définie positive. Cela revient à résoudre $L\,L^t\,x = b$. On pose alors $y = L^t\,x$ et on résout d'abord $Ly=b$, ce qui est très rapide puisque $L$ est triangulaire inférieure (on commence par $y_1 = b_1/L_{11}$, puis $y_2 = (b_2 - L_{21}y_1)/L_{22}$, etc. en descendant). On résout ensuite $L^t\,x = y$, ce qui est aussi très rapide pour la même raison (on commence par $x_n = y_n/L_{nn}$ puis on remonte).

Soit maintenant un autre vecteur gaussien $Y = (Y_1,\ldots,Y_d)$ à valeurs dans $\R^d$ et de matrice de covariance identité, notée $I_d$. Autrement dit, les $Y_i$ sont des variables aléatoires gaussiennes centrées, réduites et indépendantes.

Alors, le vecteur $Z = m + L\,Y$ est gaussien, d'espérance $m$ et de matrice de covariance $C$. En effet, $Z$ est gaussien comme combinaison linéaire de variables aléatoires gaussiennes, $\Esp(Z) = \Esp(m + L\,Y) = m$ et $\V(Z) = \Esp((L\,Y)^2) = L I_d L^t = C$.

# Echantillonnage d'importance

On introduit dans cette section la méthode d'échantillonnage d'importance (importance sampling en anglais), que l'on appelle aussi, de manière plus intuitive, échantillonnage préférentiel, pour les lois à densité. Pour ce faire, nous allons commencer par un exemple qui montre qu'il peut être plus efficace de simuler des valeurs selon une loi différente de celle d'intérêt, autrement dit de modifier la représentation de l'intégrale $\mathcal{I}$ sous la forme d'une espérance calculée selon une autre densité.

### Loi de Cauchy conditionnelle {.example}
Supposons que l'on s'intéresse à calculer la probabilité $p$ qu'une variable $X$ de loi de Cauchy standard soit plus grande que 2 (on peut le calculer directement et $p=0.15$)
$$p = \int_2^{+\infty} \frac{1}{\pi(1+x^2)}dx.$$
Si on estime $p$ directement à partir d'un échantillon $(X_1,\ldots,X_n)$ simulé selon la loi de Cauchy standard, soit
$$\widehat{p}_1 = \frac{1}{n}\sum_{i=1}^n 1_{X_i > 2},$$
la *variance de l'estimateur* $\V(\widehat{p}_1) = p(1-p)/n = 0.127/n$, puisque $\widehat{p}_1$ suit une loi binomiale de paramètre $(n,p)$. On peut réduire cette variance (et donc améliorer la qualité de l'estimateur) en tirant parti de la symétrie de la densité de la loi de Cauchy, en formant un second estimateur
$$\widehat{p}_2 = \frac{1}{n}\sum_{i=1}^n 1_{|X_i| > 2},$$
dont la variance vaut $\V(\widehat{p}_2) = p(1-p/2)/2n = 0.052/n$.
La relative inefficacité de ces méthodes est due au fait que la majeure partie des valeurs simulées seront en dehors de la zone d'intérêt $]2,+\infty[$. En passant par le complémentaire, on peut réécrire $p$ comme
$$p = \frac{1}{2} - \int_0^2 \frac{1}{\pi(1+x^2)}dx,$$
dont le second terme peut être vu comme l'espérance de $h(U) = \frac{2}{\pi(1+U^2)}$ avec $U\sim \mathcal{U}_{[0,2]}$. Tirant un échantillon $(U_1,\ldots,U_n)$ i.i.d. de loi uniforme sur $[0,2]$, on obtient un troisième estimateur :
$$\widehat{p}_3 = \frac{1}{2} - \frac{1}{n}\sum_{i=1}^n \frac{2}{\pi(1+U_i^2)},$$
dont la variance vaut $\V(\widehat{p}_3) = (\Esp(h(X)^2) - \Esp(h(U))^2)/n = 0.0285/n$ (par intégration par parties). Enfin, on peut encore réécrire (voir @ripley)
$$p = \int_0^{1/2}\frac{y^{-2}}{\pi(1+y^{-2})}dy,$$
qui peut être vue comme $\Esp\left(\frac{V^{-2}}{2\pi(1+V^{-2})}\right)$ avec $V\sim \mathcal{U}_{]0,1/2[}$. L'estimateur formé à partir de cette représentation et d'un échantillon $(V_1,\ldots,V_n)$ i.i.d. de loi uniforme sur $[0,1/2]$ a une variance de $0.95\, 10^{-4}/n$. Il est donc bien plus efficace que $\widehat{p}_1$ puisqu'il nécessite environ $\sqrt{10^3}\approx 32$ fois moins de simulations pour atteindre la même précision.

On a ainsi vu sur ce cas particulier que l'estimation d'une intégrale de la forme 
$$\mathcal{I}=\Esp\left(h(X)\right)=\int_{\R^d} h(x) f(x) dx,$$
peut s'écrire de différentes manières, en faisant varier $h$ et $f$. Par conséquent, un estimateur "optimal" devrait tenir compte de l'ensemble de ces possibilités. C'est justement l'idée développée dans la méthode d'échantillonnage d'importance dont le principe est décrit dans la définition suivante.

### Echantillonnage d'importance {.definition #is}
La méthode d'*échantillonnage d'importance* est une évaluation de $\mathcal{I}$ basée sur la simulation d'un
échantillon $X_1, \ldots,X_n$ de loi de densité $g$ et approximant :
$$\Esp_{f}\left(h(X)\right)\approx \frac{1}{n}\sum_{i=1}^{n}\frac{f(X_i)}{g(X_i)}h(X_i),$$
où la notation $\Esp_f$ signifie que l'espérance est calculée avec $X\sim f$. On appelle souvent les ratios $\frac{f(X_i)}{g(X_i)}$ les *poids d'importance* que l'on note $w_i$.

Cette méthode est basée sur la représentation suivante de $\mathcal{I}$ :

$$\Esp_{f}\left[h(X)\right]=\int h(x)\frac{f(x)}{g(x)}g(x)\,dx$$

que l'on appelle l'*identité fondamentale de l'échantillonnage d'importance* et l'estimateur converge du fait de la [loi forte des grands nombres](Probabilité III.pdf #lfgn). 

Cette identité indique qu'une intégrale du type $\mathcal{I}$ n'est pas intrinsèquement associée à une loi donnée. L'intérêt de l'échantillonnage d'importance repose sur le fait qu'il n'y a aucune restriction sur le choix de la densité $g$, dite *instrumentale*, que l'on peut donc choisir parmi les densités des lois que l'on sait simuler aisément. Il y a bien évidemment des choix qui sont meilleurs que d'autres. Remarquons tout d'abord que bien que l'estimateur proposé dans la [définition ci-dessus](#is) converge presque sûrement, sa variance est finie si
$$\Esp_g\left(h^2(X)\frac{f^2(X)}{g^2(X)}\right) = \Esp_f\left(h^2(X)\frac{f(X)}{g(X)}\right) = \int h^2(x)\frac{f^2(x)}{g(x)}\,dx < \infty.$$
On préconise alors l'usage de densités instrumentales $g$ dont la queue de distribution est plus épaisse que celle de $f$ pour éviter que cette variance puisse être infinie (on notera que cela dépend aussi de la fonction $h$ à intégrer). En pratique, on utilise généralement l'estimateur suivant, de variance finie et qui donne des résultats plus stables numériquement que celui de la définition :
$$\frac{\sum_{i=1}^{n}w_ih(X_i)}{\sum_{i=1}^n w_i}$$
où on a remplacé $n$ par la somme des poids d'importance. Puisque $\frac{1}{n}\sum_{i=1^n}w_i = \frac{1}{n}\sum_{i=1}^n\frac{f(x_i)}{g(x_i)}$ tend vers 1 quand $n\to\infty$, cet estimateur converge presque sûrement vers $\Esp_{f}\left(h(X)\right)$ par la loi forte des grands nombres (voir @roca).

Parmi les densités $g$ qui fournissent des estimateurs de variance finie, il est possible d'exhiber la densité optimale (au sens de la variance de l'estimateur associé) pour une fonction $h$ et une densité $f$ données.

### Densité optimale {.theorem}
Le choix de $g$ qui minimise la variance de l'estimateur donné dans la [définition ci-dessus](#is) est 
$$g^\ast(x) = \frac{|h(x)|f(x)}{\int |h(x)|f(x) dx}.$$

### Démonstration {.proof}
Notons d'abord que
$$\V_g\left(\frac{h(X)f(X)}{g(X)}\right) = \Esp_g\left(h^2(X)\frac{f^2(X)}{g^2(X)}\right) - \Esp_g\left(h(X)\frac{f(X)}{g(X)}\right)^2$$
et le second terme ne dépend pas de $g$. On minimise donc le premier terme. D'après l'inégalité de Jensen, on a
$$\Esp_g\left(h^2(X)\frac{f^2(X)}{g^2(X)}\right) \geq \Esp_g\left(|h(X)|\frac{f(X)}{g(X)}\right)^2 = \left(\int|h(x)|f(x)dx\right)^2,$$
qui nous donne une borne inférieure indépendante du choix de $g$. Elle est atteinte en prenant $g=g^\ast$.

### {.anonymous}
Ce résultat formel n'a que peu d'intérêt pratique : le choix optimal de $g$ fait intervenir $\int|h(x)|f(x)dx$, qui est à une valeur absolue près la quantité que l'on souhaite estimer ! Il suggère néanmoins de considérer des densités $g$ telles que $|h|f/g$ est quasi constante et de variance finie. On se reportera au chapitre 3 de @roca pour des exemples où un bon choix de $g$ permet des améliorations considérables par rapport à des estimateurs de Monte-Carlo plus naïfs.

<!-- # Contrôle de la variance de Monte-Carlo

On clôt ce chapitre par quelques considérations à propos de la convergence des estimateurs que l'on peut contrôler en calculant leur variance. Au début de ce chapitre, on a mentionné l'usage du TCL pour s'assurer de la convergence de 
$$M_n(h)=\frac{1}{n}\sum_{i=1}^{n}h(X_i),~~~X_i \sim \P_X$$
vers l'intégrale d'intérêt
$$\mathcal{I}=\Esp\left(h(X)\right)=\int_{\R^d} h(x) \P_X(dx).$$
On a montré qu'à partir d'un échantillon on peut construire un intervalle de confiance asymptotique à 95\% pour la quantité $\mathcal{I}$. En revanche,  -->

Exercices
===============================================================================

## Loi uniforme dans un domaine 

Ecrire un algorithme pour simuler un point uniforme dans les trois domaines représentés ci-dessous.

![Domaine A](images/ex1-eps-converted-to.pdf){ width=30% } 

![Domaine B](images/ex2-eps-converted-to.pdf){ width=30% } 

![Domaine C](images/ex3-eps-converted-to.pdf)

## Simulation selon la loi géométrique

Cette loi correspond à la loi du nombre d'essais avant d'obtenir un
évènement de probabilité $p$
$$X\sim{\cal G} (p)~~\P (X=n)=p(1-p)^{n-1}~~n=1,2,\ldots$$

### Question 1 {.question #loigeom1}
Calculer l'espérance et la variance de $X$
    
### Question 2 {.question #loigeom2}
Générer un échantillon de taille 1000 pour $p=0.6$, en utilisant une approche génétique. Calculer la moyenne et la variance. Comparer avec les valeurs théoriques.
    
### Question 3 {.question #loigeom3}
Montrer que si $X\sim{\cal E}(\lambda)$, alors $\lceil X \rceil \sim{\cal G}(p)$. On précisera la valeur de $\lambda$.
    
### Question 4 {.question #loigeom4}
Donner, implémenter et tester un algorithme pour simuler ${\cal G}(p)$ directement

## Simulation de la loi gaussienne par la méthode de rejet

$X$ est une variable aléatoire de loi gaussienne d'espérance $m=0$ et de variance $\sigma^2=1$, $\No(0,1)$. Sa densité est
  $$f(x) = \frac{1}{\sqrt{2\pi}}\exp\left(-\frac{1}{2}x^2\right),~x\in \R$$
  
### Question 1 {.question #lgrej1}
Montrer que $f(x) \leq C \exp \left(-|x|\right)$ où $C=\sqrt{\frac{e}{2\pi}}$

### Question 2 {.question #lgrej2}
On considère $g(x) = \frac{1}{2}\exp \left(-|x|\right),~x\in \R$. Montrer que $g$ est une densité de probabilité.

### Question 3 {.question #lgrej3}
Proposer un algorithme pour simuler selon $g$.

### Question 4 {.question #lgrej4} 
Implémenter l'algorithme de rejet pour simuler selon $f$.

## Simulation selon la loi de Wigner {.question #wigner}

La loi de Wigner (ou du demi-cercle) est la loi de support $[-2, 2]$ et de densité $f(x) = \frac{1}{2\pi}\sqrt{4 - x^2}$. Simuler un grand nombre de variables aléatoires de loi de Wigner, représenter l'histogramme associé et le comparer à la densité. 

## Loi des grands nombres et théorème central limite

### Question 1 {.question #lgntcl1}
Afin d’illustrer la [Loi des Grands Nombres](Probabilité IV.pdf #lfgn), visualiser la suite $S_n = \frac{X_1 + \ldots +X_n}{n}$
pour $(X_i)_{i \in \N^\ast}$ une suite de variables aléatoires indépendantes de loi uniforme sur [-1, 1].

Indication : pour $x= [x_1 , \ldots, x_n]$ vecteur, `np.cumsum(x)` est le vecteur
$[x_1 , x_1 + x_2 , x_1 + x_2 + x_3 , \ldots , x_1 + \ldots + x_n]$
des sommes cumulées des coordonnées de $x$.

### Question 2 {.question #lgntcl2}

Faire de même avec des variables aléatoires $Y_i$ de loi de Cauchy (c'est-à-dire de densité $\frac{1}{\pi(1+x^2)}$). La suite $\frac{Y_1 + \ldots +Y_n}{n}$ semble-t-elle converger ? Pourquoi ?

### Question 3 {.question #lgntcl3}

Calculer la moyenne $\mu$ et l’écart-type $\sigma$ des $X_i$ et vérifier, afin d’illustrer le [Théorème Central Limite](Probabilité IV.pdf #TCL), que 
$\sqrt{n} (S_n - \mu)/\sigma$ converge en loi, lorsque $n \to \infty$, vers une variable de loi $\mathcal{N}(0, 1)$ : on se fixera une grande valeur de n, on simulera un grand nombre de fois $\sqrt{n} (S_n - \mu)/\sigma$, on en tracera l’histogramme et on le comparera à la densité $(2\pi)^-1/2 e^{-x^2}$ la loi $\mathcal{N}(0, 1)$.

## Simulation d'un mélange de gaussiennes

On souhaite simuler selon la loi de mélange introduite dans l'exercice Mélange de loi du chapitre 3.

### Question 1 {.question #melloi1}
Soit $K$ une v.a.r. de loi :
$$\mathbb{P}(K=x) = \left\{\begin{array}{ll} 1/2 & \text{ si }x = 1 \\ 1/4 & \text{ si }x = 2 \\ 1/4 & \text{ si }x = 3 \\ 0 & \text{ sinon} \end{array} \right.$$
Implémenter la méthode d'inversion pour simuler $K$

### Question 2 {.question #melloi2}
Soit $X_1$, $X_2$ et $X_3$ des variables aléatoires de lois respectives $\mathcal{N}(0,1)$, $\mathcal{N}(5,1/2)$ et $\mathcal{N}(8,4)$. Implémenter un algorithme de simulation de $X_K$. Comparer l'histogramme obtenu pour un échantillon de taille 1000 avec la densité de $X_K$.

## Echantillonnage d'importance

On cherche à évaluer l'espérance d'une variable aléatoire $X$ gaussienne centrée réduite (de densité $f_X$ et de f.d.r. $F_X$) sachant qu'elle dépasse la valeur 3.

### Question 1 {.question #echimp1}
Exprimer la densité conditionnelle de $X|X>3$.

### Question 2 {.question #echimp2}
Calculer la quantité souhaitée à partir d'un échantillon de taille 1000 généré selon $F_X$. Quelle est la valeur du taux de rejet ?

### Question 3 {.question #echimp3}
Implémenter l'algorithme d'échantillonnage d'importance en prenant comme loi instrumentale la loi gaussienne d'espérance 3 et de variance 1. Quelle est la proportion de poids nuls ?


-----------------------------------------------------------

Solutions
=================================================================================

### Calcul numérique d'une probabilité {.answer .two #answer-mc1}
cf. notebook

### Exemples d'application 1 {.answer  .one #answer-exemples1}
On suppose que $U \sim \mathcal{U}_{]0,1[}$

* Uniforme sur un intervalle $I \subset \R$ : 

    Si $I = ]a,b[,~a< b$, alors la fonction de répartition de $X \sim \mathcal{U}_I$ est $F_X(x) = \frac{x-a}{b-a} 1_{]a,b[}(x) + 1_{[b,+\infty[}(x)$, d'où par inversion $X = a + (b-a)U$ 

* Exponentielle de paramètre $\lambda \in \R_+^\ast$ : 

    la fonction de répartition de $X \sim \mathcal{E}(\lambda)$ est $F_X (x) = 1-\exp(-\lambda x)$, d'où par inversion $X = -\frac{\ln(1-U)}{\lambda}$. Pour simplifier, on remarquera que si $U \sim \mathcal{U}_{]0,1 [ }$ , alors $1- U \sim \mathcal{U}_{]0,1[}$, d'où $X = -\frac{\ln(U)}{\lambda}$

* de Cauchy, de densité $x\in\R \mapsto \left(\pi\left(1+x^2\right)\right)^{-1}$,

    la loi de Cauchy admet la fonction de répartition $F(x) = \frac{1}{\pi} \arctan (x) + \frac{1}{2}$, d'où $X = \tan(\pi U -1/2)$

* de Laplace de paramètres $\mu \in \R$ et $s\in\R_+^\ast$, de densité $x\in\R \mapsto \frac{1}{2s}\,\exp\left\{-\frac{|x-\mu|}{s}\right\}$,

    la loi de Laplace admet la fonction de répartition 
    $$F(x) = \left\{ \begin{array}{ll}
    \frac{1}{2} \exp(x) & \text{ si } x < 0,\\
    1 - \frac{1}{2} \exp(-x) & \text{ si } x \geq 0,
    \end{array} \right. = \frac{1}{2}\left(1 + \text{sgn}(x)(1-\exp(-|x|))\right)$$

    d'où $X = \text{sgn}(U - 1/2)\ln(1-2|U-1/2|)$, où sgn est la fonction signe.

* Logistique de paramètres $\mu \in \R$ et $s\in\R_+^\ast$, de fonction de répartition $x\in\R \mapsto \left(1 + \exp\left\{-\frac{x-\mu}{s} \right\}\right)^{-1}$ :

    par inversion, $X = s \left(-\ln\left(\frac{1}{U}-1\right)+ \mu\right)$  

### Pile ou face {.answer  .one #answer-pf}
Il suffit d'associer à "pile" un événement portant sur $U \sim \mathcal{U}_{]0,1[}$ de la bonne probabilité, $p \in ]0,1[$, par exemple $\{U \leq p\}$. On obtient ainsi l'algorithme :
    
1. Générer $u$ selon $\mathcal{U}_{]0,1[}$
2. Renvoyer "pile" si $u \leq p$, "face" sinon

### Exemples d'application 2 {.answer  .one #answer-exemples2}

* Binomiale de paramètres $n\in\N^\ast$ et $p \in\, ]0,1[$,

    La fonction de répartition de la loi binomiale est donnée par 
    $$F(x) = \begin{cases}
    0&\text{si } \;x<0\\
    \sum_{{k=0}}^{{\lfloor x\rfloor }}{n \choose k}p^{k}(1-p)^{{n-k}} & \text{si } \;0\leq x<n\\
    1&\text{si} \;x \geq n
    \end{cases}$$
    
    où ${\lfloor x\rfloor }$ est la partie entière de $x$.   
    On peut alors découper $]0,1[$ en intervalles de la forme $]\sum_{{k=0}}^{{m}}{n \choose k}p^{k}(1-p)^{{n-k}},\sum_{{k=0}}^{{m+1}}{n \choose k}p^{k}(1-p)^{{n-k}}[$ pour $m \in \{0,n-1\}$ et renvoyer $m+1$ si un $u$ généré selon $\mathcal{U}_{] 0,1[}$ appartient à l'un de ces intervalles, 0 sinon.

    Il est cependant beaucoup plus simple de remarquer qu'une variable aléatoire de loi $\mathcal{B}(n,p)$ s'obtient comme la somme de $n$ variables de Bernoulli que l'on peut simuler comme [ci-dessus](#answer-pf).

<!-- * de Poisson de paramètre $\lambda \in \R_+^\ast$,

    La fonction de répartition de la loi de Poisson est 
    $$ F(x) = \begin{cases}
    0&\text{si } \;x<0\\
    \sum_{{k=0}}^{{\lfloor x\rfloor }} \frac{\lambda^k}{k!} e^{-\lambda} & \text{sinon}\\
    \end{cases}
    On peut encore procéder en découpant $]0,1[$ en intervalles de longueur $\frac{\lambda^k}{k!} e^{-\lambda}$ pour $k \in \N$ mais cela devient vite peu commode pour les grandes valeurs de $k$.
 -->
    
* Uniforme sur l'union de deux segments non vides et disjoints $[a,b], [c,d]\subset\R$, de densité $x\in\R \mapsto (b-a + d-c)^{-1}\,1_{[a,b]\cup[c,d]}(x)$

    La fonction de répartition d'une telle variable est 
    $$F(x) = \frac{x-a}{b-a + d-c} 1_{]a,b[}(x) + \frac{b-a}{b-a + d-c} 1_{[b,c]}(x) + \frac{x-c+b-a}{b-a + d-c} 1_{]c,d[}(x) + 1_{[d,+\infty[}(x)$$
    Pour simuler cette variable, on peut donc utiliser l'algorithme suivant :
    
    1. Générer $u$ selon $\mathcal{U}_{]0,1[}$
    2. Retourner
    $$\begin{cases} 
    a + u(b-a + d -c) & \text{ si } u \in ]0,\frac{b-a}{b-a + d-c}[ \\
    c + (u(b-a + d -c) - (b-a)) \text{ sinon }
    \end{cases}$$

### Loi uniforme sur un pavé {.answer  .one #answer-unipave}
On note $[a_1,b_1]\times\dots\times[a_d,b_d] \subset \R^d$.
On peut voir que la densité d'une v.a. uniforme sur un tel pavé s'écrit $f(x) = \frac{1}{b_1 - a_1} \cdots \frac{1}{b_d - a_d} 1_{[a_1,b_1]\times\dots\times[a_d,b_d]}(x)$ soit comme le produit des densités de ses coordonnées qui sont donc indépendantes. On peut donc simuler la variable d'intérêt avec cet algorithme :

1. Générer $u_1,\ldots,u_d$ indépendamment selon $\mathcal{U}_{]0,1[}$
2. Retourner $(a_1 + u_1(b_1-a_1), \ldots, a_d + u_d(b_d-a_d))$ 

### Démonstration {.answer  .one #answer-unicond}
Soit $C \in \B(B)$ (considérer les boréliens de $B$ suffit à caractériser la loi conditionnelle à l'événement $U \in B$ puisque si $C \cap B = \varnothing$, alors nécessairement, $\P(U \in C |U \in B) = 0$). On a 
\begin{align*}
\P(U \in C |U \in B) & = \frac{\P(U\in C, U \in B)}{\P(U \in B)} = \frac{\P(U\in C)}{\P(U \in B)} \\
& = \frac{\int_C \frac{dx}{\lambda(A)}}{\int_B \frac{dx}{\lambda(A)}} \text{ puisque } U \sim \mathcal{U}_A \\
& = \frac{\lambda(C)}{\lambda(B)} = \int_C \frac{1}{\lambda(B)} dx
\end{align*}
on reconnaît bien la loi uniforme sur $B$.

### Simulation {.answer  .one #answer-simunibor}
On prend un pavé $R$ tel que $B \subset R$ puis on applique l'algorithme suivant :
 
1. générer $u$ selon $\mathcal{U}_R$
2. Si $u \notin R$, retour en 1.
3. retourner $u$

### Taux de rejet {.answer .two  #answer-tauxrej}
Puisque le couple $(Y, Uf_Y(Y))$ est uniforme sur $A_f$, alors le couple $(Y, aUf_Y(Y))$ est uniforme sur $A_{af}$, d'où
\begin{align*}
\P(\{aUf_Y(Y) > f_X(Y)\}) & = \Esp(1_{\{aUf_Y(Y) > f_X(Y)\}}) \\
& = \Esp(\Esp(1_{\{aUf_Y(y) > f_X(y)\}}|Y=y)) \\
& = \int_R \int_0^{af_Y(y)} 1_{\{auf_Y(Y) > f_X(Y)\}} \frac{1}{af_Y(y)} du f_Y(y) dy \\
& = \int_R \left(1 - \frac{f_X(y)}{af_Y(y)}\right) f_Y(y) dy \\
& = 1 - \frac{1}{a}
\end{align*}

## Loi uniforme dans un domaine 

cf. notebook

## Simulation selon la loi géométrique

### Question 1 {.answer #answer-loigeom1}
$\P(X=n) = p (1-p)^{n-1} = (1-q)q^{n-1} \text{, où } p \text{ est la probabilité de succès, } n=1,2,\ldots$
\begin{align*}
\Esp[X]&=\sum_{i=1}^{\infty}i\P(X=i)\\
&=\sum_{i=1}^{\infty} i (1-q)q^{i-1}\\
&=(1-q)\sum_{i=1}^{\infty} iq^{i-1}\\
&=(1-q)\sum_{i=1}^{\infty} \frac{\mathrm{d}}{\mathrm{d} q} q^i\\
&=(1-q)\frac{\mathrm{d}}{\mathrm{d} q}\left(\sum_{i=1}^{\infty}  q^i\right)\\
&=(1-q)\frac{\mathrm{d}}{\mathrm{d} q}\left(\frac{q}{1-q}\right), \text{ car } \sum_{i=1}^{\infty}  q^i = q \sum_{i=0}^{\infty}  q^i = \frac{q}{1-q}\\
&=(1-q)\frac{1}{(1-q)^2} \\
&=\frac{1}{(1-q)}\\
&=\frac{1}{p}
\end{align*}
\bigskip
Pour la variance $\V[X] = \Esp[X^2]-\Esp[X]$
\begin{align*}
\Esp[X^2]&=\sum_{i=1}^{\infty}i^2\P(X=i)\\
&=\sum_{i=1}^{\infty} i^2 (1-q)q^{i-1}\\
&=(1-q)\sum_{i=1}^{\infty} i^2q^{i-1}\\
&=(1-q)\sum_{i=1}^{\infty}\left( i\left((i+1)q^{i-1} - q^{i-1}\right)\right)\\
&=(1-q)\sum_{i=1}^{\infty}\left( i(i+1)q^{i-1} - iq^{i-1}\right)\\
&=(1-q)\sum_{i=1}^{\infty}\left( \frac{\mathrm{d}^2}{\mathrm{d} q^2} q^{i+1} - \frac{\mathrm{d}}{\mathrm{d} q} q^i\right)\\
&=(1-q)\left( \frac{\mathrm{d}^2}{\mathrm{d} q^2}\left(\sum_{i=1}^{\infty}q^{i+1}\right)-\frac{\mathrm{d}}{\mathrm{d} q}\left(\sum_{i=1}^{\infty}  q^i\right)\right)
\end{align*}
On a déjà calculé le second terme ci-dessus.
\begin{align*}
\frac{\mathrm{d}^2}{\mathrm{d} q^2}\sum_{i=1}^{\infty}q^{i+1} &= \frac{\mathrm{d}^2}{\mathrm{d} q^2}q \sum_{i=1}^{\infty}q^{i}\\
&=\frac{\mathrm{d}^2}{\mathrm{d} q^2}\frac{q^2}{1-q}
\end{align*}
Calcul des dérivées :
\begin{align*}
\frac{\mathrm{d}}{\mathrm{d} q}\frac{q^2}{1-q} &= \frac{2q(1-q)+q^2}{(1-q)^2}\\
&= \frac{2q-q^2}{(1-q)^2}
\end{align*}

\begin{align*}
\frac{\mathrm{d}}{\mathrm{d} q}\frac{2q-q^2}{(1-q)^2}&=\frac{2(1-q)(1-q)^2+2(1-q)(2q-q^2)}{(1-q)^4}\\
&= \frac{2(1-q)^2+2(2q-q^2)}{(1-q)^3}\\
&= \frac{2 - 4q +2q^2 + 4q -2q^2}{(1-q)^3}\\
&= \frac{2}{(1-q)^3}
\end{align*}
On en déduit
\begin{align*}
\Esp[X^2]&=(1-q)\left(\frac{2}{(1-q)^3}-\frac{1}{(1-q)^2}\right)\\
&=\frac{2}{(1-q)^2}-\frac{1}{(1-q)}\\
&=\frac{2-(1-q)}{(1-q)^2}\\
&=\frac{1+q}{(1-q)^2}
\end{align*}
Et finalement
\begin{align*}
\V[X] &= \Esp[X^2]-\Esp[X]\\
&= \frac{1+q}{(1-q)^2}-\frac{1}{(1-q)^2}\\
&=\frac{q}{(1-q)^2}\\
&=\frac{1-p}{p^2}
\end{align*}


### Question 2 {.answer #answer-loigeom2}
cf. notebook

### Question 3 {.answer #answer-loigeom3}
\begin{align*}
\P(\lceil X \rceil = n) & = \P(n-1 < X \leq n) \\
& = F_X(n) - F_X(n-1) \\
& = e^{-\lambda (n-1)}(1-e^{-\lambda})
\end{align*}
d'où $\lambda = -\ln(1-p)$
    
### Question 4 {.answer #answer-loigeom4}
cf. notebook 

## Simulation de la loi gaussienne par la méthode de rejet

$X$ est une variable aléatoire de loi gaussienne d'espérance $m=0$ et de variance $\sigma^2=1$, $\No(0,1)$. Sa densité est
  $$f(x) = \frac{1}{\sqrt{2\pi}}\exp\left(-\frac{1}{2}x^2\right),~x\in \R$$
  
### Question 1 {.answer #answer-lgrej1}
Soit $x \in \R$
\begin{align*}
x^2 & \geq 2|x| - 1 \\
\frac{1}{\sqrt{2\pi}}e^{-x^2/2} & \leq \sqrt{\frac{e}{2\pi}} e^{-|x|}
\end{align*}

### Question 2 {.answer #answer-lgrej2}
$g$ est bien positive et son intégrale sur $\R$ vaut
$$\int_\R g(x) dx = \int_\R \frac{1}{2} e^{-|x|} dx = \int_{\R^+} e^{-x} dx = 1$$

### Question 3 {.answer #answer-lgrej3}
voir dans [exemples d'application 1](#exemples1). 

### Question 4 {.answer #answer-lgrej4} 
cf. notebook

## Simulation de la loi de Wigner {.answer #answer-wigner}
cf. notebook

## Loi des grands nombres et théorème central limite

### Question 1 {.answer #answer-lgntcl1}

cf. notebook

### Question 2 {.answer #answer-lgntcl2}

cf. notebook

### Question 3 {.answer #answer-lgntcl3}

cf. notebook

## Simulation d'un mélange de gaussiennes

### Question 1 {.answer #answer-melloi1}
cf. notebook

### Question 2 {.answer #answer-melloi2}
cf. notebook

## Echantillonnage d'importance

### Question 1 {.answer #answer-echimp1}
On a $F_{X|X>3}(x) = \P(X \leq x |X > 3) = \frac{\P(X\leq x, X>3)}{1-F_X(3)} = \frac{F_X(x)-F_X(3)}{1-F_X(3)}1_{]3,+\infty[}(x)$
d'où $f_{X|X>3}(x) = \frac{f_X(x)}{1-F_X(3)}1_{]3,+\infty[}(x)$

### Question 2 {.answer #answer-echimp2}
cf. notebook

### Question 3 {.answer #answer-echimp3}
cf. notebook

# Annexe

## Preuve de la méthode d'inversion

Pour pouvoir démontrer le [théorème de la méthode d'inversion](#invgen), il faut d'abord établir un certain nombre de propriétés de la réciproque généralisée d'une fonction de répartition. Elle peuvent être visualisées sur la figure ci-dessous.

### Proposition {.proposition #proprecgen}
Soit $F$ une fonction de répartition. Alors sa réciproque généralisée $F^-$ satisfait les propriétés suivantes.

1. $F^-$ est croissante.

2. $\forall\, x \in \R$ : $F^- \circ F (x) \leq x$.

3. $\forall\, u \in\, ]0,1[$ : $F \circ F^-(u) \geq u$ avec égalité si $u \in F(\R)$.

4. $\forall\, (u,x) \in\, ]0,1[\, \times \R$ : $\left\{F(x) \geq u\right\} \Leftrightarrow \left\{x \geq F^-(u)\right\}$ et  $\left\{F(x) < u\right\} \Rightarrow \left\{x \leq F^-(u)\right\}$.

### Démonstration {.proof}
Pour tout $u \in\, ]0,1[$ on note $F^{-1}\left([u,1]\right) := \left\{x \in \R : F(x) \geq u\right\}$ l'image réciproque de $[u,1]$ par $F$.

1. Soit $(u,v) \in\, ]0,1[^2$. Si $u < v$ alors $F^{-1}\left([v,1]\right) \subset F^{-1}\left([u,1]\right)$ d'où $F^-(u) = \inf F^{-1}\left([u,1]\right) \leq \inf F^{-1}\left([v,1]\right) = F^-(v)$. La fonction $F^-$ est donc bien croissante.

2. Soit $x \in \R$, alors $F^- \circ F(x) = \inf \bigl\{ z \in \R : F(z) \geq F(x) \bigr\} = \inf F^{-1}\left(\left[F(x),1\right]\right)$. Comme $F$ est croissante sur $\R$ on a $[x,+\infty[\, \subseteq F^{-1}\left(\left[F(x),1\right]\right)$ donc $F^- \circ F(x) = \inf F^{-1}\left(\left[F(x),1\right]\right) \leq \inf [x,+\infty[\, = x$.

3. Soit $u \in\, ]0,1[$. 
* Puisque $F^{-1}\left([u,1]\right)$ est nécessairement non vide, il existe une suite décroissante $(x_n)_{n\in\N} \subseteq F^{-1}\left([u,1]\right)$ convergeant vers $\inf F^{-1}\left([u,1]\right) = F^-(u)$. La croissance de $F$ implique que la suite $\bigl(F(x_n)\bigr)_{n\in\N}$ est elle aussi décroissante, minorée par $u$ car $(x_n)_{n\in\N} \subseteq F^{-1}\left([u,1]\right)$ donc convergente. Sa limite est de même supérieure ou égale à $u$. Comme $F$ est continue à droite, cette dernière n'est autre que $$\lim_{n \rightarrow +\infty} F(x_n) = F\left(\lim_{n\rightarrow+\infty} x_n\right) = F \circ F^-(u).$$
Nous avons donc bien $F\circ F^-(u) \geq u$.
* Supposons maintenant que $u \in F(\R)$. Alors $F^{-1}\left(\{u\}\right) := \left\{x \in \R : F(x) = u\right\} \neq \varnothing$. Il existe donc une suite décroissante $(x_n)_{n\in\N} \subseteq F^{-1}\left(\{u\}\right)$ convergeant vers $\inf F^{-1}\left(\{u\}\right) = F^-(u)$ par croissance de $F$. Comme $F$ est continue à droite en tout point de $\R$ et $F(x_n) = u$ pour tout $n \in \N$, on a bien $$u = \lim_{n \rightarrow +\infty} F(x_n) = F\left(\lim_{n\rightarrow+\infty} x_n\right) = F \circ F^-(u).$$

4. Soit $(u,x) \in\, ]0,1[\, \times \R$.
* **Equivalence.** Supposons $F(x) \geq u$. On a $F^- \circ F(x) \geq F^-(u)$ par croissance de $F^-$ (propriété 1.) et $F^- \circ F(x) \leq x$ d'après la propriété 2. Réciproquement, supposons que $x \geq F^-(u)$. Alors par croissance de $F$ on a $F(x) \geq F \circ F^-(u)$ puis $F \circ F^-(u) \geq u$ d'après la propriété 3.
* **Implication.** Supposons $F(x) < u$. Tout $z \in F^{-1}\left([u,1]\right)$ vérifie $F(z) \geq u > F(x)$. Comme $F$ est croissante sur $\R$ on a donc $z \geq x$, ce qui implique $x \leq \inf F^{-1}\left([u,1]\right) = F^-(y)$.

### {.anonymous}

![Réciproque généralisée d'une fonction de répartition](images/RecGen.tex)

Nous pouvons maintenant établir la preuve du [théorème de la méthode d'inversion](#invgen).

### Démonstration -- Méthode d'inversion {.proof}
Soient $x \in \R$ et $(\Omega,\A,\P)$ l'espace probabilisé sur lequel sont définies $U$ et $X$. D'après la propriété 4 ci-dessus, on a $\left\{\omega \in \Omega : F_X^-(U(\omega)) \leq x \right\} = \left\{\omega \in \Omega : U(\omega) \leq F(x) \right\}$, d'où
$$\P\left( F^-_X(U) \leq x \right) = \P\left(U \leq F_X(x)\right) = F_X(x).$$ 

# Références
