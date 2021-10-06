% Probabilités II

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Z}{\mathbb{Z}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
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


#### Moments d'une variable aléatoire 

- \one connaître la définition de l'espérance d'une variable aléatoire à densité
- \one connaître l'interprétation de l'espérance
- \one connaître les propriétés de base de l'espérance
- \one connaître la définition de la variance d'une variable aléatoire à densité
- \one savoir que la variance est toujours positive
- \one savoir ce que signifie variable centrée-réduite
- \one connaître la définition de la covariance
- \one savoir que la covariance est une forme bilinéaire
- \one connaître et savoir manipuler l'inégalité de Cauchy-Schwarz
- \two connaître les conditions d'existence de l'espérance d'une fonction (mesurable) d'une variable aléatoire
- \two savoir exprimer la probabilité d'un événement de la forme $X \in A$ sous la forme d'une espérance
- \two connaître et savoir calculer les moments des lois usuelles

#### Vecteurs aléatoires

- \one savoir que les composantes d'un vecteur aléatoire sont des variables aléatoires définies sur le même espace de probabilité
- \one connaître la définition d'un vecteur aléatoire à densité
- \two connaître les conditions d'existence de l'espérance d'une fonction (mesurable) d'un vecteur aléatoire à densité
- \two savoir calculer les densités marginales d'un vecteur aléatoire à densité
- \two savoir qu'un couple de variables aléatoires à densité n'admet pas nécessairement de densité
- \one connaître la définition de l'espérance d'un vecteur aléatoire à densité
- \one connaître la définition de la matrice de covariance d'un vecteur aléatoire à densité
- \one savoir que la matrice de covariance est semi-définie positive

#### Variables et vecteurs aléatoires indépendantes

- \one connaître la définition de l'indépendance de deux vecteurs/variables aléatoires
- \one savoir caractériser l'indépendance de deux vecteurs/variables aléatoires à densité
- \two savoir que si $X$ et $Y$ sont indépendantes, alors $g(X)$ et $h(Y)$ sont aussi indépendantes
- \two savoir que si $X$ et $Y$ sont indépendantes et si $g(X)$ et $h(Y)$ sont intégrables alors $\Esp(g(X)g(Y)) = \Esp(g(X))\Esp(g(Y))$
- \one savoir que la covariance de deux variables indépendantes est nulle
- \two savoir que la réciproque est fausse et connaître un contre-exemple

#### Identification de densité

- \two savoir identifier la densité d'une fonction d'une variable aléatoire par la méthode de la fonction muette 
- \two savoir identifier la densité d'une fonction d'un vecteur aléatoire par la méthode de la fonction muette 

# Moments d'une variable aléatoire à densité
 
La loi de probabilité d'une variable aléatoire va nous permettre de calculer aisément des grandeurs caractéristiques telles que sa valeur moyenne et sa variance (lorsqu'elles existent). Elles sont définies ci-dessous.

### Espérance d'une variable aléatoire à densité {.definition #defesp}
La variable aléatoire $X : \Omega \to \R$ de densité $f$ est dite  *intégrable* si l'intégrale $\int_\R |x|f(x) dx$ est définie, autrement dit si le produit $x f(x)$ est intégrable. On définit alors son *espérance* par 
        $$\Esp(X) = \int_\R x f(x)dx$$


<!-- **note : pour introduire proprement l'espérance d'une variable aléatoire réelle, on a besoin de l'intégrale de Lebesgue -> CI 5** -->

### Interprétation {.remark} 
$\Esp(X)$ est un nombre réel qui donne une valeur moyenne résumant la variable aléatoire $X$.

L’espérance mathématique d’une variable aléatoire est un concept fondamental de la théorie des probabilités. La dénomination d’espérance pour cette quantité fait référence aux problèmes de jeux et d’espérance de gain. Cette terminologie imagée a été introduite par Pascal.

On note $\L^1$ l'ensemble de toutes les variables réelles $X$ à densité intégrables. Les propriétés suivantes découlent directement des propriétés de l'intégrale.

### Propriétés de base {.proposition #propl1}
 * $\L^1$ est un espace vectoriel et $\forall X,Y \in \L^1$, $\forall a,b \in \R$ 
        $$\Esp(aX + bY) = a\Esp(X) + b\Esp(Y).$$
 * $X \in \L^1 \Leftrightarrow |X| \in \L^1$, et dans ce cas $$|\Esp(X)| \leq \Esp(|X|).$$
 * Si $X \geq 0$ et $X \in \L^1$, alors $\Esp(X) \geq 0.$
 <!-- * Si $X,Y \in \L^1$ sont telles que $X \leq Y$, alors
        $$ \Esp(X) \leq \Esp(Y).$$
 * L'espérance d'une variable presque-sûrement constante est égale à cette constante :
 $$ \text{Si } \P(X(\omega) = a ) = 1, \text{ alors } \Esp(X) = a.$$ -->
 * Si $\exists b \in \R_+$ tel que $|X| \leq b$, alors $X \in \L^1$ et $\Esp(X) \leq b$.

### Rappel : cas discret {.remark}
Dans le cas d'une variable aléatoire discrète $Y$ à valeurs dans $\N^\ast$, son espérance est définie par la quantité $\Esp(Y) = \sum_{i\in\N^\ast} i\P(Y=i)$, pourvu que celle-ci soit finie. On voit immédiatement que les propriétés ci-dessus sont également vérifiées.

Outre l'espace $\L^1$, nous pouvons définir l'espace $\L^2$ des variables aléatoires réelles dont le carré $X^2$ est dans $\L^1$.

### Variance {.definition #defvar}
La variable aléatoire $X : \Omega \to \R$ de densité $f$ est dite *de carré intégrable* si $\Esp(X^2) = \int_\R x^2 f(x)dx$ est définie, autrement dit si le produit $x^2 f(x)$ est intégrable. Sa *variance* est définie par
        $$\V(X) = \Esp((X-\Esp(X))^2)$$


### Propriétés {.proposition #propl2}
$\L^2$ est un sous-espace vectoriel de $\L^1$, et si $X \in \L^2$,
$$|\Esp(X)| \leq \Esp(|X|) \leq \sqrt{\Esp(X^2)}$$


### Démonstration {.proof}
Soient $X$ et $Y$ deux variables aléatoires réelles de $\L^2$ et $a \in \R$. Comme $(aX+ Y)^2 \leq 2 a^2 X^2 + 2 Y^2$, alors $aX + Y \in \L^2$. Ainsi, $\L^2$ est un espace vectoriel.

L'inclusion $\L^2 \subset \L^1$ découle de $|X| \leq 1 + X^2$ et de la [proposition précédente](#propl1) (linéarité).

