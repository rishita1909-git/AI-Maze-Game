
import random


ACTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
]


def train_q_learning(
    maze,
    episodes=10000,
    alpha=0.15,
    gamma=0.95,
    epsilon=1.0,
    return_stats=False
):
    rows, cols = len(maze), len(maze[0])
    start = (1, 1)
    goal = (rows - 2, cols - 2)

    q_table = {
        (r, c): [0.0] * 4
        for r in range(rows)
        for c in range(cols)
        if maze[r][c] == 0
    }

    max_steps = rows * cols * 4
    rewards = []
    successes = 0

    for episode in range(episodes):
        state = start
        total_reward = 0
        reached_goal = False

        current_epsilon = max(
            0.05,
            epsilon * (1 - episode / episodes)
        )

        for _ in range(max_steps):
            if random.random() < current_epsilon:
                action = random.randrange(4)
            else:
                values = q_table[state]
                best = max(values)
                choices = [
                    i for i, value in enumerate(values)
                    if value == best
                ]
                action = random.choice(choices)

            r, c = state
            dr, dc = ACTIONS[action]
            next_state = (r + dr, c + dc)
            nr, nc = next_state

            if (
                not (0 <= nr < rows and 0 <= nc < cols)
                or maze[nr][nc] == 1
            ):
                next_state = state
                reward = -5
                done = False
            elif next_state == goal:
                reward = 100
                done = True
            else:
                reward = -1
                done = False

            old_q = q_table[state][action]
            future_q = (
                0 if done
                else max(q_table[next_state])
            )

            q_table[state][action] = old_q + alpha * (
                reward + gamma * future_q - old_q
            )

            total_reward += reward
            state = next_state

            if done:
                reached_goal = True
                break

        rewards.append(total_reward)

        if reached_goal:
            successes += 1

    print("\nQ-Learning training complete!")
    print("Episodes:", episodes)
    print("Successful episodes:", successes)
    print(f"Success rate: {100 * successes / episodes:.2f}%")

    if return_stats:
        history = {
            "rewards": rewards,
            "successes": successes,
            "episodes": episodes
        }
        return q_table, history

    return q_table


def get_learned_path(maze, q_table, start=(1, 1), goal=None):
    rows, cols = len(maze), len(maze[0])

    if goal is None:
        goal = (rows - 2, cols - 2)

    state = start
    path = [state]
    visited = {state}

    for _ in range(rows * cols * 4):
        if state == goal:
            return path

        values = q_table.get(state, [0.0] * 4)
        best_value = max(values)

        choices = [
            i for i, value in enumerate(values)
            if value == best_value
        ]
        random.shuffle(choices)

        next_state = None

        for action in choices:
            dr, dc = ACTIONS[action]
            nr = state[0] + dr
            nc = state[1] + dc
            candidate = (nr, nc)

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and maze[nr][nc] == 0
                and candidate not in visited
            ):
                next_state = candidate
                break

        if next_state is None:
            return []

        state = next_state
        visited.add(state)
        path.append(state)

    return []
