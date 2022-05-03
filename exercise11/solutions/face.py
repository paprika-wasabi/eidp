from math import pi

from geo import GuiWrapper, Vector2D
from shapes import Circle, RotatableEllipse, Triangle


def main():
    gui = GuiWrapper(width=800, height=600)

    RotatableEllipse(Vector2D(300, 200), Vector2D(70, 30), 11 * pi / 12).draw(
        gui, fillcolor="")
    Circle(Vector2D(300, 200), 20).draw(gui, fillcolor="lightblue")
    Circle(Vector2D(300, 200), 5).draw(gui, fillcolor="black")
    Triangle(Vector2D(220, 130), Vector2D(220, 150), Vector2D(350, 140)).draw(
        gui, fillcolor="black")

    RotatableEllipse(Vector2D(500, 200), Vector2D(70, 30), pi / 12).draw(
        gui, fillcolor="")
    Circle(Vector2D(500, 200), 20).draw(gui, fillcolor="lightblue")
    Circle(Vector2D(500, 200), 5).draw(gui, fillcolor="black")

    Triangle(Vector2D(580, 130), Vector2D(580, 150), Vector2D(450, 140)).draw(
        gui, fillcolor="black")

    RotatableEllipse(Vector2D(400, 300), Vector2D(20, 70), 0).draw(
        gui, fillcolor="pink")

    Triangle(Vector2D(250, 400), Vector2D(550, 400), Vector2D(400, 500)).draw(
        gui, fillcolor="", outlinecolor="black")

    gui.start()


if __name__ == "__main__":
    main()
