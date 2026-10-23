#!/usr/bin/env python
"""
Simulation du système solaire externe (Soleil + Jupiter, Saturne, Uranus,
Neptune, Pluton) par les schémas d'Euler explicite, implicite et symplectique.

Inspiré de la figure 2.4 de Hairer, Lubich & Wanner, *Geometric Numerical
Integration* (données de la table 2.2 du même ouvrage) :
unités astronomiques (UA) pour les longueurs, jours terrestres pour le temps,
masses solaires pour les masses. La masse du Soleil inclut celle des planètes
intérieures.

Usage : python systeme_solaire.py   ->   systeme_solaire.py.pdf
"""

# Python 3 Standard Library
import pathlib

# Third-Party Packages
import numpy as np
from scipy.optimize import fsolve
import matplotlib as mpl; mpl.use("Agg")
import matplotlib.pyplot as plt

# Matplotlib Configuration (identique aux autres figures du poly)
# ------------------------------------------------------------------------------
rc = {
    "text.usetex": True,
    "pgf.preamble": r"\usepackage{amsmath,amsfonts,amssymb}",
    "font.family": "serif",
    "legend.fontsize": 10,
    "axes.titlesize":  10,
    "axes.labelsize":  10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
}
mpl.rcParams.update(rc)

# Données (Hairer, Lubich & Wanner, table 2.2)
# ------------------------------------------------------------------------------
G = 2.95912208286e-4          # constante de gravitation en UA^3 / (jour^2 . masse solaire)

LABELS = ["", "J", "S", "U", "N", "P"]   # Soleil, Jupiter, Saturne, Uranus, Neptune, Pluton

M = np.array([
    1.00000597682,             # Soleil (+ planètes intérieures)
    0.000954786104043,         # Jupiter
    0.000285583733151,         # Saturne
    0.0000437273164546,        # Uranus
    0.0000517759138449,        # Neptune
    1.0 / (1.3e8),             # Pluton
])

Q0 = np.array([
    [ 0.0,         0.0,         0.0       ],
    [-3.5023653,  -3.8169847,  -1.5507963],
    [ 9.0755314,  -3.0458353,  -1.6483708],
    [ 8.3101420, -16.2901086,  -7.2521278],
    [11.4707666, -25.7294829, -10.8169456],
    [-15.5387357, -25.2225594, -3.1902382],
])

V0 = np.array([
    [ 0.0,         0.0,         0.0       ],
    [ 0.00565429, -0.00412490, -0.00190589],
    [ 0.00168318,  0.00483525,  0.00192462],
    [ 0.00354178,  0.00137102,  0.00055029],
    [ 0.00288930,  0.00114527,  0.00039677],
    [ 0.00276725, -0.00170702, -0.00136504],
])

# Dynamique : H(q, p) = sum_i |p_i|^2 / (2 m_i) - G sum_{i<k} m_i m_k / |q_i - q_k|
# ------------------------------------------------------------------------------
def acceleration(q):
    """Accélérations gravitationnelles  a_i = -G sum_{k != i} m_k (q_i - q_k)/|q_i - q_k|^3."""
    d = q[:, None, :] - q[None, :, :]                    # d[i, k] = q_i - q_k
    r = np.linalg.norm(d, axis=2)
    np.fill_diagonal(r, np.inf)                          # pas d'auto-interaction
    return -G * np.einsum("k,ikj->ij", M, d / r[:, :, None] ** 3)

def energie(q, v):
    """Hamiltonien H(q, p) avec p = m v."""
    cinetique = 0.5 * np.sum(M[:, None] * v ** 2)
    d = q[:, None, :] - q[None, :, :]
    r = np.linalg.norm(d, axis=2)
    iu = np.triu_indices(len(M), k=1)
    potentiel = -G * np.sum(M[iu[0]] * M[iu[1]] / r[iu])
    return cinetique + potentiel

# Schémas à un pas, sur l'état (q, v) avec p = m v
# ------------------------------------------------------------------------------
def euler_explicite(q, v, h):
    return q + h * v, v + h * acceleration(q)

def euler_implicite(q, v, h):
    """q^{n+1} = q^n + h v^{n+1},  v^{n+1} = v^n + h a(q^{n+1}).
    En éliminant v^{n+1}, on résout le système non linéaire en q^{n+1} :
        F(q^{n+1}) = q^{n+1} - q^n - h v^n - h^2 a(q^{n+1}) = 0
    par une méthode de Newton (scipy), initialisée par un pas d'Euler explicite."""
    def F(x):
        qn = x.reshape(q.shape)
        return (qn - q - h * v - h ** 2 * acceleration(qn)).ravel()
    qn = fsolve(F, (q + h * v).ravel(), xtol=1e-13).reshape(q.shape)
    return qn, v + h * acceleration(qn)

