
import time
import pygame
import matplotlib.pyplot as plt

from game.maze import generate_maze
from game.solver import solve_maze
from game.q_learning import train_q_learning, get_learned_path
from comparison import save_results, show_comparison


# ================= CONFIGURATION =================

pygame.init()

CELL = 25
INFO_HEIGHT = 125
TRAINING_EPISODES = 10000
ANIMATION_SPEED = 5

DIFFICULTIES = {
    "1": {"name": "Easy", "size": 11},
    "2": {"name": "Medium", "size": 21},
    "3": {"name": "Hard", "size": 31},
}

difficulty = "2"
score = 0
game_start_time = time.time()

maze = generate_maze(DIFFICULTIES[difficulty]["size"])
ROWS, COLS = len(maze), len(maze[0])

screen = pygame.display.set_mode(
    (COLS * CELL, ROWS * CELL + INFO_HEIGHT)
)

pygame.display.set_caption("AI Maze Game - AI Pathfinding")

font = pygame.font.SysFont("Arial", 15)
title_font = pygame.font.SysFont("Arial", 21, bold=True)
clock = pygame.time.Clock()

start = (1, 1)
goal = (ROWS - 2, COLS - 2)
player = list(start)

path = []
q_table = None
training_history = None

show_ai = False
animate_ai = False
animation_index = 0
animation_counter = 0

won = False
training = False

bfs_time = None
q_path_time = None
bfs_steps = None
q_steps = None

message = "Arrows: Move | B: BFS | T: Train AI"


# ================= RESET GAME =================

def reset_game():
    global maze, ROWS, COLS, start, goal, player
    global path, q_table, training_history
    global show_ai, animate_ai, animation_index
    global animation_counter, won, score, game_start_time
    global bfs_time, q_path_time, bfs_steps, q_steps, message

    maze = generate_maze(DIFFICULTIES[difficulty]["size"])
    ROWS, COLS = len(maze), len(maze[0])

    start = (1, 1)
    goal = (ROWS - 2, COLS - 2)
    player = list(start)

    path = []
    q_table = None
    training_history = None

    show_ai = False
    animate_ai = False
    animation_index = 0
    animation_counter = 0
    won = False

    score = 0
    game_start_time = time.time()

    bfs_time = None
    q_path_time = None
    bfs_steps = None
    q_steps = None

    message = "New maze! Use arrows or train AI."

    screen_size = (COLS * CELL, ROWS * CELL + INFO_HEIGHT)
    pygame.display.set_mode(screen_size)


# ================= DRAW TEXT =================

def draw_text(text, x, y, color=(25, 25, 25)):
    surface = font.render(str(text), True, color)
    screen.blit(surface, (x, y))


# ================= DRAW GAME =================

def draw_game():
    screen.fill((245, 245, 245))

    # Maze walls and open paths
    for r in range(ROWS):
        for c in range(COLS):
            color = (35, 40, 55) if maze[r][c] == 1 else (255, 255, 255)

            pygame.draw.rect(
                screen,
                color,
                (c * CELL, r * CELL, CELL - 1, CELL - 1)
            )

    # AI path
    if show_ai and path:
        visible_path = (
            path[:animation_index + 1]
            if animate_ai else path
        )

        for r, c in visible_path:
            if (r, c) not in (start, goal):
                pygame.draw.rect(
                    screen,
                    (100, 190, 255),
                    (
                        c * CELL + 5,
                        r * CELL + 5,
                        CELL - 10,
                        CELL - 10
                    )
                )

    # Start marker
    pygame.draw.rect(
        screen,
        (40, 190, 80),
        (start[1] * CELL, start[0] * CELL, CELL - 2, CELL - 2)
    )

    # Goal marker
    pygame.draw.rect(
        screen,
        (230, 60, 60),
        (goal[1] * CELL, goal[0] * CELL, CELL - 2, CELL - 2)
    )

    # Player
    pygame.draw.circle(
        screen,
        (255, 165, 0),
        (
            player[1] * CELL + CELL // 2,
            player[0] * CELL + CELL // 2
        ),
        CELL // 3
    )

    # Information panel
    panel_y = ROWS * CELL
    pygame.draw.rect(
        screen,
        (225, 230, 240),
        (0, panel_y, COLS * CELL, INFO_HEIGHT)
    )

    elapsed = int(time.time() - game_start_time)

    screen.blit(
        title_font.render("AI Maze Game", True, (25, 45, 80)),
        (8, panel_y + 4)
    )

    draw_text(message, 8, panel_y + 30)
    draw_text(
        f"Score: {score} | Time: {elapsed}s | "
        f"Level: {DIFFICULTIES[difficulty]['name']}",
        8, panel_y + 49
    )
    draw_text(
        "Arrows: Move | B: BFS | T: Train | L: Learned path",
        8, panel_y + 68
    )
    draw_text(
        "A: Auto-solve | G: Reward graph | P: Compare",
        8, panel_y + 87
    )
    draw_text(
        "1: Easy | 2: Medium | 3: Hard | R: Reset | Esc: Quit",
        8, panel_y + 106
    )

    pygame.display.flip()


# ================= REWARD GRAPH =================

def show_reward_graph(history):
    rewards = history["rewards"]

    plt.figure(figsize=(10, 5))
    plt.plot(rewards, alpha=0.35, label="Episode reward")

    window = 100

    if len(rewards) >= window:
        averages = [
            sum(rewards[max(0, i - window + 1):i + 1])
            / len(rewards[max(0, i - window + 1):i + 1])
            for i in range(len(rewards))
        ]

        plt.plot(averages, label="100-episode moving average")

    plt.xlabel("Episode")
    plt.ylabel("Total reward")
    plt.title("Q-Learning Training Progress")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ================= COMPARISON DASHBOARD =================

