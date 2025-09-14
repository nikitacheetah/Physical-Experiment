from experimental_data import *

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.interpolate import make_interp_spline


R = 0.15
dR = 0.0005
dTeto = 15
dF = 0.1

def PlotCycle(name, vars):
    for i in range(3):
        theta = vars[i][0]
        F_str = vars[i][1]
        F = np.array([float(f) for f in F_str.split()])


        M = F * R
        dM = F * dR + R * dF
        dT = np.array([dTeto] * len(theta))

        phi_smooth = np.linspace(min(theta), max(theta), 200)
        M_smooth = make_interp_spline(theta, M)(phi_smooth)

        plt.scatter(theta, M, label=f"Кривая {i+1}")
        plt.plot(phi_smooth, M_smooth)
        plt.errorbar(theta, M, xerr = dT, yerr = dM, ecolor='red', capsize=6)

    plt.title(name)

    plt.legend()
    plt.grid()
    plt.show()



for i in ["Алюминий", "Латунь", "Медь"]:
    PlotCycle(i, RESULTS[i])