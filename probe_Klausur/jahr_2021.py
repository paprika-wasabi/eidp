from math import floor
from dataclasses import dataclass
from typing import Optional


def count_iterations(i: int):
    # while True:
    #     if i == 0:
    #         return 
    #     elif i % 3 == 0:
    #         return count_iterations(i + 4)
    #     elif i % 4 == 0:
    #         return count_iterations(i * 0.5)
    #     else:
    #         return count_iterations(i - 1)
    count = 0
    while i > 0:
        if i % 3 == 0:
            i = i + 4
            count += 1
        elif i % 4 == 0:
            i = i * 0.5
            count += 1
        else:
            i = i - 1
            count += 1
    return count 


def cluster_by_points(points: dict):
    result = {}
    for item in sorted(points.values()):
        value = item / 10 
        result.update({floor(value) * 10 : []})
    
    for item in points:
        value2 = points[item] / 10
        for el in result:
            if floor(value2) * 10 == el:
                result[el].append(item)
        # if floor(value) in for el in result:
        #     print('yes')
    sorted(result)  
    return result
    
# print(count_iterations(5))

# points = {"Paul": 15, "Frank": 44, "Tim": 20, "Anna": 29}


# points = {"Paul": 15, "Frank": 44, "Tim": 20, "Anna": 29}

# print(sorted(points.values()))
# print(cluster_by_points(points))


def is_strong(pow: str) -> bool:
    zz = ["!", "?", "+", "*"]
    if len(pow) <= 8:
        return False
    digits = 0
    s_sym = 0
    alpha = 0
    for el in pow:
        if el.isdigit() == True:
            digits += 1
            continue
        if el.isupper() == True:
            alpha += 1
            continue
        if el in zz:
            s_sym += 1
            continue

    match digits:
        case 0:
            return False
        case digits if digits <= 3:
            if s_sym < 1:
                return False

    match alpha:
        case alpha if alpha < 3 and digits <= 3 and s_sym == 1:
            return False
        
    return True
    

@dataclass
class Ranking:
    club: str
    wins: int
    draws: int
    losses: int
    goals_achieved: int
    goals_conceded: int

    def show(self):
        return self.club +" "+ str(self.wins + self.draws + self.losses) +" "+str(self.wins) +" "+ str(self.draws) +" "+ str(self.losses) +" "+ str(self.goals_achieved) + ":" + str(self.goals_conceded) +" " + str(self.goals_achieved - self.goals_conceded) + " " + str(self.wins*3 + self.draws)

    def __lt__(self, other):
        punkte = self.wins*3 + self.draws
        o_p = other.wins*3 + other.draws
        goals_dif_s = self.goals_achieved - self.goals_conceded
        goals_dif_o = other.goals_achieved - other.goals_conceded
        if punkte > (o_p):
            return False
        elif punkte == (o_p):
            if goals_dif_s > goals_dif_o:
                return False
            elif goals_dif_s == goals_dif_o:
                if self.wins < other.wins:
                    return True
        

@dataclass
class Node:
 mark: str
 left: Optional['Node']
 right: Optional['Node']


def find_substr(node: Node):
    match node:
        case str():
            pass
# password = "ABCcdefghhitgdsa123!"
# print(is_strong(password))

# r1 = Ranking("FC H", 6, 2, 2, 23, 14)
# r2 = Ranking("SC B", 5, 5, 0, 21, 12)


# # print(r1.show())
# assert(not(r1 < r1))
# assert r2 < r1
# print(r2 < r1)

def my_enumerate(s: str):
    result = []
    for i in range(len(s)):
        result.append((i, s[i]))
    return result

print(list(my_enumerate('abcd')))

def prefixes(node: list):
    result = []
    for i in range(len(node) + 1):
        n = list(node[j] for j in range(i))
        result.append(n)
    return result

print(list(prefixes([1,2,3,4])))

def alternate(xs, ys):
    # gen_s = (el for el in s)
    # gen_node = (el for el in node)
    result = []
    s_done = False
    node_done = False
    while True:
        if s_done is True and node_done is True:
            break
        if s_done is False:
            try:
                new_s = next(xs)
                result.append(new_s)
            except StopIteration:
                s_done = True
        if node_done is False:
            try:
                new_node = next(ys)
                result.append(new_node)
            except StopIteration:
                node_done = True
    return result

# print(alternate("abcdefg", [1, 2, 3, 4]))
print(list(alternate(iter("abcdef"), iter([0, 1, 2, 3]))))

def twice(f):
    return lambda x: x * 2