La première inégalité a déjà été vue [ci-dessus](#propl1). Pour la seconde, nous pouvons nous limiter au cas où $X$ est positive. Soit alors $a = \Esp(X)$ et $Y = X-a$. Par linéarité, on a 
        $$ \Esp(Y^2) = \Esp(X^2) - 2a \Esp(X) + a^2 = \Esp(X^2)-a^2.$$
Et $\Esp(Y^2) \geq 0$ par le troisième point de la [proposition ci-dessus](#propl1). Par conséquent, $\Esp(X)^2 = a^2 \leq \Esp(X^2)$ ce qui est le résultat recherché.

### Approximation par une constante {.exercise .question .one #exo-approx}

Soit $X$ une v.a. de carré intégrable. Montrer que $\Esp((X - a)^2 )$ atteint son minimum lorsque $a = \Esp(X)$.

### La variance est positive {.remark}
En vertu de cette [proposition](#propl2), $\V(X)$ est **positive** et sa racine carrée $\sigma_X$ s'appelle l'*écart-type* de $X$. L’écart-type est une grandeur qui mesure la moyenne (en un certain sens) de l’écart des valeurs de $X$ à sa moyenne, d’où son nom.

On a également 
        $$\V(X) = \Esp(X^2)-\Esp(X)^2$$
que l'on obtient en développant $(X-\Esp(X))^2$. Cette manipulation anodine est fort utile dans la pratique. On retiendra que "La variance est égale à la moyenne des carrés moins le carré de la moyenne". On désigne le terme $\Esp(X^2)$ par l'expression *moment d'ordre deux* tandis que la variance est parfois appelée *moment centré d'ordre deux*.

### Variable centrée réduite {.remark}
D'après ce qui précède, si $X$ est une variable aléatoire de carré intégrable, d'espérance $\Esp(X)$ et d'écart-type $\sigma_X >0$, alors la variable aléatoire $$\frac{X-\Esp(X)}{\sigma_X}$$
est d'espérance nulle et de variance 1. On dira qu'une telle variable aléatoire est *centrée et réduite*.

On peut remarquer que si $X$ et $Y$ sont dans $\L^2$, la variable aléatoire $XY$ est dans $\L^1$, puisque $|XY| \leq \frac{1}{2}(X^2+Y^2)$. On peut ainsi définir la *covariance* de deux variables aléatoires :

### Covariance {.definition #defcov}
Si $X$ et $Y$ sont dans $\L^2$, la variable aléatoire $(X-\Esp(X))(Y-\Esp(Y))$ est intégrable. On appelle la *covariance* de $X$ et $Y$ l'espérance de cette variable aléatoire et on la note :
        $$\cov (X,Y) = \Esp((X-\Esp(X))(Y-\Esp(Y))).$$
Le *coefficient de corrélation* des variables aléatoires $X$ et $Y$ est le nombre 
        $$\rho(X,Y) = \frac{\cov (X,Y)}{\sqrt{\V(X)}\sqrt{\V(Y)}}$$
qui est bien défini lorsque $\V(X)>0$ et $\V(Y)>0$.

### Calcul d'une covariance {.exercise .question .one #cov-unif}
Soit $U \sim \mathcal{U}_{[0,1]}$ et $V = 1-U$. Calculer $\cov(U,V)$ et $\rho(U,V)$.

### {.anonymous}

Du fait de la linéarité de l'espérance, on a 
$$\cov(X,Y) = \Esp(XY) - \Esp(X)\Esp(Y)$$
et d'ailleurs, on voit que la formule de calcul de la variance donnée plus haut est un cas particulier de cette formulation car $\V(X) = \cov(X,X)$. La linéarité de l'espérance nous donne encore pour $a,a',b,b' \in \R$
\begin{align*} 
\Esp((aX+b)(a'Y+b')) &= aa'\Esp(XY) + ab'\Esp(X) +a'b\Esp(Y) + bb'\\
\Esp(aX+b)\Esp(a'Y+b') &= aa'\Esp(X)\Esp(Y) + ab'\Esp(X) +a'b\Esp(Y) + bb'
\end{align*}
On en déduit que la covariance est une forme bilinéaire sur l'espace vectoriel des variables aléatoires de carré intégrable, et nous avons
$$\cov(aX+b,a'Y+b') = aa'\cov(X,Y)$$
En particulier, on a
$$ \V(aX) = a^2\V(X)$$
On en déduit que les coefficients de corrélation de $X$ et $Y$ et de $aX+b$ et $a'Y+b'$ sont égaux lorsque $aa' >0$.


### Inégalité de Cauchy-Schwarz {.proposition #CS}
Soit $X$ et $Y$ deux variables aléatoires de carré intégrable, alors on a *l'inégalité de Cauchy-Schwarz* :
        $$|\Esp(XY)| \leq \Esp(|XY|) \leq \sqrt{\Esp(X^2)\Esp(Y^2)}$$
avec égalité si et seulement si $X$ et $Y$ sont presque-sûrement proportionnelles.

### Démonstration {.proof}
La première inégalité a été démontrée plus haut. Pour la seconde, on a $\forall x \in \R$ d'après la linéarité de l'espérance :
$$x^2\Esp(X^2) + 2x\Esp(XY)+ \Esp(Y^2) = \Esp((xX+Y)^2) \geq 0.$$
Mais ceci n'est possible que si ce trinôme en $x$ n'a au plus qu'une seul racine réelle ; son discriminant 
        $$4\left((\Esp(XY))^2 - \Esp(X^2)\Esp(Y^2)\right)$$
doit donc être négatif ou nul ce qui donne le résultat.

Le discriminant est nul si et seulement si le trinôme admet une racine double $x_0$ et dans ce cas, $Y(\omega) = -x_0 X(\omega)$ pour presque tout $\omega$.

### Coefficient de corrélation {.exercise .question .one #CS-corr}
Montrer que le coefficient de corrélation de $X$ et $Y$ vérifie
$$-1\leq \rho(X,Y) \leq 1.$$

Enfin, il peut être intéressant de pouvoir calculer l'espérance d'une fonction mesurable d'une variable aléatoire réelle à densité qui est une variable aléatoire en vertu de la [proposition vue de composition](Probabilité I.pdf #composition).

### Espérance de $g(X)$ {.proposition #esperanceg}
Soit $X$ une variable aléatoire réelle admettant la densité $f$, et $g$ une fonction mesurable de $\R$ dans $\R$. Alors $g(X)$ est intégrable si et seulement si l'intégrale
$$\int_\R |g(x)|f(x) dx,$$
est définie et dans ce cas
$$\Esp(g(X)) = \int_\R g(x)f(x) dx.$$

Nous n'avons pas tous les éléments permettant de démontrer ce résultat, mais l'argument heuristique suivant permet de comprendre pourquoi il est vrai : supposons $g$ continue telle que $|g|f$ soit intégrable. Alors il existe une jauge $\gamma(t)$, sur $[-\infty, +\infty]$ telle que, si la subdivision pointée (totale ou partielle) $\mathcal{D} =\{(t_i, I_i)\}_i$ est subordonnée à $\gamma$, on a
$$
S(gf, \mathcal{D}) = \left|S(gf, \mathcal{D}) - \int _\R g(x)f(x) dx \right| 
\leq 
\varepsilon.
$$ 
Posons $X_n = t_i$ si $X \in I_i$, pour $i \in \{0,\ldots,n-1\}$. Ainsi, pour tout $\omega$, $X_n(\omega) \xrightarrow[n \to \infty]{} X(\omega)$ et par continuité de $g$, on a $g(X_n) \xrightarrow[n \to \infty]{} g(X)$. Comme $X_n$ est une variable aléatoire discrète, on a
$$\Esp(g(X_n)) = \sum_{i=0}^{n-1}g(t_i)\P(X\in I_i)l(I_i) \approx \sum_{i=0}^{n-1}g(t_i)f(t_i).$$

### Cas particulier {.remark}
L'espérance et la variance sont des cas particulier de ce résultat. On a de plus pour $A \in \B(\R)$ :
$$\Esp(1_A(X)) = \int_A f(x)dx = \P(X\in A)$$

## Exemples

Nous donnons ici quelques exemples de densités de probabilité. Nous reprenons en particulier les [trois exemples de densités donnés au premier cours](Probabilité I.pdf #exampledens) :

### *Loi uniforme*

sur $[a,b]$, où $a < b$ et on note $X \sim \mathcal{U}_{[a,b]}$ si $X$ est de densité
    $$ f(x) = \frac{1}{b-a} 1_{[a,b]} (x).$$

### Moments d'une variable aléatoire de loi uniforme sur $[a,b]$ {.exercise .question .one #moments-unif}   

Soit $X \sim \mathcal{U}_{[a,b]}$. Montrer que son espérance vaut
        $$ \Esp(X) = \int_a^b \frac{x}{b-a} dx = \frac{a+b}{2}$$
et que sa variance vaut
        $$ \V(X) = \Esp(X^2) - \Esp(X)^2 = \frac{(b-a)^2}{12}.$$

### *Loi exponentielle*

de paramètre $\theta > 0$ et on note $X \sim \mathcal{E}(\theta)$ si $X$ est de densité
        $$ f(x) = \theta e^{-\theta x} 1_{\{x>0\}} (x).$$

### Moments d'une v.a. exponentielle {.exercise .question .one #moments-expo}    

Montrer que son espérance et sa variance valent
        $$ \Esp(X) = \frac{1}{\theta} \text{ et } \V(X) = \frac{1}{\theta^2}$$

### *Loi gamma*

On rappelle tout d'abord que la fonction gamma est définie pour $\alpha \in \left] 0, + \infty \right[$ par 
        $$\Gamma(\alpha) = \int_0^{+\infty} x^{\alpha-1}e^{-x} dx.$$
En intégrant par partie, on obtient la relation $\Gamma(\alpha+1) = \alpha \Gamma(\alpha)$, et on a $\Gamma(1) = 1$. On en déduit que $\Gamma(n) = (n-1)!$.

Une variable aléatoire $X$ suit une loi gamma de paramètre d'échelle $\theta$ et d'indice $\alpha$ et on note $X \sim \Gamma(\alpha,\theta)$, si sa loi admet la densité
        $$f(x) = \frac{1}{\Gamma(\alpha)}\theta^\alpha x^{\alpha -1} e^{-\theta x}.$$

### Moments d'une v.a. de loi gamma {.exercise .question .one #moments-gamma}    

Soit $X\sim \Gamma(\alpha,\theta)$. Montrer que son espérance et sa variance valent :

$$ \Esp(X) = \frac{\alpha}{\theta} \text{ et } \V(X) = \frac{\alpha}{\theta^2}.$$

On remarquera que $\Gamma(1,\theta)$ est la loi exponentielle de paramètre $\theta$. 

Lorsque $\alpha$ est entier, la loi gamma permet de modéliser le temps d'attente avant la $n$-ième occurence d'événements indépendants de loi exponentielle de paramètre $\theta$.

### *Loi normale*

de paramètres $\mu$ et $\sigma^2$ et on note $X \sim \mathcal{N}(\mu,\sigma^2)$ si $X$ est de densité
        $$f(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$
Son espérance et sa variance valent
        $$\Esp(X) =  \mu \text{ et } \V(X) = \sigma^2$$

### Moments d'une v.a. gaussienne {.exercise .question .one #moments-gauss}

Après avoir vérifié que $f$ est bien une densité, calculer l'espérance et la variance de $X \sim \mathcal{N}(\mu,\sigma^2)$


### Estimation statistique {.remark}
Dans les exemples ci-dessus, on peut remarquer que les densités sont paramétrées par des nombres réels qui sont liés directement aux valeurs de l’espérance et de la variance de la variable. C’est très utile en statistique où l'on cherchera à estimer la valeur de ces paramètres à partir des observations disponibles. Dans le cas de la loi normale, la moyenne et la variance (empiriques) des échantillons fourniront ainsi directement des estimateurs des paramètres.

Il existe des variables aléatoires qui n’ont pas d’espérance, comme le montre l'exercice suivant.

### *Loi de Cauchy* {.exercise .question .two #exo-cauchy}

Un gyrophare envoie un flash lumineux dans une direction aléatoire uniforme d’angle $\theta$. On cherche la distribution de l'abscisse $X$ du point d'impact du rayon lumineux sur un écran plan infini situé à distance 1 du gyrophare. Donner la densité de $X$. Calculer son espérance.

# Vecteurs aléatoires à densité
Nous allons généraliser ici la notion de variable aléatoire en considérant qu'elle peut prendre ses valeurs dans $\R^n$. Les vecteurs aléatoires se rencontrent naturellement lorsqu'on s'intéresse à plusieurs quantités conjointement, par exemple dans le cas de la météo, la température, la pluviométrie et la vitesse et la direction du vent.

## Définitions

Une variable aléatoire $X$ à valeurs dans $\R^n$ (ou vecteur aléatoire) est simplement une collection de $n$ variables réelles définies sur le même espace probabilisé $(\Omega, \A, \P)$, qui sont les *composantes* de $X$. On écrit $X = (X_1,\ldots,X_n)$.

De même qu'en dimension 1, la loi de $X$ est caractérisée par la fonction de répartition multi-dimensionnelle $F : \R^n \to \R$ définie par 
$$F(x_1,\ldots,x_n) = \P_X(X_1\leq x_1,\ldots,X_n\leq x_n)$$
Mais caractériser les fonctions de répartition sur $\R^n$ est délicat, de sorte que cette notion est rarement utilisée. Nous allons plus particulièrement nous intéresser aux vecteurs aléatoires à densité.

### Vecteur aléatoire à densité {.definition #defvect}
On dit que $X$ admet la densité $f$ si la fonction réelle $f$ sur $\R^n$ est positive, intégrable et vérifie 
$$\int_{\R^n} f(x) dx = \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} f(x_1,\ldots,x_n) dx_1 \ldots dx_n= 1$$
et si
$$\P_X(X_1\leq x_1,\ldots,X_n\leq x_n) = \int_{-\infty}^{x_1} \ldots \int_{-\infty}^{x_n} f(x_1,\ldots,x_n) dx_1 \ldots dx_n.$$

De la même manière que dans le [cas unidimensionnel](#esperanceg), on a :

### Fonction d'un vecteur aléatoire {.proposition #esperancegvect}
Soit $X$ un vecteur aléatoire de densité $f$, et soit $g$ une fonction de $\R^n$ dans $\R$, mesurable. On a alors $g(X)\in \L^1$ si et seulement si 
$$\int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} |g(x_1,\ldots,x_n)|f(x_1,\ldots,x_n) dx_1 \ldots dx_n,$$
est définie et dans ce cas, on a 
$$\Esp(g(X)) = \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} g(x_1,\ldots,x_n)f(x_1,\ldots,x_n) dx_1 \ldots dx_n.$$

Pour revenir à la densité d'une composante d'un vecteur aléatoire, on intègre par rapport aux autres variables. On le présente ici dans le cas d'un couple $Z=(X,Y)$ de variables aléatoires. On généralise aisément à une dimension supérieure.

### Densités marginales {.proposition #loimarg}
Supposons que $Z$ admette une densité $f$. Alors $X$ et $Y$ admettent les densités $f_X$ et $f_Y$ données par
$$f_X(x) = \int_\R f(x,y) dy,\,\,\, f_Y(y) = \int_\R f(x,y) dx.$$

Les fonctions $f_X$ et $f_Y$ s'appellent les *densités marginales* de $f$.

### Démonstration {.prooof}
Pour tout $x \in \R$, on a par définition
$$ \P(X \leq x) = \P(Z \in ]-\infty,x] \times \R) = \Esp(1_{]-\infty,x] \times \R}(Z)) = \int_{-\infty}^x du \left(\int_\R f(u,v) dv\right),$$
où l'on a utilisé le [théorème de Fubini](Calcul Intégral III.pdf #Fubini) pour $1_{]-\infty,x] \times \R}(u,v)f(u,v)$ intégrable.
Donc si $f_X$ est définie par $f_X(x) = \int_\R f(x,y) dy$, on obtient que $\P(X \leq x) = \int_{-\infty}^x f_X(u) du$, ce qui montre que $f_X$ est la densité de $X$. Le raisonnement est analogue pour $Y$.

### Réciproque ? {.remark}
La réciproque de cette proposition est fausse en revanche : les variables aléatoires $X$ et $Y$ peuvent avoir des densités sans que le couple $Z = (X, Y )$ en ait une.

