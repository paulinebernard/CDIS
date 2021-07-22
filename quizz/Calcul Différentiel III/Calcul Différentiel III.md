% Calcul Différentiel III

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
Soit $f: (x_1, x_2) \in \R^2 \mapsto x_1 x_2 \in \R$. On a

 - [ ] A: $$H_f(x) = \left[\begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right]$$

 - [ ] B: Si $h_1 = (h_{11}, h_{12}) \in \R^2$ et $h_2 = (h_{21}, h_{22}) \in \R^2$,
   $$d^2 f(x_1, x_2) \cdot h_1 \cdot h_2 = h_{11}h_{22} - h_{21}h_{12}$$


 - [ ] C: Pour tout $x \in \R^2$ 
          $$\nabla f(x+h) = \nabla f(x) + \frac{1}{2} \left< h, H_f(x) \cdot h\right> + \varepsilon(h) \|h\|^2$$
          où $\varepsilon(h) \to 0$ quand $h \to 0$.

#### Question 2
Si $f: \R^n \to \R$ est deux fois différentiable en $x \in U$
et que $df(x) \cdot h \cdot h$ est connu pour tout $h \in \R^n$, 
peut-on déterminer $df(x) \cdot h_1 \cdot h_2$ pour tout $h_1, h_2 \in \R^n$ ?

  - [ ] A : oui,

  - [ ] B : non.

#### Question 3
Si $f: \R^3 \to \R^3$ est deux fois différentiable, combien y'a-t'il au plus
de coefficients différents dans le tenseur représentant $d^2f(x)$ ?

  - [ ] A : 9,

  - [ ] B : 18,

  - [ ] C : 27.

#### Question 4 (réponses multiples)
Soient $f: \R^2 \to \R$ et $a \in \R^2$ tels que $\partial_{12}f(a) = \partial_{21}f(a)$. Alors $f$ est 

  - [ ] deux fois continûment différentiable en $a$,

  - [ ] deux fois différentiable en $a$,

  - [ ] différentiable en $a$,

  - [ ] continue en $a$.


#### Question 5
La différentielle $d^3f$ d'ordre $3$ d'une fonction $f: U \subset \R^2\to \R^3$

  - [ ] A : associe linéairement à tout vecteur $h$ de $\R^2$ une application qui 
    associe linéairement à tout vecteur $k$ de $\R^2$ une application qui 
    associe linéairement à tout vecteur $p$ de $\R^2$ un vecteur de $\R^3$.

  - [ ] B : associe linéairement à tout point $x \in U$ une application 
    qui associe linéairement à tout vecteur $h$ de $\R^2$ une application qui 
    associe linéairement à tout vecteur $k$ de $\R^2$ un vecteur de $\R^3$.

  - [ ] C : associe à tout point $x \in U$ une application 
    qui associe linéairement à tout vecteur $h$ de $\R^2$ une application qui 
    associe linéairement à tout vecteur $k$ de $\R^2$ une application qui 
    associe linéairement à tout vecteur $p$ de $\R^2$ un vecteur de $\R^3$.

<!--
#### Question 4 (réponses multiples)
Le tenseur de type $(1,1,1)$ défini par $t_{ijk} = 1.0$ :

  - [ ] A : est d'ordre $1$,

  - [ ] B : est décrit en NumPy par le tableau `np.array([1.0])`,

  - [ ] C : représente l'application linéaire
    $x \in \R \to y \in \R \to xy \in \R.$

#### Question 5
La contraction du tenseur  $[t_{ijk}]_{ijk}$ de type $(m, n, p)$ et
du tenseur de type $(p,p)$ défini par $\delta_{lm} = 1$ si $l=m$ et $\delta_{lm}=0$ sinon

  - [ ] A : n'est pas définie en général,

  - [ ] B : est le tenseur $[t_{ijk}]_{ijk}$,

  - [ ] C : est le tenseur $[\sum_{k} t_{ijk}]_{ij}$.

-->

#### Question 6
Si $f: \R^2 \to \R^4$ est trois fois différentiable, quel est le type du tenseur
représentant $d^3f(x)$ ?

 - [ ] A : (4, 2, 2, 2),

 - [ ] B : (3, 4, 2),

 - [ ] C : (4, 2, 1).

#### Question 7 (réponses multiples)
Si $f$ est $k$ fois différentiable en $x$,

  - [ ] A : les dérivées partielles d'ordre $k$ de $f$ en $x$ existent,

  - [ ] B : on a $\partial^k_{i_{k} \dots i_1} f(x) = d^k f(x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_{k}},$

  - [ ] C : les dérivées partielles de d'ordre $k$ de $f$ en $x$ déterminent $d^k f(x)$ de façon unique.




  
