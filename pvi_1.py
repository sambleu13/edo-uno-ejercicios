import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-1.1, 5.1, 0.2)
y = np.sqrt(2)*np.exp((np.pi/4)-t)*(np.cos(t) + np.sin(t))


plt.plot(t, y, label=r"$y(t) = \sqrt{2}e^{(\frac{\pi}{4}-t)} (cos(t) + sen(t))$")
plt.title('Solución del problema $y\'\' + 2y\' + 2y = 0$')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()
