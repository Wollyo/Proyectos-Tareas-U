import matplotlib.pyplot as plt
from code6 import code6

A = 5
k = 10
m = 0.2
x0 = 0.8
M = 1
T = 20


t, x, u = code6(A, k, m, x0, M, T)

w = k * t / (t + 1)

plt.figure(figsize=(8,8))

plt.subplot(3,1,1)
plt.plot(t, x)
plt.title("Evolución de la Concentración de Peces")
plt.xlabel("Semanas")
plt.ylabel("Concentración de Peces")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, u)
plt.title("Tasa Óptima de Cosecha")
plt.xlabel("Semanas")
plt.ylabel("Tasa de Cosecha")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, w)
plt.title("Peso Promedio de los Peces")
plt.xlabel("Semanas")
plt.ylabel("Peso Promedio")
plt.grid(True)

plt.tight_layout()
plt.show()