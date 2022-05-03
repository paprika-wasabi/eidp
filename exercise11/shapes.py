from dataclasses import dataclass
from geo import Vector2D, Object2D, GuiWrapper
from dataclasses import dataclass
from math import pi


@dataclass
class Circle(Object2D):
    '''Represents a circle in the plane.
    Attributes:
        radius: a number indicating the radius of the circle
        position: inherited from Object2D
    Invaiants:
        radius > 0
    '''
    __radius: float

    def __post_init__(self):
        assert self.radius > 0, " radius should be greater than 0"

    @property
    def radius(self) -> float:
        return self.__radius

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        top_left = self.pos.x + self.radius, self.pos.y + self.radius
        bottom_right = self.pos.x - self.radius, self.pos.y - self.radius
        self = gui.canvas.create_oval(top_left, bottom_right,
                                      fill=fillcolor,
                                      outline=outlinecolor)


@dataclass
class RotatableEllipse(Object2D):
    '''Represents a ellipse in the plane.
    Attributes:
        size: a number indicating the height and width of the ellipse
        angle: indicating an angle of ellipse in degree
        position: inherited from Object2D
    Invaiants:
        height > 0
        width > 0
        angle is interval [0,2pi)
    '''
    __size: Vector2D
    __angle: float

    def __post_init__(self):
        assert self.size.x > 0, "width should be greater than 0"
        assert self.size.y > 0, "height should be greater than 0"
        assert self.angle >= 0, "angle should be in interval [0,2pi)"
        assert self.angle < 2 * pi, "angle should be in interval [0,2pi)"

    @property
    def size(self):
        return self.__size

    @property
    def angle(self):
        return self.__angle

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        self = gui.canvas.create_oval(self.pos.x - self.size.x, self.pos.y - self.size.y, self.pos.x + self.size.x, self.pos.y + self.size.y, fill=fillcolor, outline=outlinecolor)


@dataclass
class Triangle(Object2D):
    '''Represents a triangle in the plane.
    Attributes:
        edge1: a postion which indicating postion another corner of triangle
        edge2: a postion which indicating postion another corner of triangle
        position: inherited from Object2D
    Invaiants:
        None
    '''
    __edge1: Vector2D
    __edge2: Vector2D

    @property
    def edge1(self):
        return self.__edge1

    @property
    def edge2(self):
        return self.__edge2

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        self = gui.canvas.create_polygon(self.pos.x, self.pos.y,
                                         self.edge1.x, self.edge1.y,
                                         self.edge2.x, self.edge2.y,
                                         fill=fillcolor, outline=outlinecolor)


if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    circle = Circle(Vector2D(100, 200), 75)
    circle.draw(gui, fillcolor="lightblue")
    ellipse = RotatableEllipse(Vector2D(300, 250), Vector2D(50, 200), 0)
    ellipse.draw(gui, fillcolor="pink")
    triangle = Triangle(Vector2D(450, 150), Vector2D(650, 300), Vector2D(550, 500))
    triangle.draw(gui, fillcolor="green", outlinecolor="black")
    gui.start()