% Probabilités IV

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\L}{\mathcal{L}}
\renewcommand{\No}{\mathcal{N}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Esp}{\mathbb{E}}

\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}

#### Question 1 (réponse multiple)
Soit $(X_n)_{n\in \N^\ast}$ une suite de v.a. i.i.d. de loi $\Gamma(\alpha,\theta)$ et $M_n = \frac{1}{n}\sum_{i=1}^n X_i$

  - [ ] A : $M_n \to \frac{\alpha}{\theta}$ p.s. quand $n \to \infty$

  - [ ] B : $M_n \xrightarrow[n \to \infty]{\P} \frac{\alpha}{\theta}$ 

  - [ ] C : $\sqrt{n}(M_n - \frac{\alpha}{\theta}) \xrightarrow[n \to \infty]{\L} Y \sim \No(0,\frac{\alpha}{\theta^2})$

  - [ ] D : $M_n \xrightarrow[n \to \infty]{\L^1} \frac{\alpha}{\theta}$


#### Question 2 (réponse multiple)
Soit $(X_n)_{n\in \N^\ast}$ une suite de v.a. i.i.d. de même loi qu'une variable $X$ de fonction de répartition $F$ et $a \in ]0,1[$

  - [ ]  A : $X_n^a \to \Esp(X^a)$ p.s. quand $n \to \infty$

  - [ ]  B : $\frac{1}{n}\sum_{i=1}^n 1_{]-\infty,a]} (X_i) \to F(a)$ p.s. quand $n \to \infty$

  - [ ]  C : $\P(X_n \leq a) \to 0$  quand $n \to \infty$

  - [ ]  D : $\Esp(1_{]a,+\infty[}(X)) = 1-F(a)$

#### Question 3 (réponse multiple)
Soit $(X_n)_{n\in \N^\ast}$ une suite de v.a. indépendantes de loi $\mathcal{E}(\lambda_n)$ où $\lambda_n$ est une suite réelle qui converge vers 1.

  - [ ]  A : $X_n \xrightarrow[n \to \infty]{\P} 1$ 

  - [ ]  B : $\frac{1}{n}\sum_{i=1}^n X_i \to 1$ p.s. quand $n \to \infty$

  - [ ]  C : $\Esp(X_n) \to 1$ quand $n \to \infty$

  - [ ]  D : $X_n \xrightarrow[n \to \infty]{\L} Y \sim \mathcal{E}(1)$ 

#### Question 4 (réponse multiple)
Soit $(X_n)_{n\in \N^\ast}$ une suite de v.a. indépendantes de loi de Cauchy, dont on rappelle la densité :$f(x) = \frac{1}{\pi(1+x^2)}, x \in \R$.

  - [ ]  A : $\frac{1}{\sqrt{n}}\left(\sum_{i=1}^n X_i -1\right) \xrightarrow[n \to \infty]{\L} Y \sim \No(0,1)$ 

  - [ ]  B : $\frac{1}{n}\sum_{i=1}^n X_i \to 0$ p.s. quand $n \to \infty$

  - [ ]  C : $\Esp(X_n) \to +\infty$ quand $n \to \infty$

  - [ ]  D : Rien de tout cela

#### Question 5 (réponse multiple)

Soit $(X_n)_{n\in \N^\ast}$ une suite de v.a. indépendantes et une v.a. $X$, toutes définies sur le même espace probabilisé, telles que $\forall \varepsilon > 0$, $\P(|X_n - X|>\varepsilon) \leq \frac{1}{\varepsilon^2 n^2}$.

  - [ ]  A : $X_n \xrightarrow[n \to \infty]{\L} X$  

  - [ ]  B : $X_n \xrightarrow[n \to \infty]{\P} X$ 

  - [ ]  C : $X_n \xrightarrow[n \to \infty]{} X$ p.s. 

  - [ ]  D : Rien de tout cela
