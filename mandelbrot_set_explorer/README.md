# Mandelbrot Set Explorer
A Python visualization of the Mandelbrot fractal using iterative complex dynamics.

## About
The Mandelbrot Set is one of the most famous mathematical fractals.
It is generated using the recursive equation:
z = z² + c
where:
- z starts at 0
- c is a complex number representing a point in the complex plane
For every point, the equation is repeatedly applied.
If the value of z grows infinitely large, the point is considered outside the Mandelbrot Set.
If the value remains bounded, the point belongs to the set.

## Theory
Each pixel on the screen represents a complex number.
The program repeatedly computes:
z = z² + c
and checks whether:
|z| > 2
If the value escapes beyond 2, the point diverges.
The number of iterations before divergence is used to color the pixel, creating the fractal structure.

## Concepts Used
- Complex numbers
- Fractals
- Recursive iteration
- Computational mathematics
- Visualization
- Escape-time algorithm

## Features
- Mandelbrot fractal generation
- Pixel-based rendering
- Escape-time coloring
- Mathematical visualization

## Mathematical Significance
The Mandelbrot Set demonstrates how extremely complex and infinitely detailed structures can emerge from very simple mathematical rules.
It is widely studied in:
- chaos theory
- complex analysis
- dynamical systems
- computational mathematics
