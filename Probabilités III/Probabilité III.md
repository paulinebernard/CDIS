% Probabilités III


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

\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}


Objectifs d'apprentissage
================================================================================

Cette section s'efforce d'expliciter et de hiérarchiser les acquis d'apprentissages associés au chapitre. 
Ces objectifs sont organisés en paliers :

(\zero) Prérequis (\one) Fondamental (\two) Standard (\three) Avancé
(\four) Expert

Sauf mention particulière, la connaissance des démonstrations du document 
n'est pas exigible[^hp] 

[^hp]: l'étude des démonstrations du cours peut toutefois 
contribuer à votre apprentissage, au même titre que la résolution 
d'exercices.

#### Lois conditionnelles

- \two connaître le théorème de Fubini conditionnel 
- \two connaître les formules de balayage conditionnel 
- \two savoir appliquer ces résultats pour différents types de loi de probabilité (à densité ou non)
- \one connaître le critère d'indépendance qui résulte du théorème de Fubini conditionnel

#### Espérance conditionnelle

- \one connaître les deux points de la définition de l'espérance conditionnelle
- \one connaître les deux points de la définition de l'espérance conditionnelle d'une fonction de variables aléatoires
- \one connaître et savoir utiliser la formule de l'espérance totale
- \two savoir calculer la densité conditionnelle d'un certain nombre de composantes sachant les autres dans un vecteur gaussien à densité

#### Cas $\mathcal{L}^2$

- \two savoir que la régression linéaire est la meilleure approximation linéaire (au sens des moindres carrés) d'une variable aléatoire par une autre
- \three savoir retrouver ce résultat
- \four connaître l'interprétation géométrique de l'espérance conditionnelle dans le cas $\L^2$
- \one connaître et savoir utiliser la formule de la variance totale



# Lois conditionnelles 

## Introduction

On s'est consacré jusqu'à présent à l'étude de variables aléatoires indépendantes. En pratique cependant, on rencontre souvent des variables dépendant les unes des autres. Dans le cas de la météo, les variables température, vitesse du vent et pression en fournissent un exemple. Dans les approches bayésiennes, on résume l'information disponible sur l'état du système étudié par la **loi a priori** et on met à jour notre connaissance du système en incorporant de l'information supplémentaire (par exemple des observations). On cherche alors à caractériser la **loi a posteriori** de l'état du système, qui est la loi de l'état sachant l'information supplémentaire. On va ainsi s'attacher dans ce chapitre à décrire les **lois conditionnelles** qui vont permettre de résumer l'information apportée par une variable (ou un vecteur) sur une autre et s'intéresser en particulier à l'**espérance conditionnelle** qui indiquera le comportement moyen d'une variable conditionnellement à une autre. Ce dernier cas pose le cadre probabiliste d'un des problèmes fondamentaux en apprentissage statistique : l'apprentissage supervisé, où on dispose d'un ensemble de réalisations d'une variable dont on cherche à prédire le comportement à partir d'un ensemble de variables dites explicatives (ou prédicteurs). 

## Lois conditionnelles dans un couple

