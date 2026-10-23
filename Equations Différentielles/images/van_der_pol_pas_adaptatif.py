#!/usr/bin/env python
"""
Euler explicite à pas adaptatif sur l'oscillateur de Van der Pol
    y1' = y2,   y2' = mu (1 - y1^2) y2 - y1,   mu = 10,  y(0) = (2, 0),  t in [0, 60].

Le pas est adapté à chaque itération à partir de l'estimateur d'erreur locale du cours
    ||e^{j+1}|| ~ dt_j/2 ||f(t_{j+1}, x^{j+1}) - f(t_j, x^j)||
avec la règle  dt_new = safety * dt_j * sqrt(Tol_abs / ||e^{j+1}||)  (pas rejeté et retenté
plus petit si l'erreur estimée dépasse la tolérance).

Usage : python van_der_pol_pas_adaptatif.py   ->   van_der_pol_pas_adaptatif.py.pdf
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

# Van der Pol
# ------------------------------------------------------------------------------
MU = 10.0

def f_vdp(t, x):
    y1, y2 = x
    return np.array([y2, MU * (1 - y1 ** 2) * y2 - y1])

# Euler explicite à pas adaptatif (même fonction que dans le notebook)
# ------------------------------------------------------------------------------
def solve_euler_explicit_variable_step(f, x0, t0, tf, dtmin, dtmax, atol, safety=0.9):
    """Renvoie (t, x, dt_utilises) avec x de forme (dim, nb_points)."""
    x0 = np.atleast_1d(np.array(x0, dtype=float))
    t, x, dt = t0, x0.copy(), dtmax
    ts, xs, dts = [t], [x.copy()], []
    while t < tf - 1e-12:
        dt = min(dt, tf - t)
        fx = f(t, x)
        x_next = x + dt * fx
        f_next = f(t + dt, x_next)
        e_next = dt / 2 * np.linalg.norm(f_next - fx)          # estimateur d'erreur locale
        if e_next <= atol or dt <= dtmin * (1 + 1e-9):          # pas accepté
            t, x = t + dt, x_next
            ts.append(t); xs.append(x.copy()); dts.append(dt)
        dt_new = safety * dt * np.sqrt(atol / e_next) if e_next > 0 else dtmax
        dt = min(max(dt_new, dtmin), dtmax)                     # sinon : pas rejeté, on retente
    return np.array(ts), np.array(xs).T, np.array(dts)

# Figure
# ------------------------------------------------------------------------------
def main():
    t, x, dts = solve_euler_explicit_variable_step(
        f_vdp, [2.0, 0.0], 0.0, 60.0, dtmin=1e-6, dtmax=0.2, atol=1e-4)
    print(f"{len(t)} pas, dt min = {dts.min():.1e}, dt max = {dts.max():.1e}")

    width_in = 345.0 / 72.27
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(width_in, 0.38 * width_in))

    ax1.plot(t, x[0], "k-", linewidth=0.8)
    ax1.set_xlabel(r"$t$"); ax1.set_ylabel(r"$y_1$")
    ax1.set_title(r"Solution $y_1(t)$")

    ax2.plot(x[0], x[1], "k-", linewidth=0.8)
    ax2.set_xlabel(r"$y_1$"); ax2.set_ylabel(r"$y_2$")
    ax2.set_title(r"Plan de phase")

    ax3.semilogy(t[1:], dts, "k.", markersize=1.5)
    ax3.set_xlabel(r"$t$"); ax3.set_ylabel(r"${\Delta t}_j$")
    ax3.set_title(r"Pas de temps utilis\'e")

    for ax in (ax1, ax2, ax3):
        ax.grid(True, linewidth=0.3)
    fig.tight_layout(pad=0.3)
    filename = pathlib.Path(__file__)
    fig.savefig(filename.with_suffix(filename.suffix + ".pdf"))

if __name__ == "__main__":
    main()
