Methods

For this project, we model a damped driven oscillator using the equation:

m d²x/dt² + b dx/dt + kx = F₀ cos(ωt)

To solve this, we first rewrite the second-order equation into two first-order equations by defining velocity as v = dx/dt. This gives us:

dx/dt = v
dv/dt = (F₀ cos(ωt) − b v − k x) / m

We then solve this system numerically using two methods: the Euler method and the Verlet method.

For the Euler method, we update position and velocity step by step using a small time step Δt. At each step, we calculate acceleration based on the current position and velocity, then update velocity and position using those values.

For the Verlet method, we update position using both the current and previous positions. This method is more stable than Euler and does a better job maintaining energy over time.

We run the simulation over a set time interval and store position and velocity values at each step. Using this data, we create graphs of position vs time for both Euler and Verlet to compare their behavior.

To study resonance, we vary the driving frequency ω and run the simulation multiple times. For each frequency, we let the system run long enough so that the initial transient motion dies out. After that, we measure the steady-state amplitude and record it.

We then plot amplitude vs frequency to observe how resonance occurs in the system.

All calculations are done in Python using NumPy, and graphs are created using Matplotlib.
