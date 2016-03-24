# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015-2016.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


import numpy as np
import matplotlib.pyplot as plt


class LogitFuncException(Exception):
    pass

class LogitFunc(object):
    """
    Logistic function implementation:
    https://en.wikipedia.org/wiki/Logistic_function
    """

    def compXVar(self, xstart, xstop, xsize=100):
        if xstart >= xstop:
            raise LogitFuncException("Error: xstart must be greater than xstop...")
        if xsize <= 1:
            raise LogitFuncException("xsize must be greater than 1...")

        return np.linspace(xstart, xstop, xsize)

    def compLogitFunc(self, x, l, x0, k=1):
        """
        x: x values
        x0: x-value of the sigmoid's midpoint
        l: maximum value of the curve
        k: steepness of the curve
        """
        return(l / (1 + np.exp(-k * (x - x0))))

def runTest():

    lf = LogitFunc()

    xstart = -10
    xstop = 10
    xsize = 1000
    x = lf.compXVar(xstart, xstop, xsize=xsize)

    l = 1
    x0 = 0
    k = 1
    y = lf.compLogitFunc(x, l, x0, k=k)

    plt.axhline(y=l/2., color='red', linestyle='--')
    plt.axvline(x=x0, color='red', linestyle='--')

    plt.plot(x, y, linewidth=3)

    ymarg = (l * 10.) / 100.
    plt.ylim([0 - ymarg, l + ymarg])
    plt.xlim([xstart, xstop])

    plt.grid(True)
    plt.title("Logistic function")
    plt.show()

if __name__ == '__main__':
    runTest()
