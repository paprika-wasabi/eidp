from   dataclasses import dataclass
from   typing      import Any, Optional, Union
from unittest.util import strclass
# import math
# import pytest

@dataclass
class Node:
    mark: str
    left: Optional['Node']
    right: Optional['Node']

## Aufgabe 6 (Recursion) #######################################################
tree = Node("aab", Node("baa", None, None), Node("aba", None, None))
tree2 = Node("aab", Node("baa", Node("baa", None, None), None), Node("aba", None, None))


def find_substrings(node : Optional['Node'], substr) -> list:
    match node:
        case Node(str, None, None):
            return str
        case Node(str, left, right):  
            ls = find_substrings(left, substr)
            print(ls)
            rs = find_substrings(right, substr)
            print(rs)
            return 
        
        
                
tree = Node("aab", Node("baa", None, None), Node("aba", None, None))

# print(tree.mark)
# print(tree.left)
print(find_substrings(tree, "ab"))
print()
print(find_substrings(tree2, "ab"))