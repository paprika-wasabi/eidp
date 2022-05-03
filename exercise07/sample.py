from dataclasses import dataclass


@dataclass
class Node:
    mark: int
    children: list['Node']


def show_tree(node: Node) -> str:
    result = ""
    for child in node.children:
        result += show_tree(child) + ","
    result += node.mark + "this is node mark"
    return result


def show_num(node: Node) -> int:
    result = []
    for child in node.children:
        result += show_num(child)
    result.append(node.mark)
    return result





person = Node(60,[
             Node(30,[]),
             Node(35,[
                 Node(10,[])
             ]),
             Node(38,[
                 Node(10,[]),
                 Node(13,[])
             ])
])


tree = Node('a',[
            Node('b',[]),
            Node('c',[
                Node('e',[])
            ]),
            Node('d',[
                Node('f',[]),
                Node('g',[]),
                Node('h',[])
            ])

])
print(show_num(person))
