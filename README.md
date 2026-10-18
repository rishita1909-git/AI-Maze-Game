
# 🧩 AI Maze Game Using BFS and Q-Learning

An interactive Python-based AI Maze Game that demonstrates how traditional search algorithms and reinforcement learning can solve maze problems.

## 📌 Project Overview

The AI Maze Game is a Python-based application that generates mazes and allows users to explore different AI problem-solving techniques. It compares Breadth-First Search (BFS) with Q-Learning through an interactive game environment.

The project includes multiple difficulty levels, path visualization, reinforcement learning, and performance comparison.

## ✨ Features

- 🎮 Interactive maze game with manual player movement
- 🟢 Three difficulty levels: Easy, Medium, and Hard
- 🔍 BFS algorithm for finding a shortest path
- 🤖 Q-Learning agent training
- 🛣️ Learned-path visualization and automatic movement
- 📊 Algorithm performance comparison graphs
- 📁 CSV file for saving experimental results
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

### 1. Clone the Repository

```bash
git clone https://github.com/rishita1909-git/AI-Maze-Game.git
cd AI-Maze-Game
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Game

```bash
python main.py
```

## 🎮 Game Controls

| Key | Action |
|---|---|
| `1` | Select Easy mode |
| `2` | Select Medium mode |
| `3` | Select Hard mode |
| Arrow keys | Move the player manually |
| `B` | Find the BFS path |
| `T` | Train the Q-Learning agent |
| `L` | Display the learned path |
| `A` | Animate the current path |
| `G` | Display the reward graph |
| `P` | Compare algorithms and save results |
| `R` | Reset the maze |
| `Esc` | Exit the game |

## 🧠 Algorithms Explained

### 1. Breadth-First Search (BFS)

BFS explores the maze level by level. In an unweighted maze, it finds a shortest path to the goal if the goal is reachable.

**Advantages:**
- Finds a shortest path in an unweighted maze
- Complete when the search space is finite
- Does not require model training

### 2. Q-Learning

Q-Learning is a reinforcement learning algorithm. The agent learns which actions are useful by receiving rewards and penalties while exploring the maze.

**Advantages:**
- Learns from interactions with the environment
- Can improve its policy through training
- Demonstrates the fundamentals of reinforcement learning

## 📊 Performance Evaluation

The project compares the algorithms using the following metrics:

- **Path Length:** Number of steps required to reach the goal.
- **Search Time:** Time taken to calculate a path.
- **Training Success Rate:** Percentage of training episodes that reach the goal, according to the implementation.

The experimental results are saved in `maze_results.csv`. Matplotlib graphs are used to visualize the comparison.

Results may vary depending on maze generation, difficulty level, and Q-Learning training settings.

## 🚀 Future Improvements

- Add more maze-generation algorithms
- Implement additional AI search algorithms
- Improve Q-Learning training efficiency
- Develop a graphical performance dashboard
- Enhance the game interface
- Add more evaluation metrics and experiments

## 👩‍💻 Author

**Rishita Chaturvedi**

B.Tech — Computer Engineering

GitHub: [rishita1909-git](https://github.com/rishita1909-git)

## 📄 License

This project is intended for educational and learning purposes. Add a suitable open-source license if you want to define how others may use, modify, or distribute the code.
