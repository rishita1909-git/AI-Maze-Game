import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt


CSV_FILE = "maze_results.csv"


def save_results(
    difficulty,
    bfs_steps,
    bfs_time,
    q_steps,
    q_time,
    training_success_rate
):
    """Append one experiment's results to the CSV file."""

    file_exists = os.path.exists(CSV_FILE)
    file_is_empty = not file_exists or os.path.getsize(CSV_FILE) == 0

    results = {
        "Date and Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Difficulty": difficulty,
        "BFS Steps": bfs_steps,
        "BFS Search Time (seconds)": (
            round(bfs_time, 6) if bfs_time is not None else ""
        ),
        "Q-Learning Steps": q_steps,
        "Q-Learning Path Time (seconds)": (
            round(q_time, 6) if q_time is not None else ""
        ),
        "Training Success Rate (%)": round(training_success_rate, 2)
    }

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=results.keys())

        if file_is_empty:
            writer.writeheader()

        writer.writerow(results)

    print(f"Results appended to {os.path.abspath(CSV_FILE)}")


def show_comparison(
    bfs_steps,
    bfs_time,
    q_steps,
    q_time,
    success_rate
):
    labels = ["BFS", "Q-Learning"]

    path_values = [
        bfs_steps if bfs_steps is not None else 0,
        q_steps if q_steps is not None else 0
    ]

    plt.figure(figsize=(7, 4))
    plt.bar(labels, path_values)
    plt.title("Path Length Comparison")
    plt.ylabel("Number of Steps")
    plt.tight_layout()
    plt.show()

    time_values = [
        bfs_time if bfs_time is not None else 0,
        q_time if q_time is not None else 0
    ]

    plt.figure(figsize=(7, 4))
    plt.bar(labels, time_values)
    plt.title("Path Search Time Comparison")
    plt.ylabel("Seconds")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(5, 4))
    plt.bar(["Q-Learning"], [success_rate])
    plt.ylim(0, 100)
    plt.title("Q-Learning Training Success Rate")
    plt.ylabel("Success Rate (%)")
    plt.tight_layout()
    plt.show()
