import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0 # mass
k = 1.0 # spring constant
b = 0.2 # damping coefficient
F0 = 1.0 # driving force amplitude
omega = 1.0 # driving frequency

# Time settings
dt = 0.01
t_max = 50
t = np.arange(0, t_max, dt)

# Arrays for Euler Method
x_euler = np.zeros(len(t))
v_euler = np.zeros(len(t))

# Initial conditions
x_euler[0] = 1.0
v_euler[0] = 0.0

# Euler Method
for i in range(len(t) - 1):

# acceleration
a = (F0 * np.cos(omega * t[i]) - b * v_euler[i] - k * x_euler[i]) / m

# update velocity
v_euler[i + 1] = v_euler[i] + a * dt

# update position
x_euler[i + 1] = x_euler[i] + v_euler[i] * dt


# Arrays for Verlet Method
x_verlet = np.zeros(len(t))
v_verlet = np.zeros(len(t))

# Initial conditions
x_verlet[0] = 1.0
v_verlet[0] = 0.0

# First step for Verlet
a0 = (F0 * np.cos(omega * t[0]) - b * v_verlet[0] - k * x_verlet[0]) / m
x_verlet[1] = x_verlet[0] + v_verlet[0] * dt + 0.5 * a0 * dt**2

# Verlet Method
for i in range(1, len(t) - 1):

# approximate velocity
v_temp = (x_verlet[i] - x_verlet[i - 1]) / dt

# acceleration
a = (F0 * np.cos(omega * t[i]) - b * v_temp - k * x_verlet[i]) / m

# update position
x_verlet[i + 1] = 2 * x_verlet[i] - x_verlet[i - 1] + a * dt**2

# calculate velocity
v_verlet[i] = (x_verlet[i + 1] - x_verlet[i - 1]) / (2 * dt)


# Plot Results
plt.figure(figsize=(10, 5))

plt.plot(t, x_euler, label="Euler Method")
plt.plot(t, x_verlet, label="Verlet Method")

plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Damped Driven Oscillator: Euler vs Verlet")
plt.legend()

plt.grid(True)
plt.show()
