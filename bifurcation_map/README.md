# Bifurcation Map

A Python visualization of the bifurcation structure of the Logistic Map, illustrating the transition from order to chaos.

## About

The Bifurcation Map is one of the most iconic visualizations in chaos theory.

It is generated using the Logistic Map equation:

x(n+1) = r · x(n) · (1 - x(n))

By varying the growth parameter `r` and observing the long-term behavior of the system, complex patterns emerge that reveal how deterministic systems can produce chaotic behavior.

## Theory

For each value of `r`:

1. Start with an initial value `x₀`.
2. Repeatedly apply the Logistic Map equation.
3. Discard early iterations to remove transient behavior.
4. Plot the remaining values.

As `r` increases, the system progresses through:

- Stable equilibrium
- Period-2 oscillation
- Period-4 oscillation
- Period doubling cascade
- Chaos

This route to chaos is known as the **Period-Doubling Route to Chaos**.

## Concepts Used

- Chaos Theory
- Dynamical Systems
- Logistic Map
- Bifurcation Theory
- Nonlinear Dynamics
- Sensitive Dependence on Initial Conditions

## Features

- High-resolution bifurcation visualization
- Dark theme rendering
- Color-mapped population values
- Exploration of stability and chaos
- Period-doubling visualization

## Requirements

```bash
pip install numpy matplotlib
```

## Run

```bash
python main.py
```

## Mathematical Significance

The Bifurcation Map demonstrates how a simple nonlinear equation can generate an extraordinary range of behaviors.

It provides one of the clearest visual examples of the emergence of chaos from deterministic rules and is a cornerstone of modern chaos theory.
