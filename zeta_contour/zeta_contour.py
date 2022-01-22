# A contour plot of the Riemann zeta function on the strip -3<re(z)<3, -30,im(z)<30
import numpy

import matplotlib.pyplot as plt
from mpmath import zeta, re, im

delta = 0.1
x = numpy.arange(-3, 3, delta)
y = numpy.arange(-30, 30, delta)
X, Y = numpy.meshgrid(x, y)

@numpy.vectorize
def real(real, imag):
    if (real - 1) ** 2 + imag ** 2 < 0.3: #avoid the pole at z=1
        return 0.0
    r = re(zeta(real + imag * 1j))
    return r

R = real(X, Y)

@numpy.vectorize
def imag(real, imag):
    if (real - 1) ** 2 + imag ** 2 < 0.3:
        return 0.0
    r = im(zeta(real + imag * 1j))
    return r

I = imag(X, Y)


fig, ax = plt.subplots()
CS = ax.contour(X, Y, R, linestyles = 'solid')
CS = ax.contour(X, Y, I, linestyles = 'dashed')
ax.clabel(CS, inline=True, fontsize=10)

fig.set_figheight(90)
fig.set_figwidth(15)
plt.savefig('zeta.png', dpi=300)