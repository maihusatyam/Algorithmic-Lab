# Logistic Map Explorer
An interactive visualization of the Logistic Map using Python and Matplotlib sliders.

## About
The Logistic Map is one of the simplest mathematical models capable of producing chaotic behavior.
Despite being defined by a single equation, it demonstrates stability, oscillation, period doubling, and chaos depending on the value of the growth parameter.

## Logistic Equation
x(n+1) = r · x(n) · (1 - x(n))
where:
- x = current value (0 ≤ x ≤ 1)
- r = growth parameter
- x(n+1) = next value

## Concepts Used
- Chaos Theory
- Dynamical Systems
- Nonlinear Equations
- Sensitive Dependence on Initial Conditions
- Interactive Data Visualization

## How It Works
Starting from an initial value x₀, the Logistic Map repeatedly computes:
x → r·x·(1-x)
The resulting sequence is plotted over time.
Different values of r produce different behaviors:
- r ≈ 2.0 → Stable equilibrium
- r ≈ 3.2 → Periodic oscillation
- r ≈ 3.5 → Period doubling
- r ≈ 3.9 → Chaotic behavior

## Butterfly Effect
At chaotic values of r, extremely small differences in the initial value x₀ can lead to dramatically different long-term outcomes.
This sensitivity to initial conditions is a defining characteristic of chaotic systems.
