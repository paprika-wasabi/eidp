from typing import Optional
from tree   import Node, Var, Val, Op
from ast    import NodeTransformer
import ast


# Python comes with the library `ast` to parse python expressions.
# As our arithmetic language is a subset of python, we first parse them as
# python code and then transform the python tree to a `Node`.


class AstToNode(NodeTransformer):
    def visit_Name(self, node):
        return Var(node.id)
    def visit_Constant(self, node):
        return Val(node.value)
    def visit_Add(self, node):
        return '+'
    def visit_Mult(self, node):
        return '*'
    def visit_BinOp(self, node):
        op = self.visit(node.op)
        l = self.visit(node.left)
        r = self.visit(node.right)
        if isinstance(l, Node) and isinstance(r, Node) and type(op) is str:
            return Op(op, l, r)
    def visit_Expr(self, node):
        return self.visit(node.value)
    def visit_Module(self, node):
        if len(node.body) == 1:
            return self.visit(node.body[0])


def parse(s: str) -> Optional[Node]:
    try:
        n = AstToNode().visit(ast.parse(s))
        if isinstance(n, Node):
            return n
        return None
    except:
        return None