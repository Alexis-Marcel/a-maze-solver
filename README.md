# A-Maze Solver with A* and Maze Generation

## Overview

"A-Maze Solver" is a Python project that showcases the generation of intricate mazes and their resolution using the A* pathfinding algorithm. Utilizing Pygame for graphics, this application not only allows users to observe the fascinating process of maze creation but also demonstrates the efficiency of the A* algorithm in finding the shortest path through the maze. The maze generation is based on a variant of the Randomized Prim's algorithm, providing unique and challenging labyrinths for each run.

## Features

- Dynamic generation of complex mazes using a variant of the Randomized Prim's algorithm.
- Maze solving visualization with the A* pathfinding algorithm.
- Real-time graphical display of both maze generation and pathfinding using Pygame.

## Technologies Used

- **Language:** Python
- **Graphics Library:** Pygame
- **Maze Generation Algorithm:** Variant of Randomized Prim's Algorithm
- **Pathfinding Algorithm:** A*

## Installation and Usage

1. Ensure Python 3.x and Pip are installed on your system.
2. Clone the repository:
   ```
   git clone https://github.com/Alexis-Marcel/a-maze-solver.git
   ```
3. Navigate to the project directory:
   ```
   cd a-maze-solver
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python maze_solver.py
   ```

## How It Works

- The application starts by generating a maze with the specified dimensions. This process visualizes the maze being carved out cell by cell.
- Once the maze is generated, the A* algorithm kicks in to find the shortest path from the start to the finish.
- Users can watch as the path is determined in real-time, showcasing the power and efficiency of A*.
