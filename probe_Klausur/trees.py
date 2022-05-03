class Tree:
    def __init__(self, mark, children: list):
        self.mark = mark
        self.children = children

    
    def mark(self):
        if self == None:
            pass