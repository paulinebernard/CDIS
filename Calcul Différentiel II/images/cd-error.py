#!/usr/bin/env python

# Python 3.7 Standard Library
import pathlib
import sys

# Third-Party Packages
from numpy import *; seterr(all="ignore")
import matplotlib as mpl; mpl.use("Agg")
import matplotlib.font_manager
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
def set_ratio(ratio, scale=1.0, bottom=0.1, top=0.1, left=0.1, right=0.1):
    # The width of the standard LaTeX document is 345.0 pt.
    width_in = 345.0 / 72.0 * scale
    height_in = (1.0 - left - right)/(1.0 - bottom - top) * width_in / ratio
    gcf().set_size_inches((width_in, height_in))
    gcf().subplots_adjust(bottom=bottom, top=1.0-top, left=left, right=1.0-right)


# Forward and Central Differentiation Schemes
# ------------------------------------------------------------------------------
def FD(f, x, h):
    "Forward Difference"
    return (f(x+h) - f(x)) / h

def CD(f, x, h):
    "Central Difference"
    return 0.5 * (f(x+h) - f(x-h)) / h

# Test Function
# ------------------------------------------------------------------------------
def f(x):
    return exp(x)

# Error Graph
# ------------------------------------------------------------------------------
def cd_error():
    h = logspace(-18, 6, 1000)
    clf()
    axis([1e-18, 1e6, 1e-14, 1e2])
    y_2_x_ratio = 16 / 24
    xscale("log")
    yscale("log")
    yticks([1e-12, 1e-8, 1e-4, 1e0], ha="left")
    gca().get_yaxis().set_tick_params(pad=25, direction="out")
    xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    plot(h, abs(1.0 - FD(f, 0.0, h)), "k", color="0.75", label="erreur de FD")
    plot(h, abs(1.0 - CD(f, 0.0, h)), "k", color="0.00", label="erreur de CD")
    title("Graphe de $h \mapsto [|\mathrm{CD}(\exp, 0, h) -\exp'(0)|]$")
    set_ratio(1.0, scale=1, bottom=-0.05, top=-0.1)
    xlabel("$h$")
    gca().set_aspect(1.0)
    #gcf().set_figwidth(width_in)
    extra = 1.2
    #gcf().set_figheight(width_in * y_2_x_ratio)
    #gcf().subplots_adjust(bottom=0.05)
    legend(loc="center right")
    grid(True)
    save()

if __name__ == "__main__":
  cd_error()

