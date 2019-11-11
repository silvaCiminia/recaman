#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from scipy.interpolate import interp1d
import seq


def val_plot(data: [],
             max_: int,
             res: int
             ) -> plt:
    # Plot sequence entries to values (with a nice curve)
    x = np.linspace(0, len(data)-1, num=len(data), endpoint=True)
    y = data
    f = interp1d(x, y, kind='cubic')

    curve = np.linspace(0, len(data)-1, num=res*len(data), endpoint=True)
    plt.plot(x, y, 'o', curve, f(curve))

    return plt


def line_plot(data: [],
              max_: int,
              ) -> plt:
    # Plot values as zeroes on numberline, drawing arcs between
    fg, ax = plt.subplots(1, 1)

    # Data plotting
    x = data
    y = [0] * len(data)

    # Alternate thetas for arc plotting
    _v0 = 180
    _v1 = 0

    for i in range(0, len(data)-2):
        # plot arcs between numbers
        p0 = data[i]
        p1 = data[i+1]
        midpoint = (p0 + p1)/2
        diameter = 2 * abs(p0 - midpoint)

        _v0 = abs(_v0-180)
        _v1 = abs(_v1-180)

        arc = patches.Arc([midpoint, 0],
                          width=diameter,
                          height=diameter,
                          theta1=_v0,
                          theta2=_v1)
        ax.add_patch(arc)

    ax.axis([0, max_, -max_/2, max_/2])

    return plt
