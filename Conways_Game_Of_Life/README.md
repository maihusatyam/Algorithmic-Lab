# Conway's Game of Life
A Python implementation of Conway's Game of Life using NumPy and Matplotlib.

## About
Conway's Game of Life is a cellular automaton devised by mathematician John Conway in 1970.
The simulation consists of a grid of cells that evolve through generations according to a simple set of rules. Despite these simple rules, the system can produce highly complex and unpredictable behavior.

## Rules
For each cell:
1. A live cell with fewer than 2 live neighbors dies (underpopulation).
2. A live cell with 2 or 3 live neighbors survives.
3. A live cell with more than 3 live neighbors dies (overpopulation).
4. A dead cell with exactly 3 live neighbors becomes alive (reproduction).

## Concepts Used
- Cellular Automata
- Emergent Behavior
- Grid-Based Simulation
- Mathematical Modeling
- NumPy Arrays
- Matplotlib Animation

## Features
- Random initial population
- Real-time animation
- Dark theme visualization
- Viridis color mapping
- Configurable grid size

## Requirements
```bash
pip install numpy matplotlib
```

## Run
```bash
python main.py
```

## Theory
Conway's Game of Life demonstrates how complex patterns can emerge from simple local interactions.
Each cell only interacts with its eight neighboring cells, yet large-scale structures such as oscillators, spaceships, and stable formations can appear spontaneously.
The Game of Life is one of the most famous examples of emergence and cellular automata in computer science and mathematics.
