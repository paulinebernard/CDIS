% Calcul Intégral III

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

#### Question 1
Déterminer l'aire des pavés suivants du plan étendu :

Ensemble de $[-\infty,+\infty]^2$                    Aire (mesure de Lebesgue)
-------------------------------------                -----------------------------------------
$[0, 1] \times \left]-1, 1\right[$                   ........................................
$\R^2$                                               ........................................
$\{+\infty\} \times \left[-\infty, +\infty\right]$   ........................................ 

<!--
#### Question (réponse multiple)
Si $A$ et $B$ sont deux ensembles mesurables de $\R$,

  - [ ] A: $A \times B$ est un ensemble mesurable de $\R^2$,

  - [ ] B: si $a(A \times B) < + \infty$ alors $\ell(A) < +\infty$ et $\ell (B) < +\infty$.

  - [ ] C: si 
-->

### Question 2 (réponse multiple) 
Soit $D = \{(x,y) \in \R^2 \; | \; x = y\}$ la diagonale principale de $\R^2$.
Alors

  - [ ] A: pour tout $r>0$, $D \cap [-r, r]^2$ est négligeable,

  - [ ] B: l'ensemble $D$ est négligeable,

  - [ ] C: l'aire de l'ensemble $D$ est nulle.

#### Question 3 (réponse multiple)
Si $f: \R^2 \to \R$ est mesurable et que 
$$
\int_{-\infty}^{+\infty} \left[\int_{-\infty}^{+\infty} f(x,y) \, dx\right] \, dy
$$
est bien définie, alors

  - [ ] A: l'intégrale $\int_{-\infty}^{+\infty} f(x,y) \, dx$ est nécessairement définie pour tout $y \in \R$,

  - [ ] B: l'intégrale $\int_{\R^2} f(x, y) \, dxdy$ est bien définie,

  - [ ] C: l'intégrale $\int_{-\infty}^{+\infty} \left[\int_{-\infty}^{+\infty} f(x,y) \, dy\right] \, dx$ est bien définie,

  - [ ] D: si $\int_{-\infty}^{+\infty} \left[\int_{-\infty}^{+\infty} f(x,y) \, dy\right] \, dx$ est également bien définie, alors les deux intégrales sont égales,

#### Question 4 (réponse multiple)
Soient $f: \R \to \left[0, +\infty \right[$ et $g: \R \to \left[0, +\infty \right[$ 
deux fonctions intégrables. Alors,

  - [ ] A: la fonction $(x, y) \in \R^2 \mapsto f(x) g(y)$ est mesurable,

  - [ ] B: la fonction $(x, y) \in \R^2 \mapsto f(x) g(y)$ est intégrable,

  - [ ] C: on a $$\int_{\R^2} f(x) g(y) \, dxdy = \left(\int_{-\infty}^{+\infty} f(x) \, dx\right)\left(\int_{-\infty}^{+\infty} g(y) dy\right).$$



#### Question 5 (réponse multiple)
Soient $f: \R^2 \to \R$. L'intégrale
  $$
  \int_{\R^2} f(x, y-x) \, dxdy
  $$

  - [ ] A: est définie si $f$ est mesurable et positive,

  - [ ] B: est égale à $\int_{\R^2} f(x, y) \, dxdy$ si $f$ est intégrable.


