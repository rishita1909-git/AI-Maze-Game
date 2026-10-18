# 🧩 AI Maze Game Using BFS and Q-Learning

An interactive Python-based AI Maze Game that demonstrates how traditional search algorithms and reinforcement learning can solve maze problems.

## 📌 Project Overview

The AI Maze Game allows users to explore randomly generated mazes and compare two AI approaches: Breadth-First Search (BFS) and Q-Learning. It includes multiple difficulty levels, path visualization, agent training, and performance comparison.

## ✨ Features

- 🎮 Interactive maze game with manual player movement
- 🟢 Three difficulty levels: Easy, Medium, and Hard
- 🔍 BFS algorithm for finding the shortest path
- 🤖 Q-Learning agent training using rewards
- 🛣️ Path visualization and automatic movement
- 📊 Performance comparison graphs
- 📁 CSV file for saving algorithm results
- 🔄 Maze reset and replay functionality

## 🛠️ Technologies Used

- Python
- Pygame
- NumPy
- Matplotlib
- Breadth-First Search (BFS)
- Reinforcement Learning (Q-Learning)

## 📂 Project Structure

```text
AI_Maze_Game/
├── main.py
├── comparison.py
├── requirements.txt
├── README.md
├── maze_results.csv
├── data/
└── game/
    ├── __init__.py
    ├── maze.py
    ├── solver.py
    └── q_learning.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rishita1909-git/AI-Maze-Game.git
cd AI-Maze-Game
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the game

```bash
python main.py
```

## 🎮 Game Controls

| Key | Action |
|---|---|
| `1` | Easy mode |
| `2` | Medium mode |
| `3` | Hard mode |
| Arrow keys | Move player |
| `B` | Find BFS path |
| `T` | Train Q-Learning agent |
| `L` | Display learned path |
| `A` | Animate current path |
| `G` | Display reward graph |
| `P` | Compare algorithms and save results |
| `R` | Reset maze |
| `Esc` | Exit game |

## 🧠 Algorithms Explained

### 1. Breadth-First Search (BFS)

BFS explores the maze level by level. In an unweighted maze, it finds a shortest path when the goal is reachable.

### 2. Q-Learning

Q-Learning is a reinforcement learning algorithm. The agent learns which actions are useful by receiving rewards and penalties while exploring the maze.

## 📊 Performance Evaluation

The project compares the algorithms using:

- **Path length:** Number of steps needed to reach the goal
- **Search time:** Time taken to calculate a path
- **Training success rate:** Percentage of training episodes that reach the goal, according to the implementation

The comparison results are saved in `maze_results.csv`, and graphs help visualize performance.

## 🖼️ Screenshots

Add your actual screenshots to a folder named `screenshots/`.

### Maze Game

![AI Maze Game](screenshots/maze-game.png)

### Algorithm Comparison

![Algorithm Comparison](screenshots/comparison.png)

## 🚀 Future Improvements

- Develop a graphical dashboard for performance analysis
- Improve Q-Learning training efficiency
- Add more maze-generation algorithms
- Support additional AI search algorithms
- Enhance the user interface

## 👩‍💻 Author

**Rishita Chaturvedi**

B.Tech — Computer Engineering

GitHub: [rishita1909-git](https://github.com/rishita1909-git)

## 📄 License

This project is intended for educational and learning purposes. Add an open-source license file if you want to specify how others may use or distribute the code.
