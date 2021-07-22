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

# Function
# ------------------------------------------------------------------------------
def f(t,x0):
    return x0/(1-x0*t)

# Value Graph
# ------------------------------------------------------------------------------
def explosion_temps_fini():
    t = linspace(0,1,10)
    plot(t,0*t,'r', label = "$x_0=0$")
    grid()
    list_x0 = [1,2]
    #list_legend = array(["$x_0=0$"])
    for x0 in list_x0:
      t = linspace(0,1/x0,100)
      plot(t,f(t,x0), label = "$x_0=$ "+ str(x0))
      #new_legend = array(["$x_0=$ "+ str(x0)])
      #list_legend = concatenate([list_legend,new_legend])  
    yticks([0.0, 1.0, 2.0, 5.0,10.0])
    axis([0,1,-0.1,15])
    legend()
    #legend(list_legend)
    xlabel('$t$')
    ylabel('$x(t)$')
    save()


if __name__ == "__main__":
    explosion_temps_fini()