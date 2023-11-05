from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def model(z,t):
    """
    Funkcja definiująca model równania różniczkowego

    Parametry:
    z (float): Aktualna wartość z.
    t (float): Aktualna wartość czasu.

    Zwraca:
    dzdt (float): Aktualna wartość pochodnej dz/dt w danej chwili czasowej
    """
    dxdt = 3.0 * np.exp(-t)
    dydt = -z[1] + 3
    dzdt = [dxdt,dydt]
    return dzdt

def main():
    z0 = [0,0]
    t = np.linspace(0,5)
    z=odeint(model,z0,t)
    plt.plot(t,z)