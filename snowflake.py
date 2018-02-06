from graphics import *
from time import sleep
from random import randint

WIN = GraphWin("snow", 1000, 1000)

def create_randpoint():
    return Point(randint(0, 1000), randint(0, 1000))

def random_walk(point):
    point.move(randint(-3, 3), randint(-3, 3))


if __name__ == "__main__":
    snowflakes = [create_randpoint() for _ in range(55)]
    new_snowflakes = []
    while True:
        for s in snowflakes:
            try:
                random_walk(s)
                s.draw(WIN)
                new_snowflakes.append(s)
            except GraphicsError:
                if not isinstance(s, Rectangle):
                    new_rec = Rectangle(s, Point(s.getX()+1, s.getY()+1))
                    new_rec.setFill("black")
                    random_walk(new_rec)
                    new_snowflakes.append(new_rec)
                else:
                    new_corner1 = Point(s.getP1().getX()+randint(-1,1), s.getP1().getY()+randint(-1,1))
                    new_corner2 = Point(s.getP2().getX()+randint(-1,1), s.getP2().getY()+randint(-1,1))

                    new_rec = Rectangle(new_corner1, new_corner2)
                    new_rec.setFill("black")
                    random_walk(new_rec)
                    new_snowflakes.append(new_rec)
                random_walk(s)
        new_snowflakes.append(create_randpoint())

        snowflakes = new_snowflakes
        new_snowflakes = []
