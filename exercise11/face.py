from shapes import Circle, RotatableEllipse, Triangle
from geo import Vector2D, GuiWrapper

if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)

    ellipse = RotatableEllipse(Vector2D(150, 150), Vector2D(40, 80), 0)
    ellipse.draw(gui, fillcolor="green", outlinecolor="green")

    ellipse = RotatableEllipse(Vector2D(650, 150), Vector2D(40, 80), 0)
    ellipse.draw(gui, fillcolor="green", outlinecolor="green")

    ellipse = RotatableEllipse(Vector2D(400, 300), Vector2D(260, 300), 0)
    ellipse.draw(gui, fillcolor="green", outlinecolor="green")

    circle = Circle(Vector2D(290, 150), 75)
    circle.draw(gui, fillcolor="white")

    circle = Circle(Vector2D(510, 150), 75)
    circle.draw(gui, fillcolor="white")

    circle = Circle(Vector2D(290, 150), 20)
    circle.draw(gui, fillcolor="black")

    circle = Circle(Vector2D(510, 150), 20)
    circle.draw(gui, fillcolor="black")

    ellipse = RotatableEllipse(Vector2D(400, 420), Vector2D(200, 50), 0)
    ellipse.draw(gui, fillcolor="pink")

    ellipse = RotatableEllipse(Vector2D(400, 445), Vector2D(100, 25), 0)
    ellipse.draw(gui, fillcolor="red", outlinecolor="pink")

    triangle = Triangle(Vector2D(300, 480), Vector2D(290, 400), Vector2D(320, 400))
    triangle.draw(gui, fillcolor="white", outlinecolor="black")

    triangle = Triangle(Vector2D(500, 480), Vector2D(510, 400), Vector2D(480, 400))
    triangle.draw(gui, fillcolor="white", outlinecolor="black")

    ellipse = RotatableEllipse(Vector2D(400, 390), Vector2D(200, 50), 0)
    ellipse.draw(gui, fillcolor="green", outlinecolor="green")

    triangle = Triangle(Vector2D(400, 240), Vector2D(380, 290), Vector2D(420, 290))
    triangle.draw(gui, fillcolor="black", outlinecolor="black")

    triangle = Triangle(Vector2D(360, 70), Vector2D(210, 50), Vector2D(210, 70))
    triangle.draw(gui, fillcolor="black", outlinecolor="black")

    triangle = Triangle(Vector2D(440, 70), Vector2D(590, 50), Vector2D(590, 70))
    triangle.draw(gui, fillcolor="black", outlinecolor="black")

    circle = Circle(Vector2D(230, 280), 20)
    circle.draw(gui, fillcolor="pink", outlinecolor="red")

    circle = Circle(Vector2D(570, 280), 20)
    circle.draw(gui, fillcolor="pink", outlinecolor="red")

    gui.start()
    