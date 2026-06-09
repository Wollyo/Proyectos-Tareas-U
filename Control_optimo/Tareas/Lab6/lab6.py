import matplotlib.pyplot as plt
from code6 import code6

A = 1
k = 2
m = 0.1
x0 = 10
M = 1
T = 20

t, x, u = code6(A, k, m, x0, M, T)

w = k * t / (t + 1)

plt.figure(figsize=(8,8))

plt.subplot(3,1,1)
plt.plot(t, x)
plt.ylabel("Fish Concentration")

plt.subplot(3,1,2)
plt.plot(t, u)
plt.ylabel("Harvesting Rate")

plt.subplot(3,1,3)
plt.plot(t, w)
plt.ylabel("Average Weight")
plt.xlabel("Weeks")

plt.tight_layout()
plt.show()