#!/usr/bin/env python
"""
Erreur globale du schéma de Runge-Kutta 4 sur  x' = -x, x(0) = 1, t in [0, 2]
en fonction du pas, sur une plage de pas assez large pour voir les deux régimes :
  - pour les grands pas, l'erreur de troncature domine : erreur ~ c_v dt^4,
  - pour les petits pas, les erreurs d'arrondi s'accumulent : erreur ~ S T eps / dt.
Le pas optimal est au point de rencontre des deux asymptotes.

Usage : python pas_optimal.py   ->   pas_optimal.py.pdf   (quelques dizaines de secondes)
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
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
}
mpl.rcParams.update(rc)

# Problème test et schéma
# ------------------------------------------------------------------------------
T0, TF, X0 = 0.0, 2.0, 1.0

def f(t, x):
    return -x

def x_exact(t):
    return np.exp(-t)

def step_rk4(f, t, x, dt):
    k1 = f(t, x)
    k2 = f(t + dt / 2, x + dt / 2 * k1)
    k3 = f(t + dt / 2, x + dt / 2 * k2)
    k4 = f(t + dt, x + dt * k3)
    return x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

def erreur_globale(step, dt):
    """max_j |x^j - x(t_j)| sur [T0, TF] à pas constant dt (dernier pas ajusté pour tomber sur TF)."""
    n = int(np.ceil((TF - T0) / dt - 1e-12))
    t, x, err = T0, X0, 0.0
    for j in range(n):
        h = min(dt, TF - t)
        x = step(f, t, x, h)
        t += h
        err = max(err, abs(x - x_exact(t)))
    return err

# Figure
# ------------------------------------------------------------------------------
def main():
    dts = np.logspace(-1, -6, 21)
    errs = np.array([erreur_globale(step_rk4, dt) for dt in dts])
    eps = np.finfo(float).eps

    width_in = 345.0 / 72.27
    fig, ax = plt.subplots(figsize=(width_in, 0.65 * width_in))
    ax.loglog(dts, errs, "k*-", markersize=5, linewidth=0.8, label="Runge-Kutta 4")

    # Asymptotes : troncature c_v dt^4 (c_v ajusté sur le premier point) et arrondi ~ T eps / dt
    c_v = errs[0] / dts[0] ** 4
    ax.loglog(dts, c_v * dts ** 4, "--", color="0.5", linewidth=0.7, label=r"$c_v\,\Delta t^{4}$")
    ax.loglog(dts, (TF - T0) * eps / dts, ":", color="0.5", linewidth=0.9,
              label=r"$T\varepsilon / \Delta t$ (arrondi)")
    dt_opt = dts[np.argmin(errs)]
    ax.axvline(dt_opt, color="0.8", linewidth=0.6, zorder=0)
    ax.annotate(r"$\Delta t_{opt}$", (dt_opt, 2e-16), xytext=(4, 0),
                textcoords="offset points", fontsize=8, color="0.4", va="bottom")
    ax.set_ylim(1e-16, 1e-6)

    ax.set_xlabel(r"$\Delta t$")
    ax.set_ylabel(r"$\max_j |x(t_j) - \hat{x}^j|$")
    ax.grid(True, which="major", linewidth=0.3)
    ax.legend(loc="upper center", frameon=False)
    fig.tight_layout(pad=0.3)
    filename = pathlib.Path(__file__)
    fig.savefig(filename.with_suffix(filename.suffix + ".pdf"))

if __name__ == "__main__":
    main()
