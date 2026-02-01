# Lorenz System Simulation

This project simulates the Lorenz system, a system of ordinary differential equations first studied by Edward Lorenz. It is notable for having chaotic solutions for certain parameter values and initial conditions.

The simulation uses the 4th Order Runge-Kutta (RK4) method for numerical integration.

## Lorenz System Equations

The equations are:
- dx/dt = σ(y - x)
- dy/dt = x(ρ - z) - y
- dz/dt = xy - βz

Default parameters used in `main.py`:
- σ (sigma) = 10
- ρ (rho) = 28
- β (beta) = 8/3

## Requirements

To run this simulation, you need Python and the following libraries:
- `numpy`
- `matplotlib`

You can install the dependencies using pip:
```bash
pip install numpy matplotlib
```

## How to Run

Execute the `main.py` script:
```bash
python main.py
```

The script will generate two plots:
1. A 3D plot of the Lorenz attractor.
2. Time-series plots for each of the coordinates (x, y, z).

## Implementation Details

The core of the simulation consists of:
- `lorenzsystem(state)`: Calculates the derivatives at a given state.
- `rungekutta4(state, h)`: Performs one step of the RK4 integration with a step size `h`.
