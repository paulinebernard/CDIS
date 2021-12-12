% Probabilités III

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\renewcommand{\P}{\mathbb{P}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Esp}{\mathbb{E}}
\newcommand{\E}{\mathcal{E}}


\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}

#### Question 1
Soient $X \sim \E(\lambda)$, $\lambda >0$, et $Y \sim \mathcal{B}(1/2)$ deux variables aléatoires réelles indépendantes, et $Z = X Y + (1-Y)\lambda$. La densité $f_{Z | Y =1}$ est égale à 

  - [ ] A : $\frac{\lambda}{2} \exp(-\lambda z)1_{\R^\ast_+}$

  - [ ] B : $\lambda \exp(-\lambda z)1_{\R^\ast_+}$

  - [ ] C : $Z$ n'admet pas de densité

  - [ ] D : $Z = \lambda$ p.s.


#### Question 2 (réponses multiples)
Avec les hypothèses précédentes, on a

  - [ ]  A : $\Esp (Z | Y = 1) = \frac{1}{\lambda}$

  - [ ]  B : $\Esp (Z | Y = O) = \lambda$

  - [ ]  C : $\Esp (Z | Y ) = \frac{Y}{2\lambda} + \frac{1}{2}(1-Y)\lambda$

  - [ ]  D : $\Esp (Z | Y ) = \frac{Y}{\lambda} + (1-Y)\lambda$

#### Question 3
Soient $X$ et $Y$ deux variables aléatoires de densité jointe $f_{X,Y}(x,y) = \frac{1}{x}1_{[0,x]}(y)\lambda\exp(-\lambda x)$, $\lambda >0$. Quelle est la densité de $Y|X=x$ ?

  - [ ]  A : $\exp(-y)$

  - [ ]  B : $1_{[0,x]}(y)$

  - [ ]  C : $\frac{1}{x}1_{[0,x]}(y)$

  - [ ]  D : $\lambda\exp(-\lambda x)$

#### Question 4

En déduire la valeur de $\Esp(Y)$ :

  - [ ] A : $1/2$

  - [ ] B : $x/2$

  - [ ] C : $\frac{1}{2\lambda}$

  - [ ]  D : $\lambda^2$  

#### Question 5 

Soit $(X,Y)$ un vecteur gaussien d'espérance $(\mu_X, \mu_Y)$ et de matrice de covariance $\begin{pmatrix}1 & \rho \\ \rho & 1\end{pmatrix}$, où $\rho > 0$. L'espérance conditionnelle de $X|Y$ vaut :

  - [ ] A: $\mu_Y$

  - [ ] B: $\mu_X$

  - [ ] C: $\mu_Y + \rho (Y - \mu_X)$

  - [ ] D: $\mu_X + \rho (Y - \mu_Y)$