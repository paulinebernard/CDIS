% Calcul Différentiel II

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

#### Question 1 (réponses multiples)
Cochez la case s'il est possibe d'expliciter
une dépendance fonctionnelle de la forme $x=\psi(\lambda)$ par le théorème 
des fonctions implicites quand :

  - [ ] A: $x \lambda^2 + x^2 \lambda -1 = 0$ au voisinage de $(x,\lambda)=(1,1)$,   

  - [ ] B: $\sin(\lambda x_1) + \sin(\lambda x_2) = 0$ au voisinage de $(x_1, x_2, \lambda)=(0,0,0)$,

  - [ ] C: $\lambda x_1^2 + x_2 = x_1 + \lambda x_2^2 = 2$ au voisinage de $(x_1, x_2, \lambda)=(1,1,1)$.

#### Question 2
La méthode de Newton appliquée à la recherche d'une solution de 
$$
x^2 - 1 = 0, \; x \in \mathbb{R}
$$
produit une suite de valeurs réelles $x_k$ définies par la récurrence

  - [ ] A: $x_{k+1} = x_k^2 - 1$,

  - [ ] B: $x_{k+1} = 1/x_k$,

  - [ ] C: $x_{k+1} = 0.5 (x_k + 1 / x_k)$.

#### Question 3
Une fonction $f: \mathbb{R}^2 \mapsto \mathbb{R}^2$ continûment différentiable
et dont la matrice jacobienne est inversible en tout point est un 
$C^1$-difféomorphisme de $\mathbb{R}^2$ sur son image $f(\mathbb{R}^2)$.

  - [ ] A: vrai,

  - [ ] B: faux.

#### Question 4 (réponses multiples)
Le symbole $\varepsilon$ désigne l'epsilon machine des doubles.
Le nombre d'or $x = (1 + \sqrt{5})/2 \approx 1.618$ peut être représenté par
un double $\mathtt{x}$ avec une erreur $|\mathtt{x} - x|$:


  - [ ] A: de l'ordre de $1.618 \times \varepsilon$,

  - [ ] B: de l'ordre de $\varepsilon$,

  - [ ] C: de l'ordre de $\varepsilon / 2$.

  - [ ] D: nulle.

#### Question 5
Quand le double positif `x` diminue, l'erreur entre 

    y = ((1.0 + x) - 1.0) / x
    
et la valeur attendue `1.0` 

  - [ ] A: augmente (de façon monotone),

  - [ ] B: augmente (en tendance générale),

  - [ ] C: diminue (en tendance générale).

#### Question 6
Appliquée à une fonction d'une variable,
la méthode de différentiation automatique :

  - [ ] A: produit une fonction dérivée exacte,

  - [ ] B: produit une fonction dérivée correctement arrondie,

  - [ ] C: produit une fonction dérivée sans erreur de troncature.