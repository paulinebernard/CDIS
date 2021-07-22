#!/usr/bin/env python

# Python 3.7 Standard Library
import pathlib
import sys

# Third-Party Packages
from mpl_toolkits.mplot3d import Axes3D
from numpy import *; seterr(all="ignore")
import matplotlib as mpl; mpl.use("Agg") 
from matplotlib.pyplot import *
from scipy.integrate import solve_ivp

# Matplotlib Configuration
# ------------------------------------------------------------------------------
rc = {
    "text.usetex": True,
    "pgf.preamble": r"\usepackage{amsmath,amsfonts,amssymb}", 
    "font.family": "serif",
    #"font.serif": [],      # use latex default serif font
    #"font.sans-serif": [], # use a specific sans-serif font
    "legend.fontsize": 10, # "medium" / 10 (equivalent)
    "axes.titlesize":  10,
    "axes.labelsize":  10,
    "xtick.labelsize": 10, # alt: "small",
    "ytick.labelsize": 10, # alt: "small",
}
mpl.rcParams.update(rc)

# Save the Picture
# ------------------------------------------------------------------------------
def save():
    filename = pathlib.Path(__file__)
    output = filename.with_suffix(filename.suffix + ".pdf") 
    savefig(output)

# Layout Helper
# ------------------------------------------------------------------------------
def set_ratio(ratio, bottom=0.1, top=0.1, left=0.1, right=0.1):
    # The width of the standard LaTeX document is 345.0 pt.
    width_in = 345.0 / 72.0
    height_in = (1.0 - left - right)/(1.0 - bottom - top) * width_in / ratio
    gcf().set_size_inches((width_in, height_in))
    gcf().subplots_adjust(bottom=bottom, top=1.0-top, left=left, right=1.0-right)

# Function
# ------------------------------------------------------------------------------
def fun(t, y):
    sigma = 10; rho = 28; beta = 8/3
    x1, x2, x3 = y
    return array([sigma*(x2-x1), rho*x1-x2-x1*x3, x1*x2-beta*x3])

# Value Graph
# ------------------------------------------------------------------------------
def attracteur_lorenz():
    options = {"max_step": 0.01, "atol"    : 1e-6, "rtol"    : 1e9, "dense_output" : True}
    t_span = [0.0, 50.0]
    y0 = [1.0, 0.0 ,0.0]
    result = solve_ivp(fun=fun, t_span=t_span, y0=y0,**options)
    r_t = result["t"]
    x_1 = result["y"][0]
    x_2 = result["y"][1]
    x_3 = result["y"][2] 
    fig = figure()
    ax = fig.gca(projection='3d')
    ax.plot(x_1,x_2,x_3)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('$x_3$')
    save()


if __name__ == "__main__":
  attracteur_lorenz()