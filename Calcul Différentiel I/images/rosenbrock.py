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
    "pgf.preamble": [r"\usepackage{amsmath,amsfonts,amssymb}"], 
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

def contour_demo():
    delta = 0.025
    x = arange(-0.125, 3.125 + delta, delta)
    y = arange(-0.125, 2.125 + delta, delta)
    X, Y = meshgrid(x, y)
    Z = 1 * (Y*Y - X)**2 + (X - 1)**2

    gdelta = 0.25
    Xg, Yg = meshgrid(arange(0, 3+gdelta, gdelta), arange(0, 2+gdelta, gdelta))
    Gx = - 2 * (Yg*Yg - Xg) + 2*(Xg-1)
    Gy = 2*(Yg*Yg-Xg)*2*Yg 


    fig, ax = subplots()
    if True:
        CS = ax.contour(X, Y, Z, colors="grey", linestyles="dashed", linewidths=0.5, levels = [0.25, 0.5, 1.0, 2.0, 4.0, 8, 16, 32, 64, 128])
        fmt = {}
        for l in CS.levels:
            fmt[l] = f"$2^{{{int(log2(l))}}}$"
        ax.clabel(CS, CS.levels, inline=1, fontsize=10, fmt=fmt)#, fmt='%1.1f')

    quiver(Xg, Yg, Gx, Gy, scale=100, width=0.005, headwidth=3, headlength=5, headaxislength=4.5, zorder=3)

    xlim(-0.125, 3.125); 
    xticks([0, 1, 2, 3])
    ylim(-0.125, 2.125)
    yticks([0, 1, 2])
    xlabel("$x_1$"); ylabel("$x_2$")
    set_ratio(ratio=16/9, bottom=0.15, top=0.0)
    gca().set_aspect(1.0)
    #grid(True)
    save()

if __name__ == "__main__":
    contour_demo()

