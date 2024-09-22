# Auto Driving Car Simulation

## Overview

The Auto Driving Car Simulation is a command-line program designed to simulate an autonomous driving experience within a rectangular grid. The program allows you to create a simulation field, add multiple cars, provide them with movement commands, and then run the simulation to observe how each car navigates the field. The simulation also detects collisions between cars and stops their movements accordingly.

This project serves as a simplified model of an autonomous driving system, where multiple cars operate independently within a constrained environment, responding to a set of commands and reacting to collisions.

## Features

- **Create a rectangular simulation field** with specified width and height.
- **Add multiple cars** to the field, each with unique names, starting positions, directions (N, S, E, W), and movement commands (L, R, F).
- **Execute movement commands** for each car and observe how they navigate within the field.
- **Collision detection** between cars, with the simulation stopping any cars involved in a collision.
- Handles out-of-bound movements, ensuring cars remain within the field.

## How to Run the Simulation

### Prerequisites

- Python 3.x should be installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Running the Program

1. **Clone the project** or copy all the `.py` files into a directory on your local machine.
2. Open a terminal/command prompt and navigate to the directory where the files are located.
3. Run the program using the following command:

   ```bash
   python Run.py
