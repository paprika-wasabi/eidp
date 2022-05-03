from dataclasses import dataclass
from typing import Optional


@dataclass
class Var:
    name: str


@dataclass
class Val:
    value: int


@dataclass
class Op:
    operation: str
    left: 'Node'
    right: 'Node'


Node = Var | Val | Op
