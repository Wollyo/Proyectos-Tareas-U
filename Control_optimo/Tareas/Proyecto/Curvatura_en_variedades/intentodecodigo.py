import numpy as np
import scipy as sp
import matplotlib.pyplot as plt



#Datos iniciales
psi_f= 0.32667
psi_w = 0.21333
delta_f = 0.0333
delta_w = 0.06666
K_f = 374
K_w = 300
K_b = 33.327
K_zero = 30
r_f = psi_f - delta_f
r_w = psi_w - delta_w
F0 = K_f
W0 = 0
h = 0.01
t0, tf = 0, 147
t = np.arange(t0, tf, h)
u = 17
#ecuacion diferencial


#f = (psi_f - (r_f/K_f)*(F+W)) * F * ((F/K_zero)-1) - delta_f*F

#g = (psi_w - (r_w/K_w)*(F+W)) * W - delta_w*W + u

F = np.zeros(len(t))
F[0] = F0
W = np.zeros(len(t))
W[0] = W0

#euler
print()
for i in range(len(t)-1):
    f_n = (psi_f - (r_f/K_f)*(F[i]+W[i])) * F[i] * ((F[i]/K_zero)-1) - delta_f*F[i]
    g_n = (psi_w - (r_w/K_w)*(F[i]+W[i])) * W[i] - delta_w*W[i] + u
    F[i+1] = F[i] + h*f_n
    W[i+1] = W[i] + h*g_n
plt.plot(t,K_b *np.ones_like(t),label= "K_b",linestyle="--")
plt.plot(t, F, label='F')
plt.plot(t, W, label='W')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Evolución de F y W con control u=10')
plt.legend()
plt.grid()  
plt.show()
