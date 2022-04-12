"""
TODO
    - Trouver une fonction pour r(x) qui colle a la rocket
    - Adapter les dimensions
"""

from numpy import arctan, pi
from MyPack2.Math import integr
import scipy.integrate as integrate


L = 10 # Longeur de la rocket
X_e = 0.3*L # Position de l'interface eau/air

Pa_0 = 2 *10**5  # Pression de l'air (Pascal)

r = lambda x: arctan(5*x-4) + 2  # arbitraire
S0 = pi*r(0)**2  # Section de sortie

Veau = integrate.quad(r,0,X_e)[0]
Vair = integrate.quad(r,X_e,L)[0]
Vtotal = integrate.quad(r,0,L)[0]

print(Veau)
print(Vair)
print(Vtotal)