def compare_algorithms():
    print("\n========== ALGORITHM COMPARISON ==========")
    print("Difficulty:", DIFFICULTIES[difficulty]["name"])

    if bfs_time is not None:
        print(f"BFS search time: {bfs_time:.6f} seconds")
        print("BFS path steps:", bfs_steps)
    else:
        print("BFS results unavailable. Press B first.")

    if q_path_time is not None:
        print(f"Q-Learning path extraction time: {q_path_time:.6f} seconds")
        print("Q-Learning path steps:", q_steps)
    else:
        print("Q-Learning results unavailable. Press T, then L.")

    success_rate = 0

    if training_history is not None:
        episodes = training_history["episodes"]
        successes = training_history["successes"]

        if episodes > 0:
            success_rate = 100 * successes / episodes

        print(f"Training success rate: {success_rate:.2f}%")
        print(f"Successful episodes: {successes}/{episodes}")

    print("==========================================\n")

    # Show charts and save the measured results
    try:
        show_comparison(
            bfs_steps,
            bfs_time,
            q_steps,
            q_path_time,
            success_rate
        )

        save_results(
            DIFFICULTIES[difficulty]["name"],
            bfs_steps,
            bfs_time,
            q_steps,
            q_path_time,
            success_rate
        )

        return "Comparison charts displayed; results saved to CSV."

    except Exception as error:
        print("Comparison error:", error)
        return "Comparison failed. Check the terminal."


# ================= MAIN LOOP =================

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            # Reset at current difficulty
            elif event.key == pygame.K_r:
                reset_game()

            # Difficulty selection
            elif event.key in (
                pygame.K_1, pygame.K_2, pygame.K_3
            ):
                difficulty = str(event.key - pygame.K_0)
                reset_game()
                message = f"{DIFFICULTIES[difficulty]['name']} level selected!"

            # BFS shortest path
            elif event.key == pygame.K_b:
                search_start = time.perf_counter()

                path = solve_maze(maze, tuple(player), goal)

                bfs_time = time.perf_counter() - search_start
                bfs_steps = len(path) - 1 if path else None

                show_ai = bool(path)
                animate_ai = False
                animation_index = 0

                if path:
                    message = f"BFS path found: {bfs_steps} steps"
                else:
                    message = "BFS could not find a path."

            # Q-Learning training
            elif event.key == pygame.K_t and not training:
                training = True
                message = "Training Q-Learning agent..."
                draw_game()

                try:
                    q_table, training_history = train_q_learning(
                        maze,
                        episodes=TRAINING_EPISODES,
                        alpha=0.15,
                        gamma=0.95,
                        epsilon=1.0,
                        return_stats=True
                    )

                    message = "Training complete! Press L for path."

                except Exception as error:
                    q_table = None
                    training_history = None
                    message = f"Training error: {error}"
                    print("Training error:", error)

                finally:
                    training = False

            # Display learned path
            elif event.key == pygame.K_l:
                if q_table is None:
                    message = "Press T to train AI first."
                else:
                    search_start = time.perf_counter()

                    path = get_learned_path(
                        maze,
                        q_table,
                        start=tuple(player),
                        goal=goal
                    )

                    q_path_time = time.perf_counter() - search_start
                    q_steps = len(path) - 1 if path else None

                    show_ai = bool(path)
                    animate_ai = False
                    animation_index = 0

                    if path:
                        message = f"Learned path found: {q_steps} steps"
                    else:
                        message = "No learned path. Try training again."

            # Automatic player movement
            elif event.key == pygame.K_a:
                if path:
                    animate_ai = True
                    show_ai = True
                    animation_index = 0
                    animation_counter = 0
                    player = list(path[0])
                    won = False
                    message = "AI is solving the maze..."
                else:
                    message = "Press B or train AI and press L first."

            # Reward graph
            elif event.key == pygame.K_g:
                if training_history is None:
                    message = "Press T to train AI first."
                else:
                    show_reward_graph(training_history)
                    message = "Reward graph displayed."

            # Comparison dashboard and CSV export
            elif event.key == pygame.K_p:
                message = compare_algorithms()

            # Manual player movement
            else:
                moves = {
                    pygame.K_UP: (-1, 0),
                    pygame.K_DOWN: (1, 0),
                    pygame.K_LEFT: (0, -1),
                    pygame.K_RIGHT: (0, 1)
                }

                if event.key in moves and not won and not animate_ai:
                    dr, dc = moves[event.key]
                    nr = player[0] + dr
                    nc = player[1] + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and maze[nr][nc] == 0
                    ):
                        player = [nr, nc]
                        score += 10
                        show_ai = False

                        if tuple(player) == goal:
                            won = True
                            score += 100
                            message = "You solved the maze! Bonus: 100 points!"

    # Animate player along the selected path
    if animate_ai and path:
        animation_counter += 1

        if animation_counter >= ANIMATION_SPEED:
            animation_counter = 0

            if animation_index < len(path) - 1:
                animation_index += 1
                player = list(path[animation_index])

            if tuple(player) == goal:
                animate_ai = False
                won = True
                score += 100
                message = "AI solved the maze! Bonus: 100 points!"

    draw_game()
    clock.tick(30)

pygame.quit()
