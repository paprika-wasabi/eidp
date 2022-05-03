from typing import Optional
from parser import parse
from tree import Node, Var, Val, Op


def node_to_str(e: Op) -> str:
    match e:
        case Val(i):
            return str(i)
        case Var(x):
            return x
        case Op():
            return "(" + str(node_to_str_if(e.left)) + " " + e.operation + " " + str(node_to_str_if(e.right)) + ")"


def node_to_str_if(e: Op | Var | Val) -> str:
    if type(e) == Var:
        return str(e.name)
    if type(e) == Op:
        return "(" + str(node_to_str_if(e.left)) + " " + e.operation + " " + str(node_to_str_if(e.right)) + ")"
    if type(e) == Val:
        return str(e.value)


def optimize_step(e: Op) -> Op | Var | Val:
    match e:
        case Op(op, e1, e2) if op == "*":
            compare = []
            compare_e = []
            compare_value = []
            match e1:
                case Val(i):
                    e1 = int(i)
                    compare_value.append(i)
                    match e2:
                        case Op(op, e1_1, e2_1):
                            match e1_1:
                                case Val(j):
                                    return Op("*", Op("*", Val(i), Val(j)), e2_1)
                case Var(x):
                    e1 = x
                    compare.append(x)
                case Op():
                    return Op("*", optimize_step(e1), e2)
            match e2:
                case Val(j):
                    e2 = int(j)
                    compare_value.append(j)
                case Var(y):
                    e1 = y
                    compare.append(y)
                case Op():
                    return Op("*", Val(i), optimize_step(e2))
            match compare_value:
                case[i, j]:
                    return Val(i * j)
                case[x, y]:
                    return Op("*", Var(x), Var(y))

        case Op(op, e1, e2) if op == "+":
            compare = []
            compare_e = []
            compare_value = []
            match e1:
                case Val(i):
                    e1 = int(i)
                    compare_value.append(i)
                    match e2:
                        case Op(oper, e, f):
                            return Op("+", Val(i), optimize_step(e2))
                case Var(x):
                    e1 = x
                    compare += x
                case Op():
                    compare_e.append(e1)
            match e2:
                case Val(j):
                    e2 = int(j)
                    compare_value.append(j)
                case Var(y):
                    e2 = y
                    compare += y
                case Op():
                    compare_e.append(e2)
            match compare:
                case[x, y] if x == y:
                    return Op('*', Val(2), Var(e2))
                case[x, y] if x != y:
                    return None
            match compare_e:
                case[e, f] if e == f:
                    return Op('*', Val(2), e2)
                case[e, f] if e != f:
                    return Op('+', optimize_step(e1), e2)
            match compare_value:
                case[i, j]:
                    return Val(i + j)
        case _:
            None


def optimize_step_if(e: Op) -> Op:
    if type(e) != Op:
        return None
    if Op and e.operation == "*":
        if type(e.left) and type(e.right) == Val:
            return Val(e.left.value * e.right.value)
        if type(e.left) == Val and type(e.right) == Op:
            if optimize_step_if(e.right) is not None:
                return Op(e.operation, e.left, optimize_step_if(e.right))
            if optimize_step_if(e.right) is None:
                if type(e.right.left) == Val and type(e.right.right) == Var:
                    return Op(e.operation, Op(e.operation, e.left, e.right.left), e.right.right)
    if Op and e.operation == "+":
        if type(e.left) == Var and type(e.right) == Var:
            if e.left.name == e.right.name:
                return Op('*', Val(2), e.right)
            else:
                return None
        if type(e.left) == Op and type(e.right) == Op:
            if e.left == e.right:
                return Op('*', Val(2), e.right)
        if type(e.left) and type(e.right) == Val:
            return Val(e.left.value + e.right.value)
    if type(e.left) == Op:
        return Op(e.operation, optimize_step_if(e.left), e.right)
    if type(e.left) == Val and type(e.right) == Op:
        return Op(e.operation, e.left, optimize_step_if(e.right))


def optimize(e: Op) -> list:
    result = []
    while e is not None:
        result.append(e)
        e = optimize_step(e)
    return result


if __name__ == "__main__":
    Op_input = ''
    while Op_input != "quit":
        Op_input = str(input())
        if parse(Op_input) is None:
            print("Syntax error.")
        elif Op_input == "quit":
            print("Good bye!")
            break
        elif Op_input != "quit":
            result = optimize(parse(Op_input))
            for x in result:
                x_x = node_to_str(x)
                print(x_x)
            print()