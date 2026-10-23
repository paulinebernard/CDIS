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
def f(xy):
    x, y = xy
    q = x**2 + y**2 * (1 + (x**2 + y**2)**2) 
    dx = (x**2 * (y - x) + y**5) / q
    dy = y**2 * (y - 2*x) / q
    return array([dx, dy])

def Q(f, xs, ys):
    X, Y = meshgrid(xs, ys)
    fx = vectorize(lambda x, y: f([x, y])[0])
    fy = vectorize(lambda x, y: f([x, y])[1])
    return X, Y, fx(X, Y), fy(X, Y)

# Value Graph
# ------------------------------------------------------------------------------
def vinograd():
    figure()
    x = y = linspace(-1.0, 1.0, 1000)
    streamplot(*Q(f, x, y), color="k") 
    xticks([-1, 0, 1])
    plot([0], [0], "k.", ms=10.0)
    xlabel('$x_1$')
    ylabel('$x_2$')
    set_ratio(4/3, bottom=0.2, top=0.1, left=0.2)
    save()


if __name__ == "__main__":
  vinograd()