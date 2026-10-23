#!/usr/bin/env python
"""
Frottement sec :  x' = -sign(x), x(0) = 1,  simulé par Euler explicite (chattering autour
de 0) et Euler implicite (résolu exactement : x^{j+1} = sign(x^j) max(|x^j| - dt, 0),
qui s'arrête exactement en 0), pour deux pas de temps.

Usage : python frottement_sec.py   ->   frottement_sec.py.pdf
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
    "axes.titlesize":  9,
    "axes.labelsize":  9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
}
mpl.rcParams.update(rc)

X0, T = 1.0, 3.0

def euler_explicite(dt):
    n = int(round(T / dt))
    x = np.empty(n + 1); x[0] = X0
    for j in range(n):
        x[j + 1] = x[j] - dt * np.sign(x[j])
    return np.arange(n + 1) * dt, x

def euler_implicite(dt):
    n = int(round(T / dt))
    x = np.empty(n + 1); x[0] = X0
    for j in range(n):
        x[j + 1] = np.sign(x[j]) * max(abs(x[j]) - dt, 0.0)   # solution exacte de x^{j+1} + dt sign(x^{j+1}) = x^j
    return np.arange(n + 1) * dt, x

def main():
    width_in = 345.0 / 72.27
    fig, axes = plt.subplots(1, 2, figsize=(width_in, 0.42 * width_in), sharey=True)
    t_ex = np.linspace(0, T, 300)
    for ax, dt in zip(axes, (0.3, 0.05)):
        ax.plot(t_ex, np.maximum(X0 - t_ex, 0), "-", color="0.7", linewidth=2.5, label="solution exacte")
        t, x = euler_explicite(dt)
        ax.plot(t, x, "k:", marker=".", markersize=3, linewidth=0.8, label="Euler explicite")
        t, x = euler_implicite(dt)
        ax.plot(t, x, "k-", marker=".", markersize=3, linewidth=0.8, label="Euler implicite")
        ax.set_title(rf"$\Delta t = {dt:g}$")
        ax.set_xlabel(r"$t$")
        ax.grid(True, linewidth=0.3)
    axes[0].set_ylabel(r"$x$")
    axes[0].legend(loc="upper right", frameon=False)
    fig.tight_layout(pad=0.3)
    filename = pathlib.Path(__file__)
    fig.savefig(filename.with_suffix(filename.suffix + ".pdf"))

if __name__ == "__main__":
    main()
