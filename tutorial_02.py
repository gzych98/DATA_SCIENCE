from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def model(y,t):
    """
    Model równania rózniczkowego

    Parametry:
    t (float): Czas.
    y (float): Aktualna wartość y.

    Zwraca:
    dydt (float): Wartość pochodnej dt/dt w danym punkcie.
    """
    if t<10.0:
        u=0
    else:
        u=2
    dydt = (-y+u)/5.0
    return dydt

def main():
    """
    Główna funkcja programu.
    """
    y0=1
    t=np.linspace(0,40,1000)
    y=odeint(model,y0,t)
    plt.plot(t,y,'r-',label='Output (y(t))')
    plt.plot([0,10,10,40],[0,0,2,2],'b-',label='Input (u(t))')
    plt.xlabel("time")
    plt.ylabel("value")
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    """
    Uruchom główną funkcję.
    """
    main()