Supposons par exemple que $X = Y$. Si $\Delta = \{(x,x) ; x\in \R\}$ est la diagonale de $\R^2$, nous avons évidemment $\P_Z(\Delta) = 1$ mais si la [proposition précédente](#esperancegvect) était valide pour $\P_Z$, on aurait $\P_Z(\Delta) = \Esp(1_\Delta) = \int_{\R^2} 1_\Delta f_Z(z)dz = 0$ car $\Delta$ est de volume nul dans $\R^2$.

En particulier, il faut faire attention au fait que dans le cas général, la densité d'un couple de variables aléatoires n'est pas le produit des densités.

### Lancer de fléchette {.exercise .question .two #exo-flechette}
On lance une fléchette sur une cible circulaire de rayon unité. Le joueur est suffisamment maladroit pour que le point $M$ d’impact de la fléchette
soit supposé uniformément distribué sur la cible (On décide de n’observer que les lancés qui atteignent la cible). Exprimer la densité du couple formé par les coordonnées cartésiennes $(X,Y)$ de $M$ puis leurs densités marginales.


## Moments d'un vecteur aléatoire

### Vecteur espérance et covariance  {.definition}
Si les composantes $X_i$ du vecteur aléatoire $X = (X_1,\ldots,X_n)$ sont intégrables, on peut définir le *vecteur espérance* 
        $$\Esp(X) = (\Esp(X_1),\ldots,\Esp(X_n))$$
Si les composantes $X_i$ du vecteur aléatoire $X = (X_1,\ldots,X_n)$ sont de carré intégrable, la *matrice de covariance* de $X$ est la matrice $C_X = (c_{i,j})_{1 \leq i \leq n , 1 \leq j \leq n}$ de taille $n \times n$ et dont les éléments valent
        $$c_{i,j} = \cov (X_i,X_j)$$

### Matrice de covariance {.proposition}
La matrice de covariance est symétrique non-négative (ou encore semi-définie positive).

### Démonstration {.proof}
La symétrie est évidente. Non-négative signifie que pour tous réels $a_1,\ldots,a_n$, on a $\sum_{i=1}^n \sum_{j=1}^n a_i a_j c_{i,j} \geq 0$. Un calcul simple montre que
$$ \sum_{i=1}^n \sum_{j=1}^n a_i a_j c_{i,j} = \V(\sum_{i=1}^n a_i X_i) \geq 0.$$

### Vecteur Gaussien $n$-dimensionel {.example}
Un exemple important de vecteurs aléatoires est celui des vecteurs gaussiens, que nous étudierons plus en détail au chapitre suivant. Soient $m \in \R^n$ et $C$ une matrice symétrique définie positive (c'est-à-dire telle que pour tout $x \in \R^n$ non identiquement nul $x^tCx > 0$ où $^t$ désigne la transposée). Le vecteur $X \in \R^n$ est un vecteur aléatoire gaussien d’espérance $m$ et de matrice de covariance $C$ si sa densité s’écrit
$$ f(x) = \frac{1}{(2\pi)^{n/2}\sqrt{\det (C)}}\exp (-\frac{1}{2}(x-m)^tC^{-1}(x-m)) $$
On a alors $\Esp(X) = m$ et $C_X =C$.

![Densité de probabilité de la loi normale bivariée centrée, réduite, de coefficient de corrélation 1/2](images/PdfGauss3D.tex)

# Variables aléatoires indépendantes
Lorsqu'on modélise plusieurs variables conjointement, une hypothèse importante est celle de l'indépendance. Ce caractère traduit l'absence de lien de causalité entre les variables. Par exemple, on fait naturellement l'hypothèse d'indépendance lorsque l'on considère une répétition d'une même expérience dans les mêmes conditions.

Dans ce paragraphe, on considère un couple $(X,Y)$ de vecteurs aléatoires respectivement à valeurs dans $\R^m$ et $\R^n$. Les résultats s'étendent sans peine à une famille finie quelconque. 

On peut se ramener aux évènements pour caractériser l'indépendance de deux vecteurs aléatoires. En effet, considérons le vecteur aléatoire $Z = (X,Y)$, $A$ et $B$ deux ensembles dans $\B({\R^m})$ et $\B({\R^n})$. On a vu que les évènements $X\in A$ et $Y \in B$ sont indépendants si et seulement si $\P_Z(X \in A, Y \in B) = \P(X^{-1}(A) \cap Y^{-1}(B)) = \P(X^{-1}(A))\P(Y^{-1}(B)) = \P_X(X \in A)\P_Y(Y \in B)$. Pour que deux vecteurs aléatoires soient indépendants, on va donc demander que ceci soit valable quels que soient $A$ et $B$.

### Vecteurs aléatoires indépendants {.definition #defvai}
Les vecteurs aléatoires $X$ et $Y$ sont *indépendants* si pour tous ensembles $A$ et $B$ des tribus correspondantes, 
$$\P(X \in A, Y \in B) = \P(X \in A)\P(Y \in B)$$

Cette définition se traduit en termes de densités dans la proposition suivante que l'on énonce sans perte de généralité pour un couple de variables aléatoires.

### Caractérisation de l'indépendance {.proposition}
Soient $X$ et $Y$ deux variables aléatoires réelles de densités $f_X$ et $f_Y$. $X$ et $Y$ sont indépendantes si et seulement si 
le couple $Z = (X,Y)$ a pour densité (sur $\R^2$) :
$$f_Z(x,y) = f_X(x)f_Y(y).$$

### Démonstration {.proof}
S'il y a indépendance, la [définition](#defvai) implique 
$$P(X\leq x, Y\leq y) = P(X\leq x) \P(Y\leq y) = \int_{-\infty}^x f_X(u) du \int_{-\infty}^y f_Y(v) dv$$
ce qui montre que $\P_Z$ vérifie la [définition d'un vecteur aléatoire à densité](#defvect) avec $f_Z=f_X f_Y$.

Inversement, si $f_Z=f_X f_Y$, on a pour tous $A$, $B$ de $\B({\R})$
$$\P(X\in A, Y\in B) = \int_A \int_B f_X(x) f_Y(y) dxdy = \P(X \in A)\P(Y \in B)$$ 
où on a utilisé le [théorème de Fubini](Calcul Intégral III.pdf #Fubini).


### Lancer de fléchette (suite) {.exercise .question .one #exo-flechettebis}
Les coordonnées cartésiennes $(X,Y)$ de $M$ sont elles indépendantes ? 


### {.anonymous}

Considérons maintenant deux fonctions $g$ et $h$ définies sur $\R^m$ et $\R^n$ telles que $g(X)$ et $h(Y)$ soient aussi des variables aléatoires. 

### Fonctions de vecteurs aléatoires indépendants {.proposition #indep_fct}
Avec les notations précédentes, si $X$ et $Y$ sont indépendantes de densités respectives $f_X$ et $f_Y$, les variables aléatoires $g(X)$ et $h(Y)$ sont aussi indépendantes. Si de plus $g(X)$ et $h(Y)$ sont intégrables, alors le produit $g(X)h(Y)$ est aussi intégrable, et on a 
$$ \Esp(g(X)h(Y)) = \Esp(g(X))\Esp(h(Y))$$ 

### Démonstration {.proof}
La première assertion est évidente par définition de l'indépendance. Par ailleurs, si $g(X)$ et $h(Y)$ sont intégrables, en notant $f_{(X,Y)}$ la densité du couple $(X,Y)$, et en utilisant le [théorème de Fubini](Calcul Intégral III.pdf #Fubini), on a
\begin{align*}
\Esp(g(X)h(Y))  & = \int_{\R^{m+n}} g(x)h(y) f_{(X,Y)}(x,y) dx dy \\
                & = \int_{\R^m} \int_{\R^n} g(x)h(y)f_X(x) f_Y(y) dx dy \\
                & = \left(\int_{\R^m}  g(x) f_X(x) dx \right) \left(\int_{\R^n} h(y) f_Y(y) dy\right)\\
                & = \Esp(g(X))\Esp(h(Y))
\end{align*}

### Cas général {.remark}
Ce résultat est encore valable $X$ et $Y$ dans le cas général (sans densité), voir @Jacod pour une démonstration.

On déduit de ce résultat et de la [définition de la covariance](#defcov) que :

### Covariance de variables aléatoires indépendantes {.corollary}
Si les variables aléatoires réelles $X$ et $Y$ sont indépendantes et de carré intégrable, alors
$\cov(X,Y) = 0$ et $\rho(X,Y) = 0$.

### Démonstration {.exercise .question .one #demo-cov-indep}
Démontrer ce résultat.

### Remarque
Attention, la réciproque est fausse. Par exemple, si $X \sim \mathcal{U}_{[-1,1]}$ et $Y = X^2$. $X$ et $Y$ ne sont clairement pas indépendantes mais on a

$$\cov(X,Y) = \cov(X,X^2) = \Esp(X^3) - \Esp(X)\Esp(X^2) = 0$$

# Identification de densité

Un problème important est le suivant. Soit $X$ une variable aléatoire réelle, admettant la densité $f_X$. Soit $g$ une fonction mesurable, de sorte que $Y = g(X)$ soit aussi une variable aléatoire. Est-ce que $Y$ admet une densité, et si oui, comment la calculer ?

On peut déjà remarquer que cette densité n’existe pas toujours. Si par exemple $g(x) = a$ pour tout $x$, la loi de $Y$ est la masse de Dirac en $a$, qui n’a pas de densité.

Pour résoudre ce problème, l’idée consiste à essayer de mettre $E(h(Y )) = E(h \circ g(X))$ sous la forme $\int h(y)f_Y (y)dy$ pour une fonction convenable 
$f_Y$, et une classe de fonctions $h$ suffisamment grande. La fonction $f_Y$ sera alors la densité cherchée.

La [proposition qui assure que $g(X)$ est intégrable pour une variable aléatoire réelle $X$](#esperanceg) implique
$$ \Esp(h(Y)) = \Esp(h \circ g (X)) = \int_{\R} h \circ g(x) f_X(x) dx$$

et on fait le changement de variable $y = g(x)$ dans cette intégrale. Cela nécessite que $g$ soit dérivable et bijective “par morceaux”, et il faut faire très attention aux domaines où $g$ est croissante ou décroissante. Puisque la fonction $h$ est arbitraire, on appelle couramment cette technique la *méthode de la fonction muette*. Cette approche résulte en fait de la proposition suivante que nous ne démontrerons pas :

### Méthode de la fonction muette {.proposition}
Si il existe une fonction $f$ telle que pour toute fonction mesurable $h$ telle que $h(x) f(x)$ soit  intégrable, 
$$\Esp(h(X)) = \int_\R h(x) f(x) dx$$
alors la loi de $X$ admet la densité $f$.

### Démonstration {.proof}
L’idée de la preuve repose sur le fait que parmi ces fonctions se trouvent les $h = 1_{]-\infty,y]}$, pour laquelle la formule précédente donne la fonction de répartition de $f$.
Pour une démonstration complète, voir @Jacod.

### {.post}

Nous donnons ici quelques exemples d'application de cette méthode :

 * Soit $Y = aX + b$, où $a$ et $b$ sont des constantes. Si $a=0$, alors $Y = b$ et la loi de $Y$ est la masse de Dirac en $b$ (sans densité). Si $a \neq 0$, on fait le changement de variable $y = ax+b$, ce qui donne
        $$ \Esp(h(Y)) = \int_\R h(ax+b) f_X(x) dx = \int_\R h(y) f_X(\frac{y-b}{a})\frac{1}{|a|} dy $$
 Donc 
        $$ f_Y(y) = f_X(\frac{y-b}{a})\frac{1}{|a|} $$
 * Soit $Y =X^2$. La fonction $g$ est décroissante sur $\R_-$ et croissante sur $\R_+$. Le changement de variable $y = x^2$ donne alors
        \begin{align*}
        \Esp(h(Y)) &= \int_{-\infty}^0 h(x^2) f_X(x) dx + \int_0^{+\infty} h(x^2) f_X(x) dx\\
                   &= \int_0^{+\infty} h(y) f_X(-\sqrt{y})\frac{1}{2\sqrt{y}} dy + \int_0^{+\infty} h(y) f_X(\sqrt{y})\frac{1}{2\sqrt{y}}dy
        \end{align*}
   et on en déduit
        $$f_Y(y) = (f_X(-\sqrt{y})+f_X(\sqrt{y}))\frac{1}{2\sqrt{y}}1_{\left]0,+\infty\right[}$$

### Conséquences {.remark}

Dans le cas des vecteurs aléatoires, l'idée est la même. Soit $X = (X_1,\ldots,X_n)$, un vecteur aléatoire de densité $f_X$ sur $\R^n$, $g$ une fonction de $\R^n$ dans $\R^m$ et $Y = g(X)$. Plusieurs cas sont à considérer :

 1. $m > n$, le vecteur $Y$ n'admet pas de densité.
 2. $m=n$, on utilise comme dans le cas unidimensionel le changement de variable $y = g(x)$ dans 
        $$ \Esp(h(Y)) = \Esp(h \circ g (X)) = \int_{\R^n} h \circ g(x) f_X(x) dx $$
    Supposons d'abord que $g$ soit une bijection continûment différentiable de $A$ dans $B$, ouverts de $\R^n$. Sous l'hypothèse que $h \circ g(x) f_X(x)$ soit  intégrable, le [théorème de changement de variable](Calcul Intégral III.pdf) nous assure :
        $$ \int_A h\circ g (x) f_X(x) dx = \int_B h(y) f_X \circ g^{-1}(y) \frac{1}{|\det J_g (g^{-1}(y))|} dy,$$ 
    où $J_g$ désigne la matrice de Jacobi associée à la différentielle de $g$. Dans le cas où $f_X(x) = 0$ en dehors de $A$, on obtient que $Y$ admet la densité
        $$ f_Y(y) = 1_B(y)f_X \circ g^{-1}(y)\frac{1}{|\det J_g (g^{-1}(y))|}.$$
    Lorsque $g$ est simplement continûment différentiable, il existe souvent une partition finie $(A_i)_{1\leq i \leq n}$ de l'ensemble $\{x ; f(x) >0\}$, telle que $g$ soit injective sur chaque $A_i$. On note alors $B_i = g(A_i)$ l'image de $A_i$ par $g$. On découpe alors l'intégrale selon les $A_i$, on applique la formule précédente à chaque morceau et on somme pour obtenir :
        $$ f_Y(y) = \sum_{i=1}^n 1_{B_i}(y)f_X \circ g^{-1}(y) \frac{1}{|\det J_g (g^{-1}(y))|},$$
    où $g^{-1}$ est bien définie sur chaque $B_i$ comme image réciproque de la restriction de g à $A_i$.
 3. $m < n$, on commence par "compléter" $Y$, en essayant de construire une application $g'$ de $\R^n$ dans $\R^n$ dont les $m$ premières composantes coïncident avec les composantes de $g$ et pour laquelle on peut appliquer l'une des deux formules précédentes. On obtient ainsi la densité $f_Y'$ de $Y' = g'(X)$ puis     on obtient la densité de $Y$ en calculant sa loi marginale :
        $$f_Y(y_1,\ldots,y_m) = \int_{\R^{n-m}} f_{Y'}(y_1,\ldots,y_m,y_{m+1},\ldots y_n) dy_{m+1}\ldots dy_n.$$


### **Coordonnées polaires** {.example #polar}
Soit $X = (U,V)$ un vecteur aléatoire de $\R^2$, et $Y = (R,\Theta)$ ses coordonnées polaires. La transformation $g$ est un difféomorphisme de $A = \R^2\setminus\{0\}$ dans $B = \left]0,+\infty\right[\times \left]0,2\pi\right]$, et son inverse $g^{-1}$ s'écrit : $u = r\cos \theta,\, v= r\sin \theta$.
Le Jacobien de $g^{-1}$ au point $(r,\theta)$ vaut $r$, donc le point 2. ci-dessus entraîne que 
$$ f_Y(r,\theta) = r f_X(r\cos\theta,r\sin\theta)1_B(r,\theta)$$
Par exemple, si $U$ et $V$ sont indépendantes et de loi $\mathcal{N}(0,1)$, on a $f_X(u,v) = \frac{1}{2\pi}\exp\left(-\frac{u^2+v^2}{2}\right)$ et donc
$$ f_Y(r,\theta) = \frac{1}{2\pi} r\exp\left(-\frac{r^2}{2}\right)1_{\left]0,+\infty\right[ }(r)1_{\left]0,2\pi\right]}(\theta).$$
En particulier, on remarque que $R$ et $\Theta$ sont indépendantes de densités respectives $r\exp\left(-\frac{r^2}{2}\right)1_{\left]0,+\infty\right[}(r)$ et $1_{\left]0,2\pi\right]}(\theta)$.

