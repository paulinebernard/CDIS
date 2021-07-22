% Calcul Différentiel I

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\tr}{\operatorname{tr}}

\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}

```{=latex}
\newpage
```

Objectifs d'apprentissage
================================================================================
Cette section s'efforce d'expliciter et de hiérarchiser
les acquis d'apprentissages associés au chapitre. 
Ces objectifs sont organisés en paliers :

(\zero) Prérequis (\one) Fondamental (\two) Standard (\three) Avancé
(\four) Expert

Sauf mention particulière, les objectifs "Expert", les démonstrations du document[^hp] 
et les contenus en annexe ne sont pas exigibles ("hors-programme").

[^hp]: l'étude des démonstrations du cours peut toutefois 
contribuer à votre apprentissage, au même titre que la résolution 
d'exercices.


#### Prérequis

Les éléments du calcul différentiel supposés déjà maîtrisés :

  - \zero dérivabilité et dérivée de fonctions d'une variable réelle,

  - \zero dérivée sur des sous-ensembles ouverts et des intervalles fermés de $\R$,

  - \zero dérivées des fonctions scalaires ($\R$) et vectorielles ($\R^m$),

  - \zero dérivée et développement limité au premier ordre,

Les fondements du calcul matriciel supposés maîtrisés :

  - \zero vecteurs de $\R^n$ et applications linéaires $\R^n \to \R^m$, 

  - \zero matrices, vecteurs lignes et colonnes,

  - \zero produit matriciel, transposition de matrice,

  - \zero interprétation géométrique du calcul matriciel.


#### Matrice jacobienne et différentielle

La notion de dérivée n'est applicable que pour les fonctions d'une variable,
scalaires ou vectorielles.
L'objet généralisant la dérivée dans le cas multivariable, défini au moyen
des dérivées partielles, est la matrice jacobienne ; pour les fonctions
scalaires, on préférera souvent utiliser le gradient que la matrice
jacobienne.

  - \one savoir calculer dérivées partielles, matrices jacobiennes et gradients.

Toutefois, la seule existence de la matrice jacobienne est insuffisante 
pour exploiter la plupart des résultats du calcul différentiel. 
Pour cette raison, on exige souvent que cette matrice existe et 
dépende continûment de son argument ; c'est la "continue différentiabilité".
Avec la continue différentiabilité, même sans savoir ce que signifie le terme, 
on peut alors néanmoins exploiter tous les résultats qui nécessitent la simple 
"différentiabilité".

  - \one savoir que l'existence de la matrice jacobienne est souvent insuffisante,

  - \one savoir qu'on peut alors avoir recours à la continue différentiabilité,

  - \one savoir caractériser les fonctions continûment différentiables,

  - \one savoir exploiter que continûment différentiable implique différentiable.

La différentiabilité n'est autre que l'existence d'un développement limité
au premier ordre. C'est la généralisation de la notion de dérivabilité au
cas multivariable.

  - \two savoir que différentiabilité signifie existence d'un tel développement limité,

  - \two savoir que différentiabilité équivaut à dérivabilité dans le cas monovariable,

  - \two savoir caractériser et exploiter un développement limité au premier ordre, 

  - \two savoir ce qu'est la différentielle et son lien avec la matrice jacobienne.

#### Calcul différentiel

La définition de la différentielle et son lien avec la matrice jacobienne
et les dérivées partielles permettent le calcul des différentielles 
des fonctions élémentaires, 
fournissant autant de règles élémentaires de calcul. 
Il est donc nécessaire avant toute chose de 

  - \one connaître et savoir mettre en œuvre quelques règles élémentaires,

  - \two savoir en élaborer de nouvelles en exploitant les définitions.

Ensuite, pour faire face à des calculs plus complexes, deux stratégies
sont à mener en parallèle. Au niveau pratique, il convient de

  - \one savoir exploiter les notations simplifiant le calcul différentiel,

  - \two savoir expliciter ce qu'elles signifient.

Au niveau théorique, il s'agit de compléter les règles élémentaires
par des règles génériques, applicables non plus à une fonction particulière
mais à des classes de fonctions, donc de

  - \one connaître et savoir mettre en œuvre quelques règles de calcul génériques,

  - \two connaître les règles d'assemblage/désassemblage,

  - \two connaître la règle de dérivation en chaîne,

  - \three savoir élaborer de nouvelles règles de calcul génériques.

#### Variation des fonctions

En intégrant les variations infinitésimales d'une fonction entre deux points, 
on peut évaluer sa variation entre ces points. Utiliser pleinement cette
technique suppose de :

  - \one connaître le théorème fondamental du calcul (monovariable),

  - \two connaître le théorème fondamental du calcul (multivariable),

  - \two connaître la démonstration du cas multivariable, 
  
  - \three savoir l'adapter quand c'est nécessaire,

  - \one connaître l'inégalité des accroissements finis (monovariable),

  - \two connaître l'inégalité des accroissements finis (multivariable),

  - \two savoir les déduire du théorème fondamental du calcul[^res],

  - \four connaître la variante non-euclidienne de ces inégalités,

  - \three savoir exploiter ces résultats dans des contextes variés.

[^res]: sous une hypothèse renforcée, par exemple de continue différentiabilité. 


Conventions
================================================================================

Un vecteur $x = (x_1, \dots, x_n) \in \R^n$
sera implicitement identifié, dans le contexte d'un calcul matriciel, 
au vecteur colonne
$$
\left[ \begin{array}{c}
x_1 \\
\vdots \\
x_n
\end{array}
\right] \in \R^{n \times 1}.
$$
Une application linéaire $A: \R^m \to \R^n$, sera quant à elle
implicitement identifiée avec la matrice à $m$ lignes et $n$ colonnes
représentant l'application linéaire dans les bases canoniques de 
$\R^m$ et $\R^n$
$$
\left[ 
\begin{array}{ccccc}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots & \vdots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{array}
\right] \in \mathbb{R}^{m \times n}.
$$

Dans ce document, nous utiliserons le point "$\cdot$" pour 
désigner le produit entre matrices. Les identifications que nous venons
d'exposer nous incitent donc également à noter $A \cdot x$ l'image du vecteur $x$ 
par l'application linéaire $A$ et $A \cdot B$ la composition des 
applications linéaires $B$ par $A$. 

Sauf mention contraire, $\left< x, y \right>$ désignera le produit scalaire
usuel entre les vecteurs $x$ et $y$ de $\R^n$ et $\|x\| = \|x\|_2 = \sqrt{\left<x,x \right>}$ 
la norme euclidienne associée ; 
$\|A\|$ désignera la norme d'opérateur $\|A\|_{22}$ de $A$, 
induite par ces normes euclidiennes sur $\R^m$ et sur $\R^n$.


Matrice jacobienne et différentielle
================================================================================

### Dérivées partielles {.definition .one}
Soient $U$ un ouvert de $\R^n$, $f: U \to \mathbb{R}^m$ et 
$x=(x_1, \cdots, x_n) \in U$. Lorsque la $j$-ème fonction partielle de $f$
en $x$, $y \mapsto f(x_1, \cdots, x_{j-1}, y, x_{j+1}, \cdots, x_n)$,
est dérivable en $y = x_j$, on appelle $j$-ème *dérivée partielle
de $f$ en $x$*
et on note $\partial_j f(x)$ sa dérivée :
$$
\partial_j f(x) := \left(y \mapsto f(x_1, \cdots, x_{j-1}, y, x_{j+1}, \cdots, x_n)\right)'(x_j) \in \R^m
$$
<!--
Alternativement,
$$
\begin{split}
\partial_j f(x)
&:= \lim_{t \to 0} \frac{f(x + t e_j) - f(x)}{t} \\
&\phantom{:}= \lim_{t \to 0} \frac{f(x_1, \dots, x_j + t, \dots, x_n) - f(x_1, \dots, x_n)}{t}. 
\end{split}
$$
-->

### Domaine de définition des fonctions partielles {.exercise .question .one #ddfp}
Quel est le domaine de définition -- implicite dans l'énoncé ci-dessus -- 
de la $j$-ème fonction partielle de $f$ associée au point $x$ ?
Montrer qu'il s'agit bien d'un ouvert de $\R$.

### Matrice jacobienne {.definition .one #matrice-jacobienne}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. 
Si toutes les dérivées partielles de toutes les composantes $f_i$ de $f$ 
existent en $x$, on définit la *matrice jacobienne de $f$ en $x$*, 
notée $J_f(x)$, comme la matrice de $\R^{m \times n}$ telle que
$$
[J_f(x)]_{ij} = \partial_{j} f_i(x),
$$
c'est-à-dire
$$
J_f(x) =
\left[
\begin{array}{cccc}
\partial_1 f_1 (x) & \partial_2 f_1 (x) & \cdots & \partial_n f_1 (x) \\
\partial_1 f_2 (x) & \partial_2 f_2 (x) & \cdots & \partial_n f_2 (x) \\
\vdots & \vdots & \vdots & \vdots \\
\partial_1 f_m (x) & \partial_2 f_m (x) & \cdots & \partial_n f_m (x) \\
\end{array}
\right]
$$

### {.remark}
On peut également utiliser les dérivées partielles de la fonction vectorielle
$f$ plutôt que ses composantes $f_i$, auquel cas on définit la matrice jacobienne
de $f$ comme une concaténation de vecteurs colonnes :
$$
J_f(x) =
\left[
\begin{array}{cccc}
\vert & \vert & \cdots & \vert \\
\partial_1 f (x) & \partial_2 f (x) & \cdots & \partial_n f (x) \\
\vert & \vert & \cdots & \vert \\
\end{array}
\right]
$$

### Gradient {.definition .one #gradient}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}$ et
$x$ un point de $U$. Si toutes les dérivées partielles de $f$ existent en $x$,
on appelle *gradient de $f$ en $x$* et l'on note $\nabla f(x)$ le vecteur
de $\R^n$ défini par 
$$
\nabla f(x) =(\partial_1 f(x), \partial_2 f(x), \dots, \partial_n f(x))\in \R^n,
$$
c'est-à-dire, après identification à un vecteur colonne, 
la transposée de la matrice jacobienne de $f$ en $x$ :
$$
\nabla f(x) = J_f(x)^{\top} = 
\left[ 
\begin{array}{c}
\partial_1 f(x) \\
\partial_2 f(x) \\
\vdots \\
\partial_n f(x)
\end{array}
\right] \in \R^{n\times 1}.
$$

### Gradient et matrice jacobienne {.exercise .question #gmj .one}
Montrer qu'en  tout point $x=(x_1, x_2)$ de $\R^2$, le gradient de 
la fonction scalaire
$$f:(x_1,x_2) \in \R^2 \mapsto (x_2^2 - x_1)^2 + (x_1 - 1)^2 \in \R$$
est défini et vérifie
$$
\nabla f(x_1, x_2)
=
(-2(x_2^2 - x_1) + 2 (x_1 - 1), 4 (x_2^2 - x_1)x_2) \in \R^2
$$
c'est-à-dire, comme vecteur colonne,
$$
\nabla f(x_1, x_2) = J_f(x_1, x_2)^{\top} =
\left[ 
  \begin{array}{c}
  -2(x_2^2 - x_1) + 2 (x_1 - 1) \\
  4 (x_2^2 - x_1)x_2
  \end{array}
  \right] \in \R^{2\times 1}.
$$


### Matrice jacobienne {.exercise .question .one #exo-mj2} 
Montrer qu'en tout point $x=(x_1, x_2)$ de $\R^2$, la matrice jacobienne de
la fonction 
$$
g:(x_1, x_2) \in \R^2 \mapsto (-2(x_2^2 - x_1) + 2 (x_1 - 1), 4 (x_2^2 - x_1)x_2) \in \R^2.
$$
est définie et vérifie
$$
J_g(x_1, x_2) = 
\left[ 
  \begin{array}{cc}
  4 & -4x_2 \\
  -4x_2 & 12 x_2^2
  \end{array}
  \right]\in \R^{2 \times 2}.
$$

![Champ du gradient $\nabla f$ de la fonction 
$f:(x_1,x_2) \mapsto (x_2^2 - x_1)^2 + (x_1 - 1)^2$ (échelle des vecteurs modifiée)
et en pointillés les lignes de niveau de $f$ de la forme $\{ (x_1,x_2) |\; f(x_1,x_2)=2^n \}$ ; 
cf. exemple ["Gradient et matrice jacobienne"](#gmj).](images/rosenbrock.py)

### Matrice jacobienne et gradient {.exercise #matjac .question}
Donner une expression de la matrice jacobienne de $f$ en $x$
en fonction de gradients des fonctions scalaires $f_i$ en $x$.



<!--
### Petit o de Landau {.definition .three}
Dans ce document, la notation $o(g(h))$ désigne une expression 
de la forme
$$
o(g(h)) := \varepsilon(h) g(h) \in \R^m
$$
où $g et $\varepsilon$ sont des fonctions définies dans un voisinage $V$ 
de $h=0$, $g$ est scalaire, $\varepsilon$ est à valeurs dans $\R^m$ et
$$
\lim_{h \to 0} \varepsilon(h) = \varepsilon(0) = 0.
$$
En particulier, un "petit o de $1$" désigne une expression de la forme
$$
o(1) := \varepsilon(h)
$$
et un "petit o de $\|h\|$" fait référence à
$$
o(\|h\|) := \varepsilon(h) \|h\| = o(1) \|h\|.
$$
-->

### {.remark}
Seule, l'existence de la matrice jacobienne
en $x$ offre très peu de garanties de régularité sur $f$ en $x$. 
Il est ainsi possible que la fonction $f$ ne soit pas même pas continue en $x$. 
(On rappelle que pour les fonctions d'une variable, l'existence de
la dérivée en un point implique la continuité en ce point.)

### Fonction discontinue I {.exercise .one #discont .question}
Construire une fonction $f: \R^2 \to \R$ dont le gradient existe en $(0,0)$
mais qui soit discontinue en $(0,0)$.

### Fonction discontinue II {.exercise .two #discont2 .question}
Construire une fonction $f:\R^2 \to \R$ dont la dérivée dans la direction
$h \in \R^2$
$$
f'(x, h) := \lim_{t \to 0} \frac{f(x+th) - f(x)}{t}
$$
existe en $x=(0,0)$ pour tout $h \in \R^2$,
mais qui ne soit pas continue en $(0,0)$.

### {.remark}
Une façon simple de renforcer la régularité de la fonction $f$ est d'exiger
qu'elle soit continûment différentiable :

### Continue différentiabilité {.definition .one #cdiff}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$.
La fonction $f$ est *continûment différentiable*
si pour tout $i \in \{1,\dots, m\}$
et $j \in \{1,\dots, n\}$, la dérivée partielle
$$
x \in U \mapsto \partial_j f_i(x) \in \R
$$
est définie et continue en tout point de $U$.

### Continue différentiabilité -- définitions équivalentes {.post .two .remark}
Alternativement, la fonction $f$ est continûment différentiable si 
(et seulement si) les dérivées partielles
$x \in U \mapsto \partial_j f(x) \in \R^m$
sont définies et continues pour tout $i \in \{1, \dots, m\}$
ou encore si la fonction $x \in U \mapsto J_f(x) \in \R^{m \times n}$
est définie et continue.

### {.remark}
On qualifiera de *différentiable* une fonction qui admet un développement limité 
au premier ordre. La différentiabilité est la transposition naturelle 
du concept de dérivabilité aux fonctions de plusieurs variables :
pour jouer ce rôle, l'existence de la matrice jacobienne est une propriété 
trop faible 
et la continue différentiabilité est une propriété trop forte.

### Différentiabilité {.definition .three #différentiabilité}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. 
On dit que $f$ est *différentiable en $x$* si la matrice jacobienne de $f$ en
$x$ existe et que $f(x+h)$ admet en $h=0$ le développement limité
au 1er ordre $h \mapsto f(x) + J_f(x) \cdot h$ : il existe
sur un voisinage de $h=0$ une fonction
$\varepsilon$ à valeurs dans $\R^m$ vérifiant $\lim_{h \to 0} \varepsilon(h) = 0$
telle que 
$$
f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h) \|h\|.
$$
On dit que $f$ est *différentiable* (ou *différentiable sur $U$*)
si elle est différentiable en tout point $x$ de $U$.

### {.remark}
Le plus souvent, la façon la plus simple de prouver la différentiabilité d'une
fonction est d'établir sa continue différentiabilité ; en effet, on a :

### Continue différentiabilité implique différentiabilité {.proposition .one #cdid}
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}^m$.
Si $f$ est continûment différentiable, $f$ est différentiable.

![Relations entre existence de la matrice jacobienne, différentiabilité et
continue différentiabilité.](images/diff-et-cdiff.svg)


<!--
### Existence d'un développement limité au 1er ordre {.proposition .two #dl1}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$.
Si $f$ est continûment différentiable alors $f(x+h)$ admet le développement 
limité au 1er ordre $h \mapsto f(x) + f'(x) \cdot h$, c'est-à-dire qu'il
existe sur un voisinage de $h=0$ une fonction
$\varepsilon$ à valeurs dans $\R^m$ vérifiant
$\lim_{h \to 0} \varepsilon(h) = 0$
telle que 
$$
f(x+h) = f(x) + f'(x) \cdot h + \varepsilon(h) \|h\|.
$$
-->
### Démonstration {.proof} 
Supposons $f: U \subset \R^m \to \R^n$ continûment différentiable.
Soit $x \in U$ et $r>0$ telle que la boule fermée centrée en $x$ 
et de rayon $r$ soit incluse dans $U$
$$
\overline{B}(x, r) =
\{y \in \R^n \; | \; \|y - x\| \leq r\} \subset U
$$
et soit $h \in \R^n$ tel que $\|h\| \leq r$. 
La variation de $f$ entre $x$ et $x+h$ satisfait
\begin{multline*}
f(x+h) - f(x) = \\ 
\sum_{i=1}^n f(x+(h_1, \dots,h_{i-1}, h_i, 0, \dots)) - f(x + (h_1, \dots, h_{i-1}, 0, 0, \dots)). 
\end{multline*}

