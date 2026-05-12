import numpy as np
import matplotlib.pyplot as plt

m = 0.5; Ix = 0.02; T = 2.0
x0 = np.array([2.0, 0.5, 0.2, -0.1])  # dz, dzp, dphi, dphip

# Control calculado
def u(t):
    dT = m * ( (12*t - 6*T)/T**3 * x0[0] + (6*t - 4*T)/T**2 * x0[1] )
    dtau = Ix * ( (12*t - 6*T)/T**3 * x0[2] + (6*t - 4*T)/T**2 * x0[3] )
    return np.array([dT, dtau])

# Simulación con integración exacta (usando expAt)
A = np.array([[0,1,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]])
B = np.array([[0,0],[1/m,0],[0,0],[0,1/Ix]])
dt = 0.01
time = np.arange(0, T+dt, dt)
x = np.zeros((len(time),4))
x[0] = x0
for i, t in enumerate(time[:-1]):
    expAt = np.array([[1,dt,0,0],[0,1,0,0],[0,0,1,dt],[0,0,0,1]])
    # integral de B*u constante en intervalo (aproximación correcta dt pequeño)
    # Usamos la fórmula exacta del propagador: x(t+dt)=exp(A dt)x(t) + int_0^dt exp(A s) ds B u(t)
    # Para este sistema, la integral es simple.
    # Implementación más simple: integración de Euler ya que A es nilpotente y u variante, preferible ODE exacta.
    # Aquí usaré la fórmula exacta con muestreo de u constante en cada dt:
    u_now = u(t)
    # x(t+dt) = exp(A*dt) x(t) + (integral_0^dt exp(A s) ds) B u_now
    int_expA = np.array([[dt, dt**2/2, 0, 0],
                         [0, dt, 0, 0],
                         [0,0,dt, dt**2/2],
                         [0,0,0, dt]])
    x[i+1] = expAt @ x[i] + int_expA @ B @ u_now

plt.figure(figsize=(12,5))
plt.subplot(1,2,1); plt.plot(time, x[:,0]); plt.xlabel('t'); plt.ylabel(r'$\delta z$'); plt.grid()
plt.subplot(1,2,2); plt.plot(time, x[:,2]); plt.xlabel('t'); plt.ylabel(r'$\delta\phi$'); plt.grid()
plt.suptitle('Llevando estados a cero con control calculado'); plt.show()