### Lancer de fléchette (fin) {.exercise .question .one #exo-flechetteter}
Donner la densité du couple $(R,\Theta)$ des coordonnées polaires de $M$. Sont-elles indépendantes ?


### **Somme de deux variables aléatoires indépendantes** {.example #sum}
Soient $U$ et $V$ indépendantes et admettant les densités $f_U$ et $f_V$, on cherche la densité de la somme $Z = U+V$. On commence par compléter $Z$ en le couple $T = (U,Z)$ (par exemple), correspondant à la bijection $g(u,v) = (u, u+v)$ sur $\R^2$ dont le jacobien est 1 et d'inverse $g^{-1}(x,y) = (x,x-y)$. Appliquant le point 3. ci-dessus, on obtient :
$$f_Z(z) = \int_{\R}f_U(u)f_V(z-u) du = \int_{\R}f_U(z-v)f_V(v)dv.$$
La fonction $f_Z$ est appelée *le produit de convolution* des des fonctions $f_U$ et $f_V$.

### Loi bêta {.exercise .question .three #exo-loibeta}

Soit $X = (U,V)$ un vecteur aléatoire de $\R^2$, avec $U$ et $V$ indépendantes de lois $\Gamma(\alpha,\theta)$ et $\Gamma(\beta,\theta)$. Identifier la densité de $Y = \frac{U}{U+V}$, puis de $Z = U+V$.


Exercices complémentaires
================================================================================

## Loi de vie et de mort 

La durée de vie d'un être vivant ou d'un matériel peut-être assimilée à une variable aléatoire strictement positive $T$.
Dans ce cadre, on peut définir les notions suivantes :

* Loi de vie a priori : il s'agit de la loi du temps $T$ caractérisée par fonction de répartition complémentaire
        $$G(t) = \P(T>t)$$
* Loi de survie après $t_0 \geq 0$ : il s'agit de la loi du temps $T-t_0$ qu'il lui reste à vivre, sachant qu'il était encore en vie à $t_0$, de fonction de répartition complémentaire
        $$G_{t_0}(t) =\P(T>t+t_0|T>t_0)$$

On dira que la loi de vie satisfait la propriété de non vieillissement (ou d'absence de mémoire) si la loi de survie et la loi de vie sont égales :
        $$\forall t \geq 0 \text{ et } \forall t_0 \geq 0, G_{t_0}(t) = G(t)$$

### Question 1 {.question #viemort1}

Exprimer la loi de survie à partir de la loi de vie a priori.

### Question 2 {.question #viemort2}

Montrer qu'une variable aléatoire $T$ satisfait la propriété de non-vieillissement si et seulement si elle est de loi exponentielle.

### Question 3 {.question #viemort3}
On suppose que $T$ admet une densité continue sur $\R_+^\ast$. Montrer que l'on peut définir le taux de mort à l'instant $t$ par 
        $$D(t) = \lim_{\Delta t \to 0} \frac{1}{\Delta t}\P(t < T \leq t + \Delta t | T >t)$$
et exprimer $G$ en fonction de $D$.

Quelles lois correspondent-elles à $D$ constant ?

## Durée de vie

La durée de vie, exprimée en années, d’un circuit électronique est une variable aléatoire $T$ dont la fonction de répartition $F$ est définie par : 
$$F (t) = (1 - e^{-t^2 /2} )1_{t\geq 0}$$

### Question 1 {.question #dureevie1} 

Donner la densité de probabilité $f$ de $T$ . Calculer $\Esp(T)$.

### Question 2 {.question #dureevie2} 

Sachant que le circuit a déjà fonctionné durant 1 an, quelle est la probabilité qu’il continue à fonctionner encore durant au moins 2 ans ? La loi est-elle sans
mémoire ?

Un équipement électronique E est composé de 10 circuits identiques et indépendants. Au circuit $i (1 \leq i \leq 10)$ est associée la variable aléatoire $X_i$ , avec $X_i = 1$
si la durée de vie du circuit $i$ est inférieure à un an et $X_i = 0$ sinon.

### Question 3 {.question #dureevie3} 

Quelle est la loi du nombre $N$ de circuits de E dont la durée de vie est inférieure à 1 an ?

### Question 4 {.question #dureevie4} 
 
L’équipement E est dit en série si la défaillance de l’un de ses circuits entraîne sa défaillance. Quelle est alors la probabilité qu’il soit défaillant avant 1 an ?

### Question 5 {.question #dureevie5} 

L’équipement E est dit en parallèle si sa défaillance ne peut se produire que si tous ses circuits sont défaillants. Quelle est alors la probabilité qu’il soit défaillant avant 1 an ?



## Crues centennales de la Seine
On suppose que la hauteur d’eau maximale au cours de l’année $n$ est décrite par une variable aléatoire $X_n$ de densité $f(x)$ et de fonction de répartition $F(x)$, identique pour toutes les $X_n$, que l'on suppose également indépendantes.

### Question 1 {.question #crue1}
Calculer la fonction de répartition du maximum sur $n$ années $Y = \max(X_1,\ldots,X_n)$.

### Question 2 {.question #crue2}
En déduire la densité de $Y$.

### Question 3 {.question #crue3}
Expliciter la densité de $Y$ lorsque les $X_i$ sont de loi uniforme sur $[0,1]$. 

### Question 4 {.question #crue4}
Selon mêmes hypothèses, calculer la hauteur minimale des quais pour que la probabilité de voir la Seine déborder sur une période de $n$ années soit inférieure à 1/1000.

### Question 5 {.question #crue5}
Toujours selon les mêmes hypothèses, calculer la médiane de $Y$. La comparer avec celle des $X_i$. Commenter.

## Indépendance et vecteurs gaussiens

Soit $Z := (X,Y)$ un vecteur gaussien (i.e. qui suit une loi Normale bi-variée) d'espérance $m$ et de matrice de covariance définie positive $C$. Notons $f_Z$ sa densité.

### Question 1 {.question #covindepgauss-joint}

Rappeler la forme de $f_Z$ et en donner une expression non matricielle faisant apparaître le coefficient de corrélation noté $\rho$.

### Question 2 {.question #covindepgauss-marg}

Expliciter les lois marginales de $X$ et de $Y$.

### Question 3 {.question #covindepgauss-indep}

Montrer que $X$ et $Y$ sont indépendantes ssi $\text{Cov}\left(X,Y\right) = 0$.


## Symétrie de la gaussienne

Soit $X$ une variable aléatoire réelle de loi Normale centrée réduite, dont la densité est notée $f$ et la fonction de répartition $F$. Pour tout $c>0$ on pose 
        $$X_c := \left|\begin{array}{ll} X & \text{si } |X| > c,\\ -X & \text{si } |X| \leq c.\end{array}\right.$$

### Question 1 {.question #gausssym-loi}

Déterminer la loi de $X_c$. 

### Question 2 {.question #gausssym-cov}

Calculer la covariance de $X$ et de $X_c$ et montrer qu'il existe une valeur $c_0$ de $c$ qui l'annule. 

### Question 3 {.question #gausssym-indep}

Les deux variables $X$ et $X_{c_0}$ sont-elles indépendantes ? 

### Question 4 {.question #gausssym-vecgauss}

Le vecteur aléatoire $(X,X_{c_0})$ est-il gaussien ? 


## Loi du $\chi^2$

On considère une variable aléatoire $X$ gaussienne centrée réduite. On note $f$ sa densité et $F$ sa fonction de répartition.

### A 1 degré de liberté {.question #khi2-1dl}

1. Calculer la densité de la variable aléatoire $Y := X^2$. En donner une expression faisant apparaître la fonction gamma (on rappelle que $\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}$).

On dit que $Y$ suit une *loi du $\chi^2$ à $1$ degré de liberté*, et on note $Y \sim \chi^2$.

### A n degrés de liberté {.question #khi2-ndl}

Soient maintenant $n\in\mathbb{N}^\ast$ et $X_1,\dots,X_n$ des copies indépendantes de $X$. Pour tout $i \in \{1,\dots,n\}$ on pose $Y_i := X_i^2$.

2. Montrer que la variable aléatoire $Y := \sum_{i = 1}^n Y_i$ admet pour densité
$$ f_Y : x\in\R \mapsto \left|\begin{array}{ll} \dfrac{x^{\frac{n}{2} - 1}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{n}{2}\right)}\,\exp\left\{ -\dfrac{x}{2} \right\} & \text{si } x> 0,\\ 0 & \text{si } x \leq 0. \end{array}\right.$$
On pourra procéder par récurrence sur $n$.

