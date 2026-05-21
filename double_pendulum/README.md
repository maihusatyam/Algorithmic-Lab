# Double Pendulum Simulation

# Introduction
-A double pendulum is a mechanical system consisting of one pendulum attached to the end of another pendulum.
-Unlike a normal pendulum, the motion of a double pendulum becomes highly complex and unpredictable over time. It is one of the most well-known examples of chaos theory and nonlinear dynamics.
-This project simulates the motion of a double pendulum in real time using Python.

# Structure of the System
The system contains:
- Two rods
- Two masses (bobs)
- Two rotational joints

The first pendulum is attached to a fixed pivot point, while the second pendulum hangs from the first mass.
The motion of each pendulum continuously affects the other, creating coupled nonlinear motion.

# Chaos Theory
The double pendulum demonstrates a property called:

## Sensitive Dependence on Initial Conditions
Very tiny changes in starting angles eventually produce completely different trajectories.
For example:
- Pendulum A starting at 90°
- Pendulum B starting at 90.001°
may initially move almost identically, but after some time their motions diverge completely.
This behavior is commonly known as the Butterfly Effect.
Although the system follows deterministic physical laws, long-term prediction becomes practically impossible.

# Physics Behind the Simulation
The motion of the pendulum is governed by:
- Gravity
- Angular velocity
- Angular acceleration
- Momentum transfer
- Energy conservation

The system uses coupled nonlinear differential equations to calculate the angular acceleration of both pendulums.
Because these equations are difficult to solve analytically, the simulation approximates the motion numerically step-by-step.

# Numerical Simulation
The simulation updates the system repeatedly over very small time intervals.
For every frame:
1. Angular acceleration is calculated
2. Angular velocity is updated
3. Pendulum angles are updated
4. Angles are converted into x,y coordinates
5. The new position is drawn on screen

This process creates continuous animated motion.

# Coordinate Conversion
The pendulum angles are converted into Cartesian coordinates using trigonometry.
For the first bob:

```math
x1 = L1 sin(theta1)
y1 = -L1 cos(theta1)
```

For the second bob:

```math
x2 = x1 + L2 sin(theta2)
y2 = y1 - L2 cos(theta2)
```

These coordinates are used for visualization.

# Technologies Used
- Python
- NumPy
- Matplotlib

# Conclusion
The double pendulum is a classic example of how deterministic systems can still exhibit unpredictable behavior.
This project demonstrates how mathematics, physics, and computation can be combined to simulate complex real-world systems.
