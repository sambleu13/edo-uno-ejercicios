import matplotlib.pyplot as plt
import numpy as np

# Solución del primer problema
def y1(t, C1, C2):
    return np.exp(-t) * (C1 * np.cos(t) + C2 * np.sin(t))

# Valores específicos para C1 y C2 calculados
C1 = np.sqrt(2) * np.exp(np.pi / 4)
C2 = np.sqrt(2) * np.exp(np.pi / 4)

# Rango de tiempo para la gráfica
t_vals = np.linspace(0, 5, 400)

# Solución del segundo problema
def y2(t):
    return (3/2) * np.exp(t/3) - (1/2) * np.exp(-t/3)

# Solución del tercer problema
def y3(t):
    return 2 * t * np.exp(3 * t)

# Guardar las gráficas en un archivo de imagen
fig, ax = plt.subplots(3, 1, figsize=(8, 12))

# Gráfica del primer problema
ax[0].plot(t_vals, y1(t_vals, C1, C2), label=r"$y(t) = \sqrt{2}e^{(\frac{\pi}{4}-t)} (cos(t) + sen(t))$")
ax[0].set_title('Solución del problema 1: $y\'\' + 2y\' + 2y = 0$')
ax[0].set_xlabel('t')
ax[0].set_ylabel('y(t)')
ax[0].grid(True)
ax[0].legend()

# Gráfica del segundo problema
ax[1].plot(t_vals, y2(t_vals), label=r"$y(t) = \frac{3}{2} e^{t/3} - \frac{1}{2} e^{-t/3}$", color='orange')
ax[1].set_title('Solución del problema 2: $9y\'\' - y = 0$')
ax[1].set_xlabel('t')
ax[1].set_ylabel('y(t)')
ax[1].grid(True)
ax[1].legend()

# Gráfica del tercer problema
ax[2].plot(t_vals, y3(t_vals), label=r"$y(t) = 2t e^{3t}$", color='green')
ax[2].set_title('Solución del problema 3: $y\'\' - 6y\' + 9y = 0$')
ax[2].set_xlabel('t')
ax[2].set_ylabel('y(t)')
ax[2].grid(True)
ax[2].legend()

# Guardar la gráfica
plt.tight_layout()

#Mostrar la gráfica
plt.show()
