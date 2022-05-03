from copy import deepcopy, copy
from math import inf
from typing import Iterator


def visualize_path(world: list[list[int]],
                   path: list[tuple[int, int]]):
    # copy the world and change all fields of the path to 2
    vis_world = deepcopy(world)
    for px, py in path:
        vis_world[py][px] = 2

    # map numbers to characters to visualize the world
    chars = ['#', '.', "X"]
    for row in vis_world:
        print(''.join(chars[c] for c in row))


def find_paths(world: list[list[int]], sx: int, sy: int, ex: int, ey: int,
               path: list) -> Iterator[list[tuple[int, int]]]:
    # add current position to path
    path.append((sx, sy))

    # check if path is complete
    if sx == ex and sy == ey:
        # here we copy the path, otherwise backtracing will delete the steps
        yield copy(path)
        return

    # move up, right, down, left
    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        nx, ny = sx + dx, sy + dy

        # check if position is possible to walk on
        if (0 <= nx < len(world) and 0 <= ny < len(world[0]) and
                world[ny][nx] == 1):

            # check if position was not already walked on
            if (nx, ny) not in path:

                # start pathfinding from the new position
                yield from find_paths(world, nx, ny, ex, ey, path)

                # backtrace by deleting the last step in the path
                path.pop()


def get_shortest_path(path_generator: Iterator[list[tuple[int, int]]]
                      ) -> list[tuple[int, int]]:
    min_path_length = inf
    min_path = []
    num_paths = 0
    for path in path_generator:
        if len(path) < min_path_length:
            min_path_length = len(path)
            min_path = path
        num_paths += 1
    print(str(num_paths) + " Pfade gefunden, kürzester hat " +
          str(min_path_length)+" Schritte.")
    return min_path


def main():
    world = [[1, 1, 1, 0],
             [1, 1, 1, 0],
             [1, 0, 1, 1],
             [1, 0, 1, 1]]
    visualize_path(world, [(0, 0), (1, 0)])

    print(next(find_paths(world, 0, 0, 3, 3, [])))
    shortest_path = get_shortest_path(find_paths(world, 0, 0, 3, 3, []))
    visualize_path(world, shortest_path)


if __name__ == "__main__":
    main()
