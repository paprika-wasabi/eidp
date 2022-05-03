def visualize_path(world: list[list], path: list[tuple]):
    for y in range(len(world)):
        for x in range(len(world[y])):
            if world[y][x] == 1:
                if (x, y) in path:
                    print('X', end='')
                else:
                    print('.', end='')
            elif world[y][x] == 0:
                print('#', end='')
        print()


def find_paths(world, sx, sy, ex, ey, path: list[tuple]):
    if sx == ex and sy == ey:
        yield path
    if sx >= 0 and sx <= ex and sy >= 0 and sy <= ey and world[sy][sx] == 1:
        pass
        # if (sx, sy) in path:
        #     pass
        # path.append((sx, sy))
        # if world[sy - 1][sx]== True:S
        #     yield from find_paths(world, sx, sy - 1, ex, ey, path)
        # if world[sy][sx + 1]== True:
        #     yield from find_paths(world, sx, sy - 1, ex, ey, path)
        # if world[sy + 1][sx]== True:
        #     yield from find_paths(world, sx, sy - 1, ex, ey, path)
        # if world[sy][sx - 1]== True:
        #     yield from find_paths(world, sx, sy - 1, ex, ey, path)
        # path.remove((sx, sy))
        # return False
    # if sx >= ex and sy >= ey and sx <= (len(world) - 1) and sy <= (len(world) - 1) and world[sy][sx] == 1:
    #     if (sx, sy) in path:
    #         return False
    #     path.append((sx, sy))
    #     if find_paths(world, sx, sy - 1, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx + 1, sy, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx, sy + 1, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx - 1, sy, ex, ey, path) == True:
    #         return True
    #     path.remove((sx, sy))
    #     return False
    # if sx == ex and sy == ey :
    #     print(path)
    #     return False
    # if sx >= 0 and sx <= ex and sy >= 0 and sy <= ey and world[sy][sx] == 1:
    #     if (sx, sy) in path:
    #         return False
    #     path.append((sx, sy))
    #     if find_paths(world, sx, sy - 1, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx + 1, sy, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx, sy + 1, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx - 1, sy, ex, ey, path) == True:
    #         return True
    #     path.remove((sx, sy))
    #     return False
    # if sx >= ex and sy >= ey and sx <= (len(world) - 1) and sy <= (len(world) - 1) and world[sy][sx] == 1:
    #     if (sx, sy) in path:
    #         return False
    #     path.append((sx, sy))
    #     if find_paths(world, sx, sy - 1, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx + 1, sy, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx, sy + 1, ex, ey, path) == True:
    #         return True
    #     if find_paths(world, sx - 1, sy, ex, ey, path) == True:
    #         return True
    #     path.remove((sx, sy))
    #     return False
# world = [[1, 1, 1, 0, 1, 1, 1, 0, 1],
#              [1, 1, 1, 0, 1, 1, 0, 1, 1],
#              [1, 1, 0, 1, 1, 1, 1, 0, 1],
#              [1, 1, 1, 1, 1, 0, 1, 1, 0],
#              [1, 0, 1, 1, 0, 1, 1, 0, 0],
#              [1, 0, 1, 0, 1, 1, 1, 0, 0],
#              [1, 1, 0, 1, 1, 1, 1, 1, 1],
#              [1, 1, 1, 1, 0, 1, 0, 0, 0],
#              [1, 1, 1, 0, 1, 1, 1, 1, 1]]
# for i in range(2):
#     print(next(find_paths(world, 0, 0, 3, 3, [])))
# # print(list(find_paths(world, 0, 0, 3, 3, [])))
# # print(next(find_paths(world, 0, 0, 3, 3, [])))
# # print(list(find_paths(world, 0, 0, 3, 3, [])))
# def permute(list, s):
#    if list == 1:
#       return s
#    else:
#       return [
#          y + x
#          for y in permute(1, s)
#          for x in permute(list - 1, s)
#       ]
# def trans(x, y):
#     x = x + 1
#     y = y + 1
#     yield [(x,y)] + [(x,y)]
# # print(list(permute(2, ['a', 'b', 'c'])))
# # print(next(gen_per(2, ['a', 'b', 'c'])))
# print(next(trans(3,3)))