from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np



# Definicja modelu równania różniczkowego:
def model(y, x):
    """
    Model równania różniczkowego pierwszego rzędu.

    Parametry:
    x (float): Aktualna wartość x.
    y (float): Aktualna wartość y.

    Zwraca:
    dydx (float): Wartość pochodnej dy/dx w danym punkcie.
    """
    dydx = -y + 1
    return dydx

def main():
    """
    Główna funkcja programu, która rozwiązuje równanie różniczkowe i wizualizuje wyniki.
    """
    # Warunki początkowe rozwiązania równania
    y0=0
    x = np.linspace(0,5,100)

    y = odeint(model, y0, x)

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Rozwiązanie pierwszego równania różniczkowego!!!")
    plt.show()

if __name__ == "__main__":
    """
    Uruchom główną funkcjęm gdy skrypt jest uruchamiany jako program główny.
    """
    main()