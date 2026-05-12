import numpy as np
import matplotlib.pyplot as plt

#matriz

A = np.array([
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
])

#condiciones iniciales

x0 = np.array([
    0.2,   # z(0)
    0.1,   # dz(0)
    0.2,   # phi(0)
    0.2    # dphi(0)
])

t0 = 0
tf = 20
N = 100
t = np.linspace(t0, tf, N)
dt = t[1] - t[0]

x = np.zeros((N, 4))
x[0] = x0

for i in range(N - 1):
    x_actual = x[i]

    xdot = A @ x_actual
    x[i + 1] = x_actual + dt * xdot
print(x)
z = x[:, 0]
dz = x[:, 1]
phi = x[:, 2]
dphi = x[:, 3]

plt.figure(figsize=(12,8))


plt.subplot(2,2,1)
plt.plot(t, z)
plt.xlabel("t")
plt.ylabel("z")
plt.title("Posición z")


plt.subplot(2,2,2)
plt.plot(t, dz)
plt.xlabel("t")
plt.ylabel("dz")
plt.title("Velocidad dz")


plt.subplot(2,2,3)
plt.plot(t, phi)
plt.xlabel("t")
plt.ylabel("phi")
plt.title("Ángulo phi")

plt.subplot(2,2,4)
plt.plot(t, dphi)
plt.xlabel("t")
plt.ylabel("dphi")
plt.title("Velocidad angular dphi")

plt.tight_layout()
plt.show()