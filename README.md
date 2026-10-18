# AI Maze Game Using BFS and Q-Learning

## 1. Project Overview
The AI Maze Game is a Python-based game that demonstrates how Artificial Intelligence algorithms solve mazes. It compares Breadth-First Search (BFS), a traditional search algorithm, with Q-Learning, a reinforcement learning technique.

## 2. Features
- Random maze generation
- Three difficulty levels: Easy, Medium, and Hard
- Manual player movement
- BFS shortest-path solving
- Q-Learning agent training
- Automatic path animation
- Algorithm performance comparison
- CSV results logging
- Graphs for path length, execution time, and training success rate

## 3. Technologies Used
- Python
- Pygame
- Matplotlib
- CSV
- Q-Learning and BFS algorithms

## 4. Project Structure
```text
AI_Maze_Game/
├── main.py
├── comparison.py
├── maze_results.csv
└── game/
    ├── __init__.py
    ├── maze.py
    ├── solver.py
    └── q_learning.py
```

## 5. How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Activate the virtual environment.
4. Install the required libraries:
   `pip install pygame matplotlib numpy`
5. Run the game:
   `python main.py`

## 6. Controls
- `1` — Easy difficulty
- `2` — Medium difficulty
- `3` — Hard difficulty
- Arrow keys — Move the player
- `B` — Find the BFS path
- `T` — Train the Q-Learning agent
- `L` — Display the learned path
- `A` — Animate the current path
- `G` — Display the reward graph
- `P` — Compare algorithms and save results
- `R` — Reset the maze
- `Esc` — Exit the game

## 7. Algorithms
**Breadth-First Search (BFS):** Explores the maze level by level and finds a shortest path in an unweighted maze when a path exists.

**Q-Learning:** Learns actions through rewards and penalties to find a route from the starting point to the goal.

## 8. Results
The project records difficulty level, path length, search time, and Q-Learning training success rate in a CSV file. Graphs help compare the algorithms.

## 9. Conclusion
This project demonstrates the difference between traditional search and reinforcement learning through an interactive maze game. It provides a practical introduction to AI problem-solving and algorithm evaluation.
