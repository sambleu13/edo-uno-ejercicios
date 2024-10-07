import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-3, 1.1, 0.2)
y = (2*t) * np.exp(3) * np.exp(t)
#y= (-1/2) * np.exp(-t/3) + (3/2) * np.exp(t/3)

plt.plot(t, y, label=r"$y(t) = 2t e^{3t}$", color='green')
plt.title('Solución del problema $y\'\' - 6y\' + 9y = 0$')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()
