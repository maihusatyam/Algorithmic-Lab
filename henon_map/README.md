# Hénon Map

A Python visualization of the Hénon Map, one of the most famous discrete-time chaotic systems and strange attractors in dynamical systems theory.

## About

The Hénon Map is a two-dimensional iterative system introduced by French mathematician Michel Hénon in 1976.

Despite being defined by only two simple equations, the system produces complex and chaotic behavior, making it a classical example in chaos theory.

## Equations

x(n+1) = 1 - a·x(n)² + y(n)

y(n+1) = b·x(n)

where:

* x and y are the current state variables
* a and b are system parameters

Standard values:

* a = 1.4
* b = 0.3

## Theory

The Hénon Map repeatedly transforms a point in the plane.

Starting from an initial point, the system generates a sequence of points that eventually form a fractal structure known as the Hénon Strange Attractor.

Small changes in the initial conditions can lead to dramatically different trajectories, demonstrating sensitive dependence on initial conditions, a defining characteristic of chaotic systems.

## Concepts Used

* Chaos Theory
* Dynamical Systems
* Strange Attractors
* Fractals
* Nonlinear Dynamics
* Iterative Maps
* Sensitive Dependence on Initial Conditions

## Features

* Animated attractor generation
* Dark theme visualization
* Real-time trajectory growth
* High-resolution attractor rendering
* Exploration of chaotic behavior

## Requirements

```bash
pip install numpy matplotlib
```

## Run

```bash
python main.py
```

## Mathematical Significance

The Hénon Map is one of the simplest systems capable of generating a strange attractor.

It provides a powerful demonstration of how deterministic mathematical rules can create highly complex and unpredictable behavior.

The attractor produced by the system exhibits fractal structure and remains a cornerstone example in the study of chaos theory.