Soient deux variables aléatoire $X$ et $Y$ définies sur le même espace probabilisé $(\Omega, \A, \P)$. Dans le cas où $X$ et $Y$ sont indépendantes, on a vu que pour tous boréliens $B_1$ et $B_2$ de $\B(\R)$, on a 
$$\P(X\in B_1, Y\in B_2)= \P(X\in B_1)\P(Y\in B_2) = \P_X(B_1)\P_Y(B_2) = \int_{B_1}\P_Y(B_2)d\P_X(x),$$
où on a utilisé le [théorème de Fubini](Probabilité II.pdf #fubiniproba).

Du fait de l'indépendance, on a aussi $\P_Y(B_2) = \P(Y\in B_2) = \P(Y \in B_2 | X \in B_1) = \P_Y(B_2|X \in B_1)$ ce qui exprime que pour tout borélien $B_1$, la loi conditionnelle de $Y$ sachant $X\in B_1$ est identique à la loi de $Y$.

Lorsque $X$ et $Y$ en sont pas indépendantes, on va chercher à établir une égalité de la forme
$$\P(X\in B_1, Y\in B_2) = \P_X(B_1)\P_Y(B_2 |X\in B_1) = \int_{B_1}\P_{Y|X=x}(B_2)d\P_X(x)$$
et s'intéresser à caractériser la *loi conditionnelle de $Y$ sachant $X=x$*, que l'on notera donc $\P_{Y|X=x}$.

De même, pour toute application $g : \R^2 \to \R$ mesurable telle que $g(X,Y)$ admette une espérance (relativement à la loi du couple $\P_{X,Y}$), on voudrait écrire :
$$\Esp(g(X,Y)) = \int_{\R} \left( \int_{\R} g(x,y) d\P_{Y|X=x}(y)\right) d\P_X(x)$$

Pour bien fixer les idées, on va décrire spécifiquement les cas où $X$ est discrète puis où le couple $(X,Y)$ admet une densité avant d'aborder le cas général.

## Cas où $X$ est discrète
Dans ce paragraphe, on suppose que la variable aléatoire réelle $X$ est discrète, c'est-à-dire que l'ensemble $X(\Omega) \subset \R$ des valeurs $x_k$ prises par $X$ est au plus dénombrable.

On peut imposer que $\forall x \in X(\Omega)$ on ait $\P(X=x) > 0$, quitte à modifier $X$ sur un ensemble de probabilité nulle. On va ainsi pouvoir utiliser la définition de la probabilité conditionnelle pour des événements de la forme $\{X =x\}$. Ceci permet d'écrire pour tous boréliens $B_1$ et $B_2$ de $\R$ :
\begin{align*}
\P(X \in B_1, Y \in B_2) &= \sum_{x \in X(\Omega)\cap B_1} \P(X=x, Y\in B_2)\\
                         &= \sum_{x \in X(\Omega)\cap B_1} \P(X=x) \P(Y \in B_2 | X=x)\\
                         &= \int_{B_1} \P(Y \in B_2 | X=x) d\P_X(x)
\end{align*}
puisque $\P_X = \sum_{x \in X(\Omega)} \P(X=x)\delta_x$. On obtient ainsi l'écriture souhaitée en posant
$$\P_{Y|X=x}(B_2) = \P(Y \in B_2 | X=x),\,\,\,\forall x \in X(\Omega), \forall B_2\in\B(\R).$$

### Image de la probabilité conditionnelle {.remark}
$\P_{Y|X=x}$ ainsi définie est simplement la probabilité sur $(\R,\B(\R))$ image par $Y$ de la probabilité conditionnelle $\P(\cdot|X=x)$ définie sur $(\Omega,\A)$, autrement dit, la **loi de $Y$ relative à $\P(\cdot|X=x)$** et non à $\P$.

La formule ci-dessus s'écrit $\P_{X,Y}(B_1 \times B_2) = \int_{B_1} \P(Y \in B_2 | X=x) d\P_X(x)$, où $\P_{X,Y}$ est la loi du couple. Elle se généralise à tout borélien $B$ de $\R^2$ de la manière suivante :
$$
\begin{aligned}
\P_{X,Y}(B) &= \P((X,Y)\in B) = \sum_{x \in X(\Omega)} \P(X=x, (x,Y) \in B) \\
      &= \sum_{x \in X(\Omega)} \P(X=x) \P((x,Y) \in B | X=x) \\
      &= \sum_{x \in X(\Omega)} \P(X=x) \P_{Y|X=x}(B_x),
\end{aligned}
$$
où $B_x = \{y\in \R, (x,y) \in B\}$. Ainsi, pour tout $B$ borélien de $\R^2$,

$$\Esp(1_B(X,Y)) = \int_{\R^2} 1_B(x,y)d\P_{X,Y}(x y) = \int_\R \left(\int_\R 1_B(x,y) d\P_{Y|X=x}(y)\right)  d\P_X(x)$$

Par linéarité de l'espérance, on peut ainsi exprimer l'espérance d'une fonction étagée. Pour avoir le résultat pour une fonction mesurable positive, on exprime celle-ci comme limite simple d'une suite croissante de fonctions étagées, et on applique le théorème de convergence monotone. Enfin, on applique cette construction à $g_+$ et $g_-$ pour une fonction $g$ de signe quelconque $\P_{X,Y}$-intégrable. En d'autres termes, on reprend le procédé de construction de l'intégrale de Lebesgue. On obtient ainsi la formule souhaitée :
$$\Esp(g(X,Y)) = \int_{\R} \left( \int_{\R} g(x,y) d\P_{Y|X=x}(y)\right) d\P_X(x).$$

### Pour fixer les idées (1) {.example #ex1}

Soit $X \geq 0$ une variable aléatoire à valeurs dans $\N$ et $Y$ une variable aléatoire réelle positive telle que la loi du couple $\P_{X,Y}$ vérifie pour tout $n\in\N$ et tout borélien $B_2$ de $\R$ :
$$\P_{X,Y} (\{n\}\times B_2) = (1-\alpha)\alpha^n \int_{B_2 \cap \R_+^\ast}e^{-t}\frac{t^n}{n!}dt,\,\,\, 0 < \alpha <1$$
$\P_{X,Y}$ est bien une probabilité sur $\R^2$ puisque par convergence monotone :
\begin{align*}
\P_{X,Y} (\R^2) &= \P_{X,Y}(\N \times \R) \\
                &= \sum_{n\in\N} \P_{X,Y} (\{n\}\times \R)\\
                &= \sum_{n\in\N} (1-\alpha)\alpha^n \int_{\R_+^\ast}e^{-t}\frac{t^n}{n!}dt \\
                &= (1-\alpha)\int_{\R_+^\ast}e^{-t} \sum_{n\in\N} \frac{(\alpha t)^n}{n!}dt \\
                &= (1-\alpha)\int_{\R_+^\ast}e^{-(1-\alpha)t} dt = 1
\end{align*}               
où on aura reconnu la loi exponentielle de paramètre $(1-\alpha)$.
$\forall n \in \N$, 
$$ \int_{\R_+^\ast}e^{-t}\frac{t^n}{n!}dt = \int_{\R_+^\ast}e^{-t}\frac{t^{(n-1)}}{(n-1)!}dt = \ldots = \int_{\R_+^\ast}e^{-t}dt =1$$
par intégrations par parties itérées. La loi marginale de $X$ s'écrit donc :
$$\forall n \in \N, \P(X=n) = \P_{X,Y} (\{n\}\times \R_+^\ast) = (1-\alpha)\alpha^n,$$ 
loi géométrique de paramètre $(1-\alpha)$. On en déduit la loi conditionnelle de $Y$ sachant $X = n$ :
$$\P_{Y|X=n}(B_2) = \P(Y \in B_2 | X=n) = \frac{\P_{X,Y} (\{n\}\times B_2)}{\P(X=n)} = \int_{B_2 \cap \R_+^\ast} e^{-t}\frac{t^n}{n!}dt$$
et $\P_{Y|X=n}$ est la donc la loi gamma de paramètre $(n+1,1)$.


## Densités conditionnelles

On suppose maintenant que le couple $(X,Y)$ admet une densité $f_{X,Y}$ (par rapport à la mesure de Lebesgue). On note $f_X(x) = \int_\R f_{X,Y}(x,y)dy$ (respectivement $f_Y(y) = \int_\R f_{X,Y}(x,y)dx$) la loi marginale de $X$ (resp. de $Y$). On s'intéresse à caractériser la densité de la variable $Y$ connaissant la valeur prise par la variable $X$, c'est la *densité conditionnelle* de $Y$ sachant $\{X = x\}$ :

### Densité conditionnelle {.proposition #defdenscond}
La formule suivante définit une densité sur $\R$, pour tout $x \in \R$ tel que $f_X(x) > 0$.
$$ f_{Y|X=x}(y) = \frac{f_{X,Y}(x,y)}{f_X(x)}.$$
Cette fonction s'appelle la *densité conditionnelle de $Y$ sachant $\{X = x\}$*.
La probabilité conditionnelle de $Y$ sachant $\{X = x\}$ s'écrit ainsi $\P_{Y|X=x} = f_{Y|X=x}\lambda$, où $\lambda$ représente la mesure de Lebesgue.

### Démonstration {.proof}
La preuve est immédiate puisque $f_{Y|X=x}$ est une fonction positive d'intégrale 1.

### Dans un triangle (1) {.exercise .question .one #etb1} 

Soient $X$ et $Y$ de densité jointe $f_{X,Y}(x,y)= \frac{1}{x}1_T (x,y)$ où $T$ est le triangle $T = \{0< y< x < 1\}$.

1. Calculer la densité marginale de $X$
2. Calculer la densité conditionnelle de $Y$ sachant $X=x$.


### {.anonymous}

L’interprétation de cette définition est la suivante : la fonction $f_{Y|X=x}$ est la densité de la “loi conditionnelle de $Y$ sachant que $X = x$”. Bien sûr, nous avons $\P(X = x) = 0$ puisque $X$ admet une densité, donc la phrase ci-dessus n’a pas réellement de sens, mais elle se justifie heuristiquement ainsi : $dx$ et $dy$ étant de “petits” accroissements des variables $x$ et $y$ et lorsque $f$ et $f_X$ sont continues et strictement positives respectivement en $(x,y)$ et $x$ :
\begin{align*}
f_X(x) dx & \approx \P(X \in [x, x+dx])\\
f_{X,Y}(x,y) dx dy & \approx \P(X \in [x, x+dx], Y \in [y, y+dy])\\
\end{align*}
Par suite 
\begin{align*}
f_{Y|X=x} (y) dy & \approx \frac{\P(X \in [x, x+dx], Y \in [y, y+dy])}{\P(X \in [x, x+dx])}\\
                 & \approx \P(Y \in [y, y+dy]|X \in [x, x+dx])\\
\end{align*}

On a alors le résultat suivant qui résout le problème posé en introduction :

### Proposition {.proposition}
Pour toute fonction $g : \R^2 \to \R$ telle que $g(X,Y)$ admette une espérance, on a :
$$\Esp(g(X,Y)) = \int_\R \left( \int_\R g(x,y)f_{Y|X=x}(y) dy \right) f_X(x) dx,$$ 
dont on déduit, en prenant $g=1_{B_1 \times B_2}$, que :
$$\P(X\in B_1, Y\in B_2) = \int_{B_1} \left( \int_{B_2}f_{Y|X=x}(y) dy \right) f_X(x) dx.$$

### Démonstration {.proof}
On a 
\begin{align*}
\Esp(g(X,Y)) &= \int_{\R^2} g(x,y) f_{X,Y}(x,y) dy dx \\
             &= \int_{\R^2} g(x,y) f_{Y|X=x}(y)f_X(x) dy dx \\
             &= \int_\R \left( \int_\R g(x,y)f_{Y|X=x}(y) dy \right) f_X(x)dx,
\end{align*}
les calculs étant licites par application du [théorème de Fubini](Probabilité II.pdf #fubiniproba) et du fait que l'application $x \mapsto \int_\R g(x,y)f_{Y|X=x}(y) dy$ est définie pour $f_X(x) >0$, soit presque partout relativement à la mesure $\P_X = f_X \lambda$.

## Cas général
On peut établir le résultat suivant, qui complète le [théorème de Fubini](Probabilité II.pdf #fubiniproba) et le résultat d'existence et d'unicité des mesures produits, et que l'on admettra.

### Fubini conditionnel {.theorem #fubinicond}
Soit un couple $(X,Y)$ de variables aléatoires réelles de loi jointe $\P_{X,Y}$, il existe une famille $\left(\P_{Y|X=x}\right)_{x\in\R}$ de probabilités sur $(\R,\B(\R))$, unique à une égalité $\P_X$-presque partout près[^footequi], qui vérifie pour tous $B_1, B_2$ boréliens de $\R$ :
$$ \P_{X,Y}(B_1 \times B_2) = \int_{B_1} \left( \int_{B_2} d\P_{Y|X=x}(y) \right) d\P_X(x).$$
Ces probabilités sont appelées *lois conditionnelles* de $Y$ sachant $X =x$. On a de plus pour toute application $g : \R^2 \to \R$ telle que $g(X,Y)$ admette une espérance :
$$\Esp(g(X,Y)) = \int_\R \left( \int_\R g(x,y)d\P_{Y|X=x}(y) \right) d\P_X(x).$$ 

[^footequi]: c'est-à-dire qu'on peut définir ces probabilités de la manière qu'on souhaite pour les boréliens $B$ tels que $\P_X(B)=0$.

### A noter {.remark}

* Ce résultat peut être interprété comme un **théorème de Fubini conditionnel**, dans le sens où il permet une intégration séquentielle, mais ici la mesure de probabilité du couple $(X,Y)$ s'exprime comme un produit de mesures dont l'un des termes dépend de la variable d'intégration de l'autre. En particulier, si on change l'ordre d'intégration, on change les mesures qui interviennent.
* Fréquemment, dans les applications, la famille des lois conditionnelles est une donnée du modèle considéré, et leur existence ne pose donc pas de problème !
* On retrouve les cas vus précédemment en notant que pour tout borélien $B_1$ de $\R$ on a $\P_X(B_1) = \int_{B_1}d\P_X(x) = \sum_{x \in B_1} \P(X=x)$ lorsque $X$ est discrète, et que pour tous boréliens $B_1$ et $B_2$ de $\R$ on a $\P_X(B_1) = \int_{B_1} f_X(x)dx$ et $\P_{X,Y}(B_1 \times B_2) = \int_{B_1 \times B_2}f_{X,Y}(x,y) dx dy$.
* Dans tout ce qui précède, les rôles de $X$ et $Y$ peuvent évidemment être inversés. 

## Conséquences
Le [théorème précédent](#fubinicond) a deux conséquences majeures. Il fournit d'une part un moyen efficace d'identifier la loi marginale de $Y$ connaissant la loi marginale de $X$ et la loi de $Y$ sachant $X = x$. En effet, en notant que pour tout borélien $B$ de $\R$, $\P_Y(B) = \P_{X,Y}(\R \times B)$ et en appliquant ce théorème, on a la proposition suivante :

### Formule de balayage conditionnel {.proposition #balcond}

* La loi marginale $\P_Y$ de $Y$ s’exprime comme la moyenne des lois conditionnelles $\P_{Y|X=x}$ pondérée par la loi de $X$. Pour tout $B$ borélien de $\R$
$$\P_Y(B) = \int_\R \left( \int_{B} d\P_{Y|X=x}(y) \right) d\P_X(x) = \int_\R \P_{Y|X=x}(B) d\P_X(x)$$
* Dans le cas où $X$ est discrète (à valeurs dans $I$ dénombrable), on retrouve une expression de la formule des probabilités totales et composées :
$$\P_Y(B) = \P(Y\in B) = \sum_{x \in I} \P(Y \in B | X = x)\P(X=x)$$
* Dans le cas où le couple $(X,Y)$ admet une densité, puisqu'on a $f_{X,Y}(x,y) = f_{Y | X=x}(y)f_X(x)$, on obtient l'expression suivante pour la densité marginale :
$$f_Y(y) = \int_\R f_{X,Y}(x,y)dx = \int_\R f_{Y | X=x}(y)f_X(x) dx.$$
 On a en particulier la *formule de Bayes pour les densités* : pour tout $x$ tel que $f_X(x) > 0$ et tout $y$ tel que $f_Y(y) > 0$ :
    $$ f_{X|Y=y}(x) = \frac{f_{X,Y}(x,y)}{f_Y(y)} = \frac{f_{Y|X=x}(y)f_X(x)}{f_Y(y)} .$$


### Pour fixer les idées (2) {.example}
Poursuivons [l'exemple vu plus haut](#ex1). On rappelle qu'on a déjà identifié la loi marginale de $X$ ainsi que la loi conditionnelle de $Y$ sachant $X=n$ pour $n\in\N$ que l'on rappelle ici :
$$\P(X=n) = (1-\alpha)\alpha^n,\,n\in\N \text{ et }\forall  B \in \B(\R), \, \P_{Y|X=n}(B) = \int_{B \cap \R_+^\ast} e^{-t}\frac{t^n}{n!}dt$$
On peut en déduire la loi marginale de $Y$ en utilisant la [formule de balayage conditionnel](#balcond) et le théorème de convergence monotone :
$$\begin{aligned}
\P_Y(B)  &= \sum_{n \in \N} (1-\alpha)\alpha^n \int_{B \cap \R_+^\ast} e^{-t}\frac{t^n}{n!} dt\\
         &= (1-\alpha) \int_{B \cap \R_+^\ast} e^{-t} \sum_{n \in \N} \frac{(\alpha t)^n}{n!} dt \\
         &= \int_B 1_{\R_+}(t)(1-\alpha) e^{-(1-\alpha)t} dt,
\end{aligned}$$
de sorte que $Y$ suit une loi exponentielle de paramètre $(1-\alpha)$.

En inversant les rôles, on va pouvoir identifier la loi de $X$ sachant $Y \in B$ en notant que
\begin{align*}
\P_{X,Y}(\{n\} \times B) &= \P_X(\{n\})\P_{Y|X=n}(B) \\
                         &= \int_B \frac{(\alpha t)^n}{n!} e^{-\alpha t} d\P_Y(t)\\
                         &= \int_B \P_{X | Y =t}(\{n\}) d\P_Y(t)
\end{align*}
où l'on reconnaît que $\P_{X =n | Y =t}(\{n\}) = \frac{(\alpha t)^n}{n!} e^{-\alpha t}$, c'est-à-dire que $X$ sachant $Y = t$ suit une loi de Poisson de paramètre $\alpha t$ pour $\P_Y$-presque tout $t$.

### {.anonymous}
En utilisant, le [théorème de Fubini conditionnel](#fubinicond), on obtient également une nouvelle caractérisation de l'indépendance de deux variables aléatoires faisant intervenir les lois conditionnelles.

### Critère d'indépendance {.proposition}

1. $X$ et $Y$ sont indépendantes si et seulement si, pour $\P_X$-presque tout $x$, $\P_{Y |X = x}$ ne dépend pas de $x$ et dans ce cas, on a $\P_{Y |X = x} = \P_Y$, c'est-à-dire que la loi conditionnelle est identique à la loi marginale.

2. Dans le cas où $(X,Y)$ admet une densité, $X$ et $Y$ sont indépendantes si et seulement si la densité conditionnelle de $Y$ sachant $\{X = x\}$ ne dépend pas de $x$.

### Démonstration {.proof}

1. Si $X$ et $Y$ sont indépendantes, pour tous $B_1$, $B_2$ boréliens de $\R$, $\P_{X,Y} (B_1 \times B_2) = \P_X(B_1)\P_Y(B_2) = \int_{B_1}\P_Y(B_2)d\P_X(x) = \int_{B_2}\P_X(B_1) d\P_Y(y)$. Le résultat d'unicité du [théorème de Fubini conditionnel](#fubinicond) (à une égalité $\P_X$-presque sûre près), nous indique alors que $\P_{Y|X=x}(B_2) = \P_Y(B_2)$.

   Inversement, si $\P_{Y |X = x} = \P_Y$, alors $\P_{X,Y} (B_1 \times B_2) = \int_{B_1}\P_{Y|X=x}(B_2)d\P_X(x) = \int_{B_1}\P_Y(B_2)d\P_X(x) = \P_X(B_1)\P_Y(B_2)$.

2. Si $X$ et $Y$ sont indépendantes, $f_{X,Y} (x,y) = f_X(x) f_Y(y)$, d'où $f_{Y|X=x}(y) = f_Y(y)$.

   Inversement, si $f_{Y|X=x}(y) = f_Y(y)$ alors $f_{X,Y}(x,y) = f_{Y|X=x}(y) f_X(x) = f_Y(y)f_X(x)$ et $X$ et $Y$ sont indépendantes.

# Espérance conditionnelle

Puisque $\P_{Y|X=x}$ est la loi d'une variable aléatoire, on peut définir l'espérance qui lui est associée et introduire la notion d'espérance conditionnelle dans le cas où $Y$ est intégrable.

### Espérance conditionnelle {.definition #defespcond}
Soit $Y \in \L^1$.

 1. L'*espérance conditionnelle de $Y$ sachant $\{X=x\}$* est définie par 
    $$\Esp(Y|X=x) = \int_\R y d\P_{Y|X=x} (y).$$
 2. L'*espérance conditionnelle de $Y$ sachant $X$* est la **variable aléatoire** définie par :
    $$\Esp(Y|X) = \psi(X), \text{ avec } \psi(x) = \Esp(Y|X=x).$$

### Dans un triangle (2) {.exercise .question .one #etb2} 
Soient $X$ et $Y$ de densité jointe $f_{X,Y}(x,y)= \frac{1}{x}1_T (x,y)$ où $T$ est le triangle $T = \{0< y< x < 1\}$.
Calculer l'espérance conditionnelle de $Y$ sachant $X$.


### Conséquences {.remark}

 1. $\psi(x)$ n'est définie que pour $x \notin N$, avec $\P(X\in N) = 0$. Par conséquent, la [définition](#defespcond) définit bien l'espérance conditionnelle $\psi(X) = \Esp(Y|X)$ $\P_X$-presque partout, autrement dit avec probabilité 1, ou encore presque sûrement.
 2. $\Esp(\Esp(|Y||X)) = \Esp(|Y|)$ comme conséquence directe du [théorème de Fubini conditionnel](#fubinicond). L'espérance conditionnelle de $Y$ sachant $X$ est bien définie dès que $Y$ est intégrable. 
 3. Lorsque $(X,Y)$ admet une densité, l'espérance conditionnelle de $Y$ sachant $\{X=x\}$ s'écrit
 $$\Esp(Y|X=x) = \int_\R y f_{Y|X=x}(y) dy.$$

### Auto-conditionnement {.exercise .question .one #autocond}
Montrer que $\Esp(Y|Y) = Y$.

### {.anonymous}
On peut étendre cette définition aux variables de la forme $g(X,Y)$.

### Espérance conditionelle d'une fonction de variables aléatoires  {.definition #defespcondg}
Soit $(X,Y)$ un couple de variables aléatoires réelles et $g$ une fonction mesurable positive ou $\P_{X,Y}$-intégrable sur $\R^2$.

 1. L'*espérance conditionnelle de $g(X,Y)$ sachant $\{X=x\}$* est définie par 
    $$\Esp(g(X,Y)|X=x) = \int_\R g(x,y) d\P_{Y|X=x} (y).$$
 2. L'*espérance conditionnelle de $g(X,Y)$ sachant $X$* est la **variable aléatoire** définie par :
    $$\Esp(g(X,Y)|X) = \psi(X), \text{ avec } \psi(x) = \Esp(g(X,Y)|X=x).$$

### Espérance totale {.theorem} 
Si $Y$ est intégrable, alors $\psi(X) = \Esp(Y | X)$ est intégrable, et 
$$\Esp( \psi(X)) = E( Y ) .$$

### Démonstration {.proof} 
C'est une conséquence directe du [théorème de Fubini conditionnel](#fubinicond).

### {.anonyomous}
Ce résultat permet de calculer $\Esp( Y )$ en conditionnant par une variable auxiliaire $X$ :
$$\Esp( Y ) = \int_\R \Esp(Y | X = x) d\P_X(x)$$

Il généralise la [formule des probabilités totales](Probabilité I.pdf #formprobatot), qui correspond ici à $Y = 1_A$ , et $B_x = \{X = x\}$ où les $B_x$ forment cette fois une partition non dénombrable de $\R$. On l’écrit souvent sous la forme
$$ \Esp \left( \Esp(Y | X) \right) = \Esp( Y )$$
et on l'appelle la *formule de l'espérance totale*.


L’espérance conditionnelle étant définie comme l’espérance selon la loi conditionnelle,
elle hérite des propriétés usuelles de l’espérance :
 
 1. si $Y$ et $Z$ sont intégrables, $\Esp (aY + bZ | X) = a \Esp (Y | X) + b \Esp(Z | X)$,
 2. $\Esp (Y | X) \geq 0$ si $Y \geq 0$,
 3. $\Esp (1 | X) = 1$.

De plus, si $g$ est mesurable positive ou $\P_X$-intégrable,
$$ \Esp (Y g(X) | X) = g(X) \Esp (Y | X) $$
est une généralisation de l’égalité 1. ci-dessus, au cas où $a = g(X)$, qui doit être considéré “comme une constante” dans le calcul de l’espérance conditionnelle sachant $X$ ($X$ est fixée comme une donnée connue a priori). En effet, on a alors $\Esp(g(x)Y|X=x) = g(x)\psi(x)$. Enfin, on déduit directement du [théorème de Fubini conditionnel](#fubinicond) la proposition suivante.

### Transfert conditionnel {.proposition #transfcond}
Soient un couple $(X,Y)$ de variables aléatoires réelles de loi jointe $\P_{X,Y}$ et $g$ une fonction mesurable positive ou $\P_{X,Y}$-intégrable sur $\R^2$. On a pour $\P_X$-presque tout $x$ dans $\R$
$$\Esp(g(X,Y)|X=x) = \Esp(g(x,Y)|X=x) = \int_{\R}g(x,y) d\P_{Y|X=x} (y)$$
Si de plus $X$ et $Y$ sont indépendantes, on a :
$$\Esp(g(X,Y)|X=x) = \Esp(g(x,Y)|X=x) = \int_{\R}g(x,y) d\P_Y(y).$$

Autrement dit, lorsqu'on conditionne par l'événement $\{X=x\}$, cela revient à fixer la valeur de la variable aléatoire $X$ à la constante $x$.

### Espérance conditionnelle d'un produit de variables {.exercise .question .one #prod}
Calculer $\Esp(XY|X=x)$ puis $\Esp(XY|X)$.

## Exemple : vecteurs Gaussiens à densité

Dans ce qui précède, on a décrit les lois et les espérances conditionnelles dans le cas d'un couple de variables aléatoires à valeurs dans $\R^2$. Ces résultats sont aussi valables pour des couples de vecteurs, dont on décrit ici un cas particulier.

Dans le cas des vecteurs gaussiens à densité, c'est-à-dire dont la matrice de covariance est définie positive et donc inversible, le calcul des lois conditionnelles de certaines composantes par rapport aux autres est particulièrement aisé. On va voir en particulier que les lois conditionnelles ont le bon goût d'être elles-mêmes gaussiennes, ce qui explique (en partie) le succès de ces modèles dans les applications.

On considère un vecteur gaussien $X = (X_1,\ldots,X_n)$ à valeurs dans $\R^n$ d'espérance $m$ et de matrice de covariance $C$ définie positive. On a vu au chapitre 2 que la densité du vecteur $X$ s'écrit pour $x\in\R^d$ :
$$f_X(x) = \frac{1}{(2\pi)^{n/2}\sqrt{\det (C)}}\exp \left(-\frac{1}{2}(x-m)^t C^{-1}(x-m)\right)$$

Soit $1 \leq k < n$ un entier. On souhaite exprimer $f_{Y|Z=z}$, la densité conditionnelle de $Y = (X_1,\ldots,X_k)$ sachant $Z = (X_{k+1},\ldots,X_n) = (x_k,\ldots,x_n) = z$ (si $k+1 = n$, ce vecteur se réduit à une seul valeur). On a vu que 
$$f_X = f_{Y|Z=z} f_Z,$$
où $f_Z$ est la densité marginale de $Z$. On cherche donc à décomposer $f_X$ de la sorte. On note $m = (m_Y,m_Z)$ et on remarque que $C$ peut se décomposer en blocs :
\begin{equation*}
C = \left(\begin{array}{cc} C_Y & C_{Y,Z} \\ C_{Z,Y} & C_Z \end{array}\right)
\end{equation*}
où $C_Y = \cov(Y,Y)$, $C_Z = \cov(Z,Z)$ et $C_{Y,Z} = \cov(Y,Z)$. Le *complément de Schur*[^mckbk] du bloc $C_Y$ est la matrice 
$$CS_Y = C_Y - C_{Y,Z}C_Z^{-1}C_{Z,Y}$$
et permet d'exprimer l'inverse de $C$ comme :
\begin{equation*}
C^{-1} = \left(\begin{array}{cc} CS_Y^{-1} & -CS_Y^{-1}C_{Y,Z}C_Z^{-1} \\ -C_Z^{-1}C_{Z,Y}CS_Y^{-1}  & C_Z^{-1} + C_Z^{-1}C_{Z,Y}CS_Y^{-1}C_{Y,Z}C_Z^{-1} \end{array}\right)
\end{equation*}
On peut alors réarranger les termes de la forme quadratique dans $f_X$ et on obtient :
\begin{align*}
(x-m)^t C^{-1}(x-m) =& \left(y - (m_Y + C_{Y,Z}C_Z^{-1}(z-m_Z))\right)^t CS_Y^{-1}\\
&.\left(y - (m_Y + C_{Y,Z}C_Z^{-1}(z-m_Z))\right)\\
 &+ (z-m_Z)^t C_Z^{-1}(z-m_Z)
\end{align*}
Pour la constante, on peut remarquer que :
$$ \det (C) = \det(CS_Y)\det(C_Z).$$
On en déduit ainsi que 
<!-- \begin{align*}
f_{Y|Z=z}(y) =& \frac{1}{(2\pi)^{n/2}\sqrt{\det (CS_Y)}}\\
&\exp \left(-\frac{1}{2}\left(y - \psi(z)\right)^t CS_Y^{-1}\left(y - \psi(z))\right)\right)
\end{align*} -->
$$f_{Y|Z=z}(y) = \frac{1}{(2\pi)^{k/2}\sqrt{\det (CS_Y)}}\exp \left(-\frac{1}{2}\left(y - \psi(z)\right)^t CS_Y^{-1}\left(y - \psi(z))\right)\right)$$


C'est-à-dire que la variable aléatoire $Y|Z=z$ est gaussienne d'espérance $m_{Y|Z=z} = \psi(z) = m_Y + C_{Y,Z}C_Z^{-1}(z-m_Z)$ et de matrice de covariance $CS_Y = C_Y - C_{Y,Z}C_Z^{-1}C_{Z,Y}$. Autrement dit, l'espérance conditionnelle de $Y$ sachant $Z$ est la variable aléatoire $\Esp(Y|Z) = \psi(Z) =(m_Y + C_{Y,Z}C_Z^{-1}(Z-m_Z))$. On notera que la covariance conditionnelle donnée par $CS_Y$ ne dépend pas de la valeur prise par $Z$.

[^mckbk]: voir par exemple l'excellent [matrix cookbook](https://www.ics.uci.edu/~welling/teaching/KernelsICS273B/MatrixCookBook.pdf).



# Régression et espérance conditionnelle des variables de carré intégrable

La régression est un ensemble de méthodes (d'apprentissage) statistiques très utilisées pour analyser la relation d'une variable par rapport à une ou plusieurs autres. Ces méthodes visent notamment à décrire les liens de dépendance entre variables mais aussi de prédire au mieux la valeur d’une quantité non observée en fonction d'une ou plusieurs autres variables.


Pour fixer les idées, supposons que nous nous intéressons au lien entre une variable d'intérêt $Y$ et une variable explicative $X$ dans le but de pouvoir prédire la valeur de $Y$ étant donnée l'observation de $X$. Dans un cadre probabiliste, les variables $X$ et $Y$ sont considérées comme un couple de variables aléatoires $(X,Y)$, et leur possible observation comme des réalisations de ce couple. Notre but est alors de proposer une certaine fonction $f : \R \rightarrow \R$, que l'on appellera prédicteur, qui permette d'approximer $Y$ par $f(X)$. 

Une manière naturelle de formaliser cette notion d'approximation est de se donner pour objectif de trouver une fonction $f$ permettant de minimiser l'erreur commise en remplaçant $Y$ par $f(X)$, par exemple au sens des moindres carrés. Ainsi, notre but devient de trouver un prédicteur $f$ qui minimise
$$ \Esp((Y-f(X))^2). $$
Le prédicteur $f$ choisi ainsi minimiserait donc "en moyenne" sur les réalisations de $(X,Y)$ l'écart quadratique entre $Y$ et $f(X)$.

On va montrer dans cette section que le prédicteur optimal $f^*(X)$ de $Y$, au sens décrit ci-dessus, est précisément donné par l'espérance conditionnelle de $Y$ sachant $X$, c'est-à-dire en prenant $f^*(X)=\psi(X) = \Esp(Y|X)$. Ce faisant, nous fournirons une interprétation géométrique particulièrement frappante de l'espérance conditionnelle: celle-ci peut-être vue comme la projection orthogonale de la variable $Y$ dans l'espace constitué des variables aléatoires de la forme $f(X)$ (cf. Figure [ci-dessous](#fig_proj)). Pour ce faire, il convient d'abord de réintroduire quelques notions relatives aux espaces de Hilbert, vues dans le cadre du cours de calcul intégral et nous permettant de définir la notion de projection orthogonale de manière univoque. En particulier, nous nous restreindrons à un espace de variables aléatoires sur lequel notre objectif de prediction, $\Esp((Y-f(X))^2)$, est bien défini: l'espace $L^2(\Omega)$ des variables aléatoires de carré intégrable. 

![Illustration géométrique de l'espérance conditionnelle](images/Proj.tex){#fig_proj}




## Rappels sur les espaces de Hilbert et application en probabilités



Pour commencer, revenons à la définition même des variables aléatoires. Soit $(\Omega, \mathcal{A},\P)$  un espace probabilisé (et donc mesuré). On rappelle que par définition, une variable aléatoire $Y$ sur cet espace n'est autre qu'une fonction $\mathcal{A}$-mesurable $Y : \Omega \rightarrow \R$. Adoptant ce point de vue, on considère alors l'espace fonctionnel  $L^2(\Omega)$ introduit dans le cours de calcul intégral. Pour rappel, cet espace contient l'ensemble des fonctions $\mathcal{A}$-mesurables (i.e. des variables aléatoires) $Y$ telles que $\vert Y\vert^2$ soit integrable c'est-à-dire telles que
$$
\Vert Y\Vert_2 = \bigg(\int_{\Omega} \vert Y(\omega)\vert^2 d\P(\omega)\bigg)^{1/2}=\mathbb{E}(Y^2)^{1/2} < \infty.
$$
En particulier, contrairement à l'espace $\mathcal{L}^2$ introduit au chapitre précédent, dans l'espace $L^2(\Omega)$ les fonctions égales $\P$-presque-partout sont confondues. C'est-à-dire que deux fonctions $X$ et $Y$ égales $\P$-presque-partout correspondent à un même élément de $L^2(\Omega)$ appelé classe d'équivalence. Ainsi, pour $X, Y \in L^2(\Omega)$, l'égalité $X=Y$ signifiera donc que $X$ et $Y$ sont dans la même classe d'équivalence, soit, en termes probabilistes, que les variables $X$ et $Y$ sont égales presque-sûrement.  

On a vu dans le cours de calcul intégral que l'espace $L^2(\Omega)$, muni de la norme $\Vert \cdot\Vert_2$, était un espace de Banach, c'est-à-dire un espace vectoriel normé et complet pour cette norme. Montrons que de plus, $L^2(\Omega)$ peut être considéré comme un espace de Hilbert, c'est-à-dire un espace vectoriel muni d'un produit scalaire et complet pour la norme associée à ce produit scalaire. Considérons à cet effet l'application bilinéaire $\langle \cdot \vert \cdot\rangle$ définie par
$$\langle X \vert Y\rangle = \int_{\Omega} X(\omega) Y(\omega) d\P(\omega) = \Esp(XY), \quad X,Y\in L^2(\Omega).$$
L'application $\langle \cdot \vert \cdot\rangle$  est bien définie puisque, d'après l'inégalité de Cauchy-Schwartz, on a pour tous $X,Y\in L^2(\Omega)$:
$$\langle X \vert Y\rangle^2=\Esp(XY)^2 \leq \Esp(X^2)\Esp(Y^2)=\Vert X\Vert_2^2\Vert Y\Vert_2^2<\infty.$$
De plus, l'application $\langle \cdot \vert \cdot\rangle$ définit un produit scalaire sur $L^2(\Omega)$ car elle vérifie les propriétés suivantes pour tous  $X,Y\in L^2(\Omega)$:

* Symétrique: $\langle X \vert Y\rangle= \Esp(XY)=\Esp(YX)=\langle X \vert Y\rangle$,
* Positive: $\langle X \vert X\rangle= \Esp(X^2) \ge 0$,
* Définie: $\langle X \vert X\rangle=0 \Leftrightarrow \Esp(X^2)=0 \Leftrightarrow X=0$ .

On remarque enfin que la norme associée au produit scalaire $\langle \cdot \vert \cdot\rangle$ n'est autre que la norme $\Vert\cdot\Vert_2$ introduite précédemment (car pour tout $X\in L^2(\Omega)$, $\langle X \vert X\rangle^{1/2}=\Esp(X^2)^{1/2}=\Vert X\Vert$). On en déduit donc que l'espace $L^2(\Omega)$ muni du produit scalaire $\langle \cdot \vert \cdot\rangle$ est bien un espace de Hilbert (car il est complet pour la norme $\Vert \cdot\Vert_2$).

L'intérêt de se ramener à travailler avec un espace de Hilbert est que sur de tels espaces, il est possible de définir de manière univoque la notion de projection orthogonale sur des sous-espaces. En effet, la projection orthogonale d'un élément $Y\in L^2(\Omega)$ sur un sous-espace convexe, fermé et non-vide $K \subset L^2(\Omega)$  est définie comme l'unique élément $P_K(Y)\in K$ qui minimise la distance $\Vert Y - P_K(Y)\Vert_2$, et donc l'erreur des moindres carrés $\Esp((Y-P_K(Y))^2)$ entre $Y$ et les éléments de $K$. On retrouve en particulier l'objectif de prédiction décrit plus haut, ce qui permet de conclure que la projection orthogonale $P_K(Y)$ est bien le prédicteur optimal $Y$ parmi les éléments de $K$. On en déduit la propriété suivante qui permet en pratique de caractériser ce prédicteur optimal d'après les propriétés de la projection orthogonale vues dans le cours de calcul intégral.


### Prédicteur optimal sur un convexe fermé {.proposition #identEC}
Soit $Y\in L^2(\Omega)$ et soit $K \subset L^2(\Omega)$ convexe, fermé et non-vide. Le prédicteur optimal, au sens des moindres carrés, de $Y$ sur $K$ est la projection orthogonale de $Y$ sur $K$. Il est donc caractérisé comme étant l'unique élément de $K$ vérifiant la propriété
$$ \langle Y - P_K(Y) \vert U - P_K(Y)\rangle \le 0 \quad  \forall U\in K.$$
Si de plus $K$ est un sous-espace vectoriel, cette caractérisation prend une forme plus simple, à savoir:
$$ \langle Y - P_K(Y) \vert U \rangle = 0 \quad  \forall U\in K.$$



Pour revenir à notre problème initial de prédiction optimale de $Y$ par une fonction de $X$, il suffit donc de choisir le sous-espace $K$ de projection de manière à ce qu'il ne contienne que des éléments s'exprimant comme des fonctions de $X$, et d'identifier parmi les éléments de $K$ celui qui satisfaisant la [propriété ci-dessus](#identEC). C'est ce que nous ferons dans les prochaines sous-sections.





## Cas particulier: la régression linéaire

Reprenons les variables $X,Y\in L^2(\Omega)$ introduites en début de section, et notre problème initial de prédiction de $Y$ à partir de $X$. On suppose en particulier et que les espérances, variances et la covariance de $X$ et $Y$ sont connues.  Dans cette sous-section, nous nous restreignons à des prédicteurs affines, c'est-à-dire que nous souhaitons trouver la meilleure approximation, au sens des moindres carrés, de $Y$ par une fonction affine de $X$ de la forme $f(X)=aX + b$. Un tel prédicteur est appelé *régression linéaire de $Y$ par $X$*, et peut être calculé à partir des résultats de la sous-section précédente. 

En effet, on remarque que tout prédicteur affine $f(X)=aX+b$ peut être vu comme une combinaison linéaire de deux variables aléatoires de $L^2(\Omega)$ : $X$, et la variable aléatoire égale à $1$ presque-sûrement, que l'on note également $1\in L^2(\Omega)$. Par conséquent, $f(X)\in K$ où $K$ désigne le sous-espace vectoriel de $L^2(\Omega)$ engendré par $X\in L^2(\Omega)$ et $1\in L^2(\Omega)$. Ainsi, trouver un prédicteur affine optimal de $Y$ revient à trouver un prédicteur optimal de $Y$ dans le sous-espace vectoriel $K$.

Le sous-espace $K$ étant un sous-espace vectoriel fermé de $L^2(\Omega)$ (car de dimension finie), on peut utiliser la [propriété de caractérisation](#identEC) du prédicteur optimal vu précédemment, et conclure que le prédicteur affine optimal de $Y$ par $X$ est la projection orthogonale $P_K(Y)$ de $Y$ sur $K$.  En particulier, puisque tout élément de $K$ est une combinaison linéaire de $X$ et $1$, on peut écrire que $P_K(Y) = a^*X + b^*  1$, où les coefficients $a^*,b^*$ vérifient:
$$ \langle Y - (a^*  X + b^*  1) \vert a  X + b  1 \rangle = 0 \quad  \forall a,b\in\R,$$
Cette égalité devant être vérifiée pour tous $a,b\in\R$, elle implique, par bilinéarité du produit scalaire, que les coefficients $a^*$ et $b^*$ soient solutions du système:
$$
\left\lbrace\begin{aligned}
   &\langle Y \vert X \rangle - a^*\langle X \vert X \rangle-b^*\langle 1 \vert X \rangle  = 0 \\
   &\langle Y \vert 1 \rangle - a^*\langle X \vert 1 \rangle-b^*\langle 1 \vert 1 \rangle = 0
\end{aligned}\right.
$$
Par définition du produit scalaire $\langle\cdot\vert\cdot\rangle$, ce système se réécrit sous la forme:
$$
\left\lbrace\begin{aligned}
   &\Esp(XY) = a^*\Esp(X^2)+b^*\Esp(X)   \\
   &\Esp(Y) = a^*\Esp(X)+b^* 
\end{aligned}\right.
$$
et a pour solution
$$\begin{aligned}
a^* & = \frac{\Esp(XY)-\Esp(X)\Esp(Y)}{\Esp(X^2)-\Esp(X)^2}=\frac{\cov(X,Y)}{\V(X)} = \rho(X,Y)\frac{\sigma_Y}{\sigma_X} \\
b^* & = \Esp(Y)  - a^*~\Esp(X)
\end{aligned}$$

En conclusion, le meilleur prédicteur affine, au sens des moindres carrés, de $Y$ par $X$  est la fonction $f^*(X)$ définie par
$$ f^*(X)=P_K(Y)=a^* X + b^*=\Esp(Y) + \rho(X,Y)\frac{\sigma_Y}{\sigma_X} (X -\Esp(X)),$$
et l'erreur quadratique moyenne associée à ce prédicteur vaut:
$$\begin{aligned}
\Esp\left(\left(Y - f^*(X)\right)^2\right) & = \ell(a^*,b^*)= \sigma_Y^2 + \rho^2(X,Y)\sigma^2_Y - 2\rho^2(X,Y)\sigma^2_Y\\
                        & = \sigma^2_Y(1-\rho^2(X,Y)).
\end{aligned}$$
On voit ainsi que cette erreur est proche de 0 lorsque $|\rho(X,Y)| \approx 1$ tandis qu'elle est proche de $\V(Y) = \sigma^2_Y$ lorsque $\rho(X,Y) \approx 0$. On notera au passage qu'on obtient que la meilleure approximation de $Y$ par une constante (ce qui revient à prendre $X=0$) est son espérance.

On vérifie aisément que les valeurs $a=a^*$ et $b=b^*$ minimise bien l'erreur $\ell(a,b)=\Esp((Y - (aX + b))^2)$ (cf. [Exercice](#detail) plus bas) et donc la meilleure approximation affine de $Y$ basée sur $X$ au sens des moindres carrés est la fonction $f^*(X)$ définie par
$$ f^*(X)=a^* X + b^*=\Esp(Y) + \rho(X,Y)\frac{\sigma_Y}{\sigma_X} (X -\Esp(X)).$$
L'erreur quadratique moyenne vaut alors
$$\begin{aligned}
\Esp\left(\left(Y - f^*(X)\right)^2\right) & = \ell(a^*,b^*)= \sigma_Y^2 + \rho^2(X,Y)\sigma^2_Y - 2\rho^2(X,Y)\sigma^2_Y\\
                        & = \sigma^2_Y(1-\rho^2(X,Y)).
\end{aligned}$$

On voit ainsi que cette erreur est proche de 0 lorsque $|\rho(X,Y)| \approx 1$ tandis qu'elle est proche de $\V(Y) = \sigma^2_Y$ lorsque $\rho(X,Y) \approx 0$. On notera au passage qu'on obtient que la meilleure approximation de $Y$ par une constante (ce qui revient à prendre $X=0$) est son espérance.

### Une deuxième approche {.exercise .question .one #detail}
Montrer que les coefficients $a^*$ et $b^*$ sont les uniques minimiseurs de l'erreur $\ell(a,b)=\Esp((Y - (aX + b))^2)$, pour $a,b\in\R$. 


### Limites de la régression linéaire {.remark}
L'hypothèse d'une relation linéaire est très forte et pas nécessairement toujours adaptée pour expliquer des relations de dépendances entre variables. Soit en effet une variable aléatoire réelle $X$ de $\L^3$ (i.e. $X^3$ est $\P_X$ intégrable) symétrique, c'est-à-dire telle que $X$ et $-X$ sont de même loi. On a alors $\Esp(X) = -\Esp(X) = 0$. Les variables $X$ et $X^2$ ne sont clairement pas indépendantes. Pour autant, on a $\cov(X,X^2) = \Esp(X^3) = -\Esp(X^3) = 0$ et le coefficient de régression $a^*$ est nul. 



## Cas général

Dans le paragraphe précédent, on s'est intéressé à approximer une variable aléatoire $Y\in L^2(\Omega)$ par une fonction affine d'une autre variable $X\in L^2(\Omega)$. On va montrer ici que si on généralise la recherche du prédicteur optimal à l'ensemble des fonctions de $X$ de carré intégrable, la solution est donnée précisément par l'espérance conditionnelle $\psi(X) = \Esp(Y|X)$.

En effet, considérons d'une part le sous-espace $L^2_X(\Omega)\subset L^2(\Omega)$ constitué des (classes d'équivalence) des variables aléatoires de la forme $f(X)$, avec $f : \R \rightarrow\R$ borélienne et telle que $f(X) \in L^2(\Omega)$. On remarque que $L^2_X(\Omega)$ est sous-espace vectoriel de $L^2(\Omega)$. On admettra par ailleurs que $L^2_X(\Omega)$ est fermé. Par conséquent, le prédicteur optimal de $Y$ dans $L^2_X(\Omega)$ n'est autre que la projection orthogonale de $Y$ sur $K=L^2_X(\Omega)$, et on peut une nouvelle fois appliquer la [propriété de caractérisation](#identEC) associée pour l'identifier.

D'autre part, on note que l'espérance conditionnelle $\psi(X) = \Esp(Y|X) \in L^2_X(\Omega)$ et que pour tout $f(X)\in L^2_X(\Omega)$,
$$ 
\begin{aligned}
  \langle Y - \psi(X) \vert f(X) \rangle =  \Esp\big((Y - \psi(X))f(X)\big)
&= \Esp\big(Yf(X)\big) - \Esp\big(\Esp(Y|X)f(X)\big) \\
&= \Esp\big(Yf(X)\big) - \Esp\big(\Esp(Yf(X)|X)\big) \\
&= \Esp\big(Yf(X)\big) - \Esp\big(Yf(X)\big)=0
\end{aligned}
$$
où la seconde égalité se déduit du fait que $f(X)$ est $\P$-intégrable, et la troisième égalité découle du théorème de l'espérance totale. Ainsi l'espérance conditionnelle vérifie la [propriété de caractérisation](#identEC) et par conséquent, par unicité de la projection orthogonale, on en déduit que $P_{L^2_X(\Omega)}(Y)=\psi(X)$. On peut donc conclure que, pour toutes variables aléatoires $X,Y\in L^2(\Omega)$, 

* l'espérance conditionnelle $\psi(X)=\Esp(Y|X)$ n'est autre que la projection orthogonale de $Y$ sur $L^2_X(\Omega)$,
* l'espérance conditionelle $\psi(X)=\Esp(Y|X)$ est le prédicteur optimal (au sens des moindres carrés) de $Y$ à partir d'une fonction de $X$. 

Il est alors immédiat que le "résidu" $Y-\Esp(Y|X)$ est non corrélé avec $X$ du fait de l'orthogonalité. On en déduit aussi la *formule de la variance totale* :
$$
\begin{aligned}
\V(Y) = \|Y - \Esp(Y)\|^2 &=  \|Y - \Esp(Y|X) + \Esp(Y|X) - \Esp(Y)\|^2 \\
                          &=  \|Y - \Esp(Y|X)\|^2 + \|\Esp(Y|X) - \Esp(Y)\|^2 \\
                          &=  \Esp((Y - \Esp(Y|X))^2) + \Esp((\Esp(Y|X) - \Esp(Y))^2)\\
                          &= \Esp(\Esp((Y - \Esp(Y|X))^2|X)) + \V(\Esp(Y|X))\\
                          &= \Esp(\V(Y|X)) + \V(\Esp(Y|X)).
\end{aligned}
$$
où on a utilisé la formule de l'espérance totale et introduit la variable aléatoire variance conditionnelle $\V(Y|X) = \Esp((Y - \Esp(Y|X))^2|X)$ comme cas particulier de la [définition vue plus haut](#defespcondg).

### Variance totale {.exercise .question .one #vartot}
Redémontrer ce résultat sans utiliser la notion d'orthogonalité.


Exercices
===============================================================================

## Couple de variables
Soient $X$ et $Y$ deux v.a. réelles. On suppose que la densité conditionnelle de $X$ sachant $Y = y$ est la densité $1_{\R_+}(x)y^2 xe^{-xy}$ et que la loi de $Y$
est de densité $\frac{1}{y^2} 1_{[1,+\infty[} (y)$.
On pose $T = XY$.

### Question 1 {.question #ex1-1} 
Trouver la loi du couple $(T,Y)$. Qu’en déduit-on ?

### Question 2 {.question #ex1-2} 
Trouver la loi conditionnelle de $Y$ sachant $X = x$.

### Question 3 {.question #ex1-3} 
Calculer $E(Y |X)$.


## Mélanges de lois 

*Adapté du cours de probabilités de S. Bonnabel et M. Schmidt (MINES ParisTech).*

Pour modéliser un phénomène multimodal, on utilise souvent des mélanges de gaussiennes. C'est le cas notamment en classification non-supervisée, où on fait l'hypothèse que chacune des classes suit une loi gaussienne. Soient $n\in\N^\ast$ et $K$ une variable aléatoire prenant les valeurs $1,\dots,n$ avec les probabilités non nulles $p_1,\dots,p_n$ telles que $\sum_{i = 1}^n p_i = 1$. Soient $X_1,\dots,X_n$ des variables aléatoires gaussiennes mutuellement indépendantes, d'espérances respectives $m_1,\dots,m_n \in \R$ et de variances respectives $\sigma_1^2,\dots,\sigma_n^2 \in\R_+^\ast$, toutes indépendantes de $K$. On appelle mélange de gaussiennes la loi de la variable aléatoire $X = X_K$. Pour tout $i\in\{1,\dots,n\}$, on notera $f_i$ la densité de la variable aléatoire $X_i$.

### Question 1 {.question #melloi1} 
Soit $i \in \{1,\dots,n\}$. Quelle est la densité $f_{X\mid K = i}$ de $X$ conditionnellement à l'événement $\{K = i\}$ ?

### Question 2 {.question #melloi2} 
Calculer la densité de probabilité de la variable $X$.

### Question 3 {.question #melloi3} 
Calculer $\Esp(X)$. Montrer que $\V(X) = \sum_{i = 1}^n p_i\sigma_i^2 + \bar{\sigma}^2$, où ce dernier terme peut être interprété comme la dispersion des espérances.

### Question 4 {.question #melloi4} 
Comment approximeriez-vous le mélange par une unique gaussienne ? Faire un schéma dans le cas $m = 2$.

## Lois conjuguées

Soit un vecteur aléatoire $(X,Y)$ de loi jointe $\P_{X,Y}$. Expliciter la loi conditionnelle de $Y$ sachant $\{X=x\}$ dans les situations suivantes, en prenant soin d'expliciter pour quelles valeurs de $x$ ces dernières ont du sens.

### Question 1 {.question #loiconj-expexp}

$Y$ suit une loi Exponentielle de paramètre $\lambda \in\R_+^\ast$ et pour tout $y\in\R_+^\ast$, la variable aléatoire $X$ sachant $\{Y=y\}$ suit une loi Exponentielle de paramètre $y$.

### Question 2 {.question #loiconj-gampoi}

$Y$ suit une loi Gamma de paramètres $\alpha,\theta \in \R_+^\ast$ et pour tout $y\in\R_+^\ast$, la variable aléatoire $X$ sachant $\{Y=y\}$ suit une loi de Poisson de paramètre $y$.

## Randomisation {.question #randomize}

*Extrait du cours de probabilités de S. Bonnabel et M. Schmidt (MINES ParisTech).*

Des clients arrivent à la boutique SNCF du boulevard Saint-Michel à des instants aléatoires. On note $T_0$ l'heure d'ouverture puis $T_1, T_2, \dots$ les temps successifs d'arrivée des clients jusqu'à l'heure de fermeture. Les études statistiques montrent qu'on peut, dans une tranche horaire donnée, supposer que les temps d'attente $X_1 = T_1 -T_0, X_2 = T_2 -T_1,\dots$ peuvent être modélisés par des variables aléatoires indépendantes et de même loi qu'une variable aléatoire positive $X$. Par ailleurs, une loterie interne décide que chaque jour dans la tranche horaire considérée, le $N^{\text{ème}}$ client sera l'heureux gagnant d'un trajet gratuit Paris-La Ciotat, où $N$ est une variable aléatoire bornée dont la loi dépend du processus de loterie (e.g. tous les clients entre le
premier et le $30^{\text{ème}}$ ont une chance $1/30$ d'être tirés au sort, en supposant qu'on est sûr d'avoir au moins $30$ clients dans la tranche horaire).

On se demande alors : quel est le temps d'attente moyen avant d'obtenir un gagnant ?

## Etats cachés --- indépendance conditionnelle 

Soucieux de l'évolution du potager de l'école, des élèves à la main verte s'intéressent à l'évolution de la température dans le jardin côté Luxembourg. Ils récupèrent pour cela un thermomètre dans un laboratoire, l'installent près du potager, et en relèvent les mesures à intervalles de temps réguliers. Les résultats les surprennent rapidement : les températures affichées ne correspondent pas à celles prévues par météo-France. Leur thermomètre est sans doute déréglé.

On se propose de les aider à comprendre le phénomène dont ils sont témoins à l'aide d'un modèle probabiliste particulier, nommé *modèle de Markov caché*. Précisément, on considère la suite des vraies températures que l'on aurait souhaité relever comme une suite de v.a.r. non indépendantes $(X_n)_{n\in\N^\ast}$, dite *d'états cachés* (on ne les observe pas directement). Les erreurs commises par le thermomètre sont quant à elles modélisées par une suite de v.a.r. $(\epsilon_n)_{n\in\N^\ast}$, toutes indépendantes et de même loi admettant une densité $f_\epsilon$. Elles sont supposées indépendantes de la suite $(X_n)_{n\in\N^\ast}$ (l'erreur du thermomètre lui est propre et ne dépend pas de la température réelle). A chaque instant $n\in\N^\ast$, on suppose que la mesure du thermomètre est la variable aléatoire $$Y_n = X_n + \epsilon_n,$$
et que le vecteur aléatoire $(X_1,\dots,X_n)$ possède une densité jointe notée $f_{1:n}$.

### Question 1 {.question #ec1}
Montrer que pour tout $n \in \N^\ast$ et tout $x\in\R$, la loi de $Y_n$ sachant $\{X_n = x\}$ admet une densité, que l'on explicitera.

### Question 2 {.question #ec2}
Montrer que les $n\in\N^\ast$ relevés de température $Y_1,\dots,Y_n$ sont indépendants **conditionnellement** aux états cachés $X_1,\dots,X_n$.


## Covariance totale {.question #covtot}

Soient $X$, $Y$ et $Z$ trois variables aléatoires réelles de carré intégrable. La covariance conditionnelle de $X$ et $Y$ sachant $Z$ est définie comme la variable aléatoire
$$\cov(X,Y \mid Z) = \Esp\Bigl( \bigl( X - \Esp(X\mid Z) \bigr)\bigl( Y - \Esp(Y\mid Z) \bigr) \Bigm| Z  \Bigr).$$

Etablir la formule de la covariance totale : $$\cov(X,Y) = \Esp\bigl(\cov(X,Y\mid Z)\bigr) + \cov\bigl( \Esp(X\mid Z), \Esp(Y\mid Z) \bigr).$$

## Non-réponse 
*Inspiré du cours de probabilité de M. Christine (ENSAE ParisTech).*

Un questionnaire est diffusé aux $n\in\N^\ast$ étudiants de l'école pour savoir combien de temps ils ont consacré à l'étude des probabilités ce semestre. On note $Y_i$ le temps de travail de l'étudiant $i \in \{1,\dots,n\}$ et $X_i$ la variable valant $1$ s'il a répondu au questionnaire et $0$ sinon. On suppose que les $(X_1,Y_1),\dots,(X_n,Y_n)$ sont des vecteurs aléatoires indépendants de même distribution qu'un vecteur générique $(X,Y)$ tel que

* $X$ est une variable de Bernoulli de paramètre $p\in\,]0,1[$ indiquant la probabilité de réponse,
* $Y$ est positive, de carré intégrable, d'espérance $m\in\R_+$ et de variance $\sigma^2 \in\R_+^\ast$.
Le coefficient de corrélation entre $X$ et $Y$ est enfin noté $\rho \in [-1,1]$.

### Question 1 {.question #nonrep1}
En reprenant la définition de l'espérance conditionnelle $\Esp(Y\mid X)$ comme meilleure approximation au sens des moindres carrés de $Y$ par une fonction de $X$, montrer qu'elle coïncide ici avec l'approximation affine de $Y$ par $X$ puis l'écrire en fonction de $m$, $\rho$, $\sigma$ et $p$.

### Question 2 {.question #nonrep2}
On pose $m_0 := \Esp(Y\mid X = 0)$ et $m_1 = \Esp(Y\mid X = 1)$. Calculer $m_0$ et $m_1$ en fonction de $m$, $\rho$, $\sigma$ et $p$.

### Question 3 {.question #nonrep3}
On pose $\sigma^2_0 := \V\left(Y\mid X = 0\right)$ et $\sigma^2_1 := \V\left(Y\mid X = 1\right)$. Vérifier l'égalité $$\sigma^2 = \dfrac{(1-p)\,\sigma^2_0 + p\,\sigma^2_1}{1-\rho^2}.$$

### Question 4 {.question #nonrep4}
Que dire des résultats obtenus aux questions 2 et 3 lorsque :

* $X$ et $Y$ sont non corrélées,
* $X$ et $Y$ sont indépendantes ?

-----------------------------------------------------------


Solutions
===============================================================================

### Dans un triangle (1) {.answer #answer-etb1} 

La densité marginale de $X$ est donnée par $f_X(x) = \int f_{X,Y}(x,y) dy = 1_{]0,1[}(x)$ et pour $x \in ]0,1[$,
$$f_{Y|X=x} (y) = \frac{1}{x} 1_{]0,x[}(y)$$
Ainsi $X$ est uniformément distribué sur $]0,1[$, et la loi de $Y$ sachant $X =x$ est uniforme sur $]0,x[$ pour $(0 < x < 1)$.

### Dans un triangle (2) {.answer #answer-etb2} 

Pour un tel $x$, l'espérance conditionnelle $\Esp(Y|X=x)$ vaut ainsi $x/2$ et nous obtenons $\Esp(Y|X) = \frac{X}{2}$.


### Auto-conditionnement {.answer #answer-autocond}
On a $\psi(y) = \Esp(Y|Y=y) = y$ et donc $\Esp(Y|Y) = \psi(Y) = Y$ p.s.

### Espérance conditionnelle d'un produit de variables {.answer #answer-prod}
On a $\Esp(XY|X = x) = x\Esp(Y|X=x)$, d'où $\Esp(XY|X) = X\Esp(Y|X)$ p.s.

### Une deuxième approche {.answer #answer-detail}

On remarque qu'on peut réécrire l'erreur comme
$$\ell(a,b)= \Esp(Y^2) -2a\Esp(XY) -2b \Esp(Y) +a^2\Esp(X^2) +2ab\Esp(X) +b^2.$$
Cette fonction est convexe et par conséquent admet un minimum global atteint au point $(a^*, b^*)\in\R^2$ qui annule les dérivées dérivées partielles de $\ell$ en $a$ et $b$. Ainsi, on a
$$\frac{\partial \ell(a^*,b^*)}{\partial b} = -2\Esp(Y^2) + 2a^* \Esp(X) + 2b^*=0$$
d'où $b^* = \Esp(Y) - a^* \Esp(X)$
Et, 
$$\begin{aligned}
\frac{\partial \ell(a^*,b^*)}{\partial a} & = -2\Esp(XY) + 2a \Esp(X^2) + 2b \Esp(X)\\
                                   & = -2\Esp(XY) + 2a \Esp(X^2) + 2\Esp(X)\Esp(Y) - 2 a^* \Esp(X^2)\\
                                   & = -2\cov(X,Y) + a^*\V(X)=0
\end{aligned}$$

d'où $a^* = \frac{\cov(X,Y)}{\V(X)} = \rho(X,Y)\frac{\sigma_Y}{\sigma_X}.$

### Variance totale {.answer #answer-vartot}
\begin{align*}
\V(Y) =& \Esp((Y-\Esp(Y))^2) = \Esp(\Esp((Y-\Esp(Y))^2|X)) \text{   par la formule de l'espérance totale}\\
=& \Esp(\Esp((Y-\Esp(Y|X)+\Esp(Y|X)-\Esp(Y))^2|X)) \\
=& \Esp(\Esp((Y-\Esp(Y|X))^2|X)) + \Esp(\Esp((\Esp(Y|X)-\Esp(Y))^2|X)) \\
 &+ 2\Esp(\Esp((Y-\Esp(Y|X))(\Esp(Y|X)-\Esp(Y))|X))\\
=& \Esp(\V(Y|X)) + \Esp((\Esp(Y|X)-\Esp(Y))^2) + 2\Esp((\Esp(Y|X)-\Esp(Y))\Esp((Y-\Esp(Y|X))|X))\\
=& \Esp(\V(Y|X)) + \V(\Esp(Y|X)) \text{   car    } \Esp((Y-\Esp(Y|X))|X) = 0 
\end{align*}

## Couple de variables

### Question 1 {.answer #answer-ex1-1} 
On voit d'abord que la densité du couple $(X,Y)$ vaut :
$$f_{X,Y}(x,y) = f_{X|Y=y}(x)f_Y(y) = xe^{-xy}1_{\R_+}(x) 1_{[1,+\infty[} (y)$$
Soit $h$ une fonction continue bornée sur $\R^2_+$. Le changement de variable $(x, y) \mapsto (t = xy , y)$ de jacobien $y$, donne alors que 
$$\Esp(h(T, Y )) = \Esp(h(XY, Y )) = \int_1^{+\infty}\int_0^{+\infty} h(t,y) e^{-t} \frac{t}{y^2} dt dy$$
et donc la densité du couple $(T, Y)$ vaut 
$$f_{T,Y} = e^{-t} \frac{t}{y^2}1_{[1,+\infty[} (y)1_{\R_+}(t)$$
Elle s’écrit comme produit d’une fonction de $t$ et d’une fonction de $y$. On en déduit que $T$ et $Y$ sont indépendantes et que $T$ a pour densité $te^{-t} 1_{\R_+}(t)$.

### Question 2 {.answer #answer-ex1-2} 
La loi marginale de $X$ a pour densité $f_X (x) = \int_1^{+\infty} x e^{-xy} dy = e^{-x}$. Ainsi $X$ suit une loi exponentielle de paramètre 1 et la loi conditionnelle de $Y$ sachant $X = x$ admet la densité :
$$f_{Y|X=x}(y) = \frac{f_{X,Y}(x,y)}{f_X(x)} = x e^{-x(y-1)} 1_{[1,+\infty[} (y)$$
pour x > 0.

### Question 3 {.answer #answer-ex1-3}
On en déduit que 
$$\Esp(Y|X=x ) = \int_1^{+\infty} y x e^{-x(y-1)} dy = \frac{x+1}{x}1_{\R_+}(x)$$
par intégration par parties. Ainsi $\Esp(Y|X) = \frac{X+1}{X}$.


## Mélanges de lois

### Question 1 {.answer #answer-melloi1}
Soit $B$ un borélien. Par indépendance de $K$ avec $X_i$, on a $$\P(X \in B \mid K = i) = \P(X_i \in B \mid K = i) = \P(X_i \in B).$$ La loi de $X$ sachant $\{K = i\}$ est donc la même que celle de $X_i$, d'où $$f_{X\mid K = i} : x\in\R \mapsto f_i(x) = \dfrac{1}{\sqrt{2\pi}\sigma_i}\,\exp\left\{- \dfrac{(x-m_i)^2}{2\sigma_i^2} \right\}.$$

### Question 2 {.answer #answer-melloi2}
Soit $B$ un borélien. D'après la formule des probabilités totales et la question précédente, on a $$\P(X\in B) = \sum_{i = 1}^n p_i\,\P(X \in B \mid K = i) = \sum_{i = 1}^n p_i\,\P(X_i \in B).$$ La variable aléatoire $X$ admet donc une densité, qui vaut
$$f_X : x\in\R \mapsto \sum_{i = 1}^n p_i\,f_i(x).$$

### Question 3 {.answer #answer-melloi3}
D'après la question précédente, $X$ a pour espérance
\begin{align*}
\Esp(X) &= \int_\R x\,f_X(x)\,dx = \int_\R x \sum_{i = 1}^n p_i\, f_i(x)\,dx =  \sum_{i = 1}^n p_i \int_\R x\,f_i(x)\,dx\\
& = \sum_{i = 1}^n p_i\,m_i.
\end{align*}
Quant à la variance de $X$, en utilisant l'égalité $\sum_{i= 1}^n p_i = 1$, elle vaut
\begin{align*}
\V(X) &= \Esp\left(X^2\right) - \Esp(X)^2 = \int_\R x^2\,f_X(x)\,dx - \left(\sum_{i = 1}^n p_i\,m_i\right)^2\\
&= \sum_{i = 1}^n p_i (\sigma_i^2 + m_i^2) - \sum_{i = 1}^n p_i\left(\sum_{j = 1}^n p_j\,m_j\right)^2\\
&= \sum_{i = 1}^n p_i\,\sigma_i^2 + \sum_{i = 1}^n p_i \left(m_i - \sum_{j=1}^n p_j\,m_j \right)^2.
\end{align*}
On retrouve bien la forme désirée, avec la dispersion des espérances
$$\bar{\sigma}^2 := \sum_{i = 1}^n p_i \left(m_i - \sum_{j=1}^n p_j\,m_j \right)^2.$$

### Question 4 {.answer #answer-melloi4}
Si l'on souhaite approcher la loi de $X$ avec une unique Gaussienne, et non un mélange, les questions précédentes suggèrent de prendre celle d'espérance $\sum_{i =1}^n p_i\,m_i$ et de variance $\sum_{i = 1}^n p_i\,\sigma^2_i + \bar{\sigma}^2$. Voir figure ci-dessous.

![Illustration](images/PdfMelGauss.tex)

## Lois conjuguées {.answer #answer-loiconj}

On considère dans tout cet exercice $B_1$ et $B_2$ des Boréliens.

### Question 1 {.answer #answer-loiconj-expexp}

D'après les hypothèses on a
\begin{align*}
\P_{X,Y}(B_1\times B_2) &= \int_{B_2} \left(\int_{B_1} d\P_{X\mid Y = y}(x) \right) d\P_Y(y) \hspace{1em}\text{par Fubini conditionnel,}\\
&= \int_{B_2} \left(\int_{B_1} y\,e^{-y x}\,1_{\R_+^\ast}(x)\,dx \right) \lambda\,e^{-\lambda y}\,1_{\R_+^\ast}(y)\,dy\\
&= \int_{B_1} \int_{B_2} \lambda\, y\,e^{-(x+\lambda)\,y}1_{\R_+^\ast}(x)\,1_{\R_+^\ast}(y) \,dy\, dx \hspace{1em}\text{par Fubini.}
\end{align*}
Le vecteur aléatoire $(X,Y)$ possède donc une densité jointe
$$f_{X,Y} : (x,y) \in\R^2 \mapsto \lambda\, y\,e^{-(x+\lambda)\,y}1_{\R_+^\ast}(x)\,1_{\R_+^\ast}(y).$$
La variable aléatoire $X$ a donc aussi une densité : pour tout $x\in\R$
\begin{align*}
f_X(x) &= \int_{\R} f_{X,Y}(x,y)\,dy = \int_\R \lambda\, y\,e^{-(x+\lambda)\,y}1_{\R_+^\ast}(x)\,1_{\R_+^\ast}(y)\,dy\\
&= \left|\begin{array}{ll}\displaystyle \dfrac{\lambda}{x+\lambda} \int_{0}^{+\infty} y\,(x+\lambda)\,e^{-(x+\lambda)\,y}\,dy & \text{si } x>0,\\[1em] 0 & \text{sinon.} \end{array}\right.
\end{align*}
On reconnaît dans cette dernière intégrale la formule de l'espérance d'une loi Exponentielle de paramètre $x+\lambda$, et on en déduit que pour tout $x\in\R$
$$f_X(x) = \dfrac{\lambda}{(x+\lambda)^2}\,1_{\R_+^\ast}(x).$$
Pour tout $x\in\R_+^\ast$ la variable $Y$ sachant $\{X=x\}$ admet donc aussi une densité, que l'on explicite avec la formule de Bayes : pour tout $y\in\R$
\begin{align*}
f_{Y\mid X=x}(y) &= \dfrac{f_{X,Y}(x,y)}{f_X(x)} = \dfrac{\lambda\, y\,e^{-(x+\lambda)\,y}\,1_{\R_+^\ast}(y)}{\dfrac{\lambda}{(x+\lambda)^2}}\\
&= (x+\lambda)^2\,y\,e^{-(x+\lambda)\,y}\,1_{\R_+\ast}(y).
\end{align*}
Comme $\Gamma(2) = 1$, on reconnaît ici la densité d'une loi Gamma d'indice $2$ et de paramètre d'échelle $x+\lambda$.

### Question 2 {.answer #answer-loiconj-gampoi}

D'après les hypothèses, en procédant comme précédemment, on a
\begin{align*}
\P_{X,Y}(B_1\times B_2) &= \int_{B_2} \left(\int_{B_1} d\P_{X\mid Y = y}(x) \right) d\P_Y(y)\\
&= \int_{B_2} \left(\sum_{x\in B_1} \dfrac{y^{x}}{x!}\,e^{-y}\,1_{\N}(x) \right) \dfrac{\theta^{\alpha}}{\Gamma(\alpha)}\,y^{\alpha-1}e^{-\theta y}\,1_{\R_+}(y)\,dy\\
&= \sum_{x\in B_1\cap\N} \left(\dfrac{1}{x!} \int_{B_2\cap\R_+} \dfrac{\theta^{\alpha}}{\Gamma(\alpha)}\,y^{x+\alpha-1}e^{-(\theta+1) y}\,dy\right)\\
&= \sum_{x\in B_1\cap\N} \biggl(\dfrac{\Gamma(x+\alpha)\,\theta^\alpha}{x!\,\Gamma(\alpha)\,(\theta+1)^{x+\alpha}}\\
&\hspace{5em} \times \int_{B_2\cap\R_+} \dfrac{(\theta+1)^{x+\alpha}}{\Gamma(x+\alpha)}\,y^{x+\alpha-1}e^{-(\theta+1) y}\,dy\biggr).
\end{align*}
On reconnaît dans cette dernière intégrale la densité d'une loi Gamma d'indice $x+\alpha$ et de paramètre d'échelle $\theta+1$, qui correspond exactement à la loi conditionnelle de $Y$ sachant $\{X=x\}$ pour $x\in\N$. En effet, on a d'une part
\begin{align*}
\P_X(B_1) &= \P_{X,Y}(B_1 \times \R) = \sum_{x\in B_1\cap\N} \dfrac{\theta^\alpha}{\Gamma(\alpha)}\, \dfrac{\Gamma(x+\alpha)}{x!\,(\theta+1)^{x+\alpha}},
\end{align*}
ce qui donne bien pour tout $x\in\N$ :
\begin{align*}
\P_{Y\mid X=x} (B_2) &= \P\left(Y \in B_2 \mid X = x\right) = \dfrac{\P_{X,Y}\left(\{x\}\times B_2\right)}{\P_X(\{x\})}\\
&= \int_{B_2\cap\R_+} \dfrac{(\theta+1)^{x+\alpha}}{\Gamma(x+\alpha)}\,y^{x+\alpha-1}\,e^{-(\theta+1)y}\,dy.
\end{align*}

## Randomisation {.answer #answer-randomize}

En termes probabilistes et selon les notations de l'exercice, il s'agit de calculer $\Esp(T_N - T_0)$, où la variable aléatoire $T_N$ peut s'écrire en fonction d'une somme aléatoire de variables aléatoires indépendantes : $$T_N = \sum_{i = 1}^N X_i + T_0.$$
Comme la boutique ferme au bout d'un certain temps, toutes les variables aléatoires figurant dans l'équation précédente sont bornées, donc intégrables. On peut ainsi calculer $\Esp(T_N-T_0)$ à l'aide de la formule de l'espérance totale : $$\Esp\left(T_N - T_0\right) = \Esp\left(\Esp\left(T_N \mid N\right)\right) - T_0.$$
Pour tout $n\in\N^\ast$ l'énoncé suggère que $N$ est indépendante de $X_1,\dots,X_n$, elles-mêmes indépendantes et de même loi que $X$, d'où :
$$\Esp\left(T_n \mid N = n\right) = \sum_{i = 1}^n \Esp(X_i\mid N = n) = \sum_{i = 1}^n \Esp(X_i) = n\Esp(X).$$
Ainsi, en posant $\psi : n \in\N^\ast \mapsto n \Esp(X)$, on obtient
$$\Esp\left(T_N - T_0\right) = \Esp\left(\psi(N)\right) - T_0 = \Esp(N)\Esp(X) - T_0.$$
C'était prévisible : en posant arbitrairement $T_0 = 0$, le temps d'attente moyen est le temps d'attente moyen entre deux arrivées, multiplié par le rang moyen du gagnant. Si la loterie dépendait des temps d'arrivées, par exemple en faisant gagner le premier client qui arrive au moins 10 minutes après le client précédent, $\psi$, et donc le résultat, seraient différents.

## Etats cachés --- indépendance conditionnelle 

### Question 1 {.answer #answer-ec1}
Soit $n\in\N^\ast$. Quels que soient $x\in\R$ et $B$ borélien on a
\begin{align*}
\P_{Y_n \mid X_n = x}(B) &= \Esp\left(1_B(X_n+\epsilon_n) \mid X_n = x \right)\\
&= \int_\R 1_B(x+y)\,d\P_{\epsilon_n\mid X_n = x}(y)\\
& = \int_\R 1_B(x+y)\,f_\epsilon(y)\,dy \hspace{1em}\text{par indépendance de $X_n$ et $\epsilon_n$}\\
&= \int_B f_\epsilon(y-x)\,dy.
\end{align*}
Ainsi, $\P_{Y_n\mid X_n =x}$ admet bien une densité : $$f_{Y_n\mid X_n=x} : y \in\R \mapsto f_\epsilon(y - x).$$

### Question 2 {.answer #answer-ec2}
Soient $n\in\N^\ast$, $(x_1,\dots,x_n)\in\R^n$ et $B_1,\dots,B_n$ des boréliens. Pour simplifier les écritures, on note $x_{1:n}$ tout vecteur $(x_1,\dots,x_n)$ de $\R^n$. Alors
\begin{align*}
&\P_{Y_{1:n}\mid X_{1:n}=x_{1:n}}(B_1\times\dots\times B_n)
=\Esp\left(\prod_{i = 1}^n 1_{B_i}(X_i + \epsilon_i) \Bigm\vert X_{1:n} = x_{1:n} \right)\\
&= \int_{\R^n} \prod_{i = 1}^n 1_{B_i}(x_i + y_i)\,d\P_{\epsilon_{1:n}\mid X_{1:n} = x_{1:n}}(y_{1:n})\\
&= \int_{\R^n} \prod_{i = 1}^n 1_{B_i}(x_i + y_i)\,d\P_{\epsilon_{1:n}}(y_{1:n}) \ \text{par indépendance des $\epsilon_i$ et $X_j$,}\\
&= \prod_{i = 1}^n \int_{\R} 1_{B_i}(x_i + y_i)\,f_\epsilon(x_i)\,dy_{i} \ \text{par Fubini et indépendance et même loi des $\epsilon_i$,}\\
&= \prod_{i = 1}^n \int_{\R} 1_{B_i}(y_i)\,f_\epsilon(y_i - x_i)\,dy_i\\
& = \prod_{i = 1}^n \int_{\R} 1_{B_i}(y_i)\,f_{Y_i\mid X_i = x_i}(y_i)\,dy_i\ \text{par la question 1,}\\
&= \prod_{i = 1}^n \P_{Y_i\mid X_i = x_i}(B_i).
\end{align*}
Les $n$ relevés de température sont donc bien indépendants conditionnellement aux états cachés.


## Covariance totale {.answer #answer-covtot}

Tout d'abord, par linéarité de l'espérance conditionnelle on a :
\begin{align*}
\cov(X,Y \mid Z) &= \Esp\Bigl( \bigl( X - \Esp(X\mid Z) \bigr)\bigl( Y - \Esp(Y\mid Z) \bigr) \Bigm| Z  \Bigr)\\
&= \Esp\Bigl( XY - X\Esp(Y\mid Z) - Y\Esp(X\mid Z) + \Esp(X\mid Z)\Esp(Y\mid Z) \Bigm| Z  \Bigr)\\
&= \Esp(XY \mid Z) - \Esp(X\mid Z)\Esp(Y\mid Z).
\end{align*}

En utilisant la formule de l'espérance totale et la linéarité de l'espérance, on obtient alors
\begin{align*}
\cov(X,Y) &= \Esp(XY) - \Esp(X)\Esp(Y)\\
&= \Esp\bigl( \Esp(XY \mid Z) \bigr) - \Esp\bigl( \Esp(X \mid Z) \bigr)\Esp\bigl( \Esp(Y \mid Z) \bigr)\\
&= \Esp\bigl( \Esp(XY \mid Z) - \Esp(X\mid Z)\Esp(Y\mid Z) \bigr)\\
&\ \ \  + \Esp\bigl( \Esp(X\mid Z)\Esp(Y\mid Z) \bigr) - \Esp\bigl( \Esp(X \mid Z) \bigr)\Esp\bigl( \Esp(Y \mid Z) \bigr)\\
&= \Esp\bigl(\cov(X,Y\mid Z)\bigr) + \cov\bigl( \Esp(X\mid Z), \Esp(Y\mid Z) \bigr).
\end{align*}

## Non-réponse 

### Question 1 {.answer #answer-nonrep1}
L'espérance conditionnelle de $Y$ sachant $X$ peut s'écrire comme la solution au problème de minimisation
$$\min_{\phi(X)\in L^2_X} \Esp\left(\left(Y-\phi(X)\right)^2\right).$$
Or pour $\phi(X)\in L^2_X$ on a ici
$$\Esp\left(\left(Y-\phi(X)\right)^2\right) = \Esp\left( \left(Y - \phi(1)\right)^2 1_{\{1\}}(X) \right) + \Esp\left( \left(Y - \phi(0)\right)^2 1_{\{0\}}(X) \right),$$
il suffit donc de résoudre pour tout $x\in\{0,1\}$
$$\min_{\lambda \in \R} \Esp\left(\left(Y-\lambda\right)^2 1_{\{x\}}(X)\right).$$
Soit $x\in\{0,1\}$ et posons $J_x : \lambda\in\R \mapsto \Esp\left(\left(Y-\lambda\right)^2 1_{\{x\}}(X)\right)$. Alors pour tout $\lambda\in\R$
$$J_x(\lambda) = \Esp\left(Y^21_{\{x\}}(X)\right) + \lambda^2\,\P(X=x) -2\lambda\,\Esp\left(Y1_{\{x\}}(X)\right)$$
et sa dérivée
$$J_x^\prime(\lambda) = 2\lambda\,\P(X=x) -2\,\Esp\left(Y1_{\{x\}}(X)\right)$$
s'annule en $$\lambda_x := \dfrac{\Esp\left(Y1_{\{x\}}(X)\right)}{\P(X=x)} = \Esp(Y\mid X = x).$$
On en conclut que $$\Esp(Y\mid X) = \Esp(Y\mid X = 1)1_{\{1\}}(X) + \Esp(Y\mid X = 0)1_{\{0\}}(X).$$
Or on remarque que $1_{\{1\}}(X) = X$ et $1_{\{0\}}(X) = 1 - X$, ce qui fait de $\Esp(Y\mid X)$ une fonction affine de $X$. Elle est par définition la meilleure approximation de $Y$ par une fonction de $X$, elle coïncide donc avec l'approximation affine de $Y$ par $X$:
$$\Esp(Y\mid X) = m + \dfrac{\rho\,\sigma}{\sqrt{p(1-p)}}\,(X - p).$$

### Question 2 {.answer #answer-nonrep2}
D'après la question précédente, on a $\Esp(Y\mid X) = m_0 + (m_1 - m_0) X$, la meilleure approximation affine de $Y$ par $X$. Ainsi, $m_0$ et $m_1$ satisfont
$$\left|\begin{array}{l} m_1 - m_0 = \dfrac{\rho\sigma}{\sqrt{p(1-p)}},\\[1em] m_0 = m - (m_1-m_0)p,  \end{array}\right. \Leftrightarrow \left|\begin{array}{l} m_1 = m + \rho\sigma\sqrt{\dfrac{1-p}{p}},\\[1em] m_0 = m - \rho\sigma\sqrt{\dfrac{p}{1-p}}.  \end{array}\right.$$

### Question 3 {.answer #answer-nonrep3}
Par la formule de la variance totale et d'après la question 1, on a
\begin{align*}
\sigma^2 &= \V\left(Y\right) = \Esp\bigl(\V\left(Y\mid X\right)\bigr) + \V\bigl(\Esp(Y\mid X)\bigr)\\
&= p\,\sigma^2_1 + (1-p)\,\sigma^2_0 + \dfrac{\rho^2\sigma^2}{p\,(1-p)}\V(X)\\
&= p\,\sigma^2_1 + (1-p)\,\sigma^2_0 + \rho^2\sigma^2.
\end{align*}
Cette égalité se simplifie et donne bien
$$\sigma^2 = \dfrac{(1-p)\,\sigma_0^2 + p\,\sigma_1^2}{1-\rho^2}.$$

### Question 4 {.answer #answer-nonrep4}
Lorsque $X$ et $Y$ sont non corrélées, i.e. $\rho = 0$, on obtient $m_0 = m_1 = m$ puis $\sigma^2 = (1-p)\,\sigma_0^2 + p\,\sigma_1^2$. En d'autres termes, $\Esp(Y\mid X) = m$ est une variable aléatoire constante, et $\Esp\bigl(\V(Y\mid X)\bigr) = \sigma^2$. Dans ce cas, la non-réponse n'affecte pas l'espérance, mais potentiellement la variance (la dispersion du temps de travail peut être différente chez les répondants et les non-répondants). Ces deux propriétés sont encore vraies en cas d'indépendance entre $X$ et $Y$, puisque l'indépendance implique la non corrélation, mais nous avons de plus $\V(Y\mid X) = \sigma^2 = \sigma^2_1 = \sigma^2_0$; la variable aléatoire $\V(Y\mid X)$ est elle aussi constante. Cette fois-ci, la dispersion est la même chez les répondants et les non-répondants : la non-réponse n'affecte pas la variance.


Références
===============================================================================
