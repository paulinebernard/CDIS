#!/usr/bin/env python

# Python 3.7 Standard Library
import pathlib
import sys

# Third-Party Packages
from numpy import *; seterr(all="ignore")
import matplotlib as mpl; mpl.use("Agg")
from matplotlib.pyplot import *

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
    width_in = 345.0 / 100.0
    height_in = (1.0 - left - right)/(1.0 - bottom - top) * width_in / ratio
    gcf().set_size_inches((width_in, height_in))
    gcf().subplots_adjust(bottom=bottom, top=1.0-top, left=left, right=1.0-right)

# Function
# ------------------------------------------------------------------------------

alpha = 2/3; beta = 4/3; gamma = 1; delta = 1

def f(x):
    x1, x2 = x
    dx1  = x1*(alpha -beta*x2)
    dx2  = -x2*(gamma-delta*x1)
    return array([dx1, dx2])

def Q(f, xs, ys):
    X, Y = meshgrid(xs, ys)
    fx = vectorize(lambda x, y: f([x, y])[0])
    fy = vectorize(lambda x, y: f([x, y])[1])
    return X, Y, fx(X, Y), fy(X, Y)

# Value Graph
# ------------------------------------------------------------------------------
def cycle_limiteII_courbes():
    fig = figure()
    x1 = linspace(0.1, 2, 1000)
    x2 = linspace(0.1, 1.5, 1000)
    X1, X2 = np.meshgrid(x1, x2)
    Z = delta*X1-gamma*np.log(X1)+beta*X2-alpha*np.log(X2)
    contour(X1,X2,Z,levels=10)
    grid(True)
    #axis('equal')
    xbar = np.array([gamma/delta,alpha/beta])
    scatter(xbar[0],xbar[1]) 
    xlabel('$x_1$')
    ylabel('$x_2$')
    #set_ratio(4/3, bottom=0.2, top=0.1, left=0.2)
    save()


if __name__ == "__main__":
  cycle_limiteII_courbes()