def euler_symplectique(q, v, h):
    """Euler symplectique : q explicite, puis v évalué en la nouvelle position."""
    qn = q + h * v
    return qn, v + h * acceleration(qn)

def simuler(schema, h, T):
    n = int(round(T / h))
    q, v = Q0.copy(), V0.copy()
    traj = np.empty((n + 1,) + q.shape)
    H = np.empty(n + 1)
    traj[0], H[0] = q, energie(q, v)
    for j in range(n):
        q, v = schema(q, v, h)
        traj[j + 1], H[j + 1] = q, energie(q, v)
    return traj, H

# Figure
# ------------------------------------------------------------------------------
T_COURT = 200_000.0          # jours (~ 550 ans)
T_LONG = 2_000_000.0         # jours (~ 5 500 ans), pour le schéma symplectique

CAS = [
    (euler_explicite,    10.0,  T_COURT, r"Euler explicite, $\Delta t = 10$ j",      "k:"),
    (euler_implicite,    10.0,  T_COURT, r"Euler implicite, $\Delta t = 10$ j",      "k--"),
    (euler_symplectique, 100.0, T_LONG,  r"Euler symplectique, $\Delta t = 100$ j", "k-"),
]

def sci(x):
    """Ecriture LaTeX de x en notation scientifique : +1.2 \\cdot 10^{-3}."""
    mantisse, exposant = f"{x:+.1e}".split("e")
    return rf"{mantisse} \cdot 10^{{{int(exposant)}}}"

def main():
    width_in = 345.0 / 72.27                             # largeur du texte LaTeX (345 pt)
    fig, axes = plt.subplots(2, 2, figsize=(width_in, 0.98 * width_in))
    ax_energie = axes[1, 1]

    for ax, (schema, h, T, titre, style) in zip(axes.flat, CAS):
        traj, H = simuler(schema, h, T)
        # Orbites dans le référentiel du Soleil (positions relatives), projetées dans le plan (x, y)
        rel = traj - traj[:, :1, :]
        lw = 0.4 if T <= T_COURT else 0.2
        for i in range(1, len(M)):
            ax.plot(rel[:, i, 0], rel[:, i, 1], "k-", linewidth=lw)
            ax.plot(rel[-1, i, 0], rel[-1, i, 1], "ko", markersize=2.5)
            ax.annotate(LABELS[i], rel[-1, i, :2], xytext=(3, 3),
                        textcoords="offset points", fontsize=8)
        ax.plot(0, 0, "ko", markersize=4)                                # Soleil
        ax.set_title(titre + "\n" + rf"$T = {T:,.0f}$ j $\approx$ {T / 365.25:,.0f} ans"
                     .replace(",", r"\,"), fontsize=8)
        ax.set_xlim(-50, 50); ax.set_ylim(-50, 50)
        ax.set_aspect("equal")
        ax.set_xticks([]); ax.set_yticks([])
        # Dérive relative d'énergie (signée) en fonction du temps. Echelle "symlog" :
        # linéaire entre -1e-2 et 1e-2 (où oscille le schéma symplectique), log au-delà.
        # Pour rester lisible sur des milliers de révolutions, on trace par blocs de
        # temps la bande [min, max] de la dérive (gris) et sa moyenne (trait).
        t = np.arange(len(H)) * h / 365.25
        derive = (H - H[0]) / abs(H[0])
        bloc = max(1, len(H) // 400)
        n = (len(H) // bloc) * bloc
        tb = t[:n].reshape(-1, bloc).mean(axis=1)
        db = derive[:n].reshape(-1, bloc)
        ax_energie.fill_between(tb, db.min(axis=1), db.max(axis=1), color="0.75", linewidth=0)
        ax_energie.plot(tb, db.mean(axis=1), style, linewidth=0.8, label=titre.split(",")[0])

    ax_energie.set_yscale("symlog", linthresh=1e-2, linscale=0.6)
    ax_energie.axhline(0, color="0.8", linewidth=0.5, zorder=0)
    ax_energie.set_xlabel(r"$t$ (ann\'ees)", fontsize=8)
    ax_energie.set_ylabel(r"$(H(t) - H(0)) / |H(0)|$", fontsize=8)
    ax_energie.set_title(r"D\'erive relative de l'\'energie", fontsize=8)
    ax_energie.tick_params(labelsize=7)
    ax_energie.legend(fontsize=7, loc="upper right", frameon=False)
    ax_energie.set_box_aspect(1)

    fig.tight_layout(pad=0.3)
    filename = pathlib.Path(__file__)
    fig.savefig(filename.with_suffix(filename.suffix + ".pdf"))

if __name__ == "__main__":
    main()
