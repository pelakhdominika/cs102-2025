from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def bin_tree_maze(
        rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    grid = create_grid(rows, cols)

    for i in range(1, rows - 1, 2):
        for j in range(1, cols - 1, 2):
            grid[i][j] = " "

    for i in range(1, rows - 1, 2):
        for j in range(1, cols - 1, 2):
            directions = []

            if i > 1:
                directions.append("up")

            if j < cols - 3:
                directions.append("right")

            if directions:
                direction = choice(directions)

                if direction == "up":
                    grid[i - 1][j] = " "
                elif direction == "right":
                    grid[i][j + 1] = " "

    if not random_exit:
        grid[rows - 1][0] = "X"
        grid[rows - 2][0] = " "

        grid[0][cols - 1] = "X"
        grid[0][cols - 2] = " "

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    exits = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "X":
                exits.append((i, j))

    return exits


def encircled_exit(grid: List[List[Union[str, int]]],
                   coord: Tuple[int, int]) -> bool:
    x, y = coord
    rows = len(grid)
    cols = len(grid[0])

    passable = 0

    if x > 0 and grid[x - 1][y] != "■":
        passable += 1
    if x < rows - 1 and grid[x + 1][y] != "■":
        passable += 1
    if y > 0 and grid[x][y - 1] != "■":
        passable += 1
    if y < cols - 1 and grid[x][y + 1] != "■":
        passable += 1

    return passable == 0


def wave_algorithm(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])

    wave_grid = [[-1 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "■":
                wave_grid[i][j] = -2

    sx, sy = start
    ex, ey = end

    wave_grid[sx][sy] = 0
    queue = [(sx, sy)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.pop(0)

        if (x, y) == (ex, ey):
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if wave_grid[nx][ny] == -1:
                    wave_grid[nx][ny] = wave_grid[x][y] + 1
                    queue.append((nx, ny))

    if wave_grid[ex][ey] == -1:
        return None

    path = []
    x, y = ex, ey

    while (x, y) != (sx, sy):
        path.append((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if wave_grid[nx][ny] == wave_grid[x][y] - 1:
                    x, y = nx, ny
                    break

    path.append((sx, sy))
    path.reverse()
    return path


def solve_maze(grid):
    exits = get_exits(grid)

    if len(exits) != 2:
        return grid, None

    entry, exit_cell = exits[0], exits[1]

    if encircled_exit(grid, entry) or encircled_exit(grid, exit_cell):
        return grid, None

    path = wave_algorithm(grid, entry, exit_cell)

    return grid, path


def add_path_to_grid(grid, path):
    if path:
        for i, j in path:
            if grid[i][j] != "X":
                grid[i][j] = "•"
    return grid


if __name__ == "__main__":
    print("=== Тест: Маленький лабиринт 7x7 ===")
    GRID = bin_tree_maze(7, 7, random_exit=False)

    print("Лабиринт:")
    for row in GRID:
        print(' '.join(str(cell) for cell in row))

    exits = get_exits(GRID)
    print(f"\nВходы/выходы: {exits}")

    print("\n=== Поиск пути ===")
    MAZE, PATH = solve_maze(GRID)

    if PATH:
        print(f"✓ Путь найден! Длина: {len(PATH)}")
        print(f"Координаты пути: {PATH}")

        maze_with_path = deepcopy(MAZE)
        maze_with_path = add_path_to_grid(maze_with_path, PATH)

        print("\n=== Лабиринт с путем ===")
        for row in maze_with_path:
            print(' '.join(str(cell) for cell in row))
    else:
        print("✗ Путь не найден!")

        print("\n=== Отладка ===")
        print("Проверка проходимости входа/выхода:")
        for exit_coord in exits:
            x, y = exit_coord
            print(f"\nКлетка {exit_coord}: {GRID[x][y]}")
            print(f"Соседи:")
            if x > 0:
                print(f"  Вверх ({x - 1}, {y}): {GRID[x - 1][y]}")
            if x < len(GRID) - 1:
                print(f"  Вниз ({x + 1}, {y}): {GRID[x + 1][y]}")
            if y > 0:
                print(f"  Влево ({x}, {y - 1}): {GRID[x][y - 1]}")
            if y < len(GRID[0]) - 1:
                print(f"  Вправо ({x}, {y + 1}): {GRID[x][y + 1]}")
