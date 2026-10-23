#!/usr/bin/env python
"""
Ordre de convergence expérimental des schémas à un pas du cours
(Euler explicite, Euler implicite, Heun, trapèzes, point milieu, Runge-Kutta 4)
sur le problème test  x' = -x, x(0) = 1, t in [0, 2]  de solution x(t) = exp(-t).

On trace l'erreur globale  max_j |x^j - x(t_j)|  en fonction du pas (log-log) :
la pente est l'ordre de convergence. Pour les pas les plus petits, RK4 atteint
le niveau des erreurs d'arrondi et la pente casse.

Le problème étant linéaire, les schémas implicites sont résolus exactement
(pas de solveur non linéaire, dont la tolérance polluerait les petites erreurs).

Usage : python ordre_schemas.py   ->   ordre_schemas.py.pdf
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

# Problème test : x' = f(t, x) = -x
# ------------------------------------------------------------------------------
def f(t, x):
    return -x

def x_exact(t):
    return np.exp(-t)

T0, TF, X0 = 0.0, 2.0, 1.0

# Schémas à un pas : x^{j+1} = step(f, t_j, x^j, dt)
# ------------------------------------------------------------------------------
def step_euler_explicite(f, t, x, dt):
    return x + dt * f(t, x)

def step_heun(f, t, x, dt):
    k1 = f(t, x)
    k2 = f(t + dt, x + dt * k1)
    return x + dt / 2 * (k1 + k2)

def step_rk4(f, t, x, dt):
    k1 = f(t, x)
    k2 = f(t + dt / 2, x + dt / 2 * k1)
    k3 = f(t + dt / 2, x + dt / 2 * k2)
    k4 = f(t + dt, x + dt * k3)
    return x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

# Schémas implicites, résolus exactement pour f(t, x) = -x
def step_euler_implicite(f, t, x, dt):
    return x / (1 + dt)                                  # x_{n+1} = x_n - dt x_{n+1}

def step_trapezes(f, t, x, dt):
    return x * (1 - dt / 2) / (1 + dt / 2)               # x_{n+1} = x_n - dt/2 (x_n + x_{n+1})

def step_point_milieu(f, t, x, dt):
    return x * (1 - dt / 2) / (1 + dt / 2)               # x_{n+1} = x_n - dt (x_n + x_{n+1})/2 : idem trapèzes ici

SCHEMAS = [
    # (nom, step, ordre attendu, style)
    ("Euler explicite",  step_euler_explicite, 1, "o-"),
    ("Euler implicite",  step_euler_implicite, 1, "s--"),
    ("Heun",             step_heun,            2, "^-"),
    (r"Trap\`ezes",      step_trapezes,        2, "v--"),
    ("Point milieu",     step_point_milieu,    2, "d:"),
    ("Runge-Kutta 4",    step_rk4,             4, "*-"),
]

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
    dts = np.logspace(-1, -4, 13)
    width_in = 345.0 / 72.27
    fig, ax = plt.subplots(figsize=(width_in, 0.85 * width_in))

    for nom, step, p, style in SCHEMAS:
        errs = np.array([erreur_globale(step, dt) for dt in dts])
        # pente estimée sur les pas les plus grands (hors régime d'arrondi)
        pente = np.polyfit(np.log(dts[:6]), np.log(errs[:6]), 1)[0]
        ax.loglog(dts, errs, style, color="k", markersize=4, linewidth=0.8,
                  markerfacecolor="w" if "-" in style else "k",
                  label=rf"{nom} (pente {pente:.2f}, ordre {p})")

    for p in (1, 2, 4):
        ax.loglog(dts, 0.3 * dts ** p, "-", color="0.75", linewidth=0.6, zorder=0)
        ax.annotate(rf"$\Delta t^{p}$", (dts[-1], 0.3 * dts[-1] ** p), xytext=(-14, 0),
                    textcoords="offset points", fontsize=8, color="0.4", va="center")

    ax.set_xlabel(r"$\Delta t$")
    ax.set_ylabel(r"$\max_j |x^j - x(t_j)|$")
    ax.grid(True, which="major", linewidth=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=False, fontsize=7)
    fig.tight_layout(pad=0.3)
    filename = pathlib.Path(__file__)
    fig.savefig(filename.with_suffix(filename.suffix + ".pdf"))

if __name__ == "__main__":
    main()
