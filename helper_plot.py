import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import torch
from sklearn.mixture import GaussianMixture
import torch.distributions as distribution
from matplotlib.patches import Ellipse


def hdr_plot_style():
    plt.style.use("dark_background")
    mpl.rcParams.update({"font.size": 18, "lines.linewidth": 3, "lines.markersize": 15})

    # avoid type 3 (i.e. bitmap) fonts in figures
    mpl.rcParams["ps.useafm"] = True
    mpl.rcParams["pdf.use14corefonts"] = True
    mpl.rcParams["text.usetex"] = False
    mpl.rcParams["font.family"] = "sans-serif"
    mpl.rcParams["font.sans-serif"] = "Courier New"

    # set colors cycle
    colors = mpl.cycler("color", ["#3388BB", "#EE6666", "#9988DD", "#EECC55", "#88BB44", "#FFBBBB"])
    plt.rc("legend", facecolor="#666666EE", edgecolor="white", fontsize=16)
    plt.rc("grid", color="white", linestyle="solid")
    plt.rc("text", color="white")
    plt.rc("xtick", direction="out", color="white")
    plt.rc("ytick", direction="out", color="white")
    plt.rc("patch", edgecolor="E6E6E6")