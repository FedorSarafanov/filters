# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.backends.backend_pgf import FigureCanvasPgf
from scipy.interpolate import spline
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)
pgf_with_latex = {
    "pgf.texsystem": "xelatex",         # use Xelatex which is TTF font aware
}

mpl.rcParams.update(pgf_with_latex)
plt.rc('text', usetex=True)
plt.rc('font', family='serif', serif = 'CMU Serif', size = 12)
plt.rcParams['text.latex.preamble'] = [
            r'\usepackage{amsmath}',
            r'\usepackage{amsfonts}',
            r'\usepackage{graphicx}',
            r'\usepackage[english,russian]{babel}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            ]
g = np.genfromtxt('task2(exp).csv',delimiter=';')
spline = np.genfromtxt('task2.csv',delimiter=';')
amount = g[:,0]
tau = g[:,1]
x1 = spline[0:,0]
y1 = spline[0:,1]
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(121)
ax.grid(which='both')
ax.plot(x1,y1,color = '#FF7800', label = r'')
ax.errorbar(amount, tau, yerr=0.1, fmt=' ', color = '#FF7800', linewidth=2)
ax.tick_params(axis='x', direction='inout')
ax.tick_params(axis='y', direction='inout')
ax.set_xlabel(r'$N$, количество звеньев')
ax.set_ylabel(r'$\tau$, мс')
fig.savefig('task2.pdf')
plt.show()
