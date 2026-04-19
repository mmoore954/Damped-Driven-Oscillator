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

Project Update – Damped Driven Oscillator
At this point in the project, we are on track with our original timeline. We have set up the basic structure of the project and started implementing the numerical solution. So far, we have begun coding the Euler method in Python and tested a simple case of the system without added complexity. This aligns with our initial plan of starting simple and building up step by step.
There have not been major changes to our overall approach. We are still using the Euler method to solve the differential equation by converting the second-order equation into two first-order equations and stepping forward in time. We are using NumPy for calculations and plan to use Matplotlib for generating graphs such as position vs time, velocity vs time, and amplitude vs frequency to analyze resonance.
One of the main challenges so far has been making sure the time step is chosen correctly. If the step is too large, the results can become inaccurate or unstable, and if it is too small, the simulation takes longer to run. We are also paying attention to making sure the results make physical sense and that the graphs look correct. Debugging the code and verifying correctness has taken some time, especially when testing different parameter values.
Currently, we are not stuck on any major issues, but we still need to continue building the model by adding damping and the external driving force. After that, we will generate the required graphs and begin testing different parameter values to observe how the system behaves, especially in terms of resonance.
Overall, we are following our planned timeline and progressing steadily. The next steps are to complete the full implementation of the system, refine the graphs, and analyze how changing parameters like damping and frequency affect the motion.