On dit que $Y$ suit une *loi du $\chi^2$ à $n$ degrés de liberté* et on note $Y \sim \chi^2_n$.



## Combinaisons linéaires de variables Gaussiennes indépendantes

Soit $X$ une variable aléatoire de loi Normale centrée réduite, dont on note $f$ la densité et $F$ la fonction de répartition.

### Préliminaires {.question #CLIGauss-pre}

1. Rappeler la loi de la variable aléatoire $s\,X + m$, où $s, m \in \R$.

### Combinaisons linéaires {.question #CLIGauss-cl}

Soient maintenant $n\in\mathbb{N}^\ast$ variables aléatoires $X_1,\dots,X_n$ indépendantes et de même loi que $X$ (on dit que ce sont des *copies indépendantes* de $X$). Pour tout vecteur $a = (a_1,\dots,a_n) \in (\R^{*})^n$ on pose $S_n^a := \sum_{i = 1}^n a_i\,X_i$. 

2. Montrer que pour $S_n^a$ suit une loi Normale d'espérance nulle et de variance $\sum_{i = 1}^n a_i^2$ (on pourra raisonner par récurrence sur $n$).

3. Soient $a,b\in(\R^{*})^n$. Sous quelle condition a-t-on $\text{Cov}\left(S_n^a, S_n^b\right) = 0$ ?




---

# Solutions

Exercices essentiels
--------------------------------------------------------------------------------

