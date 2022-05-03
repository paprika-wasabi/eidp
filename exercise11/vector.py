from dataclasses import dataclass


def apply_binary_operator(op: str, n1: float, n2: float) -> float:
    match op:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case '*':
            return n1 * n2


@dataclass
class Vector:
    '''represent a Vector in n Dimension
    Attributes:
        value: a value which define a vector
    Invaiants:
        Dimension > 0
    '''
    __values: list[float]

    def __post_init__(self):
        assert self.dim > 0, "Dimension should be greater than 0"

    @property
    def values(self):
        return self.__values

    @property
    def dim(self):
        return len(self.__values)

    @property
    def length(self):
        result = 0
        for val in self.values:
            result += val**2
        return result**0.5

    def __str__(self):
        return str(self.dim) + "D" + " vector: " + str(self.values)

    def __pos__(self):
        return self

    def __neg__(self):
        result = []
        for val in self.values:
            neg_val = val * -1
            result.append(neg_val)
        return Vector(result)

    def operate_binary(self, op: str, other):
        result = []
        match other:
            case int():
                for val in self.values:
                    result.append(apply_binary_operator(op, val, other))
            case float():
                for val in self.values:
                    result.append(apply_binary_operator(op, val, other))
            case Vector():
                if self.dim == other.dim:
                    for i in range(self.dim):
                        result.append(apply_binary_operator(op, self.values[i], other.values[i]))
                else:
                    return 'invalid input'
            case _:
                return 'invalid input'
        return result

    def __add__(self, other):
        return Vector(self.operate_binary('+', other))

    def __radd__(self, other):
        return Vector(self.operate_binary('+', other))

    def __sub__(self, other):
        return Vector(self.operate_binary('-', other))

    def __rsub__(self, other):
        x = -self
        return Vector(x.operate_binary('+', other))

    def __mul__(self, other):
        return Vector(self.operate_binary('*', other))

    def __rmul__(self, other):
        return Vector(self.operate_binary('*', other))


other = Vector | int | float