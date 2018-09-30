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
g = np.genfromtxt('FHF(ampl,phasa).csv',delimiter=';')
spline = np.genfromtxt('FHF.csv',delimiter=';')
frec = g[1:,0]
phasa = g[1:,1]
ampl = g[1:,2]
frecerr = g[1:,3]
x1 = spline[0:,0]
y1 = spline[0:,1]
y2 = spline[0:,2]
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(121)
ax.grid(which='both')
ax.plot(x1,y1,color = '#FF7800', label = r'ФЧХ')
ax.errorbar(frec, phasa, xerr=frecerr,fmt=' ', color = '#FF7800', linewidth=2)
ax.tick_params(axis='x', direction='inout')
ax.tick_params(axis='y', direction='inout')
ax.set_xlabel(r'$f$, Гц')
ax.set_ylabel(r'$\varphi$, рад.')
ax.legend(loc='upper left')
ax2 = fig.add_subplot(122)
ax2.grid(which='both')
ax2.plot(x1,y2,color = '#133CAC', label = r'АЧХ')
ax2.errorbar(frec, ampl, xerr = frecerr, yerr = .5, fmt=' ', color = '#133CAC', linewidth=2)
ax2.tick_params(axis='x', direction='inout')
ax2.tick_params(axis='y', direction='inout')
ax2.set_xlabel(r'$f$, Гц')
ax2.set_ylabel(r'$A$, В')
ax2.legend(loc='lower left')
fig.savefig('FHF.pdf')
plt.show()