### Approximation par une constante {.answer #answer-exo-approx}
On a 
$$\Esp((X-a)^2) = \Esp((X-\Esp(X) + \Esp(X) - a)^2 = \Esp((X - \Esp(X))^2 ) + (\Esp(X) - a)^2$$
le terme de gauche ne dépend pas de $a$ tandis que celui de droite s'annule en $a = \Esp(X)$.

### Calcul d'une covariance {.answer #answer-cov-unif}
On a 
\begin{align*}
\cov(U,V) &= \Esp((U-\Esp(U))(V-\Esp(V)))\\
          &= \Esp(UV - \frac{U}{2} - \frac{U}{2} - \Esp(U)\Esp(V))\\
          &= \Esp(U(1-U)) - 1/4 - 1/4 +1/4 \text{ par linéarité et d'après la solution ci-dessous}\\
          &= 1/2 - 1/3 -1/4 = -1/12
\end{align*}
et 
$$\rho(U,V) = \frac{\cov(U,V)}{\sqrt{\V(U)}\sqrt{\V(V)}} = -1$$

### Coefficient de corrélation {.answer #answer-CS-corr}

On déduit de l'inégalité de [Cauchy-Schwarz](#CS) que 
$$|\rho(X,Y)| = \left|\frac{\Esp((X-\Esp(X))(X-\Esp(Y)))}{\sqrt{\V(X)\V(Y)}} \right| \leq \frac{\sqrt{\Esp((X-\Esp(X))^2)\Esp((X-\Esp(Y))^2)}}{\sqrt{\V(X)\V(Y)}} =1$$

### Moments d'une variable aléatoire de loi uniforme sur $[a,b]$ {.answser  #answer-moments-unif}    

Soit $X \sim \mathcal{U}_{[a,b]}$. Son espérance vaut
        $$\Esp(X) = \int_a^b \frac{x}{b-a} dx = \frac{a+b}{2}$$
et puisque
        $$\Esp(X^2) = \int_a^b \frac{x^2}{b-a} dx = \frac{a^2 + ab +b^2}{3},$$
alors sa variance vaut
        $$\V(X) = \Esp(X^2) - \Esp(X)^2 = \frac{(b-a)^2}{12}.$$

### Moments d'une v.a. de loi exponentielle {.answer #answer-moments-expo}    

Soit $X \sim \E(\theta)$, alors
$$\Esp(X) = \int_0^{+\infty} x \theta \exp(-\theta x) dx = [\frac{x}{\theta}\exp(-\theta x)]_0^{+\infty} + \int_0^{+\infty} \exp(-\theta x) dx = \frac{1}{\theta}$$

### Moments d'une v.a. de loi gamma {.answer #answer-moments-gamma}    

Soit $X\sim \Gamma(\alpha,\beta)$. On a
\begin{align*}
\Esp(X) &= \frac{1}{\Gamma(\alpha)}\int_0^{+\infty} \theta^\alpha x^\alpha e^{-\theta x} dx\\
        &= \frac{1}{\Gamma(\alpha)}\int_0^{+\infty} \frac{1}{\theta} u^\alpha e^{-u} du \text{ par le changement de variable } u = \theta x\\
        &= \frac{\Gamma(\alpha+1)}{\Gamma(\alpha)} \frac{1}{\theta} = \frac{\alpha}{\theta}
\end{align*}
puis
\begin{align*}
\Esp(X^2) &= \frac{1}{\Gamma(\alpha)}\int_0^{+\infty} \theta^\alpha x^{\alpha+1} e^{-\theta x} dx\\
        &= \frac{1}{\Gamma(\alpha)}\int_0^{+\infty} \frac{1}{\theta^2} u^{\alpha+1} e^{-u} du \text{ par le changement de variable } u = \theta x\\
        &= \frac{\Gamma(\alpha+2)}{\Gamma(\alpha)} \frac{1}{\theta^2} = \frac{\alpha(\alpha+1)}{\theta^2}
\end{align*}
d'où
$$\V(X) = \Esp(X^2) - \Esp(X)^2 = \frac{\alpha}{\theta^2}$$

### Moments d'une v.a. gaussienne {.answer #answer-moments-gauss}

Pour s'assurer qu'il s'agit bien d'une densité, on remarque que  $I = \int_{-\infty}^{+\infty} f(x) dx$ vérifie 
$$ I^2 = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f(x) f(y) dxdy = \int_{0}^{2\pi} d\theta\int_{0}^{+\infty}\frac{1}{2\pi} r e^{-r^2/2}dr $$
(en passant en coordonnées polaires dans l'intégrale double). 
Le calcul est ensuite aisé et on obtient $I = 1$.


Pour les moments, on fait d'abord le calcul dans le cas centré réduit ($\mu = 0$ et $\sigma^2 =1$) puis on s'y ramène par le changement de variable $x \mapsto \frac{x-\mu}{\sigma}$. Soit donc $X \sim \mathcal{N}(0,1)$, on a
\begin{align*}
\Esp(X) &= \int_{-\infty}^{+\infty} \frac{x}{\sqrt{2\pi}} e^{-x^2/2} dx\\
         &= \left[-\frac{1}{\sqrt{2\pi}} e^{-x^2/2} \right]_{-\infty}^{+\infty} = 0.
\end{align*}
et 
\begin{align*}
\V(X) = \Esp(X^2) &= \int_{-\infty}^{+\infty} \frac{x^2}{\sqrt{2\pi}} e^{-x^2/2} dx\\
         &= \left[-\frac{x}{\sqrt{2\pi}} e^{-x^2/2} \right]_{-\infty}^{+\infty} +\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx \\
         &= 0 + 1.
\end{align*}

### *Loi de Cauchy* {.answer #answer-exo-cauchy}

L'angle $\theta$ est une variable aléatoire uniforme sur $[-\pi/2,\pi/2]$, de densité $g(\theta) = \frac{1}{\pi}1_{[ -\pi/2,\pi/2 ]}(\theta)$. L'abscisse $X$ est donnée par $X = \tan \theta$, c'est donc une variable aléatoire, de fonction de répartition
\begin{align*}        
F(x) & = \P(X \leq x) \\
     & = \P(\theta \leq \arctan x) \\
     & = \int_{-\infty}^{\arctan x} \frac{1}{\pi}1_{[ -\pi/2,\pi/2 ]}(\theta) d\theta \\
     & = \frac{1}{\pi} \arctan x + \frac{1}{2}.
\end{align*}

$F$ est de classe $C^1$ de dérivée
        $$f(x) = \frac{1}{\pi(1+x^2)}, x \in \R$$

C'est la densité de la loi de Cauchy. Une variable aléatoire $X$ de loi de Cauchy n'admet pas d'espérance. En effet, $\frac{x}{\pi(1+x^2)} \sim_{x\to \infty} \frac{1}{x}$ n'est pas intégrable.

### Lancer de fléchette {.answer #answer-exo-flechette}

Les coordonnées cartésiennes de $M \in D = \{(x,y) \in \R^2 , x^2+y^2 \leq 1\}$ constituent un couple de variables aléatoires de densité
$$f_{(X,Y)}(x,y) = \frac{1}{\pi}1_{D} (x,y)$$
uniforme sur le disque, par hypothèse. L'abscisse de $X$ est distribuée selon la densité marginale
$$f_X(x) = \int f_{(X,Y)}(x,y) dy = \frac{2}{\pi} (1-x^2)^{1/2} 1_{[-1,1]}(x).$$
La loi de $Y$ a la même densité.

### Lancer de fléchette (suite) {.answer #answer-exo-flechettebis}
La densité des coordonnées cartésiennes ne s'exprime pas comme le produit des densités marginales ; elles ne sont pas indépendantes.

### Démonstration {.answer #answer-demo-cov-indep}
Soit $X$ et $Y$ deux v.a. aléatoires indépendantes et de carré intégrable. On a d'après [la proposition](#indep_fct)
$$\Esp((X-\Esp(X))(Y-\Esp(Y))) = \Esp(X-\Esp(X))\Esp(Y-\Esp(Y)) = 0 = \rho(X,Y)$$

### Lancer de fléchette (fin) {.answer #answer-exo-flechetteter}
En coordonnées polaires, le domaine $D$ est décrit par $D = \{(r,\theta) \in [0,1] \times [0,2\pi]\}$. La densité de $(R,\theta)$ s'écrit ainsi :
$$f_{(R,\theta)}(r,\theta) = \frac{r}{\pi}1_{D} (r\cos(\theta),r\sin(\theta)) = 2r 1_{[0,1]}(r) \frac{1}{2\pi}1_{[0,2\pi]}(r).$$
Ainsi $R$ et $\Theta$ sont indépendantes de densités respectives $2r 1_{[0,1]}(r)$ et $\frac{1}{2\pi}1_{[0,2\pi]}(\theta)$.

### Loi bêta {.answer #answer-exo-loibeta}
On note d'abord que la dimension de $Y$ est plus petite que celle de $X$. On va donc compléter $Y$ en prenant par exemple $Y' = (Y,Z)$, avec $Z=U+V$, ce qui correspond à $g(u,v) = \left(\frac{u}{u+v},u+v\right)$. Cette application est bijective de $A = \left]0,+\infty\right[^2$ dans $B = \left]0,1\right[ \times \left]0,+\infty\right[$, d'inverse $g^{-1}(y,z) = (yz,z(1-y))$, qui a pour jacobien $z$.

Comme $f_X(u,v) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}u^{\alpha-1}v^{\beta-1}e^{-\theta(u+v)}1_A(u,v)$, on a 
        $$f_{Y'}(y,z) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}z^{\alpha+\beta -1}y^{\alpha-1}(1-y)^{\beta-1}e^{-\theta z}1_B(y,z).$$
On obtient alors la densité de Y en intégrant $f_{Y'}(y,z)$ par rapport à $z\in \left]0,+\infty\right[$ :
\begin{align*}
f_Y(y) &= \int_0^{+\infty} f_{Y'}(y,z) dz\\
       &= \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}y^{\alpha-1}(1-y)^{\beta-1}1_{\left]0,1\right[}(y)\int_0^{+\infty}z^{\alpha+\beta -1}e^{-\theta(z)}dz\\
       &= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}y^{\alpha-1}(1-y)^{\beta-1}1_{\left]0,1\right[}(y),
\end{align*}
où on a utilisé la définition de la fonction gamma et le changement de variable linéaire $z \mapsto \theta z$.
On appelle loi bêta de paramètres $\alpha$ et $\beta$ la loi admettant cette densité. Admettant une grande variété de formes, elle permet de modéliser de nombreuses distributions à support fini.

La loi bêta apparaît naturellement dans une expérience d'urnes, donnée par George Pólya dans un article de 1930, [*Sur quelques points de la théorie des probabilités*](http://www.numdam.org/article/AIHP_1930__1_2_117_0.pdf). Il décrit l'expérience suivante : on se donne une urne contenant initialement $r$ boules rouges et $b$ boules bleues, on tire une boule dans l'urne, puis on la remet dans l'urne avec une deuxième boule de même couleur. Alors la proportion de boules rouges tend vers une variable aléatoire de loi Beta$(r,b)$, et, inversement, la proportion de boules bleues tend vers une variable aléatoire de loi Beta$(b,r)$. 

Nous obtenons aussi facilement la densité de $Z$. En effet, on a $f_{Y'}(y,z) = f_Y(y)f_Z(z)$ ($Y$ et $Z$ sont donc indépendantes), où
$$f_Z(z) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha+\beta)}z^{\alpha+\beta -1}e^{-\theta z}1_{\left]0,+\infty\right[}$$
On a ainsi démontré que si $U$ et $V$ sont deux variables aléatoires indépendantes de lois respectives $\Gamma(\alpha,\theta)$ et $\Gamma(\beta,\theta)$, alors $U+V$ suit la loi $\Gamma(\alpha+\beta,\theta)$ et est indépendante de $\frac{U}{U+V}$ qui suit une loi bêta de paramètres $(\alpha,\beta)$.



## Loi de vie et de mort 

### Question 1 {.answer #answer-viemort1}

Par définition, on a 
$$ G_{t_0}(t) = \P(T>t+t_0|T>t_0) = \frac{\P(T>t+t_0,T>t)}{\P(T>t)} = \frac{G(t+t_0)}{G(t)}$$

### Question 2 {.answer #answer-viemort2}

D'après la question précédente, $G$ vérifie alors $G(t_0+t) = G(t)G(t_0)$ pour tous $t, t_0 > 0$. Comme $G$ est décroissante, continue à droite et tend vers 0 à l'infini, on en déduit que $G(t) = e ^{-\theta t}$, pour un $\theta > 0$. On reconnaît la fonction de répartition complémentaire d'une loi exponentielle de paramètre $\theta$.

### Question 3 {.answer #answer-viemort3}
\begin{align*}
D(t) &= \lim_{\Delta t \to 0} \frac{1}{\Delta t}\P(t < T \leq t + \Delta t | T >t)\\
     &= \lim_{\Delta t \to 0} \frac{1}{\Delta t}\frac{\P(t < T \leq t + \Delta t)}{\P(T >t)}\\
     &= \frac{1}{G(t)} \lim_{\Delta t \to 0} \frac{G(t) - G(t + \Delta t)}{\Delta t}\\
     &= -\frac{g(t)}{G(t)}
\end{align*}
Ainsi, $D(t) = \frac{d}{dt}(-\ln G(t))$ et comme $G(0) = 1$, alors on a pour $t >0$
        $$G(t) = \exp\left(-\int_0^tD(s) ds\right)$$
Si $D$ est constant, on retrouve une loi exponentielle.


## Durée de vie

### Question 1 {.answer #answer-dureevie1} 
En dérivant, on obtient que la densité de $T$ est $f(t) = t e^{-t^2/2}1_{t>0}$.

L'espérance vaut :

\begin{align*}
\Esp(T) &= \int_0^{+\infty} t^2 e^{-t^2/2} dt\\
        &= \left[-t e^{-t^2/2} \right]_0^{+\infty} + \int_0^{+\infty} e^{-t^2/2} dt \text{ par intégration par parties}\\
        &= \frac{1}{2} \int_{-\infty}^{+\infty} e^{-t^2/2} dt \\
        &= \frac{\sqrt{2\pi}}{2}
\end{align*}

### Question 2 {.answer #answer-dureevie2} 

La probabilité s'écrit :

$$\P(T\geq 3 |T \geq 1) = \frac{\P(T \geq 3,T \geq 1)}{\P(T \geq 1)} = \frac{\P(T \geq 3)}{\P(T \geq 1)} = \frac{e^{-9/2}}{e^{-1/2}} = e^{-4}$$

### Question 3 {.answer #answer-dureevie3} 

Les variables aléatoires $X_1 , \ldots , X_{10}$ sont indépendantes et suivent une loi de Bernoulli de paramètre :
$$ \P (T \leq 1) = F (1) = 1 - e^{- 1/2}$$

On en déduit que la loi de N est la loi binomiale de paramètre $(10, 1 - e^{- 1/2})$.

### Question 4 {.answer #answer-dureevie4} 

La probabilité que l’équipement en série soit défaillant avant 1 an vaut :
$$ P(N \geq 1) = 1 - \P(N = 0) = 1 - e^{-1/2} \approx 9.9 10 -1 = 99%$$

### Question 5 {.answer #answer-dureevie5} 
La probabilité que l’équipement en parallèle soit défaillant avant 1 an vaut :
$$ \P(N = 10) = (1 - e^{-1/2})^10 \approx 8.9 10 -5 $$

## Crues centennales de la Seine

### Question 1 {.answer #answer-crue1}
Soit $x\in \R$
\begin{align*}
F_Y(x) = F(Y\leq x) &= F(X_1\leq x,\ldots,X_n\leq x)\\
           &= \prod_{i=1}^n F(X_i\leq x) \\
           &= F(x)^n
\end{align*}
puisque les $X_i$ sont indépendantes et de même loi

### Question 2 {.answer #answer-crue2}
Soit $x\in \R$
\begin{align*}
f_Y(x) &= \frac{d}{d x} F_Y(x)\\
       &= \frac{d}{d x} F(x)^n\\
       &= nf(x)F(x)^{n-1}
\end{align*}

### Question 3 {.answer #answer-crue3}
On a alors $f(x) = 1_{[0,1]}(x)$ et $F(x) = x 1_{[0,1]}(x) + 1_{[1,+\infty]}$. On en déduit
$$ f_Y(x) = n x^{n-1}1_{[0,1]} $$

### Question 4 {.answer #answer-crue4}

On cherche à déterminer $x$ tel que $\P(Y > x) \leq \frac{1}{1000}$. Or,
$$ \P(Y > x) = 1-\P(Y \leq x) = 1 - F_Y(x) = 1 - F(x)^n = 1-x^n $$
Ainsi
$$ 1-x^n \leq \frac{1}{1000} \Leftrightarrow (1-\frac{1}{1000})^{1/n} \leq x $$

### Question 5 {.answer #answer-crue5}
On rappelle que la médiane est le réel $m$ tel que $\frac{1}{2} = \P(Y \leq m) = F_Y(m)$.

On cherche donc $m$ tel que $m^n = \frac{1}{2}$, soit $m = \frac{1}{2^{1/n}}$.

On voit que cette valeur est plus élevée que la médiane des $X_i$ qui vaut $\frac{1}{2}$. Elle tend même vers 1 lorsque $n$ tend vers l'infini.

## Indépendance et vecteurs gaussiens

### Question 1 {.answer #answer-covindepgauss-joint}

D'après le cours, en interprétant les éléments de $\R^2$ comme des vecteurs colonnes, pour tout $z =(x,y)\in\R^2$ on a
$$
f_Z(z) = \dfrac{1}{2\pi\,\sqrt{\det(C)}}\,\exp\left\{ -\dfrac{1}{2}\,\left(z - m\right)^t\,C^{-1}\,\left(z - m\right) \right\}.
$$
Or par construction $C$ peut s'écrire
$$C = \left( \begin{array}{cc} \sigma_X^2 & c\\ c & \sigma_Y^2 \end{array}\right), $$
où $\sigma_X^2 := \mathbb{V}\left(X\right)$, $\sigma_Y^2 := \mathbb{V}\left(Y\right)$ et $c = \text{Cov}\left(X,Y\right)$. Comme $C$ est définie positive elle est inversible, avec $\det(C) = \sigma_X^2\,\sigma_Y^2 - c^2 > 0$ et
$$C^{-1} = \dfrac{1}{\sigma_X^2\,\sigma_Y^2 - c^2}\,\left( \begin{array}{cc} \sigma_Y^2 & -c\\ -c & \sigma_X^2 \end{array}\right).$$
En outre, $m = \left(m_X, m_Y \right)$ avec $m_X := \Esp(X)$ et $m_Y := \Esp(Y)$. On en déduit que
\begin{align*}
f_Z(x,y) &= \dfrac{1}{2\pi\,\sqrt{\sigma_X^2\,\sigma_Y^2 - c^2}}\,\exp\biggl\{ \dfrac{-1}{2\,\left(\sigma_X^2\,\sigma_Y^2 - c^2 \right)}\times\\
&\ \ \ \left( \sigma_Y^2\,(x-m_X)^2 - 2c\,(x-m_X)\,(y-m_Y) + \sigma_X^2\,(y-m_Y)^2 \right) \biggr\}\\
&= \dfrac{1}{2\pi\,\sigma_X\,\sigma_Y\,\sqrt{1-\rho^2}}\,\,\exp\biggl\{ \dfrac{-1}{2\,\left( 1 - \rho^2 \right)}\times\\
&\ \ \ \left( \dfrac{(x-m_X)^2}{\sigma_X^2} - 2\rho\,\dfrac{(x-m_X)}{\sigma_X}\,\dfrac{(y-m_Y)}{\sigma_Y} + \dfrac{(y-m_Y)^2}{\sigma_Y^2} \right) \biggr\}.
\end{align*}

### Question 2 {.answer #answer-covindepgauss-marg}

Ici, pour $x,y \in \R^2$, on remarque que :
\begin{align*}
f_Z(x,y) &= \dfrac{1}{2\pi\,\sigma_X\,\sigma_Y\,\sqrt{1-\rho^2}}\,\,\exp\biggl\{ \dfrac{-1}{2\,\left( 1 - \rho^2 \right)}\times\\
&\ \ \ \left( \left(\dfrac{y-m_Y}{\sigma_Y} - \rho\,\dfrac{x-m_X}{\sigma_X}\right)^2 + (1 - \rho^2)\,\dfrac{(x-m_X)^2}{\sigma_X^2} \right) \biggr\}\\
& = \dfrac{1}{\sqrt{2\pi}\,\sigma_X}\,\exp\left\{-\dfrac{(x-m_X)^2}{2\,\sigma_X^2} \right\}\times\\
&\ \ \ \dfrac{1}{\sqrt{2\pi}\,\sigma_Y\,\sqrt{1-\rho^2}}\,\exp\left\{-\dfrac{1}{2\,(1-\rho^2)}\,\left(\dfrac{y-m_Y}{\sigma_Y} - \rho\,\dfrac{x-m_X}{\sigma_X}\right)^2 \right\}.
\end{align*}
Ainsi, avec le changement de variable $u = \dfrac{y-m_Y}{\sigma_Y}$ on obtient
\begin{align*}
f_X(x) &= \int_{-\infty}^{+\infty} f_Z(x,y)\,dy\\
&= \dfrac{1}{\sqrt{2\pi}\,\sigma_X}\,\exp\left\{-\dfrac{(x-m_X)^2}{2\,\sigma_X^2} \right\}\times\\
&\ \ \ \int_{-\infty}^{+\infty} \dfrac{1}{\sqrt{2\pi}\,\sqrt{1-\rho^2}}\,\exp\left\{-\dfrac{1}{2\,(1-\rho^2)}\,\left(u - \rho\,\dfrac{x-m_X}{\sigma_X}\right)^2 \right\}\,du,
\end{align*}
et on reconnaît dans cette dernière intégrale la densité d'une loi Normale d'espérance $\rho\,\dfrac{x-m_X}{\sigma_X}$ et de variance $1-\rho^2$. Cette intégrale vaut donc $1$ et on conclut que
$$f_X(x) = \dfrac{1}{\sqrt{2\pi}\,\sigma_X}\,\exp\left\{-\dfrac{(x-m_X)^2}{2\,\sigma_X^2} \right\}, $$
qui correspond à la densité d'une loi Normale d'espérance $m_X$ et de variance $\sigma_X^2$.

En procédant de manière symétrique, on obtient de même que $Y$ suit une loi Normale d'espérance $m_Y$ et de variance $\sigma_Y^2$.

### Question 3 {.answer #answer-covindepgauss-indep}
Le premier sens est évident : si $X$ et $Y$ sont indépendantes, alors nous avons vu dans le cours que $\text{Cov}\left(X,Y\right) = 0$, et ce que l'on soit gaussien ou non.

Supposons maintenant que $\text{Cov}\left(X,Y\right) = 0$, et montrons l'indépendance entre $X$ et $Y$. En reprenant la formule de la question 1 et en remplaçant $\rho$ par $0$, pour tout $(x,y) \in \R^2$ on a:
\begin{align*}
f_Z(x,y) &= \dfrac{1}{2\,\pi\,\sigma_X\,\sigma_Y}\,\exp\left\{ -\dfrac{1}{2}\,\left( \dfrac{(x-\mu_X)^2}{\sigma_X^2} + \dfrac{(y-\mu_Y)^2}{\sigma_Y^2} \right) \right\}\\
&= \dfrac{1}{\sqrt{2\pi}\,\sigma_X}\,\exp\left\{ -\dfrac{(x-m_X)^2}{2\,\sigma_X^2} \right\} \times \dfrac{1}{\sqrt{2\pi}\,\sigma_Y}\,\exp\left\{ -\dfrac{(y-m_Y)^2}{2\,\sigma_Y^2} \right\}\\
&= f_X(x)\times f_Y(y)
\end{align*}
d'après la question 2. On en conclut que $X$ et $Y$ sont bien indépendantes.

## Symétrie de la gaussienne

### Question 1 {.answer #answer-gausssym-loi}

Nous avons admis dans le cours que la fonction de répartition $F_c$ de $X_c$ caractérisait sa loi. Nous allons donc l'expliciter. Soit $x \in \R$. Par définition de la fonction de répartition d'une variable aléatoire et d'après la formule des probabilités totales, on a
\begin{align*}
F_c(x) &= \P\left(X_c \leq x\right) = \P\left( X_c \leq x, |X| > c \right) + \P\left( X_c \leq x, |X| \leq c\right)\\
&= \P\left( X\leq x, |X| > c \right) + \P\left(-X \leq x, |X| \leq c\right)\\
&= \P\left( X\leq x, X > c \right) + \P\left(X \leq x, X < -c \right) + \P\left( X \geq -x, -c \leq X \leq c\right).
\end{align*}
Or $$\P\left( X\leq x, X > c \right) = \left|\begin{array}{ll} \P\left(c < X \leq x \right) = F(x) - F(c) & \text{si } x > c,\\ 0 & \text{si } x\leq c,\end{array}\right.$$
$$ \P\left(X \leq x, X < -c \right) = \P\left( X \leq \min\{-c,x\} \right) = F\left(\min\{-c,x\}\right), $$
$$ \P\left( X \geq -x, -c \leq X \leq c\right) = \left|\begin{array}{ll} \P\left(-c \leq X \leq c \right) = F(c) - F(-c) & \text{si } x > c, \\ \P\left(-x \leq X \leq c \right) = F(c) - F(-x) & \text{si } -c \leq x \leq c,\\ 0 & \text{si } x<-c. \end{array}\right.$$
Ainsi,

* si $x > c$ alors $\min\{-c,x\} = -c$ et
$$F_c(x) = F(x) - F(c) + F\left(\min\{-c,x\}\right) + F(c) - F(-c) = F(x),$$

* si $-c \leq x \leq c$ alors $\min\{-c,x\} = -c$ et
$$F_c(x) = F\left(\min\{-c,x\}\right) + F(c) - F(-x) = 1 - F(c) + F(c) - 1 + F(x) = F(x)$$
car la densité de la loi Normale centrée réduite est paire, ce qui implique que $F(-x) = 1 - F(x)$ pour tout $x\in\R$,

* si $x < -c$ alors $\min\{-c,x\} = x$ et
$$F_c(x) =  F\left(\min\{-c,x\}\right) = F(x).$$

On en conclut que $F_c = F$ : $X_c$ a la même loi que $X$. Ce résultat est dû à la symétrie de la densité de la loi Normale centrée réduite. On remarque d'ailleurs que le résultat resterait inchangé si l'on prenait n'importe quelle autre loi de densité paire !

### Question 2 {.answer #answer-gausssym-cov}

Tout d'abord, par définition, $$\text{Cov}\left(X,X_c\right) = \Esp\left( \left(X - \Esp\left(X\right)\right)\,\left(X_c - \Esp\left(X_c\right) \right) \right) = \Esp\left(X\,X_c \right) $$
puisque $X$ et $X_c$ sont gaussiennes centrées (d'espérance nulle) réduites. Or on remarque que l'on peut écrire $X_c = X\,1_{\R\backslash[-c,c]}(X) - X\,\,1_{[-c,c]}(X)$. On déduit par linéarité de l'espérance que
\begin{align*}
\Esp\left(X\,X_c\right) &= \Esp\left(X^2\,1_{\R\backslash[-c,c]}(X) - X^2\,1_{[-c,c]}(X)\right)\\
&= \Esp\left(X^2\,\left(1_{\R\backslash[-c,c]}(X) + 1_{[-c,c]}(X) - 1_{[-c,c]}(X)\right) - X^2\,1_{[-c,c]}(X)\right)\\
&= \Esp\left(X^2\right) - 2\,\Esp\left(X^2\,1_{[-c,c]}(X)\right).
\end{align*}
Etant donné que $X$ est de loi Normale centrée réduite, on a directement que $\Esp\left(X^2\right)=1$; il suffit donc de calculer la dernière espérance pour obtenir le résultat. Comme $x\mapsto x^2\,1_{[-c,c]}(x)$ est bornée et continue sur $\R\backslash\{-c,c\}$ (donc continue presque partout), elle est intégrable et
$$\Esp\left(X^2\,1_{[-c,c]}(X)\right) = \int_{-\infty}^{+\infty} x^2\,1_{[-c,c]}\,f(x)\,dx = \int_{-c}^c x^2\,f(x)\,dx. $$
Or on pourra remarquer que $f^\prime(x) = -x\,f(x)$ puis que $f^{\prime\prime}(x) = (x^2-1)\,f(x)$. Puisque $f$, $f^\prime$ et $f^{\prime\prime}$ sont continues et bornées (voir l'exercice *Densité et fonction de répartition d'une loi Normale* du chapitre Probabilités I) elles sont intégrables sur des segments. On en déduit que
\begin{align*}
\Esp\left(X^2\,1_{[-c,c]}(X)\right) &= \int_{-c}^c (x^2-1)\,f(x)\,dx + \int_{-c}^c f(x)\,dx\\
&= \left[-x\,f(x) \right]_{-c}^c + F(c) - F(-c)\\
&= -c\,\left(f(c) + f(-c)\right) + F(c) - F(-c)\\
&= 2\,\left(F(c) - c\,f(c)\right) - 1
\end{align*}
par parité de $f$. On en conclut que $\text{Cov}\left(X,X_c\right) = 3 + 4\,\left(c\,f(c) - F(c)\right)$.

La fonction $g : c\in\R_+^\ast \mapsto 3+4\,\left(c\,f(c) - F(c)\right)$ est continue, infiniment dérivable et pour tout $c > 0$ on a $g^\prime(c) = -4\,c^2\,f(c) < 0$. Par conséquent, $g$ est strictement décroissante, avec $\lim\limits_{c\to0^+} g(c) = 1$ et $\lim\limits_{c\to+\infty} g(c) = -1$. Le théorème des valeurs intermédiaires nous permet de conclure qu'il existe bien un unique $c_0 > 0$ tel que $g(c_0) = 0$.

### Question 3 {.answer #answer-gausssym-indep}

Les variables aléatoires $X$ et $X_{c_0}$ sont indépendantes ssi pour tous ensembles $A,B \in \mathcal{E}_\R$ on a
$$\P\left(X \in A, X_{c_0} \in B \right) = \P\left(X \in A\right)\,\P\left(X_{c_0} \in B \right).$$

Or si l'on prend $A = B = ]-\infty, x]$ où $x < -c_0$, alors
\begin{align*}
\P\left( X \leq x, X_{c_0} \leq x \right) &= \P\left( X \leq x, X < -c_0 \right) + \P\left( X \leq x, X > c_0 \right)\\
&\ \ \ + \P\left( X\leq x, X \geq -x, -c_0 \leq X \leq c_0 \right)\\
&= \P\left( X \leq x \right) +0 + 0 = F(x)\\
& \neq F(x)\,F(x) = \P\left( X \leq x \right)\,\P\left(X_{c_0} \leq x \right).
\end{align*}

On en conclut que bien que $\text{Cov}\left(X,X_{c_0}\right) = 0$, $X$ et $X_{c_0}$ ne sont pas indépendantes.

### Question 4 {.answer #answer-gausssym-vecgauss}

Supposons que $(X,X_{c_0})$ soit un vecteur gaussien. Alors, puisque $\text{Cov}\left(X,X_{c_0}\right) = 0$, $X$ et $X_{c_0}$ sont nécessairement indépendantes. Or nous venons de voir que ce n'était pas le cas; nous avons donc contradiction. On en conclut que $(X,X_{c_0})$ n'est pas gaussien.

## Loi du $\chi^2$

### A 1 degré de liberté {.answer #answer-khi2-1dl}

1. Soit $h : \R \to \R$ une fonction mesurable telle que $h\times f$ est  intégrable. Alors en opérant le changement de variable $u = x^2$ on a
\begin{align*}
\Esp\left( h(Y) \right) &= \Esp\left(h(X^2)\right) = \int_{\R} h(x^2)\,f(x)\,dx\\
& = \int_{-\infty}^{0} h(x^2)\,f(x)\,dx + \int_{0}^{+\infty} h(x^2)\,f(x)\,dx\\
&= \int_{0}^{+\infty} h(u)\,f\left(-\sqrt{u}\right)\,\dfrac{1}{2\,\sqrt{u}} \,du + \int_{0}^{+\infty} h(u)\,f\left(\sqrt{u}\right)\,\dfrac{1}{2\,\sqrt{u}} \,du.
\end{align*}
Or $f$ est paire, donc pour tout $u \in \R^+$ on a $f\left(-\sqrt{u}\right) = f\left(\sqrt{u}\right)$ et
\begin{align*}
\Esp\left( h(Y) \right) &= \int_{\R_+} h(u)\,f\left(\sqrt{u}\right)\,\dfrac{1}{\sqrt{u}} \,du.
\end{align*}
Par propriété $Y$ possède donc une densité $f_Y$ valant pour tout $x\in\R$
$$f_Y(x) = \left|\begin{array}{ll} f\left(\sqrt{x}\right)\,\dfrac{1}{\sqrt{x}} = \dfrac{x^{-\frac{1}{2}}}{2^{\frac{1}{2}}\,\Gamma\left(\frac{1}{2}\right)}\,\exp\left\{-\dfrac{x}{2}\right\} & \text{si } x > 0,\\ 0 & \text{si } x \leq 0. \end{array}\right. $$

**Remarque.** La fonction $f_Y$ est bien une densité : elle est continue par morceaux donc mesurable, puis positive, et son intégrale sur $\R$ vaut bien $1$ :
\begin{align*}
\int_{\R} f_Y(x)\,dx &= \dfrac{1}{2\,\Gamma\left(\frac{1}{2}\right)}\,\int_{0}^{+\infty} \left(\dfrac{x}{2}\right)^{\frac{1}{2}-1}\,\exp\left\{-\dfrac{x}{2}\right\}\,dx \\
&= \dfrac{1}{\Gamma\left(\frac{1}{2}\right)}\,\int_{0}^{+\infty} u^{\frac{1}{2}-1}\,e^{-u}\,du = \dfrac{\Gamma\left(\frac{1}{2}\right)}{\Gamma\left(\frac{1}{2}\right)} = 1.
\end{align*}

### A n degrés de liberté {.answer #answer-khi2-ndl}

2. On note $(\mathcal{P}_n)$ la propriété à démonter au rang $n$.

**Initialisation.** Nous avons vu à la question précédente que $(\mathcal{P}_1)$ est vraie.

**Hérédité.** Soit maintenant $n \geq 2$ et supposons $(\mathcal{P}_{n-1})$ vraie. Alors $Y = \sum_{i = 1}^{n-1}Y_i + Y_n$ est la somme de deux variables aléatoires indépendantes, dont la première suit un $\chi_{n-1}^2$ de densité notée $f_{n-1}$ et la seconde un $\chi_1^2$ de densité notée $f_1$. Elle possède donc une densité, égale au produit de convolution de $f_{n-1}$ et $f_1$ : pour tout $x\in\R$
$$f_Y(x) = \int_{\R} f_1(x-u)\,f_{n-1}(u)\,du.$$
Or pour tout $x,u\in\R$ on a $f_1(x-u) = 0$ ssi $x \leq u$ et $f_{n-1}(u) = 0$ ssi $u \leq 0$. Donc leur produit est strictement positif ssi $x > u > 0$, nul sinon. La densité $f_Y$ est par conséquent nulle sur $\R^-$ et nous allons maintenant exhiber son expression sur $\R_+^\ast$. Soit $x > 0$, alors
\begin{align*}
f_Y(x) &= \int_{0}^{x} \dfrac{(x-u)^{-\frac{1}{2}}}{\sqrt{2}\,\Gamma\left(\frac{1}{2}\right)}\,\exp\left\{-\dfrac{x-u}{2}\right\}\,\dfrac{u^{\frac{n-1}{2}-1}}{2^{\frac{n-1}{2}}\,\Gamma\left(\frac{n-1}{2}\right)}\,\exp\left\{-\dfrac{u}{2}\right\} \,du\\
&= \dfrac{\exp\left\{-\dfrac{x}{2} \right\}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)} \,\int_0^x \left(x-u\right)^{-\frac{1}{2}}\,u^{\frac{n-3}{2}}\,du.
\end{align*}
Avec le changement de variable $v=\dfrac{u}{x}$ on obtient
\begin{align*}
f_Y(x) &= \dfrac{x^{\frac{n}{2}-1}\,\exp\left\{-\dfrac{x}{2} \right\}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)} \,\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv.
\end{align*}
Or $f_Y$ est une densité, son intégrale vaut donc $1$ :
\begin{align*}
\int_{\R} f_Y(x)\,dx &= \int_0^{+\infty} \dfrac{x^{\frac{n}{2}-1}\,\exp\left\{-\dfrac{x}{2} \right\}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}\,\left(\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv\right)\,dx\\
&= \left(\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv\right)\,\left(\int_0^{+\infty} \dfrac{x^{\frac{n}{2}-1}\,\exp\left\{-\dfrac{x}{2} \right\}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}\,dx\right)\\
& \left(\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv\right)\,\left(\int_0^{+\infty} \dfrac{x^{\frac{n}{2}-1}\,\exp\left\{-x \right\}}{\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}\,dx\right)\\
&= \left(\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv\right)\,\left( \dfrac{\Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}\right) = 1.
\end{align*}

On en déduit que $$ \int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv = \dfrac{\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}{\Gamma\left(\frac{n}{2}\right)}, $$
et finalement que pour tout $x\in\R$
$$f_Y(x) = \left|\begin{array}{ll} \dfrac{x^{\frac{n}{2}-1}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{n}{2}\right)}\,\exp\left\{-\dfrac{x}{2}\right\} & \text{si } x> 0,\\ 0 & \text{sinon;}\end{array}\right.$$
$(\mathcal{P}_n)$ est donc vraie.

