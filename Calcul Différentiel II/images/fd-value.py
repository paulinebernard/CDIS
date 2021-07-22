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
    width_in = 345.0 / 72.0
    height_in = (1.0 - left - right)/(1.0 - bottom - top) * width_in / ratio
    gcf().set_size_inches((width_in, height_in))
    gcf().subplots_adjust(bottom=bottom, top=1.0-top, left=left, right=1.0-right)

# Forward Differentiation Scheme
# ------------------------------------------------------------------------------
def FD(f, x, h):
    "Forward Difference"
    return (f(x+h) - f(x)) / h

# Test Function
# ------------------------------------------------------------------------------
def f(x):
    return exp(x)

# Value Graph
# ------------------------------------------------------------------------------
def fd_value():
    h = logspace(-18, 6, 1000)
    clf()
    axis([1e-18, 1e2, -0.3, 2.3])
    xscale("log")
    yticks([0.0, 1.0, 2.0])
    xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    plot(h, FD(f, 0.0, h), "k", label="$\mathrm{FD}(\exp, 0, h)$")
    plot([h[0], h[-1]],[1.0, 1.0], "k--", label=r"$[\exp'(0)]$",alpha=1.0) 
    plot(h, 2**(-52) / h, "k:", label=r"$[\varepsilon/h]$")
    legend()
    set_ratio(sqrt(3.0), bottom=0.15, top=0.1)
    xlabel("$h$")
    title(r"Graphe de $h \mapsto \mathrm{FD}(\exp, 0, h)$")
    save()

if __name__ == "__main__":
  fd_value()

