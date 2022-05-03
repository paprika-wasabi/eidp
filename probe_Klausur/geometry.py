from dataclasses import dataclass

@dataclass
class Rect:
    _x1: int
    _y1: int
    _x2: int
    _y2: int

    @property
    def unten_links(self):
        return (self._x1, self._y1)
    
    @property
    def oben_rects(self):
        return (self._x2, self._y2)


    def __eq__(self, other):
        if self.oben_rects == other.oben_rects and self.unten_links == other.unten_links:
            return True
        else:
            return False


def merge(r1: Rect, r2: Rect):
    return Rect(r1._x1 + r2._x1,
                r1._y1 + r2._y1,
                r1._x2 + r2._x2,
                r1._y2 + r2._y2
                )


r1 = Rect(1,1,2,2)
r2 = Rect(1,1,2,2)

print(merge(r1,r2))