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
def f(theta_d_theta):
    m=1.0; b=0.0; l=1.0; g=9.81
    theta, d_theta = theta_d_theta
    J = m * l * l
    d2_theta  = - b / J * d_theta 
    d2_theta += - g / l * sin(theta)
    return array([d_theta, d2_theta])

def f_amorti(theta_d_theta):
    m=1.0; b=3.0; l=1.0; g=9.81
    theta, d_theta = theta_d_theta
    J = m * l * l
    d2_theta  = - b / J * d_theta 
    d2_theta += - g / l * sin(theta)
    return array([d_theta, d2_theta])

def Q(f, xs, ys):
    X, Y = meshgrid(xs, ys)
    fx = vectorize(lambda x, y: f([x, y])[0])
    fy = vectorize(lambda x, y: f([x, y])[1])
    return X, Y, fx(X, Y), fy(X, Y)

# Value Graph
# ------------------------------------------------------------------------------
def pendule():
    fig = figure()
    theta = linspace(-1.5 * pi, 1.5 * pi, 100)
    d_theta = linspace(-5.0, 5.0, 100)
    fig.add_subplot(2,1,1)
    grid(True)
    xticks([-pi, 0, pi], [r"$-\pi$", "$0$", r"$\pi$"])
    streamplot(*Q(f, theta, d_theta), color="k") 
    xlabel('$x_1$')
    ylabel('$x_2$')
    #set_ratio(4/3, bottom=0.2, top=0.1, left=0.2)
    fig.add_subplot(2,1,2)
    grid(True)
    xticks([-pi, 0, pi], [r"$-\pi$", "$0$", r"$\pi$"])
    streamplot(*Q(f_amorti, theta, d_theta), color="k") 
    xlabel('$x_1$')
    ylabel('$x_2$')
    #set_ratio(4/3, bottom=0.2, top=0.1, left=0.2)
    save()


if __name__ == "__main__":
  pendule()