import numpy as np

def code6(A, k, m, x0, M, T):

    test = -1

    delta = 0.001
    N = 1000

    t = np.linspace(0, T, N + 1)

    h = T / N
    h2 = h / 2

    u = np.zeros(N + 1)

    x = np.zeros(N + 1)
    x[0] = x0

    lam = np.zeros(N + 1)

    while test < 0:

        oldu = u.copy()
        oldx = x.copy()
        oldlam = lam.copy()

        # Resolver x hacia adelante
        for i in range(N):

            k1 = -(m + u[i]) * x[i]

            k2 = -(m + 0.5 * (u[i] + u[i+1])) * (x[i] + h2 * k1)

            k3 = -(m + 0.5 * (u[i] + u[i+1])) * (x[i] + h2 * k2)

            k4 = -(m + u[i+1]) * (x[i] + h * k3)

            x[i+1] = x[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

        # Resolver lambda hacia atrás
        for i in range(N):

            j = N - i

            k1 = (
                -A * u[j] * k * t[j] / (t[j] + 1)
                + lam[j] * (m + u[j])
            )

            k2 = (
                -A * 0.5 * (u[j] + u[j-1]) * k * (t[j] - h2) / ((t[j] - h2) + 1)
                + (lam[j] - h2 * k1) * (m + 0.5 * (u[j] + u[j-1]))
            )

            k3 = (
                -A * 0.5 * (u[j] + u[j-1]) * k * (t[j] - h2) / ((t[j] - h2) + 1)
                + (lam[j] - h2 * k2) * (m + 0.5 * (u[j] + u[j-1]))
            )

            k4 = (
                -A * u[j-1] * k * (t[j] - h) / ((t[j] - h) + 1)
                + (lam[j] - h * k3) * (m + u[j-1])
            )

            lam[j-1] = lam[j] - (h/6) * (k1 + 2*k2 + 2*k3 + k4)

        temp = -0.5 * (lam * x - A * k * t * x / (t + 1))

        u1 = np.minimum(M, np.maximum(temp, 0))

        u = 0.5 * (u1 + oldu)

        temp1 = delta * np.sum(np.abs(u)) - np.sum(np.abs(oldu - u))
        temp2 = delta * np.sum(np.abs(x)) - np.sum(np.abs(oldx - x))
        temp3 = delta * np.sum(np.abs(lam)) - np.sum(np.abs(oldlam - lam))

        test = min(temp1, temp2, temp3)

    return t, x, u