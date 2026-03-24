# Damped-Driven-Oscillator
Project: Spring System Simulation

Problem Statement:
For this project we are gonna simulate a damped driven oscillator, which is basically a mass on a spring with friction and an external force pushing it. This matters because real stuff like car suspension systems and vibrations in machines all have damping and outside forces. We wanna see how the motion changes when we mess with things like damping and frequency. It’s interesting because you can see how the system changes over time and how resonance happens when everything lines up.

Proposed Methods:
We are gonna solve the differential equation using numerical methods in Python. We’ll use the Euler method since that’s what we learned in class. First we’ll turn the second order equation into two first order ones, then solve step by step over time. We’ll use NumPy for calculations and Matplotlib for graphs. We plan to make graphs like position vs time, velocity vs time, and also amplitude vs frequency to show resonance.

Expected Challenges:
One challenge is picking a good time step so the results are accurate but not too slow. Another issue could be making sure the method doesn’t give weird or unstable results. Understanding resonance and how changing parameters affects the system might also be a little confusing at first. Debugging the code and making sure the graphs actually look right will probably take some time too.

Timeline:
Week 1: Set everything up, code Euler method, test basic case
Week 2: Add damping and make sure everything works
Week 3: Add driving force and create graphs
Week 4: Test different values and look at resonance
Week 5: Clean everything up, finalize graphs, and finish report

This project is doable because we’re starting simple and building it up step by step. It also matches what we learned since it uses numerical methods, Python, and graphs to solve a physics problem.