![Ligne brisée joignant $x$ et $x+h$.](images/cont-diff.tex){#cont-diff}

Or comme pour tout $i$ la fonction
$$t \in [0,1] \mapsto f(x+(h_1, \dots, th_i, 0, \dots))$$
est dérivable de dérivée
$\partial_i f(x+(h_1, \dots, th_i, 0, \dots)) h_i$ et que cette expression
est une fonction continue -- et donc intégrable -- de la variable $t$, 
par [le théorème fondamental du calcul](#TFC), on obtient
\begin{multline*}
f(x+(h_1, \dots, h_{i-1},h_i, 0, \dots)) - f(x + (h_1, \dots, h_{i-1}, 0, 0, \dots)) = \\
h_i \int_0^1 \partial_i f(x+(h_1, \dots, h_{i-1}, th_i, 0, \dots)) \, dt.
\end{multline*}
Par ailleurs, comme
$$
f'(x) \cdot h =
\sum_{i=1}^n \partial_i f(x) h_i
=
\sum_{i=1}^n h_i \int_0^1 \partial_i f(x) \, dt,
$$
on a 
\begin{multline*}
f(x+h) - f(x) - \sum_i \partial_i f(x) h_i = \\
\sum_{i=1}^n h_i \int_0^1 \left[\partial_i f(x+(h_1, \dots, h_{i-1}, th_i, 0, \dots)) - \partial_i f(x) \right] \, dt. 
\end{multline*}
Par continuité des dérivées partielles en $x$, si $r$ est choisi suffisamment 
petit pour que $\|\partial_i f(y) - \partial_i f(x)\| \leq \varepsilon / n$ 
quand $\|y-x\| \leq r$, alors l'inégalité triangulaire
fournit
\begin{multline*}
\left\|\int_0^1 \left[\partial_i f(x+(h_1, \dots, h_{i-1}, th_i, 0, \dots)) - \partial_i f(x) \right] \, dt \right\| \leq \\
\int_0^1 \left\|\partial_i f(x+(h_1, \dots, h_{i-1}, th_i, 0, \dots)) - \partial_i f(x) \right\| \, dt \leq \varepsilon/n
\end{multline*}
et donc, toujours par inégalité triangulaire, comme $|h_i| \leq \|h\|$,
$$
\left\|f(x+h) - f(x) - \sum_{i=1}^n \partial_i f(x) h_i \right\|
\leq
\sum_{i=1}^n |h_i| {\varepsilon}/{n}
\leq \varepsilon \|h\|.
$$
La fonction $f$ admet donc un dévelopement limité au 1er ordre en $x$.

### Différentiabilité implique continuité {.proposition .one #dic}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et $x \in U$.
Si $f$ est différentiable en $x$, $f$ est continue en $x$.

### Différentiabilité implique continuité {.exercise .question .one #exo-dic}
Démontrer la proposition ["Différentiabilité implique continuité"](#dic).

<!--
### Dérivée directionnelle {.definition .one}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$,
$x$ un point de $U$ et $h$ un vecteur de $\R^n$. La *dérivée de $f$ en $x$
dans la direction $h$* est définie comme
$$
f'(x, h) := \lim_{\substack{t \to 0 \\ t \neq 0}} \frac{f(x+ th) - f(x)}{t}
$$
quand cette limite existe.

### Différentielle et dérivée directionnelle {.proposition #ddd .one}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. Si la fonction $f$ est différentiable en $x$
alors sa dérivée dans la direction $h \in \R^n$ existe et
$$
f'(x, h) = J_f(x) \cdot h.
$$

### Différentielle et dérivée directionnelle {.exercise .question #exo-ddd .one}
Démontrer la proposition ["Différentielle et dérivée directionnelle"](#ddd).

### Dérivée directionnelle et différentielle {.exercise .question #exo-ddd2 .three}
Montrer que la réciproque de la proposition ["Différentielle et dérivée directionnelle"](#ddd)
est fausse : construire une fonction dont les dérivées directionnelles en $x$
existent dans toute direction $h \in \R^n$ mais qui ne soit pas différentiable
en $x$.
--->

### Fonctions affines {.exercise .question #fa .one}
Soit $A \in \R^{m\times n}$ et $b \in \R^m$. 
Calculer la matrice jacobienne de la fonction $f:\R^n \to \R^m$ définie par 
$f(x) = A \cdot x + b$ et montrer que cette fonction est différentiable.

### {.remark}
L'existence de la matrice jacobienne de $f$ en $x$ ne garantit pas
l'existence d'un développement au premier ordre de $f$ en $x$.
Par contre, si un tel développement existe, il est nécessairement
obtenu à partir de la matrice jacobienne comme le montre l'exercice suivant.

### Développement limité au premier ordre {.exercise .question #dlmj .two}
Montrer que pour $a\in \R^m$ et 
$B \in \R^{m \times n}$, si $f$ est une fonction qui vérifie dans un voisinage de $h=0$
$$
f(x+h) = a + B \cdot h + \varepsilon(h) \|h\|
$$
avec $\lim_{h \to 0} \varepsilon(h) =  0$
alors $a = f(x)$, la matrice jacobienne $J_f(x)$ est bien définie et $B = J_f(x)$.

### Différentielle {.definition .two #différentielle} 
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. 
Si $f$ est différentiable en $x$ on appelle alors *différentielle de $f$ en $x$* 
l'application linéaire 
$df(x)$ associée à la matrice jacobienne 
$$
df(x) := \left(h \in \R^n \mapsto J_f(x) \cdot h \in \R^m \right)
$$
Si l'on identifie applications linéaires et matrices, la différentielle
se confond avec la matrice jacobienne elle-même. Pour tout $h \in \R^n$,
$$
df(x) \cdot h = J_f(x) \cdot h = \sum_{i=1}^n \partial_i f(x) h_i.
$$

### Variation d'une fonction en un point {.remark .one}
Comme le montre l'égalité caractérisant la différentiabilité de $f$ en $x$,
le terme $df(x) \cdot h$ représente une approximation 
-- linéaire en $h$ -- de la variation $\Delta f(x, h):= f(x+h) - f(x)$ de 
$f$ en $x$ dans la direction $h$, car
$$
\Delta f(x, h) = df(x)\cdot h + \varepsilon(h)\|h\|.
$$

### Différentiabilité {.two .exercise .question #vareps}
Montrer que $f$ est différentiable en $x$ si et seulement si $J_f(x)$ est bien
définie et que
$$
\lim_{\substack{h \to 0 \\ h\neq 0}} \left(\frac{f(x+h) - f(x)}{\|h\|} - J_f(x) \cdot \frac{h}{\|h\|}\right) = 0.
$$

### Différentielle et dérivée {.proposition .one #dad}
Soit $U$ un ouvert de $\R$, $f:U \to \R^m$ et $x\in U$. La fonction $f$ est
différentiable en $x$ si et seulement si elle est dérivable en $x$. 
Dans ce cas, pour tout $h \in \R$,
$$
df(x)\cdot h = f'(x) h.
$$

### Démonstration {.proof}
Avec la définition de la matrice jacobienne,
il est clair que la dérivée de $f$ en $x$ existe si et seulement si
$J_f(x)$ existe et qu'auquel cas on a $J_f(x) = [f'(x)]$.
On sait aussi que la fonction $f$ est dérivable en $x$ si et seulement si
elle admet un développement limité au premier ordre en $x$
(cf. [la proposition "Dérivée et développement limité"](#ddl) ainsi que [sa réciproque](#ddlr)),
soit
$$
f(x+h) = f(x) + f'(x) h + \varepsilon(h) |h|
$$
avec $\lim_{h\to 0} \varepsilon (h) = 0$, ce que l'on peut écrire sous
la forme
$$
f(x+h)= f(x) + [f'(x)] \cdot h + \varepsilon(h) \|h\|
= f(x) + J_f(x) \cdot h +\varepsilon(h) \|h\|,
$$
ce qui équivaut à la différentiabilité de $f$ en $x$.
La relation $df(x) \cdot h= J_f(x) \cdot h$ fournit le dernier élément
de la proposition.

### Différentielle et gradient {.proposition .one #dag}
Soit $U$ un ouvert de $\R^n$, $f: U \to \R$ et $x \in U$. Si la fonction
$f$ est différentiable en $x$, alors pour tout $h \in \R^n$,
$$
df(x) \cdot h= \left<\nabla f(x), h\right>.
$$

### Démonstration {.proof}
Par [définition de la différentielle](#différentielle), 
$df(x) \cdot h = J_f(x) \cdot h$.
Or, d'après [la définition du gradient](#gradient), 
$\nabla f(x) = J_f(x)^{\top}$. Par conséquent,
$df(x)\cdot h = \nabla f(x)^{\top} \cdot h = \left<\nabla f(x), h\right>$.



Calcul Différentiel
================================================================================


Notations {#notations}
--------------------------------------------------------------------------------

Comme utilisateur du calcul différentiel
vous avez probablement déjà croisé des notations assez éloignées de celles 
que nous avons exploitées jusqu'à présent. Vous avez peut-être mémorisé 
des règles de calcul élémentaires telles que
$$
d (x+ y)  = dx + dy, \; d (xy) = y \, dx + x \, dy 
$$
ou appris en thermodynamique que
$$
dU = TdS - PdV, \; \mbox{ soit } \; T = \frac{\partial U}{\partial S} \mbox{ et } P = -\frac{\partial U}{\partial V}.
$$

<!--
on trouve une formule du type
$$
d (f(x_1, \dots, x_n)) = \frac{\partial f(x_1,\dots, x_n)}{\partial x_1} d x_1 + \dots + \frac{\partial f(x_1,\dots, x_n)}{\partial x_n} dx_n.
$$
-->
Bien utilisées, ces notations ont le potentiel de simplifier significativement
la pratique du calcul différentiel ; elle recèlent toutefois un potentiel d'ambiguité
-- et donc des risques d'erreurs -- contre lequel il faut se prémunir. 
Nous allons donc détailler ces notations sur un exemple et les interpréter 
à la lumière des concepts déjà introduits.

### Expressions (fonctions implicites)
La première technique consiste à favoriser l'usage d'expressions
mathématiques -- comme "$x^2 + y^2$" -- pour désigner des grandeurs variables,
sans nécessairement expliciter les fonctions correspondantes, la liste de
leurs arguments ou le domaine de définition associés. 
Tous ces éléments doivent alors être inférés du contexte ; 
ainsi on peut assez naturellement associer à l'expression "$x^2 + y^2$" la fonction 
$f: (x, y) \in \R^2 \mapsto x^2 + y^2 \in \R$. Mais d'autres choix sont
défendables[^df]. Une fois ce choix fait, on interprète le terme
$d(x^2 + y^2)$ comme
$$
d(x^2 + y^2) := df(x, y).
$$

[^df]: Peut-être que dans le contexte où l'on exploite l'expression, 
les grandeurs $x$ et $y$ ne sont définies que si $x>0$ et $y>0$ ; 
peut-être a-t-on une bonne raison de plutôt lister la variable $y$ avant $x$ ; 
peut-être y a-t-il une troisième variable $z$ et que ça n'est que "par accident" que
l'expression $x^2 + y^2$ ne dépend pas de $z$, etc.


### Variables nommées
Dans un contexte applicatif donné, il est fréquent que des noms (ou symboles)
particuliers soit attachés aux grandeurs variables (plutôt que les génériques
"$x_1$", \dots, "$x_n$") et qu'il soit plus naturel ou pratique d'utiliser 
ces noms pour désigner les variables plutôt qu'un indice[^lv][^py].
Pour ce qui est des dérivées partielles en particulier, dans cet esprit,
on peut alors convenir de noter
$$
\frac{\partial  (x^2 + y^2)}{\partial x} := \frac{\partial  f}{\partial x}(x, y) := \partial_x f(x, y) := \partial_1 f(x, y)
$$
et
$$
\frac{\partial  (x^2 + y^2)}{\partial y} := \frac{\partial  f}{\partial y} (x, y):= \partial_y f(x, y) := \partial_2 f(x, y).
$$

[^lv]: En particulier, si la fonction considérée est implicite, 
car issue d'une expression, il n'y a probablement pas d'ordre "naturel" 
pour lister les variables.

[^py]: C'est le même argument qui motive en Python de n'utiliser les
arguments positionnels, comme dans l'appel `ask("Quit?", 3)`, qu'avec modération.
L'alternative, utiliser les arguments nommés, 
comme dans l'appel `ask(question="Quit?", retries=3)`, 
peut s'avérer plus lisible.

Compte tenu de l'égalité $f(x,y)=x^2 + y^2$, on a ici
$$
\frac{\partial (x^2 + y^2)}{\partial x} = 2x 
\; \mbox{ et } \;
\frac{\partial (x^2 + y^2)}{\partial y} = 2y. 
$$

### Différentielle des variables
En poussant jusqu'au bout la logique de la différentiation des expressions,
on peut encore simplifier les notations. À ce stade,
nous avons établi que pour tout $(h_x, h_y) \in \R^2$, nous avions
\begin{equation} \label{iff}
d(x^2 + y^2) \cdot (h_x, h_y) 
= 
\frac{\partial(x^2+y^2)}{\partial x} h_x + \frac{\partial(x^2+y^2)}{\partial y} h_y= 2x \, h_x + 2 y \, h_y.
\end{equation}
Or, en utilisant les mêmes conventions, nous obtenons
$$
dx \cdot (h_x, h_y) 
= 
\frac{\partial x}{\partial x} h_x + \frac{\partial x}{\partial y} h_y= h_x
\; \mbox{ et } \;
dy \cdot (h_x, h_y) 
= 
\frac{\partial y}{\partial x} h_x + \frac{\partial y}{\partial y} h_y= h_y.
$$
Par conséquent, nous pouvons réécrire la relation \eqref{iff} sous la forme
$$
d(x^2 + y^2) =  \frac{\partial(x^2+y^2)}{\partial x} dx + \frac{\partial(x^2+y^2)}{\partial y} dy = 2x \, dx + 2 y \, dy.
$$

<!--

#### Différentielle d'expressions
L'idée clé est d'étendre le calcul différentiel des fonctions 
à des formules mathématiques ou expressions, 
composées de symboles de fonctions, d'opérateurs, de constantes et de variables. 
Considérons par exemple, l'expression $$e := ``x^2 - c^2 t^2".$$ 
Nous allons rapidement omettre les guillemets pour simplifier les notations ; 
mais pour le moment ils soulignent que nous avons affaire à une formule 
(à une suite de symboles) et pas à un nombre réel.
Cette expression exploite les opérateurs d'addition 
et d'exponentiation ; le symbole "$2$" désigne une
constante numérique ainsi que "$c$" (ici, la vitesse de la lumière 
dans le vide) ;
les symboles "$x$" et "$t$" font référence à des variables (de position et de 
temps respectivement). 
La valeur numérique que désigne $e$ est définie pour toute valeur réelle des
variables $x$ et $t$ ;
on peut donc lui associer la fonction
$$
f: (x,t) \in \R \times \R \mapsto x^2 - c^2 t^2 \in \R
$$
et utiliser ensuite les expressions $e$ et "$f(x, t)$" de façon interchangeable.
La fonction $f$ étant différentiable, on définit la différentielle
de l'expression $e$ comme
$$
d e := d(f(x, t)) := df (x, t).
$$


#### Différentielle des variables
Remarquons que les symboles de variables "$x$" et "$t$" sont aussi des 
expressions à part entière. Elles peuvent donc être associées aux fonctions
linéaires
$(x,t) \in \R \times \R \mapsto x \in \R$ et 
$(x,t) \in \R \times \R \mapsto t \in \R$ ; leur différentielle satisfait donc
$$
dx\cdot (h_x, h_t) = h_x \; \mbox{ et } \; dt \cdot (h_x, h_t) = h_t. 
$$
Les fonctions $dx$ et $dt$ -- il s'agit bien de fonctions et pas de nombres -- 
prélèvent donc dans le vecteur de variation des arguments $(h_x, h_t)$ la 
composante associée à la variable $x$ et $t$ respectivement.

La différentielle de $e$ satisfait
$d e \cdot (h_x, h_t) = ({\partial e}/{\partial x}) h_x + ({\partial e}/{\partial t}) h_t$
pour toute variation $(h_x, h_t)$. On peut donc réécrire cette relation sous la forme
$$
d e = \frac{\partial e}{\partial x} dx + \frac{\partial e}{\partial t} dt,
$$
et donc ici
$$
d (x^2 - c^2 t^2) = 2x \, dx - 2 c^2 t \, dt.
$$
-->

### Espace-temps {.exercise .question .one #st}
Montrer l'existence et calculer la différentielle de 
$$x^2 +y^2 + z^2 - c^2 t^2$$ en utilisant
les conventions de cette section.

### Robustesse des notations {.exercise .two .question #rn}
On considère successivement l'expression $x^2 + y^2$ comme une fonction 
non plus de $(x, y)$, mais de $(y,x)$ puis de $(x, y, z)$. 
Comment interpréter les termes
$dx$ et $dy$ dans chacun de ces cas ?
La relation $d (x^2 + y^2) = 2x \, dx + 2 y \, dy$ est-elle
toujours valable ?

Règles de calcul
--------------------------------------------------------------------------------

### {.ante .remark}
La définition de la différentielle, sa relation à la matrice jacobienne et 
avec la continue différentiabilité permettent d'élaborer un nombre 
quasi-illimité de "règles de calcul élémentaires" réutilisables 
dont nous donnons quelques exemples importants.

### Différentielle d'une application linéaire {.proposition #dal .one}
Pour toute matrice $A \in \R^{m\times n}$, 
l'application linéaire $f: x \in \R^n \mapsto  A \cdot x \in \R^m$ 
est différentiable et pour tout $x \in \R^n$,
$df(x) = A$ ; autrement dit
$$
d(A \cdot x) = A  \cdot dx.
$$

### Démonstration {.proof}
Pour tout $x \in \R^n$, on a
$f_i(x) = (A \cdot x)_i = \sum_{k=1}^n A_{ik} x_k$,
donc la $j$-ème dérivée partielle de $f_i$ existe et
$$
\partial_j f_i(x) = \partial_j \left(x \mapsto \sum_{k=1}^n A_{ik} x_k \right)(x)
= A_{ij}.
$$
La matrice jacobienne $J_f(x)$ est donc définie et $J_f(x) = A$.
Chaque coefficient de $J_f$ est une constante et donc une fonction continue de
$x$ : la fonction $f$ est [continûment différentiable -- et donc
différentiable](#cdid) -- et $df(x) = J_f(x) = A$.

### Règle du produit (élémentaire) {.proposition .one #product-rule}
L'application produit $\pi : (x, y) \in \R^2 \mapsto xy \in \R$ est différentiable
et pour tout $(h_x, h_y) \in \R^2$, on a $d\pi(x, y) \cdot (h_x, h_y)= x h_y + y h_x$ ; 
autrement dit 
$$
d(xy) = x \, dy + y \, dx.
$$

### Démonstration {.proof}
Les dérivées partielles de $xy$ existent et sont continues : on a 
$$
\frac{\partial (xy)}{\partial x} = y
\; \mbox{ et } \; 
\frac{\partial (xy)}{\partial y} = x.
$$
Par conséquent, l'application produit est [continûment différentiable, donc différentiable](#cdid),
et
$$
d(xy) = \frac{\partial (xy)}{\partial x} dx + \frac{\partial (xy)}{\partial y} dy
= x \, dy + y \, dx.
$$

### {.remark .ante}
Ce type de règles de calcul élémentaires peuvent servir de briques de base pour
élaborer des règles de calcul "génériques", faisant intervenir des fonctions
différentiables arbitraires et permettant de traiter des calculs plus complexes. 
Les deux résultats qui permettent de mener cette extension du calcul différentiel 
sont [la règle d'assemblage](#assemblage) 
-- fondée sur la règle de [différentiation composante par composante](#diff-cc) -- 
et la règle de [différentiation en chaîne](#chain-rule).


### Règle de différentiation en chaîne {.theorem #chain-rule .two}
Soit $f: U \subset \mathbb{R}^p \to \mathbb{R}^{n}$ et 
$g: V \subset \mathbb{R}^n \to \mathbb{R}^{m}$ deux fonctions définies
sur des ouverts $U$ et $V$ et telles que $f(U) \subset V$. 
Si $f$ est différentiable en $x \in U$ et $g$ est différentiable en $f(x) \in V$,
alors la composée $g \circ f$ est différentiable en $x$ et
$$
d(g \circ f)(x) = dg(y) \cdot df(x) \; \mbox{ où } \; y = f(x).
$$

### Démonstration {.proof}
L'objectif de la preuve est de montrer que dans un voisinage de $h=0$,
$$
g(f(x+h)) - g(f(x)) =  (dg(f(x)) \cdot df(x)) \cdot h + \varepsilon(h)\|h\|
$$
où $\lim_{h \to 0} \varepsilon(h) = 0$.
La fonction $g$ étant différentiable en $f(x)$, il existe une fonction
$\varepsilon_1$ définie dans un voisinage de $0$ et telle que
$\lim_{h \to 0} \varepsilon_1(h) = 0$, 
vérifiant
$$
g(f(x)+k) - g(f(x)) = dg(f(x)) \cdot k + \varepsilon_1(k) \|k\|.
$$
Choisissons $k=f(x+h) - f(x)$ dans cette équation, de telle sorte que
$$
g(f(x)+k) = g\left(f(x) + (f(x+h) - f(x))\right) = g(f(x+h)).
$$
Nous obtenons donc
$$
g(f(x+h)) - g(f(x)) = dg(f(x)) \cdot (f(x+h)-f(x)) + \varepsilon_1(k) \|k\|.
$$

Notons que la fonction $\varepsilon_2(h) := \varepsilon_1(f(x+h) - f(x))$
est définie dans un voisinage de $0$ et que par continuité de $f$ en 
$x$, $f(x+h) - f(x)$ tend vers $0$ quand $h$ tend vers $0$, et par conséquent
$\varepsilon_2(h) \to 0$ quand $h\to 0$.
Avec cette notation, on a
$$
\begin{split}
g(f(x+h)) - g(f(x)) &= dg(f(x)) \cdot (f(x+h)-f(x)) \\
                    &\phantom{=} + \varepsilon_2(h) \|f(x+h)-f(x)\|.
\end{split}
$$
Comme $f$ est également différentiable en $x$, il existe une fonction 
$\varepsilon_3$ définie dans un voisinage de $0$ et telle que
$\lim_{h \to 0} \varepsilon(h) = 0$ vérifiant
$$
f(x+h) - f(x) = df(x) \cdot h + \varepsilon_3(h) \|h\|.
$$
En substituant cette relation dans la précédente, nous obtenons
$$
g(f(x+h)) - g(f(x)) = dg(f(x)) \cdot (df(x) \cdot h) + \varepsilon(h) \|h\|
$$
où $\varepsilon(0) = 0$ et dans le cas contraire,
$$
\varepsilon(h) =  dg(f(x)) \cdot \varepsilon_3(h) + \varepsilon_2(h) 
\left\|df(x) \cdot \frac{h}{\|h\|} + \varepsilon_3(h) \right\|.
$$
Il suffit pour conclure de prouver que $\varepsilon(h) \to 0$ quand $h \to 0$.
Or, 
$$
\begin{split}
\|\varepsilon(h)\| & \leq \|dg(f(x)) \cdot \varepsilon_3(h)\| + \|\varepsilon_2(h)\| \times \|df(x) \cdot (h / \|h\|) \| + \|\varepsilon_2(h)\| \times \|\varepsilon_3(h) \|   \\
& \leq \|dg(f(x))\| \times \|\varepsilon_3(h)\| + \|\varepsilon_2(h)\|  \times \|df(x)\| + \|\varepsilon_2(h)\| \times \|\varepsilon_3(h) \|,  
\end{split}
$$
le résultat est donc acquis.

### Différentiation en chaîne des fonctions continûment différentiables {.exercise #cfcd .question .one}
Montrer que si dans [l'énoncé de la règle de différentiation en chaîne](#chain-rule) 
les fonctions $f$ et $g$ sont continûment différentiables, alors $g \circ f$
l'est également.

<!--
### TODO
Montrer d'abord la chain rule et montrer comment la règle de différentation
composante par composante résulte de ça et de la diff des projections, 
insertion et somme. Ou faire ça en exo ? Ou faire juste les règles élémentaires
citées ici en exo (ou en résultat ?), et changer la démo pour montrer 
qu'on peut utiliser la chain rule ?
-->

### Règle de différentiation composante par composante {.one .theorem #diff-cc .one}
Soit $U$ un ouvert de $\R^n$, $f: U \to \R^m$ et $x \in U$. La fonction
$f$ est différentiable en $x$ si et seulement si toutes ses composantes
$f_i$ sont différentiables en $x$. Dans ce cas, on a 
$$
(df(x))_i = df_i(x).
$$

### Démonstration {.proof}
Par [la règle de dérivation composante par composante](#der-cc),
la matrice jacobienne de $f$ en $x$ existe si et seulement si 
toutes les matrices jacobienne $J_{f_i}(x)$ existent et on a alors
$(J_f(x))_i = J_{f_i}(x)$.
La différentiabilité de $f$ en $x$ se traduit donc par
$$
f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h)\|h\|
$$
où $\lim_{h\to 0} \varepsilon (h) = 0$, ce qui entraine pour tout $i$,
$$
f_i(x+h) = f_i(x) + (J_f(x))_i \cdot h + \varepsilon_i(h) \|h\|
= f_i(x) + J_{f_i}(x) \cdot h + \varepsilon_i(h) \|h\|
$$
avec $\lim_{h\to 0} \varepsilon_i (h) = 0$ ; 
chaque composante $f_i$ est donc différentiable. La réciproque
s'établit de manière similaire. On déduit alors de la relation
$(J_f(x))_i = J_{f_i}(x)$ que $(df(x))_i = df_i(x)$.

### {.remark .ante .post} 
Cette règle entraîne :

### Règles d'assemblage et désassemblage {.one .corollary #assemblage}
Soit $U$ un ouvert de $\R^n$, $f: U \to \R^m$, $g: U \to \R^p$ et $x \in U$.
La fonction $(f,g) : U \to \R^{m+p}$ est différentiable en $x$ si et 
seulement si $f$ et $g$ sont différentiables en $x$ ; on a alors
$$
d(f, g)(x) = (df(x), dg(x)).
$$

### Désassemblage {.exercise .question .two #exo-desass}
Montrer que pour tous $m, p \in \N$, les fonctions 
$(x_1,x_2) \in \R^m\times\R^p \mapsto x_1 \in \R^m$
et $(x_1,x_2) \in \R^m\times\R^p \mapsto x_2 \in \R^p$ sont différentiables.
En déduire une démonstration de ["la règle de désassemblage"](#assemblage).

### Démonstration {.proof}
La fonction $(f, g)$ d'une part et les fonctions $f$ et $g$ d'autre part
ont le même jeu de composantes scalaires ; la conclusion s'ensuit par
[la règle de différentiation composante par composante](#diff-cc).


### Différentiation en chaîne et assemblage {.exercise .question .three #exo-dca}
Combiner [la règle d'assemblage](#assemblage) 
et [la règle de différentiation en chaîne](#chain-rule) en
un résultat unique qui implique les deux résultats

### {.remark}
À titre d'exemple, montrons comment ces deux résultats permettent de généraliser 
[la règle élémentaire du produit](#product-rule) :

### Règle du produit (générique) {.proposition .one}
Soit $U$ un ouvert de $\R^n$, $f: U \to \R$, $g: U \to \R$ et $x \in U$.
Si les fonctions $f$ et $g$ sont différentiables en $x$, 
alors leur produit $fg$ également et $$d(fg)(x)  = f(x) dg(x) + g(x) df(x).$$

![Graphe de calcul de l'application $x \mapsto f(x) g(x)$.](images/graphe-de-calcul.svg)

### Démonstration {.proof}
Par [assemblage](#assemblage), la fonction $(f, g)$ est différentiable en $x$ 
et $d(f,g)(x) = (df(x), dg(x))$.
Sa composition par la fonction produit $\pi: (x, y) \mapsto xy$ est 
le produit $fg$ :
$$
fg = \pi \circ (f, g).
$$
Par [la règle de différentation en chaîne](#chain-rule), le produit $fg$ est
différentiable et
\begin{align*}
d(fg) (x) 
 &= d \pi (f(x), g(x)) \cdot d(f,g)(x) \\
&= d \pi (f(x), g(x)) \cdot (df(x), dg(x)) \\
&= f(x) dg(x) + g(x) df(x).
\end{align*}

### {.remark}
De façon similaire, on peut désormais tirer des conséquences élargies 
de la proposition ["Différentielle d'une application linéaire"](#dal) :

### Linéarité de la différentielle {.proposition .one #ld}
Soit $U$ un ouvert de $\R^n$, $f: U \to \R$, $g: U \to \R$,
$\lambda \in \R$, $\mu \in \R$ et $x \in U$.
Si les fonctions $f$ et $g$ sont différentiables en $x$, 
alors la combinaison linéaire $\lambda f + \mu g$ également et
$$d(\lambda f + \mu g)(x)  = \lambda df(x) + \mu dg(x).$$

### Démonstration {.proof}
La fonction $\lambda f + \mu g$ peut être obtenue en composant la fonction
$(f, g)$ et la fonction linéaire $A : (x, y) \in \R^2 \mapsto \lambda x + \mu y$.
Par [la règle d'assemblage](#assemblage) et [la règle de différentation en chaîne](#chain-rule),
elle est donc différentiable en $x$ et [comme la différentielle de l'application
linéaire $A$ en tout point est elle-même](#dal), 
\begin{align*}
d(\lambda f + \mu g)(x) &= d A(f(x), g(x)) \cdot (df(x), dg(x)) \\
&= A \cdot (df(x), dg(x)) \\ &= \lambda df(x) + \mu dg(x).
\end{align*}


<!--



### Différentielle d'une application bilinéaire {.theorem #dab .two}
Pour toute matrice $B \in \R^{m\times n}$, la fonction bilinéaire
$$f: (x, y) \in \R^m \times \R^n \mapsto x^{\top} \cdot B \cdot y \in \R$$
est différentiable et pour tout $x \in \R^n$,
$$
df(x, y)\cdot(h_x, h_y) = h_x^{\top} \cdot B \cdot y + x^{\top} \cdot B \cdot h_y.
$$
-->



<!--
### TODO : exo diff produit scalaire


Déduire la règle du produit de
$$
d(x^{\top} \cdot A \cdot y) =  x^{\top} \cdot A \cdot dy + y^{\top} \cdot A^{\top} \cdot dx
$$
(csq exo : difff $\left<x, y\right>$ et $\|x\|$ (si $x \neq 0$))

### TODO: diff fct bilin

### Différentielle et norme euclidienne {.exercice .question #diff-norm}
En exploitant la règle de différentiation en chaîne, montrer que le
carré de la norme euclidienne
$$
f: x \in \R^n \mapsto \|x\|^2 \in \R
$$ 
est différentiable, puis calculer son gradient $\nabla f$.

### Différentiabilité et norme euclidienne {.answer #answer-diff-norm}
Pour tout $x \in \R^n$ on a
$$
\|x\|^2 = x^{\top} \cdot I \cdot x,
$$
La fonction $x \in \R^n$ peut donc s'écrire comme la composée
des fonctions
\begin{align*}
f &: x \in \R^n  \mapsto (x, x) \in \R^{n} \times \R^n \\
g &: (x, y) \in \R^n \times \R^n \mapsto x^{\top} \cdot y \in \R \\
\end{align*}

**TODO**

-->

### Produit scalaire {.exercise .question #ps}
Montrer que la fonction $$\left<\cdot, \cdot\right>: (x, y) \in \R^{2n} \to \left<x, y\right> \in \R$$ est différentiable et
calculer son gradient.






Variation des fonctions
================================================================================

### {.remark}
Lorsque la fonction $f$ est différentiable en $x$, 
nous disposons de l'égalité 
$$
f(x + h) - f(x) = df(x) \cdot h + \varepsilon(h) \|h\|
$$
avec $\lim_{h \to 0}\varepsilon(h) = 0$. 
Cette égalité est de nature asymptotique, ce qui veut dire que
pour maîtriser l'écart entre
$f(x+h)$ et $f(x)$, 
nous devons être en mesure de faire tendre $h$ vers $0$ ;
si le vecteur $h$ est fixé et même s'il est "petit", en toute rigueur,
cette relation ne nous fournit aucune information. 

Mais tout n'est pas perdu : si nous savons que $f$ est différentiable 
non pas uniquement en $x$ mais sur tout le segment $[x,x+h]$, 
il est possible de calculer la différence entre $f(x+h)$ et $f(x)$ 
en intégrant les variations infinitésimales 
de $f$ le long de ce segment. 

### Théorème fondamental du calcul (monovariable) {.theorem #TFC .one}
Soit $x \in \R$ et $h\geq 0$.
Si la fonction $f: [x, x+h] \subset \R \to \R^m$ est dérivable 
et que sa dérivée $f'$ est intégrable alors
$$
f(x+h) - f(x)  = \int_x^{x+h} f'(y) \, dy.
$$

### Démonstration {.proof}
Voir l'enseignement de calcul intégral.

### À propos du terme "intégrable" {.remark .three}
À ce stade, vous pouvez retenir que si $f'$ est continue, 
continue par morceaux ou même intégrable au sens de Riemann, 
elle est "intégrable" comme le demandent les hypothèses du théorème.

Dans ce chapitre, sauf précision contraire, le terme "intégrable" 
doit être compris comme "intégrable au sens de Lebesgue". 
La définition de ce concept 
-- ainsi que la preuve du théorème fondamental du calcul -- 
seront fournies dans le volet calcul intégral de l'enseignement.  


### Forme générale du théorème fondamental du calcul {.remark .four #TFCE}
Si l'on adopte au lieu de l'intégrale de Lebesgue l'intégrale encore
plus générale de Henstock-Kurzweil (cf. calcul intégral), 
alors toute fonction dérivée est automatiquement 
intégrable. 
Le théorème fondamental du calcul est alors valable en toute généralité ; 
il prend la forme suivante : si $x \in \R$, $h\geq 0$ et 
la fonction $f: [x, x+h] \to \R^m$ est dérivable, alors $f'$ est intégrable 
(au sens de Henstock-Kurzweil) et
$$
f(x+h) - f(x)  = \mbox{(HK)} \int_x^{x+h} f'(y) \, dy.
$$
Cette forme avancée du théorème est toutefois rarement nécessaire ; 
elle est néanmoins utile pour prouver 
[l'inégalité des accroissements finis](#TAFS) en toute généralité.
Cette extension est aussi applicable à 
[la version multivariable du théorème fondamental du calcul](#VF) : 
si l'on utilise l'intégrale de Henstock-Kurzweil, il sera inutile
de vérifier que l'application 
$t \mapsto df(x+th)  \cdot h$ est intégrable pour appliquer le théorème ;
comme dérivée de l'application $t \mapsto f(x+th)$, 
cette fonction l'est automatiquement.

### Théorème fondamental du calcul (multivariable) {.theorem #VF .two}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$,
$x \in U$ et $h \in \mathbb{R}^n$ tels que le segment
  $$
  [x, x+h] = \{x + th \; | \; t \in [0,1]\}
  $$
soit inclus dans $U$. Si $f$ est différentiable en tout point de $[x, x+h]$
et que l'application $t \in [0,1] \mapsto df(x+th) \cdot h \in \R^m$ 
est intégrable, alors
$$
f(x + h) - f(x) = \int_0^1 df(x+th) \cdot h \, dt.
$$

![Géométrie [du théorème du calcul multivariable](#VF)](images/peanut.tex)

### Démonstration {.proof}
L'ensemble $U$ étant ouvert, il existe un $\varepsilon > 0$ tel que
l'intervalle ouvert $I := \left]-\varepsilon, 1+\varepsilon \right[$ 
soit inclus dans $U$. 
On note $\phi$ la fonction $I \to \mathbb{R}^n$ 
définie par
$$
\phi(t) = f(x + th)
$$
La fonction $\phi$ est différentiable -- et donc dérivable -- 
en tout point de $[0,1]$ [comme composée des fonctions 
différentiables $f$ et $t \mapsto x + th$](#chain-rule) ; 
sa dérivée est donnée par
$$
\begin{split}
\phi'(t) &= d\phi(t) \\
         &= df(x+th) \cdot d(t \mapsto x+th) \\
         &= df(x+th) \cdot (t \mapsto x+th)' \\
         &= df(x+th) \cdot h
\end{split}
$$
Par [le théorème fondamental du calcul](#TFC), comme par hypothèse $\phi'$ 
est intégrable sur $[0, 1]$, on a donc
$$
f(x+h) - f(x) = \phi(1) - \phi(0) = \int_0^1 \phi'(t) \, dt 
                                  = \int_0^1 df(x+th) \cdot h \, dt.
$$

### Cas des fonctions continûment différentiables {.exercise .one .question #cfcd3}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$,
$x \in U$ et $h \in \mathbb{R}^n$ tels que le segment
$[x, x+h] = \{x + th \; | \; t \in [0,1]\}$
soit inclus dans $U$. 
Montrer que si $f$ est continûment différentiable sur $U$, 
[le théorème fondamental du calcul](#VF) est applicable.

### Inégalité des accroissements finis (monovariable) {.theorem #TAFS .two}
Soit $x \in \R$, $h \geq 0$, $f:[x, x+h] \to \mathbb{R}^m$.
Si $f$ est dérivable sur $[x,x+h]$ et $M$ est un majorant de $\|f'\|$,
c'est-à-dire si
$$
\mbox{pour tout } y \in [x, x+h], \;\|f'(y)\| \leq M.
$$
Alors 
$$
\|f(x+h) - f(x)\| \leq M h.
$$

### Démonstration {.proof}
Par [la forme générale du théorème fondamental du calcul](#TFCE),
la fonction $f'$ est intégrable au sens de Henstock-Kurzweil et
$$
f(x+h) - f(x) =  \mbox{(HK)} \int_x^{x+h} f'(y) \, dy.
$$
La théorie de l'intégrale de Henstock-Kurzweil nous garantit qu'il est possible 
d'obtenir des approximations arbitrairement précises de cette intégrale au moyen de 
sommes de Riemman[^aci]. Cela signifie que pour tout $\varepsilon > 0$, 
il existe des réels $x_0, \dots, x_k, t_0, \dots, t_{k-1}$ vérifiant
$$
x = x_0 \leq t_0 \leq x_1 \leq t_1 \leq  \dots \leq x_{k-1} \leq t_{k-1} \leq x_{k} = x+h
$$
telle que la somme
$$
S = \sum_{i=0}^{k-1} f'(t_i)(x_{i+1} - x_i)
$$
satisfasse
$$
\left\|  \mbox{(HK)} \int_x^{x+h} f'(t) \, dt -  S \right\| 
\leq 
\varepsilon.
$$

[^aci]:  en combinant la définition de l'intégrabilité de $f'$ 
au sens de Henstock-Kurzweil et 
[le lemme de Cousin](Calcul Intégral I.pdf#cousin) du calcul intégral.

En exploitant deux fois l'inégalité triangulaire, on obtient donc
$$
\|f(x+h) - f(x)\|
\leq 
\|S\| + \varepsilon \leq \sum_{i=0}^{k-1} \|f'(t_i)\| |x_{i+1} - x_i| +\varepsilon.
$$
Comme $\|f'(t_i)\| \leq M$ pour tout $i \in \{0,\dots,k-1\},$
$$
\sum_{i=0}^{k-1} \|f'(t_i)\| |x_{i+1} - x_i|
\leq
\sum_{i=0}^{k-1} M |x_{i+1} - x_i|
\leq M \sum_{i=0}^{k-1} |x_{i+1} - x_i|
$$
et comme $x=x_0 \leq x_1 \leq \dots \leq x_k = x+h$,
$$
\sum_{i=0}^{k-1} |x_{i+1} - x_i| = \sum_{i=0}^{k-1} (x_{i+1} - x_i) =
x_p - x_0 = (x+h) - x = h.
$$ 
On a donc $\|S\| \leq Mh$  et
par conséquent $\|f(x+h) - f(x)\| \leq M h + \varepsilon$ ;
le choix de $\varepsilon > 0$ étant arbitraire, on en déduit
le résultat cherché.


### {.remark}
L'énoncé de l'inégalité des accroissements finis ne fait aucune hypothèse sur 
la régularité de la fonction $f'$ ; c'est cette généralité qui rend sa 
démonstration technique. Si l'on accepte des hypothèses un peu plus 
contraignantes, elle peut être simplifiée de façon significative.

### Cas des fonctions continûment différentiables {.exercise .question .one #cfcd2}
Trouver une démonstration simple de [l'inégalité des accroissement finis](#TAFS)
reposant sur [le théorème fondamental du calcul](#TFC)
dans le cas où la fonction $f'$ est continue (ou continue par morceaux,
ou intégrable au sens de Riemann, ou intégrable au sens de Lebesgue, 
selon la théorie de l'intégration que vous connaissez à ce stade).

### {.remark}
Il existe également une démonstration alternative
de l'inégalité des accroissements finis qui ne repose pas sur le calcul intégral, 
mais sur les identités associées à la norme euclidienne et sur le théorème des
valeurs intermédiaires :

### Inégalité des accroissements finis (version euclidienne)  {.exercise #mitch .question .two}
Soit $\phi: y \in [a, a+h] \to \R$ la fonction définie par
$$
\phi(y) = \left<f(x+h) - f(x), f(y) \right>.
$$
En appliquant le théorème des valeurs intermédiaires à $\phi$, 
prouver [l'inégalité des accroissements finis](#TAFS).

### Inégalité de la valeur moyenne {.exercise .one .question #ivm}
Soit $f:[a, b] \subset \R \to \R^m$ une fonction intégrable et admettant une
primitive ;
on appelle *valeur moyenne de $f$* la grandeur
$$
\left<f\right> := \frac{1}{b-a} \int_a^b f(x) \, dx.
$$
Quel est le lien entre $\left<f\right>$ et la grandeur 
$\sup_{x \in [a, b]} \|f(x)\|$ ?

### Égalité des accroissements finis ? {.question #eaf .exercise .one}
Soit $f:[0, 2\pi] \to \mathbb{R}^2$ la fonction définie par
$$
f(t) = (\cos t, \sin t)
$$
Peut-on trouver un $t \in [0, 2\pi]$ tel que $f(2\pi) - f(0) = f'(t) \times 2\pi$ ?


### Inégalité des accroissements finis (multivariable) {.theorem #TAF .two}

Soient $U$ un ouvert de $\mathbb{R}^n$, et $f: U \to \mathbb{R}^m$
supposée différentiable en tout point d'un segment $[a, a+h]$ inclus 
dans $U$ et dont la différentielle est majorée en norme par $M$ sur $[a, a+h]$, 
c'est-à-dire telle que
$$
\mbox{pour tout } x \in [a, a+h], \;\|df(x)\| \leq M.
$$
Alors 
$$
\|f(a+h) - f(a)\| \leq M \|h\|.
$$


### Démonstration {.proof}
Considérons la fonction $\phi: t \mapsto f(a+th)$ déjà exploitée 
dans la démonstration de la proposition ["Variation d'une fonction"](#VF) ;
cette fonction est dérivable sur $[0,1]$, de dérivée $\phi'(t) = df(a+th) \cdot h$.
De plus, 
$$
\|\phi'(t)\| = \| df(a+th) \cdot h \| \leq \| df(a+th) \|\|h\| \leq M \|h\|.
$$
Par [l'inégalité des accroissements finis dans le cas d'une variable réelle](#TAFS), 
$$
\|f(a+h) - f(a)\| = \|\phi(1) - \phi(0)\|
\leq M \|h\| \times 1 = M \|h\|.
$$

### Variation du logarithme {.exercice .two .question #log}
Il est possible de définir une version multivariable et vectorielle 
de la fonction logarithme, définie sur le *plan coupé*
$$U = \R^2 \setminus \{(x, 0) \; | \;  x \leq 0\}$$ et à valeurs dans $\R^2$. 
Cette fonction est différentiable et vérifie en tout point
$$\|d \log (x, y)\| = \frac{1}{\sqrt{x^2 + y^2}}.$$ 
Montrer que pour tout $(x, y) \in U$, on a 
$$
\|\log (x, y) - \log (x, -y)\| \leq 2 \pi.
$$

### Normes non euclidiennes {.remark .four}

Les versions [monovariable](#TAFS) et [multivariable](#TAF) de l'inégalité des 
accroissements finis peuvent être généralisées à d'autres normes que la 
norme euclidienne. Dans le cas monovariable, si $\|\cdot\|_{\R^m}$ est
une norme arbitraire sur $\R^m$ et que l'on dispose de la borne $\|f'(y)\|_{\R^m} \leq M$
sur $[x, x+h]$,
alors on peut conclure que $$\|f(x+h) - f(x)\|_{\R^m} \leq Mh.$$ 
Dans le cas multivariable, si de plus $\|\cdot\|_{\R^n}$ est une norme arbitraire 
sur $\R^n$ et que l'on définit pour tout $A \in \R^{m\times n}$ la norme d'opérateur
associée
$$
\|A\|_{\R^{m\times n}} := \sup_{x \neq 0} \frac{\|A \cdot x\|_{\R^m}}{\|x\|_{\R^n}},
$$
alors on peut déduire de la borne $\|df(y)\|_{\R^{m\times n}} \leq M$ sur $[x, x+h]$ 
que $$\|f(x+h) - f(x)\|_{\R^m} \leq M \|h\|_{\R^n}.$$
Seules des modifications mineures des démonstrations déjà présentées sont 
nécessaires pour établir ces résultats.

Annexes
================================================================================

Dérivée
--------------------------------------------------------------------------------

### Dérivée {.definition .zero}
Soient $U$ un ouvert de $\R$, $f: U \to \mathbb{R}^m$ et $x \in U$.
La fonction $f$ est *dérivable en $x$* si la limite du 
*taux d'accroissement* de $f$ en $x$ existe ; 
cette limite est appelée *dérivée de $f$ en $x$* 
et notée $f'(x)$ :
$$
f'(x) := \lim_{\substack{h \to 0 \\ h \neq 0}} \frac{f(x+h) - f(x)}{h}.
$$
La fonction $f$ est *dérivable (sur $U$)* si elle est dérivable en tout point
$x$ de $U$.

### {.remark}
Cette définition accomode sans difficulté le cas des fonctions scalaires
et vectorielles d'une variable réelle. 
Dans ce second cas, il suffit d'interpréter le terme 
$(f(x+h) - f(x)) / h$ comme la multiplication du vecteur $f(x+h) - f(x)$
par le scalaire $1/h$. En outre, la dérivée d'une fonction vectorielle
se déduit aisément de la dérivée de ses composantes :

### Dérivée composante par composante {.definition .zero #der-cc}
Soient $U$ un ouvert de $\R$, $f: U \to \mathbb{R}^m$ et $x \in U$.
La fonction $f$ est dérivable en $x$ si et seulement si pour tout 
$i \in \{1,\dots, m\}$, sa $i$-ème composante $f_i  : U \to \R$ est dérivable
en $x$. 
On a alors $(f'(x))_i = f_i'(x)$.


### {.post .remark}
La définition de dérivée couvre le cas où la fonction $f$ est définie sur un 
intervalle ouvert $\left]a, b\right[$ -- ou d'ailleurs sur une réunion arbitraire
d'intervalles ouverts de $\R$ --
mais pas sur un intervalle fermé et borné $[a, b]$. 
Pour appréhender ce cas, on introduit classiquement les notions de dérivées 
à gauche et à droite.

### Dérivée sur un intervalle fermé et borné {.definition .zero}
Soient $a, b \in \R$ avec $a < b$ et $f: [a, b] \to \mathbb{R}^m$.
La fonction $f$ est *dérivable sur $[a, b]$* 
si elle est dérivable sur l'intervalle ouvert $\left]a, b\right[$ 
et que les dérivées de $f$ à droite en $a$ et à gauche en $b$ existent.
On pose alors
$$
f'(a) := \lim_{\substack{h \to 0 \\ h > 0}} \frac{f(a+h) - f(a)}{h}
\; \mbox{ et } \;
f'(b) := \lim_{\substack{h \to 0 \\ h < 0}} \frac{f(b+h) - f(b)}{h}.
$$

### {.remark}
Alternativement, on peut utiliser une pirouette pour se ramener à un domaine
de définition ouvert. Cette approche nous est utile pour intégrer les dérivées 
au calcul différentiel multivariable qui n'est développé que 
pour des domaines de définition ouverts.

### Dérivée et prolongement {.proposition .one #dep}
Soient $a, b \in \R$ avec $a < b$ et $f: [a, b] \to \mathbb{R}^m$.
La fonction $f$ est dérivable sur $[a, b]$ si et seulement si elle admet un 
prolongement $g$ à un ensemble ouvert $U$ de $\R$ contenant $[a, b]$ qui soit 
dérivable. Si c'est le cas, sa dérivée $f'$ est égale à la restriction 
de la fonction $g'$ à $[a, b]$.

\newcommand{\lb}{\left]}
\newcommand{\rb}{\right[}

![Un prolongement dérivable de $f:x \in [0,1] \mapsto e^{-x}$ à $\lb-0.5, 1.5 \rb$.
Ce prolongement $g$ est défini par 
$g(x) = 1 - x$ si $x < 0$ et $g(x) = (2-x)/e$ si $x>1$.](images/prolongement.tex)

### Dérivée et prolongement {.exercise .one .question #exo-dep}
Démontrer la proposition ["Dérivée et prolongement"](#dep).

### {.remark .ante}
La dérivabilité est équivalente à l'existence d'un développement limité au
1er ordre ; si elle est acquise, la valeur de la fonction et de sa dérivée
au point de référence fournissent ce développement.

### Dérivée et développement limité  {.proposition .zero #ddl}
Soient $U$ un ouvert de $\R$, $f: U \to \mathbb{R}^m$ et $x \in U$.
Si la fonction $f$ est dérivable en $x$, alors dans un voisinage de $x$
on a
$$
f(x+h) = f(x) + f'(x) h + \varepsilon(h)|h|
$$
où la fonction $\varepsilon$, définie dans un voisinage de $h=0$ et à valeurs
dans $\R^m$, satisfait
$$
\lim_{h \to 0}\varepsilon(h) = 0.
$$

###  Dérivée et développement limité (réciproque)  {.proposition .zero #ddlr}
Soient $U$ un ouvert de $\R$, $f: U \to \mathbb{R}^m$ et $x \in U$.
S'il existe deux vecteurs $a$ et $b$ de $\R^m$ tels que
$$
f(x+h) = a + b h + \varepsilon(h)|h|
$$
pour une fonction $\varepsilon$ définie dans un voisinage de $h=0$ 
telle que $\lim_{h \to 0}\varepsilon(h) = 0$,
alors $f$ est dérivable en $x$, $a=f(x)$ et et $b = f'(x)$.

Calcul matriciel
--------------------------------------------------------------------------------

### {.remark}
Les fragments de code de ce document utilisent le langage Python 3.
La bibliothèque [NumPy](http://www.numpy.org/) est exploitée :

    >>> from numpy import *

<!--
Ensembles et fonctions
--------------------------------------------------------------------------------

La notation classique $f: A \to B$ pour désigner une fonction $f$ d'un
ensemble $A$ dans un ensemble $B$ suggère d'utiliser $A \to B$ 
pour désigner l'ensemble des fonctions de $A$ dans $B$.
Avec cette convention, $f: A \to B$ signifie la
même chose que $f \in A \to B$.

La convention que nous adoptons a vocation à simplifier la manipulation
de fonctions dont les valeurs sont des fonctions, un schéma très fréquent
en calcul différentiel.
Si $f: A \to B$ et $g: B \to C$, la composée des fonctions $f$ et $g$,
notée $g \circ f$, appartient à $A \to C$ et est définie par
$$
(g \circ f) (x) = g(f(x)).
$$
Si l'on applique bien $f$ à $x$, puis $g$ au résultat, il est néanmoins
naturel d'inverser l'ordre d'apparition des fonctions dans la notation $g \circ f$;
il faut en effet s'adapter à la notation classique (infixe ou polonaise) 
qui désigne par $f(x)$ l'image de $x$ par $f$. 
Pour cette même raison, il pourra être utile de
d'utiliser $B \leftarrow A$ comme une variante de la notation $A \to B$.
On pourra alors utiliser la règle
$$
g: C \leftarrow B, \; f: B \leftarrow A \; \implies \; g \circ f: C \leftarrow A
$$
où les notations des ensembles et fonctions $g$, $f$, $A$, $B$ et $C$
restent dans le même ordre d'apparition et les deux occurrences de 
l'ensemble intermédiaire $B$ se touchent.

-->

<!-- -------------------------------------------------------------------------------- -->

### Multiplication scalaire-vecteur
Pour tout scalaire $\lambda \in \mathbb{R}$ et vecteur $x \in \mathbb{R}^n$,
on notera $\lambda x$ ou parfois $x \lambda$ la multiplication du vecteur $x$ 
par le scalaire $\lambda$. Lorsque $\lambda$ est non nul, on
notera également $x / \lambda$ le vecteur $(1 / \lambda) x$.

Un vecteur de $\mathbb{R}^n$ est représenté dans NumPy par un tableau à une
dimension :

    >>> x = array([1, 2, 3])
    >>> x.ndim
    1
    >>> shape(x)
    (3,)
    >>> size(x)
    3

La multiplication d'un scalaire et d'un vecteur est désignée par le symbole
`*` :

    >>> 2 * x
    array([2, 4, 6])

### Matrices

Nous noterons $\mathbb{R}^{m \times n}$ l'ensemble des matrices à 
$m$ lignes et $n$ colonnes à coefficients réels. 
Une matrice telle que

$$
\left[
\begin{array}{ccc}
1 & 2 & 3 \\
4 & 5 & 6
\end{array}
\right] \in \mathbb{R}^{2 \times 3}
$$

sera représentée avec NumPy par un tableau bi-dimensionnel:

    >>> A = array([[1, 2, 3], [4, 5, 6]])
    >>> A
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> A.ndim
    2
    >>> shape(A)
    (2, 3)
    >>> size(A)
    6

<!--
### Mise à plat des matrices {.warning #flatten}
Dans la notation $\mathbb{R}^{m \times n}$, 
$\times$ est un symbole de séparation, purement syntactique : 
$\mathbb{R}^{2 \times 3}$ désigne ainsi 
l'ensemble des matrices à 2 lignes et 3 colonnes à coefficients réels 
et diffère de $\mathbb{R}^6$ qui
désigne l'ensemble des $6$-uplets à coefficients réels. 

Ces deux ensembles sont toutefois similaires: pour toute matrice 
$A \in \mathbb{R}^{m\times n}$, on peut construire un $mn$-uplet en 
listant tous les coefficients de la matrices en parcourant l'ensemble 
des lignes de la matrice de haut en bas et chaque ligne de gauche à
droite; cette façon de faire définit un vecteur de $\mathbb{R}^{mn}$.
L'opération ainsi définie sera notée $\pi_{m\times n}$ (voire $\pi$
s'il n'y a pas d'ambiguité).
Par exemple :

$$
\pi_{2 \times 3}: 
\left[
\begin{array}{ccc}
1 & 2 & 3 \\
4 & 5 & 6
\end{array}
\right] \in \mathbb{R}^{2 \times 3}
\; \mapsto \;
(1,2,3,4,5,6) \in \mathbb{R}^6
$$

Cette opération est bijective ; elle-même ainsi que son inverse sont linéaires.
$\mathbb{R}^{m \times n}$ et $\mathbb{R}^{m n}$ sont donc isomorphes (en tant
qu'espace vectoriels), ce que l'on notera :

$$
\mathbb{R}^{m \times n} \, \cong \, \mathbb{R}^{mn}
$$

Le passage de la forme matrice à la forme vecteur se fait de la façon suivante
avec NumPy:

    >>> A
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> a = reshape(A, (6,))
    >>> a
    array([1, 2, 3, 4, 5, 6])
    >>> reshape(a, (2, 3))
    array([[1, 2, 3],
           [4, 5, 6]])
-->

### Applications linéaires

<!--
Notons
$$
\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m
\; \mbox{ ou } \;
\mathbb{R}^m \stackrel{\ell}{\leftarrow} \mathbb{R}^n
$$ 
l'ensemble des applications linéaires de $\mathbb{R}^n$ dans $\mathbb{R}^m$.
-->
La raison d'être des matrices $\mathbb{R}^{m \times n}$ est de représenter
les applications linéaires de $\R^n$ dans $\R^m$.
Si $A$ désigne une telle application linéaire, notons $A_i$ ses
$m$ composantes scalaires :
$$
A = (A_1, A_2, \dots, A_m).
$$
Si l'on désigne maintenant par $e_j$ le $j$-ème vecteur de la base canonique de 
$\mathbb{R}^n$
$$
e_1 = (1, 0, 0, \dots, 0), \; e_2 = (0,1,0,\dots, 0), \; \dots \;, \;
e_n = (0,0,0,\dots, 1),
$$
il est possible d'associer à l'application linéaire 
$A: \mathbb{R}^n \to \mathbb{R}^m$ la matrice
$$
[A] :=
[A_i(e_j)]_{ij}=
\left[ 
\begin{array}{ccccc}
A_1(e_1) & A_1(e_2) & \cdots & A_1(e_n) \\
\vdots & \vdots & \vdots & \vdots\\
A_m(e_1) & A_m(e_2) & \cdots & A_m(e_n)
\end{array}
\right] \in \mathbb{R}^{m \times n}.
$$
Réciproquement, étant donné une matrice
$$
[a_{ij}]_{ij}=
\left[ 
\begin{array}{ccccc}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots & \vdots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{array}
\right] \in \mathbb{R}^{m \times n},
$$
il est possible de définir une application linéaire 
$A: \mathbb{R}^n \to \mathbb{R}^m$ par la relation
$$
(A \cdot x)_i := \sum_{j} a_{ij} x_j
$$
et cette opération est l'inverse de la précédente.
Techniquement, cette correspondance établit un isomorphisme d'espaces vectoriels 
entre les applications linéaires de $\mathbb{R}^n$ dans $\mathbb{R}^m$ et 
les matrices de $\R^{m \times n}$.

### Composition d'applications linéaires
 
Si $A$ et $B$ désignent des applications linéaires de 
$\mathbb{R}^p$ dans $\mathbb{R}^n$ et de $\mathbb{R}^n$ dans $\mathbb{R}^m$ 
respectivement, la fonction composée $C = B \cdot A$ est une application
linéaire qui vérifie
  $$
  C_{ij} = \sum_{k} B_{ik} A_{kj}.
  $$
Autrement dit, la composition de fonction linéaires se traduit par la
multiplication des matrices associées.

<!--
Dans la suite on évitera en général l'utilisation du symbole $\circ$ pour
désigner la composition d'applications linéaires, en lui préférant le
symbole $\cdot$ ("point"). 

Le même symbole sera utilisé pour désigner le produit
entre deux matrices (on évitera dans la mesure du possible de désigner
le produit de deux matrices par simple juxtaposition des symboles).
-->

La méthode `dot` des tableaux NumPy permet de calculer ce produit matriciel :

    >>> A = array([[1, 2, 3], [4, 5, 6]])
    >>> B = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> A.dot(B)
    array([[1, 2, 3],
           [4, 5, 6]])

### Adjoint d'un opérateur
Lorsque $A: \R^n \to \R^m$ est un opérateur linéaire, on peut définir de
façon unique l'opérateur adjoint $A^{\top} : \R^m \to \R^n$ comme l'unique
opérateur tel que pour tout $x \in \R^n$ et tout $y \in \R^m$, on ait
$$
\left<y, A \cdot x \right> = \left<A^{\top} \cdot y, x \right>.
$$
La matrice associée à $A^{\top}$ est la transposée de la matrice représentant $A$ :

    >>> A
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> A.T
    array([[1, 4],
           [2, 5],
           [3, 6]])


### Vecteurs colonnes et vecteur lignes
Dans le cadre du calcul matriciel, on associe souvent à un vecteur 
$x=(x_1, \dots, x_n)$ de $\mathbb{R}^n$ le vecteur colonne
$$
\left[ 
\begin{array}{c}
x_1 \\
\vdots \\
x_n
\end{array}
\right] \in \mathbb{R}^{n \times 1}.
$$
Dans cette terminologie, un vecteur colonne n'est pas, 
malgré son nom, un vecteur de $\mathbb{R}^n$, mais bien 
une matrice de taille $n \times 1$. 
Formellement, on a associé à $x$
une matrice
$X \in \mathbb{R}^{n\times 1}$, telle que $X_{i1} = x_i$.
Le produit entre une matrice et un vecteur colonne de taille compatible
n'est rien d'autre qu'un produit matriciel classique. 

<!--
Le vecteur $x$ étant associé à une matrice, on peut se demander quel
opérateur linéaire est associé à cette matrice. La réponse est simple:
il s'agit de l'application
$$
\lambda \in \R \mapsto \lambda x \in \R^n.
$$
Identifier un vecteur et son opérateur linéaire de $\R \to \R^n$
permet par exemple de disposer "gratuitement" de la définition 
$x^*$ (l'adjoint de l'opérateur associé à $x$) : il s'agit
de l'application linéaire de $\R^n$ dans $\R$ dont la matrice
est la transposée du vecteur colonne associé à $x$, autrement dit,
la représentation de $x$ comme vecteur ligne.
-->

<!--
L'intérêt de la représentation des vecteurs comme vecteurs colonnes : 
si $A$ est une application linéaire de $\mathbb{R}^n$ dans
$\mathbb{R}^m$ et $x$ un vecteur de $\mathbb{R}^n$, le vecteur
image $y=A \cdot x \in \mathbb{R}^m$ de $x$ par $A$ est représenté par 
le vecteur colonne qui est le produit entre 
la représentation de $A$ comme matrice et la représentation de
$x$ comme vecteur colonne.
-->

Concrètement, NumPy ne nécessite pas qu'un vecteur soit d'abord 
transformé en matrice pour réaliser un produit matrice-vecteur.
La méthode `dot` des tableaux peut être utilisée ici aussi 
pour réaliser cette opération :

    >>> A = array([[1, 2, 3], [4, 5, 6]])
    >>> x = array([7, 8, 9])
    >>> A.dot(x)
    array([ 50, 122])

Le produit matriciel étant associatif, tant que l'on manipule des matrices
et des vecteurs, il n'y a pas lieu de préciser si $A \cdot B \cdot C$ 
désigne $(A \cdot B) \cdot C$ (association à gauche) ou $A \cdot (B \cdot C)$
(association à droite).
Comme le produit matrice-vecteur est un produit matriciel classique,
quand $x$ est un vecteur, 
$A \cdot B \cdot x$ désigne indifféremment $(A \cdot B) \cdot x$ ou
$A \cdot (B \cdot x)$.

Exercices complémentaires
================================================================================

<!--
Vecteurs, vecteurs colonnes, vecteurs lignes
--------------------------------------------------------------------------------

Soit $x = (x_1, \cdots, x_n)$ un vecteur de $\mathbb{R}^n$.

### Question 1
Le vecteur colonne $X$ associé à $x$
$$
X = \left[ 
\begin{array}{c}
x_1 \\
\vdots \\
x_n
\end{array}
\right] \in \mathbb{R}^{n \times 1}.
$$
est une matrice et représente donc une application linéaire. Laquelle ?

$\to$ [Solution](#sol-vvcvl-1)

### Question 2
Le vecteur colonne ligne $X^*$ associé à $x$
$$
X^* = \left[ 
\begin{array}{ccc}
x_1 & \cdots & x_n
\end{array}
\right] \in \mathbb{R}^{1 \times n}.
$$
représente également une application linéaire. Laquelle ?

$\to$ [Solution](#sol-vvcvl-2)

-->

<!--
### TODO

Pt spline / point de contôle. Avec dessin. 

Question / "contrôle de la direction" d'un point / mouvement point de contrôle ?

-->

Spécialisation de la différentiation en chaîne {#dec}
--------------------------------------------------------------------------------

[La règle générale de différentiation en chaîne](#chain-rule)
s'applique à la composée de deux fonctions différentiables 
$f: U \subset \R^p \to \R^n$ et $g: V \subset \R^n \to \R^m$
quelles que soient les valeurs des entiers $p, n$ et $m$.

En pratique, on préfère souvent "spécialiser" le calcul différentiel 
en utilisant les dérivées ou les gradients quand c'est possible
et la différentielle uniquement en dernier recours.

### Question 1 {.question #dec-1 .zero}
Spécialiser [la règle de différentiation en chaîne](#chain-rule)
quand $p=n=1$.

### Question 2 {.question #dec-2 .one}
Spécialiser [la règle de différentiation en chaîne](#chain-rule)
quand $p=m=1$, puis quand $n=m=1$.

### Question 3 {.question #dec-3 .two}
Spécialiser [la règle de différentiation en chaîne](#chain-rule)
quand $p=1$, puis $n=1$, puis $m=1$.



<!--
Soit $f: U \subset \mathbb{R} \to \mathbb{R}$ et 
$g: V \subset \mathbb{R} \to \mathbb{R}$ deux fonctions définies
sur des ouverts $U$ et $V$ et telles que $f(U) \subset V$. 
Si $f$ est dérivable en $x \in U$ et $g$ est dérivable en $f(x) \in V$,
alors la composée $g \circ f$ est dérivable en $x$ et
$$
(g \circ f)'(x) = g'(f(x)) f'(x).
$$
-->

Fonction quadratique 
--------------------------------------------------------------------------------
Soit $A: \R^n \to \R^n$ un opérateur linéaire, $b$ un vecteur de $\R^n$ et
$c \in \R$. On considère la fonction $f:\R^n \to \R$ définie par
$$
f(x) = \frac{1}{2} \left<x, A \cdot x \right> + \left<b, x\right> + c. 
$$

### Question 1 -- Gradient {.question #fq-1 .two}
Montrer que $f$ différentiable en tout point $x$ de $\R^n$ et
calculer $\nabla f(x)$.

### Question 2 -- Matrice hessienne {.question #fq-2 .one}
Montrer que la fonction $\nabla f: \R^n \to \R^n$ est différentiable et
calculer la matrice jacobienne de $\nabla f$ en $x$. On note désormais
 $H_f(x) := J_{\nabla f}(x)$.

### Question 3 -- Point critique {.question #fq-3 .one}
Soit $x \in \R^n$ ; on suppose que $H_f(x)$ est inversible. 
Montrer qu'il existe un unique $x_0 \in \R^n$ où s'annule $\nabla f$ ; 
le calculer en fonction de $x$, $\nabla f(x)$ et $H_f(x)$.

### Question 4 -- Vecteur gaussien {.question #fq-4 .two}
La densité de probabilité associée à un vecteur gaussien $X \in \R^d$ 
est proportionnelle à la fonction
$$
g: x \in \R^d \mapsto \exp\left( -\frac{1}{2} \left<x, \Sigma^{-1} \cdot x \right> \right)
$$
où $\Sigma : \R^d \to \R^d$ est un opérateur linéaire autoadjoint 
($\Sigma^{\top} = \Sigma$) tel que $\left<x, \Sigma \cdot x \right> > 0$ quand $x\neq 0$.

Montrer que la fonction $g$ est différentiable et calculer son gradient.

Robot manipulateur
--------------------------------------------------------------------------------

Les coordonnées cartésiennes $x$ et $y$ de l'effecteur final 
d'un robot dans le plan, composé de deux barres rigides de longueur
$\ell_1$ et $\ell_2$ et d'articulations rotoïdes sont données
par
$$
\left|
\begin{array}{rcl}
x &=& \ell_1 \cos \theta_1 + \ell_2 \cos (\theta_1 + \theta_2) \\
y &=& \ell_1 \sin \theta_1 + \ell_2 \sin (\theta_1 + \theta_2) \\
\end{array}
\right.
$$
où $\theta_1$ et $\theta_2$ sont les coordonnées articulaires du robot.

![$\ell_1 = 3$, $\ell_2 = 2$, $\theta_1 = \pi/4$, $\theta_2 = - \pi/4$.](images/robot.tex){#robot}

On souhaite quantifier quel impact un jeu au niveau des articulations affecte
la précision du positionnement de l'effecteur final.

### Question 1  {.question #rm-1 .one}
Montrer que l'application 
$f: (\theta_1, \theta_2) \in \R^2 \mapsto (x, y) \in \R^2$ 
est différentiable et déterminer sa matrice jacobienne.

### Question 2  {.question #rm-2 .two}

Soit $(\theta_{10}, \theta_{20}) \in \R^2$ et 
$(x_0, y_0) = f(\theta_{10}, \theta_{20})$.
Montrer que si 
$$|\theta_1 - \theta_{10}| \leq \varepsilon \; \mbox{ et } \; 
|\theta_2 - \theta_{20}| \leq \varepsilon$$ alors $(x, y) = f(\theta_1, \theta_2)$
appartient au carré centré en $(x_0, y_0)$ d'arête de longueur 
$2(\ell_1 + 2\ell_2) \varepsilon$.

Dérivée directionnelle d'Hadamard
--------------------------------------------------------------------------------

Source : [@Sha90]

Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et $x \in U$. 
La fonction $f$ est *directionnellement dérivable* si pour tout
vecteur $h \in \mathbb{R}^n$, la dérivée directionnelle
$$
f'(x, h) := (t \mapsto f(x+ th))'(0) = \lim_{t \to 0} \frac{f(x+th) - f(x)}{t}
$$
est bien définie.

On introduit une variante à cette définition :
la fonction $f$ est *directionnellement dérivable au sens de Hadamard* 
en $x$ si pour tout chemin $\gamma: I \subset \mathbb{R} \to \mathbb{R}^n$,
défini sur un intervalle ouvert $I$ contenant $0$, tel que
$\gamma(I) \subset U$,  $\gamma(0) = x$ et $\gamma'(0)$ existe,
la dérivée $(f \circ \gamma)'(0)$ existe. 

### Question 1 {.question #ddh-1 .one}
Montrer que si $f$ est directionnellement dérivable au sens de Hadamard 
en $x$, alors $f$ est directionnellement dérivable au sens classique.

### Question 2 {.question #ddh-2 .three}
Montrer que si $f$ est directionnellement dérivable au sens de Hadamard
en $x$, la grandeur $(f \circ \gamma)'(0)$ ne dépend de $\gamma$
qu'à travers $\gamma'(0)$ et que par conséquent
$$
(f\circ \gamma)'(0) = f'(x, \gamma'(0)).
$$

### Question 3 -- Dérivation en chaîne {.question #ddh-3 .two}
Soit $f: U \subset \mathbb{R}^p \to \mathbb{R}^{n}$ et 
$g: V \subset \mathbb{R}^n \to \mathbb{R}^{m}$ deux fonctions définies
sur des ouverts $U$ et $V$ et telles que $f(U) \subset V$. 
Montrer que si $f$ est directionnellement dérivable au sens de Hadamard 
en $x \in U$ et que $g$ est directionnellement dérivable au sens de Hadamard 
en $f(x) \in V$, alors la composée $g \circ f$ est directionnellement 
dérivable au sens de Hadamard en en $x$ et
$$
(g\circ f)'(x, h) = g'(f(x), f'(x, h)).
$$

### Question 4 {.question #ddh-4 .four}
Montrer que $f$ est directionnellement dérivable au sens de Hadamard en $x$ 
si et seulement si la limite
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t}
$$
existe et que la limite est alors égale à $f'(x, h)$.

### Question 5 {.question #ddh-5 .four}
Une fonction dérivable directionnellement au sens de Hadamard en $x$ est 
*différentiable au sens de Hadamard* en $x$ si de plus $f'(x, h)$ 
est une fonction linéaire de $h$.
Montrer que $f$ est différentiable en $x$ au sens de Hadamard 
si et seulement si elle est différentiable en $x$.


Thermodynamique
--------------------------------------------------------------------------------

Pour un gaz parfait, la pression $P$, le volume $V$, le nombre de particules 
$N$ et la température $T$ sont reliés par la relation
$$
PV = N k_B T
$$
où $k_B$ est la constante de Boltzmann. Si en outre le gaz est mono-atomique, 
son entropie $S$ est donnée par l'expression[^gibbs]
$$
S = N k_B \left[\frac{5}{2} + \ln \left(\frac{V}{N} \frac{(2\pi m k_B T)^{3/2}}{h^3} \right)\right]
$$
où $h$ est la constante de Planck et $m$ la masse d'un atome de gaz.
On s'intéresse dans la suite à une quantité fixe d'un gaz donné de ce type.

[^gibbs]: cf. par exemple [l'article consacré au "Paradoxe de Gibbs" sur Wikipédia](https://fr.wikipedia.org/wiki/Paradoxe_de_Gibbs).

### Question 0 {.question #th-0 .zero}
Quelles sont les grandeurs variables ("variables d'état") associées à 
cette expression de l'entropie $S$ ? Quelle intervalle de valeurs peuvent
prendre ces variables ? (On souhaite que l'entropie soit toujours définie.)

### Question 1 {.question #th-1 .one}
Montrer que la différentielle $dS$ est bien définie et la calculer
en utilisant les notations les plus appropriées.

### Question 2 {.question #th-2 .three}
L'énergie interne $U$ du gaz est une fonction des variables d'état 
(une "fonction d'état") ;
sa variation infinitésimale est reliée à celle de l'entropie et 
du volume par la relation
$$
dU = T dS - P dV.
$$
Quel sens donnez-vous à cette relation mathématiquement ? 
Pouvez-vous la réécrire en utilisant les variations associées aux variables
d'état utilisées précédemment ? 

### Question 3 {.question #th-3 .two}
Déduire de la question précédente une expression de l'énergie interne 
(définie à une constante près).




<!--
TODO -- Analycité
--------------------------------------------------------------------------------

Borne sur $f^{(n)}$ et analycité ?

-->

<!--
TODO -- Oloid
--------------------------------------------------------------------------------

Source: [@DS97]

cf <http://www.heldermann-verlag.de/jgg/jgg01_05/jgg0113.pdf>, par exemple
calcul plan tangent ?

-->


<!--
### TODO

$df = 0$ et connexité par arcs.
-->

Solutions
================================================================================

Exercices essentiels
--------------------------------------------------------------------------------

### Dérivée et prolongement {.answer #answer-exo-dep}

Si une fonction $g$ dérivable sur un ouvert $U$ de $\R$ contenant $[a, b]$
prolonge la fonction $f$ définie sur $[a, b]$,
il est clair que $f$ est dérivable en tout point de $[a, b]$ et que
$g'|_{[a, b]} = f'$.

Réciproquement, si $f$ est dérivable sur $[a, b]$ (à droite en $a$ et à gauche
en $b$), alors la fonction $g: \left]-\infty, +\infty \right[ \to \R^m$ définie par 
$$
g(x) = \left|
\begin{array}{rl}
f(a) + f'(a) \times (x-a) & \mbox{si } x < a \\
f(x) & \mbox{si } x \in [a, b] \\
f(b) + f'(b) \times (x-b) & \mbox{si } x > b
\end{array}
\right.
$$
prolonge la fonction $f$ et est dérivable par construction.


### Domaine de définition des fonctions partielles {.answer #answer-ddfp}
La valeur de 
$f(x_1, \cdots, x_{j-1}, y_j, x_{j+1}, \cdots, x_n)$
est définie si et seulement si l'argument $(x_1, \cdots, x_{j-1}, y_j, x_{j+1}, \cdots, x_n)$
appartient à $U$. Le domaine de définition de la fonction partielle
$y_j \mapsto f(x_1, \cdots, x_{j-1}, y_j, x_{j+1}, \cdots, x_n)$
est donc l'image réciproque de $U$ par la fonction
$$
y_j \in \R \mapsto (x_1, \cdots, x_{j-1}, y_j, x_{j+1}, \cdots, x_n) \in \R^n.
$$
Cette fonction étant continue (il s'agit d'une fonction affine) 
et $U$ ouvert par hypothèse, cet ensemble est bien ouvert.


### Gradient et matrice jacobienne {.answer #answer-gmj}
Les deux fonctions partielles de la fonction
$$f:(x_1,x_2) \in \R^2 \mapsto (x_2^2 - x_1)^2 + (x_1 - 1)^2 \in \R$$ sont dérivables,
vérifient $\partial_1 f(x_1, x_2) = -2(x_2^2 - x_1) + 2 (x_1 - 1)$ et 
$\partial_2 f(x_1, x_2) = 4 (x_2^2 - x_1)x_2$. 
Par conséquent,
$$
J_f(x_1, x_2) = 
\left[ 
  \begin{array}{cc}
  -2(x_2^2 - x_1) + 2 (x_1 - 1) &
  4 (x_2^2 - x_1)x_2
  \end{array}
  \right] \in \R^{1 \times 2}.
$$
Son gradient est donc donné par
$$
\nabla f(x_1, x_2)
=
(-2(x_2^2 - x_1) + 2 (x_1 - 1), 4 (x_2^2 - x_1)x_2) \in \R^2
$$
ou, représenté comme un vecteur colonne
$$
\nabla f(x_1, x_2) = J_f(x_1, x_2)^{\top} =
\left[ 
  \begin{array}{c}
  -2(x_2^2 - x_1) + 2 (x_1 - 1) \\
  4 (x_2^2 - x_1)x_2
  \end{array}
  \right] \in \R^{2\times 1}.
$$


### Matrice jacobienne {.exercise .one #answer-exo-mj2} 
La fonction 
$$
g:(x_1, x_2) \in \R^2 \mapsto (-2(x_2^2 - x_1) + 2 (x_1 - 1), 4 (x_2^2 - x_1)x_2) \in \R^2.
$$
a deux composantes, les fonctions (scalaires) 
$$g_1:(x_1, x_2) \in \R^2 \mapsto -2(x_2^2 - x_1) + 2 (x_1 - 1)\in \R
$$
et
$$
g_2:(x_1, x_2) \in \R^2 \mapsto 4 (x_2^2 - x_1)x_2\in \R.$$
En tout point $x=(x_1, x_2)$ de $\R^2$, les fonctions partielles de ces deux
fonctions existent et vérifient
$\partial_1 g_1(x_1, x_2) = 4$, $\partial_2 g_1(x_1, x_2) = -4x_2$,
$\partial_1 g_2(x_1, x_2) = -4x_2$ et $\partial_2 g_2(x_1, x_2) = 12 x_2^2$.
Sa matrice jacobienne est donc définie en tout point et vaut 
$$
J_g(x_1, x_2) = 
\left[ 
  \begin{array}{cc}
  4 & -4x_2 \\
  -4x_2 & 12 x_2^2
  \end{array}
  \right]\in \R^{2 \times 2}.
$$

### Matrice jacobienne et gradient {.answer #answer-matjac}
D'après la définition de [la matrice jacobienne](#matrice-jacobienne) 
et [du gradient](#gradient), on a 
$$
J_f(x) =
\left[
\begin{array}{ccc}
\text{---} & \nabla f_1(x)^{\top} & \text{---} \\
\text{---} & \nabla f_2(x)^{\top} & \text{---} \\
\vdots & \vdots & \vdots \\
\text{---} & \nabla f_m(x)^{\top} & \text{---} \\
\end{array}
\right].
$$

### Fonction discontinue I {.answer #answer-discont}
La fonction $f: \R^2 \to \R$ définie par :
$$
f(x,y) = \left|
\begin{array}{rl}
0 & \mbox{si $x=0$ ou $y=0$,} \\
1 & \mbox{sinon.}
\end{array}
\right.
$$
est discontinue en $(0,0)$, car $f(2^{-n}, 2^{-n}) = 1$ pour tout $n \in \N$,
donc
$$
\lim_{n \to +\infty} f(2^{-n}, 2^{-n}) = 1 \neq 0 = f(0,0).
$$
Par contre, les deux fonctions partielles de $f$ en $(0,0)$
$$
x_1 \mapsto f(x_1, 0) \; \mbox{ et } \; x_2 \mapsto f(0, x_2)
$$
sont constantes et égales à $0$. Les dérivées partielles $\partial_1 f(0,0)$
et $\partial_2 f(0,0)$ existent donc et sont nulles. Le gradient de $f$ en
$(0,0)$ est donc définie (et nul).

### Fonction discontinue II {.answer #answer-discont2}
Les dérivées directionnelles de la fonction $f:\R^2 \to \R$ définie par
$$
f(x,y) 
= \left|
\begin{array}{cl}
1 & \mbox{si } x > 0 \mbox{ et } y=x^2, \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
existent en $(0,0)$ et sont nulles pour tout $h \in \R^2$, 
puisque les fonctions associées $t \in \R \mapsto f(t h)$
sont nulles pour $|t|$ suffisamment petit.
Mais $f$ n'est pas continue en l'origine ; 
elle n'y est donc a fortiori pas différentiable.

### Fonctions affines {.answer #answer-fa}
Comme $f(x) = A \cdot x + b$, la $i$-ème composante de $f$ satisfait
$$
f_i(x) = \sum_{k=1}^n A_{ik} x_k + b_i
$$
et donc la $j$-ème fonction partielle de $f_i$ en $x$ est la fonction 
de la variable $y_j$ dont la valeur est
\begin{multline*}
f_i(x_1, \dots, x_{j-1}, y_i, x_{j+1}, \dots, x_n) = \\
A_{i1} x_1 + \dots + A_{i,j-1} x_{j-1} + A_{ij} y_j + A_{i,j+1} x_{j+1} + b_i.
\end{multline*}
C'est une fonction affine de $y_j$ qui est dérivable, de dérivée
$A_{ij}$. On a donc
$\partial_j f_i(x) = A_{ij}$ ; la matrice jacobienne $J_f(x)$ existe en tout
point $x \in \R^n$ et vérifie $J_f(x) = A$.

Pour tout $x \in \R^n$ et $h \in \R^n$, on a donc
$$
f(x+h) -  f(x) - J_f(x) \cdot h = A \cdot (x+h) - A \cdot x - A\cdot h = 0,
$$
ce que l'on peut écrire sous la forme
$$
f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h) \|h\|
$$
en prenant pour fonction $\varepsilon$ la fonction de $\R^n$ dans $\R^m$ 
identiquement nulle. La fonction $f$ est donc différentiable sur $\R^n$.

### Développement limité au premier ordre {.answer #answer-dlmj}
De l'hypothèse 
$$
f(x+h) = a + B \cdot h + \varepsilon(h) \|h\|
$$
on peut déduire en faisant tendre $h$ vers $0$ que $a = f(x)$,
puis que pour tout $i \in \{1,\dots, n\}$, on a 
$$f_i(x+h) = f_i(x) + [B \cdot h]_i + \varepsilon_i(h) \|h\|$$ et donc
\begin{align*}
\frac{f_i(x + t e_j) - f_i(x)}{t} 
&= \frac{f_i(x) + [B \cdot te_j]_i + \varepsilon_i(te_j) \|te_j\| - f_i(x)}{t} \\
&= [B \cdot e_j]_i + \varepsilon_i(t e_j) \\
&= B_{ij} + \varepsilon_i(t e_j).
\end{align*}
Comme $\lim_{h \to 0}\varepsilon(h) = \varepsilon(0) = 0$,
cette expression a une limite quand $t \to 0$, donc
$\partial_j f_i(x)$ existe et vérifie
$$
\partial_j f_i(x) = \lim_{t \to 0} \frac{f_i(x + t e_j) - f_i(x)}{t} = B_{ij}.
$$
La matrice jacobienne $J_f(x)$ de $f$ en $x$ existe donc et est égale à $B$.

### Différentiabilité implique continuité {.answer #answer-exo-dic}
Comme $f$ est différentiable en $x$, 
sa matrice jacobienne en $x$ existe et 
$$
f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h) \|h\|
$$
avec $\lim_{h \to 0} \varepsilon(h) = 0$. Or $\|J_f(x) \cdot h\| \leq \|J_f(x)\| \|h\|$
donc $\lim_{h\to 0} J_f(x) \cdot h =0$ ; de même $\lim_{h \to 0} \varepsilon(h) \|h\| = 0$.
Par conséquent, $f(x+h) \to f(x)$ quand $h \to 0$.

<!--
### Différentielle et dérivée directionnelle {.answer #answer-exo-ddd}
Comme $f$ est différentiable en $x$ par hypothèse, 
sa matrice jacobienne en $x$ existe et 
$$
f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h) \|h\|
$$
avec $\lim_{h \to 0} \varepsilon(h) = 0$. Par conséquent,
$$
\frac{f(x+ th) - f(x)}{t} = \frac{J_f(x) \cdot (th)}{t} + \frac{\varepsilon(th) \|th\|}{t}
= J_f(x) \cdot h + \frac{|t|}{t}\varepsilon(th) \|h\|,
$$
et donc en passant à la limite, comme $\lim_{t \to 0} \varepsilon(th) = 0$,
$$
f'(x, h) = \lim_{t \to 0} \frac{f(x+ th) - f(x)}{t} = J_f(x) \cdot h.
$$

### Différentielle et dérivée directionnelle {.answer #answer-exo-ddd2}
On peut considérer la fonction $f :\R^2 \to \R$ définie par
$$
f(x_1, x_2) = \left|
\begin{array}{rl}
1 & \mbox{si $x_1 > 0$ et $x_2 = x_1^2$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
Elle n'est pas continue en $(0,0)$, [donc elle n'y est pas différentiable](#dic).
Par contre, pour tout $h \in \R^2$, pour $t$ assez
petit on a $th_2 \neq (t h_1)^2$ et donc $f(th) = 0$ ; par conséquent
$$
f'(0, h) = \lim_{h\to 0} \frac{f(t h) - f(0)}{t} = 0.
$$
La dérivée directionnelle de $f$ en $(0,0)$ dans la direction $h$ existe et
est nulle.
-->

### Différentiabilité {.answer #answer-vareps}
Si $f$ est différentiable en $x$, alors la matrice jacobienne de $f$ en
$x$ existe et il existe
sur un voisinage de $h=0$ une fonction
$\varepsilon$ à valeurs dans $\R^m$ vérifiant $\lim_{h \to 0} \varepsilon(h) = 0$
telle que 
$$
f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h) \|h\|.
$$
On en déduit que sur ce voisinage de $0$ (et hormis pour $h=0$), on a
$$
\varepsilon(h) = \left(\frac{f(x+h) - f(x)}{\|h\|} - J_f(x) \cdot \frac{h}{\|h\|}\right).
$$
Par hypothèse la fonction $\varepsilon$ est continue et nulle en $0$, donc
le membre de droite de cette équation tend bien vers $0$ quand $h\to 0$ 
avec $h\neq 0$.
Réciproquement, si 
$$
\lim_{\substack{h \to 0 \\ h\neq 0}} \left(\frac{f(x+h) - f(x)}{\|h\|} - J_f(x) \cdot \frac{h}{\|h\|}\right) = 0,
$$
on peut définir sur l'ensemble $V$ des $h$ tels que $x+h \in U$ ($U$ étant le domaine
de définition de $f$) la fonction $\varepsilon$ par
$$
\varepsilon(h) = \left|
\begin{array}{cl}
0 & \mbox{si $h=0$,} \\
\displaystyle \frac{f(x+h) - f(x)}{\|h\|} - J_f(x) \cdot \frac{h}{\|h\|} & \mbox{si $h \in V$ et $h\neq 0$.}
\end{array}
\right.
$$
Par construction, $V$ est un voisinage de $0$ et $\varepsilon$ vérifie 
$\lim_{h \to 0} \varepsilon(h) = 0$ ainsi que la relation
$f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h) \|h\|$ ; $f$ est donc
différentiable en $x$.

### Espace-temps {.answer #answer-st}
Etant donné le contexte ("Espace-temps"), il est probable que $c$ désigne la vitesse
de la lumière dans le vide et soit donc considérée comme une constante.
L'expression $e:=x^2 + y^2 + z^2 - c^2 t^2$ est définie pour toutes les valeurs
possibles des variables réelles $x$, $y$, $z$ et $t$. Il est clair que toutes
les dérivées partielles de cette expression existent et sont continues en tout 
point; 
l'application des conventions de la section ["Notations"](#notations) fournit
$$
de = \frac{\partial e}{\partial x} dx + \frac{\partial e}{\partial y} dy + 
\frac{\partial e}{\partial z} dz + \frac{\partial e}{\partial t} dt
= 2 (x \, dx + y \, dy + z \, dz - c^2 t \, dt).
$$

### Robustesse des notations {.answer #answer-rn}
Si l'on considère successivement les jeux de variables 
$(y,x)$ puis de $(x, y, z)$, on obtient
$$
dy \cdot (h_y, h_x) = h_y, \; dx \cdot (h_y, h_x) = h_x 
$$
et 
$$
dx \cdot (h_x, h_y, h_z) = h_x, \; dy \cdot (h_x, h_y, h_z) = h_y, \;
dz \cdot (h_x, h_y, h_z) = h_z. 
$$
Comme on a toujours
$$
\frac{\partial (x^2+y^2) }{\partial x} = 2x, \;
\frac{\partial (x^2+y^2) }{\partial y} = 2y, \;
\frac{\partial (x^2+y^2) }{\partial z} = 0,
$$
on constate qu'on a à nouveau $d(x^2 + y^2) = 2 x \, dx + 2y \, dy$ dans les
deux cas.


### Composition de fonctions continûment différentiables {.answer #answer-cfcd}
D'après [la règle de différentiation en chaîne](#chain-rule), $d (g\circ f)(x)= dg(f(x)) \cdot df(x)$.
Donc pour tout $i \in \{1, \dots, m\}$ et $j \in \{1,\dots, p\}$,
\begin{align*}
[d (g\circ f)(x)]_{ij} &= 
[dg(f(x)) \cdot df(x)]_{ij} \\
&= \sum_{k=1}^n [dg(f(x))]_{ik} [df(x)]_{kj} \\
&= \sum_{k=1}^n \partial_k g_i(f(x)) \partial_j f_k(x).
\end{align*}
Chaque coefficient $\partial_j (g\circ f)_i$ est une somme de produit de 
fonctions continues et est donc continu. Par conséquent, $g\circ f$ est
continûment différentiable.


### Désassemblage {.answer #answer-exo-desass}
Les fonctions $p_1: (x_1,x_2) \in \R^m\times\R^p \mapsto x_1 \in \R^m$
et $p_2: (x_1,x_2) \in \R^m\times\R^p \mapsto x_2 \in \R^p$ sont 
[linéaires, et donc différentiables en tout point $x$](#dal) ; 
leurs différentielles sont données par
$dp_1(x_1, x_2) = p_1$ et $dp_2(x_1, x_2) = p_2$.
Par conséquent, si $U$ est un ouvert de $\R^n$, $x \in U$ et que la fonction
$(f, g): U \to \R^m \times \R^p$ est différentiable en $x$, en appliquant
à deux reprises [la règle de différentiation en chaîne](#chain-rule),
on en déduit que $f = p_1 \circ (f, g)$ et que $g= p_2 \circ (f,g)$ sont
différentiables et que $df(x) = p_1 \cdot d(f,g)(x)$ et $dg(x) = p_2 \cdot d(f,g)(x)$,
soit $d(f, g)(x) = (df(x), dg(x))$.


### Différentiation en chaîne et assemblage {.answer #answer-exo-dca}
La combinaison des deux résultats prend la forme suivante :

> Soient $f_1: U \subset \mathbb{R}^p \to \mathbb{R}^{n_1}$,
> $\dots$, $f_m: U \subset \mathbb{R}^p \to \mathbb{R}^{n_m}$ 
> et $g: V \subset \mathbb{R}^n \to \mathbb{R}^{m}$ 
> -- où $n={n_1 + \dots + n_m}$ --
> des fonctions définies sur des ouverts $U$ et $V$ et telles que $(f_1,\dots, f_m)(U) \subset V$. 
> Si les $f_i$ sont différentiables en $x \in U$ et que $g$ est différentiable en 
> $(f_1(x), \dots, f_m(x)) \in V$,
> alors la composée $g \circ (f_1, \dots, f_m)$ est différentiable en $x$ et
> $$d(g \circ (f_1, \dots, f_m))(x) = dg(f_1(x),\cdots, f_m(x)) \cdot (df_1(x), \dots, df_m(x)).$$

Le cas $m=1$ de cet énoncé correspond à [la règle de différentiation en
chaîne](#chain-rule) ; le cas où $g$ est la fonction identité correspond 
à la [règle d'assemblage](#assemblage).

### Produit scalaire {.answer #answer-ps .one}
On a $\left<x, y \right> = \sum_{i=1}^n x_i y_i$. Chaque fonction 
$(x, y) \mapsto x_i y_i$ est (continûment) différentiable, avec
$d(x_i y_i) = x_i dy_i + y_i dx_i$ (par calcul direct des dérivées partielles ;
alternativement, on peut combiner 
[le désassemblage](#assemblage) de $(x, y) \mapsto (x_i, y_i)$ et 
[la règle du produit](#product-rule) par [différentiation en chaîne](#chain-rule)).
Par [linéarité de la différentielle](#ld), le produit scalaire est 
donc différentiable et 
$$
d \left<x,y \right> = \sum_{i=1}^n x_i dy_i + y_i dx_i
= \left[ 
  \begin{array}{cccccc}
  y_1 & \cdots & y_n & x_1 & \cdots & x_n
  \end{array}
  \right]
  \cdot
  \left[
  \begin{array}{c}
  dx_1 \\ \vdots \\ dx_n \\ dy_1 \\ \vdots \\ dy_n
  \end{array}
  \right].
$$
Par conséquent, $\nabla \left<\cdot, \cdot\right>(x, y) = (y, x)$.

### Cas des fonctions continûment différentiables {.answer #answer-cfcd3}
Si $f$ est continûment différentiable sur $U$, elle est en particulier
différentiable sur $[x, a+h]$. De plus, 
$$
df(x+th) \cdot h = \sum_{i=1}^{n} \partial_j f(x+th) h_j,
$$
donc la fonction $t \in [0,1] \mapsto df(x+th) \cdot h$ est continue
et par conséquent intégrable. [Le théorème fondamental du calcul](#VF)
est donc applicable.

### Cas des fonctions continûment différentiables {.answer #answer-cfcd2}
Si la fonction $f'$ est continue (ou intégrable au sens de
Riemann, ou intégrable au sens de Lebesgue), 
[le théorème fondamental du calcul](#TAFS) est applicable, donc 
$$
f(x+h) - f(x) = \int_x^{x+h} f'(t) \, dt.
$$
L'inégalité triangulaire appliquée à l'intégrale du membre de droite fournit
alors
$$
\left\|f(x+h) - f(x)\right\| = \left\|\int_x^{x+h} f'(t) \, dt\right\|
\leq \int_x^{x+h} \|f'(y)\| \, dy \leq \int_x^{x+h} M \, dt = M h.
$$

### Inégalité des accroissements finis (version euclidienne) {.answer #answer-mitch}
Comme
$$
\frac{\phi(y+s) - \phi(y)}{s} 
= 
\left<f(x+h) - f(x), \frac{f(y+s) - f(y)}{s}\right>,
$$
la fonction $\phi$ est dérivable en tout point $y\in [a,a+h]$ et
$$
\phi'(y) = \left<f(x+h) - f(x), f'(y) \right>.
$$
La fonction $f$ étant à valeurs réelles, 
le théorème des valeurs intermédiaires est applicable : il existe un 
$y \in [x,x+h]$ tel que
$$
\phi(x+h) - \phi(x) = \phi'(y) h = \left<f(x+h) - f(x), f'(y) \right> h.
$$
Comme par ailleurs
\begin{align*}
\phi(x+h) - \phi(x) &= 
\left<f(x+h) - f(x), f(x+h) \right> - \left<f(x+h) - f(x), f(x) \right>  \\
&= \|f(x+h) - f(x)\|^2,
\end{align*}
on a 
$$
\|f(x+h) - f(x)\|^2 = \left<f(x+h) - f(x), f'(y) \right> h \leq \|f(x+h) - f(x)\| \|f'(y)\| h.
$$
Etant donné que $\|f'(y)\| \leq M$, on en déduit $\|f(x+h) - f(x)\| \leq M h.$



### Inégalité de la valeur moyenne {.answer #answer-ivm}
Soit $F:[a, b] \to \R^m$ une primitive de $f$. 
Par [le théorème fondamental du calcul](#TFC), on a 
$$
\left<f\right> = \frac{1}{b-a} \int_a^b f(x) \, dx
= \frac{F(b) - F(a)}{b-a}.
$$
Or si $\|F'\| = \|f\|$ est borné sur $[a, b]$, par 
[l'inégalité des accroissements finis](#TAFS),
$$
\|F(b) - F(a)\| \leq \sup_{x \in [a, b]} \|f(x)\| \times  (b-a),
$$
et donc
$$
\left\|\left<f\right>\right\| \leq  \sup_{x \in [a, b]} \|f(x)\|.
$$
Il va de soi que cette inégalité reste vérifiée si $\|f\|$ est non-bornée,
c'est-à-dire si $\sup_{x \in [a, b]} \|f(x)\| = +\infty$.

### Egalité des accroissements finis ? {.answer #answer-eaf}
La dérivée de $f$ est donnée par $f'(t) = (-\sin t, \cos t)$ ;  
en particulier pour tout $t \in [0, 2\pi]$, $\|f'(t)\| = 1$.
Or $f(2\pi) - f(0) = 0$, donc il est impossible de trouver un 
$t$ tel que $f(2\pi) - f(0) = f'(t) \times 2\pi$.


### Variation du logarithme {.answer #answer-log}
En premier lieu, on peut noter qu'en général, 
le segment d'extrémités $(x, y)$ et $(x, -y)$ 
n'est pas inclus dans le plan coupé $U$.
On ne peut donc pas appliquer directement [la version multivariable de 
l'inégalité des accroissements finis](#VF).
Nous allons donc adapter la technique utilisée dans la démonstration de ce 
théorème en introduisant un chemin $\phi: [0, 1] \to \R^2$ qui joint $(x, y)$ et 
$(x, -y)$ et dont l'image est incluse dans $U$.

![Représentation du chemin $\phi$ quand $(x, y)=(-1, -1)$.](images/log.tex)

On note $\theta$ l'unique détermination de l'angle polaire de $(x, y)$ comprise
dans l'intervalle $\left]-\pi, \pi\right[$ et on pose
$$
\phi(t) := \left(r\cos ((1 - 2 t)\theta), r\sin ((1-2t)\theta) \right)
\; \mbox{ où } \; r := \sqrt{x^2 + y^2}.
$$
On remarque que $\phi(t) \in U$ pour tout $t$, que $\phi(0) = (x, y)$
et que $\phi(1) = (x, -y)$. La fonction $\phi$ est dérivable et 
$$
\phi'(t) = \left(2 \theta r\sin ((1 - 2 t)\theta), -2 \theta r\cos ((1-2t)\theta) \right) ;
$$
la fonction $\log \circ  \, \phi$ est donc définie et dérivable et 
$$
d (\log \circ \, \phi) (t) = d \log (\phi(t)) \cdot d \phi(t)=
d \log(\phi(t)) \cdot \phi'(t).
$$
Par conséquent,
$$
\|d (\log \circ \, \phi) (t)\| \leq \|d \log (\phi(t))\| \|\phi'(t)\|
\leq \frac{1}{r} \times 2 |\theta| r = 2 |\theta| \leq 2 \pi.
$$
L'application de 
[l'inégalité des accroissement finis (monovariable)](#TAFS) à la fonction 
$\log \circ \, \phi$ fournit donc l'inégalité
$$
\|\log (x, y) - \log (x, -y)\| \leq 2 \pi.
$$



<!--
Vecteurs, vecteurs colonnes, vecteurs lignes
--------------------------------------------------------------------------------

### Question 1 {#sol-vvcvl-1}
Par définition, le vecteur colonne associé à $x$ représente l'application
linéaire $A$ de $\mathbb{R}$ dans $\mathbb{R}^n$ telle que pour tout
$h \in \mathbb{R}$ et tout $i=1,\dots, n$, 
$$
(A h)_i = \sum_{k=1}^1 X_{ik} h = x_i h,
$$
soit $A h = h$.

### Question 2 {#sol-vvcvl-2}
Par définition, le vecteur ligne associé à $x$ représente l'application
linéaire $B$ de $\mathbb{R}^n$ dans $\mathbb{R}$ telle que pour tout
$h=(h_1, \dots, h_n) \in \mathbb{R}^n$ 
$$
B h = \sum_k x_i h_i,
$$
soit $B h = \left< x, h \right>$ ou $\left<\cdot, \cdot\right>$
désigne le produit scalaire dans $\mathbb{R}^n$. 

-->

Spécialisation de la différentiation en chaîne 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-dec-1}
Comme fonctions d'une variable, $f$ et $g$ sont 
[différentiables donc dérivables](#dad), $df(x) \cdot h = f'(x) h$ et 
$dg(x) \cdot h = g'(x)h$.
Par la [règle de différentiation en chaîne](#chain-rule),
on obtient
$$
d(g \circ f)(x)= dg(f(x)) \cdot df(x).
$$
On en déduit
$$
\begin{split}
d(g \circ f)(x) \cdot h 
&= (dg(f(x)) \cdot df(x) )\cdot h \\
&=dg(f(x)) \cdot (df(x) \cdot h) \\
&= dg(f(x)) \cdot (f'(x) h) \\
&= g'(f(x)) (f'(x) h) \\
&= (g'(f(x)) f'(x)) h.
\end{split}
$$
La fonction $g \circ f$ étant également fonction d'une variable, elle
est dérivable et
$$
(g\circ f)'(x) = d(g \circ f)(x) \cdot 1 = g'(f(x)) f'(x).
$$

### Question 2 {.answer #answer-dec-2}
La fonction $f$ dépendant d'une variable scalaire, elle est dérivable et 
$df(x) \cdot h = f'(x) h$. Quant à $g$ qui est à valeur scalaire, 
[sa différentielle en $x$ est reliée à son gradient par 
$dg(x) \cdot h =\left<\nabla g(x), h\right>$](#dag).
La [règle de différentiation en chaîne](#chain-rule),
$d(g \circ f)(x)= dg(f(x)) \cdot df(x)$ se décline donc ici en
$$
\begin{split}
d(g \circ f)(x) \cdot h 
&= dg(f(x)) \cdot (df(x) \cdot h) \\
&= dg(f(x)) \cdot (f'(x) h) \\
&= \left<\nabla g(f(x), f'(x)h \right>  \\
&= \left<\nabla g(f(x)), f'(x) \right> h,
\end{split}
$$ 
soit $(g \circ f)'(x) = d(g \circ f)(x) \cdot 1 = \left<\nabla g(f(x)), f'(x) \right>$.
Quand $n=m=1$, on a
$$
\begin{split}
d(g \circ f)(x) \cdot h 
&= dg(f(x)) \cdot (df(x) \cdot h) \\
&= g'(f(x)) (df(x) \cdot h) \\
&= g'(f(x)) \left<\nabla f(x), h\right> \\
&= \left<g'(f(x)) \nabla f(x), h\right> \\
\end{split}
$$ 
donc $\nabla (g\circ f)(x) = g'(f(x)) \nabla f(x)$.

### Question 3 {.answer #answer-dec-3}
Quand $p=1$, on a
$$
\begin{split}
d(g \circ f)(x) \cdot h 
&= dg(f(x)) \cdot (df(x) \cdot h) \\
&= dg(f(x)) \cdot (f'(x) h) \\
&= (dg(f(x)) \cdot f'(x)) h.
\end{split}
$$ 
donc $(g \circ f)'(x) = dg(f(x)) \cdot f'(x)$.
Quand $n=1$, on a
$$
\begin{split}
d(g \circ f)(x) \cdot h 
&= dg(f(x)) \cdot (df(x) \cdot h) \\
&= g'(f(x)) \left<\nabla f(x), h\right> \\
&= g'(f(x)){\nabla f(x)}^{\top} h.
\end{split}
$$ 
donc $d (g\circ f)(x) = g'(f(x)){\nabla f(x)}^{\top}$. 
Finalement, quand $m=1$, on a
$$
\begin{split}
d(g \circ f)(x) \cdot h 
&= dg(f(x)) \cdot (df(x) \cdot h) \\
&= \left<\nabla g(f(x)), df(x) \cdot h\right> \\
&= \left<(df(x))^{\top} \cdot \nabla g(f(x)), \cdot h\right>
\end{split}
$$ 
et donc $\nabla (g \circ f)(x) = (df(x))^{\top} \cdot \nabla g(f(x))$.


Fonction quadratique 
--------------------------------------------------------------------------------

### Question 1 -- Gradient {.answer #answer-fq-1}
La fonction présentée est la somme de la fonction
$x \mapsto \left<x, A\cdot x \right> = x^{\top} \cdot A \cdot x$, de l'application linéaire 
$x \mapsto \left<b, x\right> = b^{\top} x$ et de l'application constante
$x \mapsto c$. Les deux dernières fonctions sont différentiables, de 
différentielles les fonctions $x \mapsto b^{\top}$ 
(comme [différentielle d'application linéaire](#dal))
et $x \mapsto 0$ respectivement.
Seul reste donc à étudier la fonction $g:x \mapsto x^{\top} \cdot A \cdot x$.

Comme
$$
g(x) = \frac{1}{2}x^{\top} \cdot A \cdot x = \frac{1}{2}\sum_{i=1}^{n} \sum_{k=1}^n x_i A_{ik} x_k,
$$
pour tout $j \in \{1,\dots, n\}$ on a 
$$
g(x) = \frac{1}{2} \left(x_j A_{jj} x_j + \sum_{\substack{k=1 \\ k\neq j}}^n x_j  A_{jk} x_k +  \sum_{\substack{i=1\\i\neq j}}^n x_i A_{ij} x_j
+ \sum_{\substack{i=1\\i\neq j}}^{n} \sum_{\substack{k=1\\k\neq j}}^n x_i A_{ik} x_k\right).
$$
Par conséquent, la dérivée partielle $\partial_j g(x)$ existe et vérifie
\begin{align*}
\partial_j g(x) &= A_{jj} x_{j} + \frac{1}{2} \left(\sum_{\substack{k=1 \\ k\neq j}}^n A_{jk} x_k + \sum_{\substack{i=1\\i\neq j}}^n x_i A_{ij} \right)\\
&= \frac{1}{2} \sum_{k=1}^n A_{jk} x_k + \frac{1}{2} \sum_{i=1}^n x_i A_{ij} \\
&= \left[\frac{1}{2}A \cdot x\right]_j + \left[\frac{1}{2}A^{\top} \cdot x\right]_j \\
&= \left[\frac{1}{2}(A + A^{\top}) \cdot x\right]_j.
\end{align*}
Toute ces dérivées partielles sont des fonctions linéaires de $x$, 
elles sont donc continues et la fonction $g$ est continûment différentiable ;
[elle est donc différentiable](#cdid).
De plus, l'égalité ci-dessus nous fournit
$$
\nabla g(x) = \frac{1}{2}(A + A^{\top}) \cdot x.
$$
La fonction $f$ est donc différentiable (comme [combinaison linéaire de 
fonctions différentiables](#ld)) et
$$
\nabla f(x) = \frac{1}{2}(A + A^{\top}) \cdot x + b^{\top}.
$$


<!--
Pour tout $x \in \R^n$ et tout $h \in \R^n$, on a 
$$
\begin{split}
f(x+h) - f(x) &= \frac{1}{2} \left<(x+h), A \cdot (x+h) \right> + \left<b, x+h\right> + c
- \frac{1}{2} \left<x, A \cdot x \right> - \left<b, x\right> - c \\
& =
\frac{1}{2} \left<x, A \cdot h \right> + \frac{1}{2} \left<h, A \cdot x \right> +
\left<b, h\right> + \frac{1}{2} \left<h, A \cdot h \right> \\
&=
\frac{1}{2} \left<A^{\top} \cdot x, h \right> + \frac{1}{2} \left<A \cdot x, h \right> +
\left<b, h\right> + \frac{1}{2} \left<h, A \cdot h \right>.
\end{split}
$$
Comme $|\left<h, A \cdot h \right>| \leq \|h\| \times \|A\| \|h\|$, ce terme
est un $o(\|h\|)$. On en conclut que
$$
f(x+h) - f(x)
= \left<\frac{1}{2}(A + A^{\top}) \cdot x + b, h\right> + o(\|h\|).
$$
La fonction $f$ est donc différentiable en $x$, de gradient
$$
\nabla f(x) = \frac{1}{2}(A + A^{\top}) \cdot x + b.
$$
-->
### Question 2 -- Matrice hessienne {.answer #answer-fq-2}
La fonction 
$$
\nabla f: x \in \R^n \mapsto \frac{1}{2}(A + A^{\top}) \cdot x + b^{\top}.
$$
est affine, somme d'une fonction linéaire et d'une fonction constante.
Elle est donc différentiable, et
$$
H_f(x) := J_{\nabla f}(x) = \frac{1}{2}(A + A^{\top}).
$$

### Question 3 -- Point critique {.answer #answer-fq-3}
Si $H_f(x)$ est inversible (cet opérateur est constant), comme
$$
\nabla f(y) = \frac{1}{2}(A + A^{\top}) \cdot y + b = H_f(x) \cdot y + b,
$$
résoudre $\nabla f(x_0) = 0$ revient à rechercher les solutions de
$$
H_f(x) \cdot x_0 + b = H_f(x) \cdot x_0 + (\nabla f(x) - H_f(x) \cdot x) = 0.
$$
Il existe donc un unique zéro de $\nabla f$, donné par
$$
x_0 = x - (H_f(x))^{-1} \nabla f(x).
$$

### Question 4 -- Vecteur gaussien {.answer #answer-fq-4}
La fonction 
$$
g: x \in \R^d \mapsto \exp\left( -\frac{1}{2} \left<x, \Sigma^{-1} \cdot x \right> \right)
$$
apparaît comme la composée des fonctions
$$
x \in \R^d \mapsto -\frac{1}{2} \left<x, \Sigma^{-1} \cdot x \right>
\; \mbox{ et } \; \exp:\R \to \R.
$$ 
La fonction $\exp$ est dérivable, et donc différentiable 
sur tout $\R$ avec $d (\exp(y)) = \exp'(y) dy = \exp(y) dy$, c'est-à-dire
$$
d\exp(y) \cdot h = \exp(y) h.
$$ 
Quant à la première fonction, d'après les questions qui précèdent, elle est
différentiable et 
$$
\nabla \left(  -\frac{1}{2} \left(\left<x, \Sigma^{-1} \cdot x \right>\right) \right)
 = \frac{1}{2}\left(-\Sigma^{-1} - (\Sigma^{-1})^{\top} \right) \cdot x
= -\Sigma^{-1} \cdot x.
$$
Sa différentielle vérifie donc
$$
d \left( -\frac{1}{2} \left(\left<x, \Sigma^{-1} \cdot x \right>\right) \right) \cdot h
= - \left<\Sigma^{-1} \cdot x, h \right>.
$$
Par conséquent, la fonction $g$ est différentiable sur $\R^d$ comme composée
de fonctions différentiables et 
$$
d g(x) \cdot h = - \exp \left( -\frac{1}{2} \left(\left<x, \Sigma^{-1} \cdot x \right>\right) \right)
\left<\Sigma^{-1} \cdot x, h \right>
= \left<-g(x) \times \Sigma^{-1} \cdot x, h \right>,
$$
le gradient de $g$ vaut donc
$$
\nabla g(x) = -g(x) \times \Sigma^{-1} \cdot x.
$$

Robot manipulateur
--------------------------------------------------------------------------------

### Question 1  {.answer #answer-rm-1}

Des équations
$$
\left|
\begin{array}{rcr}
x &=& \ell_1 \cos \theta_1 + \ell_2 \cos (\theta_1 + \theta_2) \\
y &=& \ell_1 \sin \theta_1 + \ell_2 \sin (\theta_1 + \theta_2) \\
\end{array}
\right.
$$
on déduit que les dérivées partielles de $x$ et de $y$ par rapport
à $\theta_1$ et $\theta_2$ existent et vérifient
$$
\begin{array}{rcl}
\partial x/ \partial \theta_1
&=& -\ell_1 \sin \theta_1 - \ell_2 \sin (\theta_1 + \theta_2), \\
\partial x / \partial \theta_2
&=& - \ell_2 \sin (\theta_1 + \theta_2), \\
\partial y / \partial \theta_1
&=& \ell_1 \cos \theta_1 + \ell_2 \cos (\theta_1 + \theta_2), \\
\partial y / \partial \theta_2
&=& \ell_2 \cos (\theta_1 + \theta_2).
\end{array}
$$
Ces grandeurs étant continues, la fonction $f$ est continûment
différentiable et donc différentiable. Si l'on note $s_1 = \sin \theta_1$,
$s_{12}= \sin(\theta_1+\theta_2)$, $c_1 = \cos \theta_1$ et
$c_{12}= \cos(\theta_1+\theta_2)$, on obtient donc
$$
J_f(\theta_1, \theta_2)
=
\left[
\begin{array}{rr}
-\ell_1 s_1 -\ell_2 s_{12} & -\ell_2 s_{12} \\
\ell_1 c_1 + \ell_2 c_{12} & \ell_2 c_{12} 
\end{array}
\right].
$$

### Question 2  {.answer #answer-rm-2}
Soient $\delta \theta_1 := \theta_1 - \theta_{10}$
et $\delta \theta_2 := \theta_2 - \theta_{20}$. La fonction
$$
\phi : t \in [0, 1]  
\mapsto
f(\theta_{10} + t\delta \theta_1, \theta_{12} + t\delta \theta_2)
$$
est continûment dérivable, de dérivée
$$
\phi'(t)=
df(\theta_{10} +t \delta \theta_1, \theta_{20} +t \delta \theta_2) 
\cdot (\delta \theta_1 , \delta \theta_2)
$$
Si l'on note $s_1(t) = \sin (\theta_{10} + t\delta \theta_1)$,
$c_1(t) = \cos (\theta_{10} + t\delta \theta_1)$, ...,
le [théorème fondamental du calcul](#TFC) et l'expression de la matrice
jacobienne de $f$ nous fournissent donc
\begin{multline*}
f(\theta_1, \theta_2) - f(\theta_{10}, \theta_{20})
=
\int_0^1 \, \phi'(t) \, dt 
= \\
\int_0^1
\left[
\begin{array}{c}
(-\ell_1 s_1(t) -\ell_2 s_{12}(t)) \delta \theta_1  -\ell_2 s_{12}(t) \delta \theta_2 \\
(\ell_1 c_1(t) + \ell_2 c_{12}(t)) \delta \theta_1 + \ell_2 c_{12}(t) \delta \theta_2
\end{array}
\right] dt
\end{multline*}
et donc par inégalité triangulaire et majoration de l'intégrande,
$$
|x- x_0| = |f_1(\theta_1,\theta_2) - f_1(\theta_{10}, \theta_{20})| \leq (\ell_1 + \ell_2) |\delta \theta_1| + \ell_2 |\delta \theta_2|
$$
ainsi que 
$$
|y - y_0| = |f_2(\theta_1,\theta_2) - f_2(\theta_{10}, \theta_{20})|
\leq (\ell_1 + \ell_2) |\delta \theta_1| + \ell_2 |\delta \theta_2|.
$$
Si $|\delta \theta_1| \leq  \varepsilon$ et $|\delta \theta_2| \leq  \varepsilon$,
on en déduit
$$
|x - x_0| \leq (\ell_1 + 2\ell_2) \varepsilon \; \mbox{ et } \;
|y - y_0| \leq (\ell_1 + 2\ell_2) \varepsilon.
$$
Le point $(x, y) = f(\theta_1, \theta_2)$ appartient donc au carré centré 
en $(x_0, y_0)$ d'arête de longueur $2(\ell_1 + 2\ell_2)\varepsilon$.

Dérivée directionnelle d'Hadamard
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-ddh-1}
Supposons que $f$ soit directionnellement dérivable au sens de Hadamard
en $x$. Pour tout $h \in \mathbb{R}^n$, par continuité de l'application
$t \in \mathbb{R} \mapsto x + th$, pour $\varepsilon > 0$ assez petit,
et parce que le domaine de définition de $f$ est ouvert,
l'image de la fonction 
$$
\gamma: t \in \left]-\varepsilon, \varepsilon \right[ \mapsto x + th
$$
est incluse dans le domaine de définition de $f$, est telle que
$\gamma(0) = x$, $\gamma'(0) = h$. Par conséquent, la dérivée
de $f\circ \gamma$ en $0$ existe, et c'est par construction la
dérivée directionnelle de $f$ en $x$ dans la direction $h$.
La fonction $f$ est donc directionnellement dérivable en $x$ 
au sens classique.

### Question 2 {.answer #answer-ddh-2}
Supposons que $f$ soit directionnellement dérivable au sens de Hadamard
en $x$. Pour montrer que l'expression $(f \circ \gamma)'(0)$ ne dépend
de $\gamma$ qu'à travers $\gamma'(0)$, nous allons considérer un
second chemin arbitraire $\beta: J \to \mathbb{R}^n$, 
où $J$ est un intervalle ouvert de $\mathbb{R}$ contenant $0$, 
tel que $\beta(0) = x$,
$\beta'(0)=\gamma'(0)$ et montrer que 
$$
(f \circ \gamma)'(0) = (f \circ \beta)'(0).
$$
L'idée de la démonstration consiste à construire un troisième chemin 
$\alpha$ qui en "mélangeant" les chemins $\beta$ et $\gamma$, 
satisfait les hypothèses de la définition de "directionnellement 
dérivable au sens de Hadamard",
est tel que $\alpha'(0) = \beta'(0) = \gamma'(0)$
et également tel que
d'une part $(f \circ \alpha)'(0)= (f \circ \beta)'(0)$ et d'autre 
part $(f \circ \alpha)'(0)=(f \circ \gamma)'(0)$.

Un chemin qui permette de tenir ce raisonnement est le suivant. 
Tout d'abord, choisissons
$\varepsilon > 0$ tel que 
$\left]-\varepsilon, \varepsilon\right[ \subset I \cap J$,
puis définissons $\alpha: \left]-\varepsilon,\varepsilon\right[ \to \mathbb{R}^n$
par
$$
\alpha(t) = \left|
\begin{array}{cl}
x & \mbox{si } \, t=0, \\
\beta(t) & \mbox{si } \, \varepsilon /2^{2k+1} \leq |t| < \varepsilon / 2^{2k}, \, \mbox{pour un entier } \, k \in \mathbb{N}, \\
\gamma(t) & \mbox{si } \, \varepsilon / 2^{2k+2} \leq |t| < \varepsilon / 2^{2k+1},  \, \mbox{pour un entier } \, k \in \mathbb{N}.
\end{array}
\right.
$$
Les hypothèses de la définition sont facilement vérifiées, 
ainsi que la preuve que $\alpha'(0) = \beta'(0) = \gamma'(0)$.
Avec l'hypothèse de différentiabilité au sens de Hadamard, nous
savons donc que la dérivée $(f\circ \alpha)'(0)$ existe.
On peut la calculer comme la limite de
$$
(f \circ \alpha)'(0) = \lim_{k \to +\infty} \frac{f(\alpha(t_k)) - f(x)}{t_n}
$$
où $t_k$ est une suite arbitraire de valeurs non nulles tendant vers $0$.
Or, si l'on choisit $t_k = \varepsilon/2^{2k+1}$, on trouve
$$
\lim_{k \to +\infty} \frac{f(\alpha(t_k)) - f(x)}{t_k}
=
\lim_{k \to +\infty} \frac{f(\beta(t_k)) - f(x)}{t_k}
= (f \circ \beta)'(0)
$$
et si l'on choisit $t_k = \varepsilon/2^{2k+2}$, on trouve
$$
\lim_{k \to +\infty} \frac{f(\alpha(t_k)) - f(x)}{t_k}
=
\lim_{k \to +\infty} \frac{f(\gamma(t_k)) - f(x)}{t_k}
= (f \circ \gamma)'(0),
$$
ce qui prouve le résultat d'indépendance souhaité.
Pour prouver que $(f\circ \gamma)'(0) = f'(x, \gamma'(0))$, 
il suffit d'associer à un chemin quelconque $\gamma$ le
chemin "canonique" $\beta: t \mapsto x+ t\gamma'(0)$ de la question 1,
qui est tel que $\beta'(0) = \gamma'(0)$ d'une part et d'autre part
$(f \circ \beta)'(0) = f'(x, \beta'(0))$ par construction.
On en déduit que
$$
(f \circ \gamma)'(0) = (f \circ \beta)'(0) = f'(x, \beta'(0)) = f'(x, \gamma'(0)).
$$

### Question 3 {.answer #answer-ddh-3}
Soit $\gamma: I \subset \mathbb{R} \to \mathbb{R}^n$,
un chemin défini sur un intervalle ouvert $I$ contenant $0$, 
tel que $\gamma(I) \subset U$,  $\gamma(0) = x$ et $\gamma'(0)$ existe.
Alors, sous les hypothèses du théorème de dérivée en chaîne que nous
souhaitons montrer, le chemin $\beta = f \circ \gamma$ est 
défini sur $I$, vérifie $\beta(I) \subset V$, $\beta(0) = f(x)$ 
et par hypothèse de dérivabilité directionnelle au sens de
Hadamard sur $f$ en $x$,
$\beta'(0) = f'(x, \gamma'(0))$.
Par hypothèse de dérivabilité directionnelle au sens de
Hadamard sur $g$ en $f(x)$, 
$$
((g\circ f) \circ \gamma)'(0) = 
(g \circ \beta)'(0) = g'(f(x), \beta'(0)) = g'(f(x), f'(x, \gamma'(0))),
$$
ce qui prouve la dérivabilité directionnelle au sens de Hadamard pour
la composée $g \circ f$ en $x$. Il suffit d'associer à un vecteur $h$
le chemin canonique $t \mapsto x + th$ pour obtenir la relation
$$
(g \circ f)'(x, h) = g'(f(x), f'(x, h)).
$$

### Question 4 {.answer #answer-ddh-4}
Tout d'abord, si la limite 
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t}
$$
existe, elle est égale à la limite obtenue en fixant $k=h$ 
$$
\lim_{t \to 0} \frac{f(x+ t h) - f(x)}{t}
$$
qui est par définition $f'(x, h)$.

Supposons que cette limite existe et montrons que $f$ a une dérivée
directionnelle au sens de Hadamard.
Soit $\gamma$ un chemin satisfaisant les hypothèses de cette définition.
La fonction $f\circ \gamma$ est dérivable en $0$ si et seulement si
le taux d'accroissement associé converge en $0$. Or, ce taux
d'accroissement peut s'écrire sous la forme
$$
\frac{f(\gamma(t)) - f(\gamma(0))}{t}
=
\frac{f\left(x + t \frac{\gamma(t) - \gamma(0)}{t}\right) - x}{t}.
$$ 
Le chemin $\gamma$ étant dérivable en $0$,
$$
k(t) :=  \frac{\gamma(t) - \gamma(0)}{t} \to \gamma'(0)
\, \mbox{ quand } \, t \to 0
$$
donc par hypothèse, le taux d'accroissement de $f\circ \gamma$ a une
limite en $0$.

Réciproquement, suppose que $f$ soit directionnellement dérivable au
sens de Hadamard en $0$. Pour montrer que la limite 
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t}
$$
existe, il nous suffit de montrer que pour toute suite $t_i$ de valeurs
non nulles tendant vers $0$ et toute suite de vecteurs $k_i$ convergeant
vers $h$, la limite
$$
\lim_{i \to +\infty} \frac{f(x+ t_i k_i) - f(x)}{t_i}
$$
existe. On peut imposer la restriction que la suite $|t_i|$ soit 
strictement décroissante et le résultat reste valable.

Pour tout $t \in \mathbb{R}^*$ notons $j(t)$ le plus
petit parmi les entiers $j$ satisfaisant
$$
|t - t_j| = \min_{i \in \mathbb{N}} |t - t_i|,
$$
puis définissons $\gamma(t)$ par $\gamma(0) = x$ et si $t \neq 0$,
$$
\gamma(t) = x + t k_{j(t)}.
$$
S'il est défini sur un intervalle $\left]-\varepsilon, \varepsilon\right[$
assez petit, $\gamma$ satisfait les hypothèses de la dérivabilité 
directionnelle. Le point critique à vérifier est que $\gamma$ est dérivable
en $0$. Mais par construction
$$
\frac{\gamma(t) - \gamma(0)}{t} = k_{j(t)}
$$
et $j(t)$ tend vers $+\infty$ quand $t$ tend vers $0$; 
par conséquent la limite existe et
$$
\lim_{t \to 0} \frac{\gamma(t) - \gamma(0)}{t} = h.
$$
Par construction
$$
\frac{f(\gamma(t_i)) - f(\gamma(0))}{t_i} = \frac{f(x+ t_i k_i) - f(x)}{t_i}.
$$
Comme la fonction est dérivable directionnellement au sens de 
Hadamard, 
$$
\lim_{i \to +\infty} \frac{f(x+ t_i k_i) - f(x)}{t_i}
$$
existe.

### Question 5 {.answer #answer-ddh-5}
Si $f$ est différentiable, notons $\varepsilon$
la fonction définie dans un voisinage de $0$, continue et nulle en $0$,
telle que
$$
f(x+h) = f(x) + df(x) \cdot h + \varepsilon(h)\|h\|.
$$
On a alors pour tout $t\in \mathbb{R}$ non nul et tout vecteur
$k \in \mathbb{R}^n$ suffisamment petits, en posant $h=tk$, 
$$
\begin{split}
\frac{f(x+ t k) - f(x)}{t}
&= \frac{1}{t}df(x) \cdot tk + \frac{1}{t}\varepsilon(tk) \|tk\| \\
&= df(x) \cdot k + \varepsilon(t k) \frac{|t|}{t} \|k\|.
\end{split}
$$
Le terme $df(x) \cdot k$ tend vers $df(x)\cdot h$ quand $k \to h$
et le second terme du membre de droite tend vers $0$ quand 
$t$ et $k$ tendent vers $0$, donc
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t} = df(x) \cdot h.
$$
Par conséquent la fonction $f$
est directionnellement dérivable au sens de Hadamard.
Le membre de droite, égal à $f'(x, h)$, est linéaire en $h$ ;
la fonction $f$ est donc différentiable au sens de Hadamard.

Réciproquement, supposons que $f$ est différentiable au sens de Hadamard.
Pour montrer que $f$ est différentiable, 
de différentielle $f'(x, h)$, montrons que
$$
\frac{\|f(x+h) - f(x) - f'(x, h)\|}{\|h\|} \to 0 \, \mbox{ quand } \, h \to 0,
$$
ou de façon équivalente, que
$$
\frac{f\left(x+ \|h\|\frac{h}{\|h\|} \right) - f(x)}{\|h\|} - f'\left(x, \frac{h}{\|h\|} \right) \to 0
\, \mbox{ quand } \, h \to 0.
$$
Il nous suffit de montrer que pour toute suite $t_i > 0$ telle
que $t_i \to 0$ quand $i \to +\infty$ et 
$k_i \in \mathbb{R}^n$ telle que $\|k_i\| = 1$,
$$
\frac{f\left(x+ t_i k_i \right) - f(x)}{t_i} - f'\left(x, k_i \right) \to 0
\, \mbox{ quand } \, i \to +\infty.
$$
Imaginons au contraire que cette expression ne tende pas vers $0$.
Alors on pourrait trouver un $\varepsilon > 0$ et une sous-suite de 
$(t_i, k_i)$, notée de $(t'_i, k'_i)$, telle que pour tout $i$,
$$
\left\|
\frac{f \left(x+ t'_i k'_i \right) - f(x)}{t'_i} - f'\left(x, k'_i \right)
\right\| \geq \varepsilon.
$$
Mais la suite des $k'_i$ est de norme égale à $1$ ;
la sphère fermée de centre $1$ étant compacte, il existe des sous-suites
$t''_i$ et $k''_i$ de $t'_i$ et $k'_i$ et un $h \in \mathbb{R}^n$ tels que
$\|h\| = 1$ et
$k''_i \to h$. 
Par hypothèse de dérivabilité au sens de Hadamard,
on aurait
$$
\frac{f\left(x+ t''_i k''_i \right) - f(x)}{t''_i} \to f'\left(x, h\right)
\, \mbox{ quand } \, i \to +\infty
$$
ce qui contredit l'inégalité ci-dessus et prouve la contradiction.
Par conséquent, $f$ est bien différentiable.


Thermodynamique
--------------------------------------------------------------------------------

### Question 0 {.answer #answer-th-0}
Les variables associées à l'expression fournie de l'entropie $S$ sont le volume
$V$ et la température $T$. Pour que l'expression définissant l'entropie soit 
toujours définie, il suffit d'exiger que $V$ et $T$ soient strictement positives.

### Question 1 {.answer #answer-th-1}
L'entropie, en tant que fonction de $(V, T) \in \left]0,+\infty\right[^2$, 
est une fonction (continûment) différentiable. En effet, les dérivées partielles
de $S(V,T)$ sont définies en tout point et vérifient
$$
\frac{\partial S(V, T)}{\partial V} = N k_B \frac{1}{V} 
\; \mbox{ et } \;
\frac{\partial S(V,T)}{\partial T} = \frac{3}{2}N k_B \frac{1}{T},
$$
deux expressions dépendant continûment de $(V, T)$. 
On a par conséquent
$$
d S = \frac{\partial S(V, T)}{\partial V} d V + \frac{\partial S(V,T)}{\partial T} dT = N k_B \left[\frac{dV}{V} + \frac{3}{2} \frac{dT}{T}\right].
$$

### Question 2 {.answer #answer-th-2}
Si $U$ est une fonction (différentiable) de $(V, T)$, 
on peut interpréter mathématiquement la relation $dU = T dS - P dV$ comme
$$
d(U(V, T)) = T d(S(V, T)) - P(V, T) dV
$$
où $P(V, T) := N k_B T / V$ résulte de la loi des gaz parfaits $PV = N k_B T$.
En exploitant la différentielle $dS(V, T)$ déjà calculée, on en déduit 
$$
d(U(V, T)) =  T N k_B \left[\frac{dV}{V} + \frac{3}{2} \frac{dT}{T}\right] - N k_B T \frac{dV}{V}
= \frac{3}{2} N k_B dT.
$$

### Question 3 {.answer #answer-th-3}
Soit $(V_0, T_0) \in \left]0, +\infty\right[^2$ et 
$(V, T) \in \left]0, +\infty\right[^2$. Le segment reliant $(V_0, T_0)$
et $(V, T)$ est inclus tout entier dans $\left]0, +\infty\right[^2$
qui est convexe. Pour tout $t \in [0, 1]$, on a 
\begin{align*}
\phi(t) & :=
dU(V_0 + t(V - V_0), T_0 + t(T - T_0)) \cdot (V - V_0, T - T_0) \\ 
&\phantom{:}= \frac{3}{2}  N k_B dT \cdot (V - V_0, T - T_0) \\
&\phantom{:}= \frac{3}{2}  N k_B (T - T_0).
\end{align*}
La fonction $\phi$ est constante, donc intégrable sur $[0, 1]$.
Par [le théorème fondamental du calcul multivariable](#VF), on a
$$
U(V, T) = U(V_0, T_0) + \int_0^1 \phi(t) \, dt
= \left[U(V_0, T_0) - \frac{3}{2}  N k_B T_0\right] + \frac{3}{2}  N k_B T,
$$
ce qui démontre qu'à une constante près, on a $$U(V, T) =  \frac{3}{2} Nk_B T.$$

<!--
TODO -- Analycité
--------------------------------------------------------------------------------
-->


<!--

TODO -- Oloid
--------------------------------------------------------------------------------
-->

Références
================================================================================

