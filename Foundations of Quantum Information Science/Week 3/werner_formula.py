"""werner_formula.py"""
#Reference: wikipedia
#Reference: tutorials via AI/search

import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return np.sin(.8*x)
def f2(x):
    return np.sin(.5*x)
def f3(x):
    return np.sin(.8*x) * np.sin(.5*x)
def f4(x):
    return .5*(np.cos(.3*x) - np.cos(1.3*x)) # Werner's Product to Sum Formula

x=np.linspace(-3*np.pi,3*np.pi,100)

p1 = plt.plot(x,f1(x), label=r'$\sin(.8x)$')
p2 = plt.plot(x,f2(x), label=r'$\sin(.5x)$')
p3 = plt.plot(x,f3(x), label=r'$\ .5(sin(.8x)sin(.5x))$')
p4 = plt.scatter(x, f4(x), facecolors='none', edgecolors='gray', s=100, label=r'$\.5(cos(.3x) - cos(1.3x))$')
plt.xlabel(r'x')
plt.ylabel(r'y')
plt.legend(loc='lower right')
plt.show()