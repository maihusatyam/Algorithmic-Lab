# Lorenz Attractor
A Python simulation of the Lorenz Attractor using matplotlib 3D animation.

## About
The Lorenz Attractor is a chaotic dynamical system introduced by Edward Lorenz while studying atmospheric convection and weather prediction.
It is one of the most famous examples of chaos theory and sensitive dependence on initial conditions, also known as the Butterfly Effect.
Tiny differences in starting values eventually produce drastically different trajectories.

## Lorenz Equations
dx/dt = a(y - x)
dy/dt = x(r - z) - y
dz/dt = xy - bz

Standard parameter values used:
- a = 10
- b = 8/3
- r = 28

These values generate the famous butterfly-shaped attractor.

## Concepts Used
- Chaos theory
- Numerical integration
- Differential equations
- 3D plotting
- Dynamical systems
- Matplotlib animation

## Features
- Real-time 3D animation
- Dark theme visualization
- Chaotic trajectory plotting
- Adjustable parameters

## Theory
The Lorenz system is deterministic but highly sensitive to initial conditions.
Although governed by fixed equations, long-term prediction becomes practically impossible because tiny numerical differences grow exponentially over time.
This behavior is a fundamental characteristic of chaotic systems.