**Conclusion.** La propriété est vraie pour tout $n\in\mathbb{N}^\ast$.


##  Combinaisons linéaires de variables Gaussiennes indépendantes

### Préliminaires {.answer #answer-CLIGauss-pre}

Cette question a été traitée de manière générale dans le cours. Nous en proposons une preuve alternative, basée sur le calcul de la fonction de répartition de la variable aléatoire $s\,X + m$, qui caractérise sa loi. Elle dépend clairement des valeurs de $s$.

* Si $s = 0$, alors $s\,X + m$ est toujours égale à $m$ : sa loi est une masse de Dirac en $\{m\}$ et pour tout $x\in\R$ on a $\P\left(s\,X +m \leq x\right) = 1_{[m,+\infty[}(x)$.

* Si $s\neq 0$, alors pour tout $x\in\R$ on a
$$\P\left( s\,X + m \leq x \right) = \left|\begin{array}{ll}\displaystyle\P\left( X \leq \dfrac{x-m}{s} \right) = \int_{-\infty}^{\frac{x-m}{s}} f(u)\,du & \text{si } s>0,\\[1em] \displaystyle \P\left( X \geq \dfrac{x-m}{s} \right) = \int_{\frac{x-m}{s}}^{+\infty} f(u)\,du & \text{si } s<0,\end{array}\right.$$
qui en posant le changement de variable $v = s\,x+m$ donne
$$\P\left( s\,X + m \leq x \right) = \int_{-\infty}^{x} \dfrac{1}{|s|}\,f\left(\dfrac{u-m}{s} \right)\,dx.$$
<!-- On pourra remarquer que cela revient à utiliser la méthode avec E(h(X)) du cours, pour h l'indicatrice qu'on est plus petit que x, car P(X in A) = E(1\_A(X)) -->
Ainsi, $s\,X+m$ admet une densité, qui pour tout $x\in\R$ est égale à
$$ \dfrac{1}{|s|}\,f\left(\dfrac{u-m}{s}\right) = \dfrac{1}{\sqrt{2\,\pi}\,|s|}\,\exp\left\{-\dfrac{(x-m)^2}{2\,s^2} \right\}.$$
On reconnaît la densité d'une loi Normale d'espérance $m$ et de variance $s^2$.

### Combinaisons linéaires {.answer #answer-CLIGauss-cl}

2. Commençons par supposer que pour tout $n\in\mathbb{N}^\ast$, $a\in\R^n$ est tel qu'aucune de ses composantes n'est nulle. Nous allons montrer par récurrence sur $n$ que $S_n^a$ suit une loi Normale d'espérance nulle et de variance $\sum_{i = 1}^n a_i^2$. On note cette propriété $(\mathcal{P}_n)$. 

**Initialisation.**

* Si $n = 1$ et $a_1 \neq 0$, alors $S_1^a = a_1\,X_1$ suit une loi Normale centrée de variance $a_1^2$ d'après la question 1; $(\mathcal{P}_1)$ est donc vraie.

* Si $n=2$ et $a_1,a_2 \neq 0$, alors d'après le cours $S_2^a = a_1\,X_1 + a_2\,X_2$ admet une densité, notée $f_n^a$, égale au produit de convolution des densités $f_1$ de $a_1\,X_1$ et $f_2$ de $a_2\,X_2$. En outre, d'après la question 1, pour tout $x\in\R$ on a $f_1(x) = \dfrac{1}{|a_1|}\,f\left(\dfrac{x}{a_1} \right)$ et $f_2(x) = \dfrac{1}{|a_2|}\,f\left(\dfrac{x}{a_2} \right)$. Par conséquent, pour tout $x\in\R$,
\begin{align*}
f_2^a(x) &= \int_{\R} f_1(x-u)\,f_2(u)\,du = \int_\R \dfrac{1}{|a_1|\,|a_2|}\,f\left(\dfrac{x - u}{a_1}\right)\,f\left(\dfrac{u}{a_2}\right)\,du\\
&= \dfrac{1}{\sqrt{a_1^2 +a_2^2}}\,f\left(\dfrac{x}{\sqrt{a_1^2+a_2^2}}\right)\, \int_{\R} \dfrac{\sqrt{a_1^2+a_2^2}}{|a_1|\,|a_2|}\,\dfrac{f\left(\dfrac{x - u}{a_1}\right)}{f\left(\dfrac{x}{\sqrt{a_1^2+a_2^2}}\right)}\,f\left(\dfrac{u}{a_2}\right)\,du.
\end{align*}
Or pour tout $x,u\in\R$ on a
\begin{align*}
\dfrac{f\left(\dfrac{x - u}{a_1}\right)}{f\left(\dfrac{x}{\sqrt{a_1^2+a_2^2}}\right)}\,f\left(\dfrac{u}{a_2}\right) & = \dfrac{1}{\sqrt{2\pi}}\,\dfrac{\exp\left\{-\dfrac{(x-u)^2}{2\,a_1^2} \right\}}{\exp\left\{ -\dfrac{x^2}{2\,(a_1^2+a_2^2)} \right\}}\,\exp\left\{ -\dfrac{u^2}{2\,a_2^2} \right\}\\
& = \dfrac{1}{\sqrt{2\pi}}\,\exp\left\{-\dfrac{1}{2}\,\left( \dfrac{(x-u)^2}{a_1^2} + \dfrac{u^2}{a_2^2} - \dfrac{x^2}{a_1^2+a_2^2} \right) \right\}\\
&= \dfrac{1}{\sqrt{2\pi}}\,\exp\left\{ -\dfrac{\left(a_2^2\,x - (a_1^2 + a_2^2)\,u\right)^2}{2\,a_1^2\,a_2^2\,(a_1^2+a_2^2)} \right\}\\
&= \dfrac{1}{\sqrt{2\pi}}\,\exp\left\{-\dfrac{\left(u - \dfrac{a_2^2\,x}{a_1^2 + a_2^2}\right)^2}{2\,\dfrac{a_1^2\,a_2^2}{a_1^2+a_2^2}}\right\},
\end{align*}
qui multiplié par $\dfrac{\sqrt{a_1^2+a_2^2}}{|a_1|\,|a_2|}$ correspond à la densité d'une loi Normale d'espérance $\dfrac{a_2^2\,x}{a_1^2+a_2^2}$ et de variance $\dfrac{a_1^2\,a_2^2}{a_1^2+a_2^2}$. La précédente intégrale vaut donc $1$ et $(\mathcal{P}_2)$ est vraie.

**Héritage.** Soit maintenant $n\geq 2$, et supposons $(\mathcal{P}_{n-1})$ vraie. Alors $S_n^a = S_{n-1}^{a_{-n}} + a_n\,X_n$, où $a_{-n} := (a_1,\dots,a_{n-1})$. Or $S_{n-1}^{a_{-n}}$ et $a_n\,X_n$ sont des variables gaussiennes centrées, de variances respectives $\sum_{i = 1}^{n-1} a_i^2$ d'après $(\mathcal{P}_{n-1})$ et $a_n^2$ d'après la question 1. Par $(\mathcal{P}_2)$, $S_n^a$ suit donc une loi Normale centrée de variance $\sum_{i = 1}^n a_i^2$.

**Conclusion.** On en conclut que $(\mathcal{P}_n)$ est vraie pour tout $n\in\mathbb{N}^\ast$.


3. Calculons cette covariance :
\begin{align*}
\text{Cov}\left(S_n^a, S_n^b\right) &= \text{Cov}\left(\sum_{i =1}^n a_i\,X_i, \sum_{j = 1}^n b_j\,X_j\right)\\
&= \sum_{i = 1}^n a_i\,b_i\,\mathbb{V}\left(X_i\right) + \sum_{1\leq i\neq j \leq n} a_i\,b_j\,\text{Cov}\left(X_i,X_j\right).
\end{align*}
Or par hypothèse $\mathbb{V}\left(X_i\right) = 1$ pour tout $i\in\{1,\dots,n\}$ et par indépendance on a $\text{Cov}\left(X_i,X_j\right) = 0$ pour tous $i,j \in \{1,\dots,n\}$ tels que $i\neq j$. Ainsi,
$$ \text{Cov}\left(S_n^a, S_n^b\right) = \sum_{i = 1}^n a_i\,b_i $$
qui est nulle ssi $a$ et $b$ sont orthogonaux.


