from copy import deepcopy
from typing import Iterator
from random import uniform, random, randrange, seed
from math import inf
from timeit import default_timer as timer
from pathfinder import find_paths, visualize_path, get_shortest_path


def test_pathfinder():
    # small world
    world = [[1, 1, 1, 0],
             [1, 1, 1, 0],
             [1, 0, 1, 1],
             [1, 0, 1, 1]]
    print("Kleines Labyrinth:")
    visualize_path(world, [])
    print()

    # test first path
    start_timer = timer()
    print("Kleines Labyrinth, erster Pfad:")
    first_path = next(find_paths(world, 0, 0, 3, 3, []))
    assert first_path == [
        (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]
    visualize_path(world, first_path)
    print("Berechnungsdauer: " + str(round(timer() - start_timer, 6)) + "s.\n")

    # test first path when swapping start and end
    assert next(find_paths(world, 3, 3, 0, 0, [])) == [
        (3, 3), (3, 2), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1), (0, 1), (0, 0)]

    # test shortest path
    print("Kleines Labyrinth, alle Pfade:")
    start_timer = timer()
    path_generator = find_paths(world, 0, 0, 3, 3, [])
    shortest_path = get_shortest_path(path_generator)
    assert shortest_path == [
        (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]
    visualize_path(world, shortest_path)
    print("Berechnungsdauer: " + str(round(timer() - start_timer, 6)) + "s.\n")

    # bigger world
    world = [[1, 1, 1, 0, 1, 1, 1, 0, 1],
             [1, 1, 1, 0, 1, 1, 0, 1, 1],
             [1, 1, 0, 1, 1, 1, 1, 0, 1],
             [1, 1, 1, 1, 1, 0, 1, 1, 0],
             [1, 0, 1, 1, 0, 1, 1, 0, 0],
             [1, 0, 1, 0, 1, 1, 1, 0, 0],
             [1, 1, 0, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 0, 1, 0, 0, 0],
             [1, 1, 1, 0, 1, 1, 1, 1, 1]]
    print("GroÃŸes Labyrinth:")
    visualize_path(world, [])
    print()

    # test first path
    start_timer = timer()
    print("GroÃŸes Labyrinth, erster Pfad:")
    first_path = next(find_paths(world, 0, 0, 8, 8, []))
    visualize_path(world, first_path)
    assert first_path == [
        (0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3),
        (3, 3), (3, 2), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2),
        (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (5, 6), (5, 7), (5, 8),
        (6, 8), (7, 8), (8, 8)]
    print("Berechnungsdauer: " + str(round(timer() - start_timer, 6)) + "s.\n")

    start_timer = timer()
    print("GroÃŸes Labyrinth, alle Pfade:")
    path_generator = find_paths(world, 0, 0, 8, 8, [])
    shortest_path = get_shortest_path(path_generator)
    visualize_path(world, shortest_path)
    assert shortest_path == [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6),
        (1, 7), (2, 7), (3, 7), (3, 6), (4, 6), (5, 6), (5, 7), (5, 8),
        (6, 8), (7, 8), (8, 8)]
    print("Berechnungsdauer: " + str(round(timer() - start_timer, 6)) + "s.\n")


if __name__ == "__main__":
    test_pathfinder()