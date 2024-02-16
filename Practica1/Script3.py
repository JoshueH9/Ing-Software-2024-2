import matplotlib.pyplot as plt
import numpy as np


def funcion_cuadratica(x):
    return x ** 2


# Generar valores de x
x = np.linspace(-5, 5, 100)

# Calcular los valores de y usando la función cuadrática
y = funcion_cuadratica(x)

# Graficar la función
plt.plot(x, y)
plt.title('Gráfica de la función cuadrática')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
