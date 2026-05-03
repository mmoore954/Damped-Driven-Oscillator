import numpy as np
import matplotlib.pyplot as plt

# constants
m = 1
k = 1
b = 0.2
F0 = 1
omega = 1.2

dt = 0.01
t_max = 50
t = np.arange(0, t_max, dt)

# Euler method
x_e = np.zeros(len(t))
v_e = np.zeros(len(t))

for i in range(len(t)-1):
    a = (F0*np.cos(omega*t[i]) - b*v_e[i] - k*x_e[i]) / m
    v_e[i+1] = v_e[i] + a*dt
    x_e[i+1] = x_e[i] + v_e[i]*dt

# Verlet method
x_v = np.zeros(len(t))
v_v = np.zeros(len(t))

for i in range(1, len(t)-1):
    a = (F0*np.cos(omega*t[i]) - b*v_v[i] - k*x_v[i]) / m
    x_v[i+1] = 2*x_v[i] - x_v[i-1] + a*(dt**2)
    v_v[i] = (x_v[i+1] - x_v[i-1]) / (2*dt)

# Plot comparison
plt.plot(t, x_e, label="Euler")
plt.plot(t, x_v, label="Verlet")
plt.xlabel("Time")
plt.ylabel("Position")
plt.legend()
plt.title("Euler vs Verlet Comparison")
plt.show()
