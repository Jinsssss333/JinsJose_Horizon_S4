# Rover Navigation System

This Python script calculates the distance and time required for a rover to reach its destination based on its movement kinematics. It takes into account uniform acceleration until the rover reaches its top speed, and then calculates the remaining time if it cruises at that maximal velocity.

## Features

- Calculates Euclidean distance between two 2D coordinates (`Origin` and `Destination`).
- Calculates the total time required to travel the distance given the rover's:
  - Initial Velocity ($v_0$)
  - Constant Acceleration ($a$)
  - Maximum Speed ($v_{max}$)
- Considers two phases of motion: 
  - Acceleration phase (until $v_{max}$ is reached).
  - Cruising phase (constant $v_{max}$).
- Includes robust input validation and error handling for invalid or non-physical inputs (e.g., zero acceleration with zero initial velocity, negative values, and non-numerical inputs).

## Requirements

- Python 3.x

## How to Run

Execute the script from the terminal:

```bash
python main.py
```

## Usage

When you run the script, it will interactively prompt you for the following mission parameters:

1. **Origin X1**: The starting X-coordinate.
2. **Origin Y1**: The starting Y-coordinate.
3. **Destination X2**: The target X-coordinate.
4. **Destination Y2**: The target Y-coordinate.
5. **Initial Velocity (m/s)**: State of motion at the start.
6. **Acceleration (m/s²)**: How fast the rover accelerates.
7. **Top Speed (m/s)**: The velocity limit of the rover.

### Example Output

```text
--- Rover Navigation System: Task 1 ---
Enter Origin X1: 0
Enter Origin Y1: 0
Enter Destination X2: 100
Enter Destination Y2: 100
Enter Initial Velocity (m/s): 0
Enter Acceleration (m/s^2): 2
Enter Top Speed (m/s): 10

--- Results ---
Distance to destination: 141.42 m
Time required: 16.64 seconds
```
