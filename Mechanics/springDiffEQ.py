import numpy as np
import matplotlib.pyplot as plt 

plt.style.use('Solarize_Light2')

t = np.linspace(-2*np.pi, 10*np.pi, 1000)

def waveEq(b, a):
    if b**2 < 4*a:

        eq = np.exp(1j*np.sqrt(4*a - b**2) * t) + np.exp(-1j*np.sqrt(4*a - b**2) * t)
    else:
        eq = np.exp(np.sqrt(b**2 - 4*a) * t) + np.exp(np.sqrt(b**2 - 4*a) * t)
    return eq

plt.plot(t, waveEq(1, 2))
plt.plot(t, waveEq(2, 1))
plt.plot(t, waveEq(3, 4))
plt.xlim(-2*np.pi, 10*np.pi)
plt.show()