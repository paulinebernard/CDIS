#!/usr/bin/env python
"""
Oscillateur harmonique  x1' = x2, x2' = -w^2 x1, x(0) = (1, 0)  simulé par
Euler explicite, Euler implicite et Euler symplectique (exercice *Euler symplectique*).

A gauche : trajectoires dans le plan de phase (la vraie solution est le cercle).
A droite : énergie  E = w^2 x1^2 + x2^2  le long des solutions numériques, et, pour le
schéma symplectique, la quantité conservée  E + dt w^2 x1 x2  (question 2).

Usage : python oscillateur_symplectique.py   ->   oscillateur_symplectique.py.pdf
"""

# Python 3 Standard Library
import pathlib

# Third-Party Packages
import numpy as np
import matplotlib as mpl; mpl.use("Agg")
import matplotlib.pyplot as plt

# Matplotlib Configuration (identique aux autres figures du poly)
# ------------------------------------------------------------------------------
rc = {
    "text.usetex": True,
    "pgf.preamble": r"\usepackage{amsmath,amsfonts,amssymb}",
    "font.family": "serif",
    "legend.fontsize": 8,
    "axes.titlesize":  10,
    "axes.labelsize":  10,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
}
mpl.rcParams.update(rc)

# Paramètres
# ------------------------------------------------------------------------------
W, DT, T = 1.0, 0.1, 20.0
X0 = np.array([1.0, 0.0])

# Schémas : x^{j+1} = A x^j (voir le corrigé des questions 1 et 2)
# ------------------------------------------------------------------------------
A_EXPLICITE = np.array([[1.0, DT], [-DT * W ** 2, 1.0]])
A_IMPLICITE = np.linalg.inv(np.array([[1.0, -DT], [DT * W ** 2, 1.0]]))
A_SYMPLECTIQUE = np.array([[1.0, DT], [-DT * W ** 2, 1.0 - DT ** 2 * W ** 2]])

def simuler(A):
    n = int(round(T / DT))
    x = np.empty((n + 1, 2))
    x[0] = X0
    for j in range(n):
        x[j + 1] = A @ x[j]
    return x

SCHEMAS = [
    ("Euler explicite",    A_EXPLICITE,    "k:"),
    ("Euler implicite",    A_IMPLICITE,    "k--"),
    ("Euler symplectique", A_SYMPLECTIQUE, "k-"),
]

# Figure
# ------------------------------------------------------------------------------
def main():
    width_in = 345.0 / 72.27
    fig, (ax_phase, ax_energie) = plt.subplots(1, 2, figsize=(width_in, 0.56 * width_in))
    t = np.arange(int(round(T / DT)) + 1) * DT

    # Vraie solution : cercle de rayon 1 (w = 1), énergie constante
    theta = np.linspace(0, 2 * np.pi, 400)
    ax_phase.plot(np.cos(theta), np.sin(theta), "-", color="0.7", linewidth=2.5, label="solution exacte")
    ax_energie.axhline(W ** 2, color="0.7", linewidth=2.5, label="solution exacte")

    for nom, A, style in SCHEMAS:
        x = simuler(A)
        ax_phase.plot(x[:, 0], x[:, 1], style, linewidth=0.8, label=nom)
        ax_energie.plot(t, W ** 2 * x[:, 0] ** 2 + x[:, 1] ** 2, style, linewidth=0.8, label=nom)
    # Quantité conservée par le schéma symplectique (question 2)
    x = simuler(A_SYMPLECTIQUE)
    ax_energie.plot(t, W ** 2 * x[:, 0] ** 2 + x[:, 1] ** 2 + DT * W ** 2 * x[:, 0] * x[:, 1],
                    "-", color="0.4", linewidth=0.6,
                    label=r"$\omega^2 x_1^2 + x_2^2 + \Delta t\,\omega^2 x_1 x_2$ (sympl.)")

    ax_phase.set_xlabel(r"$x_1$"); ax_phase.set_ylabel(r"$x_2$")
    ax_phase.set_aspect("equal")
    ax_phase.set_xlim(-3, 3); ax_phase.set_ylim(-3, 3)
    ax_phase.set_title(r"Plan de phase", fontsize=9)

    ax_energie.set_yscale("log")
    ax_energie.set_xlabel(r"$t$"); ax_energie.set_ylabel(r"$\omega^2 x_1^2 + x_2^2$")
    ax_energie.set_title(r"\'Energie", fontsize=9)
    # Légende commune sous les deux panneaux
    handles, labels = ax_energie.get_legend_handles_labels()
    fig.legend(handles, labels, fontsize=7, loc="lower center", ncol=3, frameon=False,
               bbox_to_anchor=(0.5, -0.02))

    fig.suptitle(rf"$\omega = {W:g}$, $\Delta t = {DT:g}$, $x(0) = (1, 0)$", fontsize=9)
    fig.tight_layout(pad=0.3, rect=(0, 0.12, 1, 1))
    filename = pathlib.Path(__file__)
    fig.savefig(filename.with_suffix(filename.suffix + ".pdf"))

if __name__ == "__main__":
    main()
