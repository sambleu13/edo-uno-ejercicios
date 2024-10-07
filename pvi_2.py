import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-3, 3.1, 0.2)
y= (-1/2) * np.exp(-t/3) + (3/2) * np.exp(t/3)

plt.plot(t, y, label=r"$y(t) = \frac{-1}{2} e^{-t/3} + \frac{3}{2} e^{t/3}$", color='orange')
plt.title('Solución del problema $9y\'\' - y = 0$')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()
