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






(PROJECT PROPOSAL)
Me and Mukesh are currently working on our damped driven oscillator simulation. Right now we have the basic setup done and we started coding the Euler method to simulate the motion of the system over time. We were able to get position vs time working and the system runs, so we know the base of the project is good. We also set up our GitHub repo and both of us have been pushing commits so there is clear progress being made.

One change we made from our original plan is that we are not only using Euler anymore. Based on feedback, we are now also adding the Verlet method. This is because Euler has accuracy issues, especially over longer time, and does not conserve energy well. By adding Verlet, we can compare the two methods and show how they behave differently, which makes the project more advanced and more meaningful.

One challenge we ran into was getting the system to behave correctly over time. At first the motion looked off because the time step was too big, so we had to adjust it and test different values until the graph looked right. Another challenge is understanding how to properly measure amplitude for the amplitude vs frequency graph. We realized we cannot just take the first peak, and instead we need to let the system run long enough so the transient behavior dies out before measuring steady-state amplitude.

Right now we are not fully stuck, but the main thing we are still working on is finishing the Verlet method and making sure both methods are running correctly so we can compare them. We also still need to implement the frequency sweep for the amplitude vs frequency graph.

As for our progress compared to the timeline, we are a little behind on adding the second method, but we are catching up by splitting the work more clearly. I (Mason) am focusing on finishing and cleaning up the Euler method and making sure all the basic graphs are correct. Mukesh is working on implementing the Verlet method and will handle the comparison graph between Euler and Verlet. After that, we will both work on the amplitude vs frequency graph and final analysis.

Moving forward, our plan is to first finish the Verlet method completely, then combine both methods into one script so we can directly compare results. After that, we will run simulations over a range of driving frequencies and record steady-state amplitude to create the amplitude vs frequency plot. If we have extra time, we may also try to create a 2D heatmap showing how amplitude changes with both damping and frequency.

Overall, we have a solid base working and a clear plan for finishing the project, and we are continuing to make steady progress through commits and testing.
