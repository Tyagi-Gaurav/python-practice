import random
from game_turtle import Turtle


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


class Car(Turtle):
    def __init__(self, screen_x, screen_y):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_len=2)
        self.color(random_color())
        self.penup()
        self.screen_x = screen_x
        self.goto(screen_x / 2, random.randint(int(-1 * screen_y/2) + 50, int(screen_y/2) - 50))
        self.is_displayed = True

    def move(self):
        if self.is_displayed:
            if self.xcor() > -1 * self.screen_x + 20:
                self.goto(self.xcor() - 20, self.ycor())
            else:
                self.is_displayed = False


class CarManager:
    def __init__(self, screen_x, screen_y):
        self.car_speed = 0.2
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.cars = []

    def generate_cars(self, max):
        car_count = random.randint(0, max)
        for _ in range(0, car_count):
            self.cars.append(Car(self.screen_x, self.screen_y))

    def move_all_cars(self):
        for car_index in range(len(self.cars)):
            self.cars[car_index].move()

    def any_car_collides_with(self, my_turtle):
        for car_index in range(len(self.cars)):
            if self.cars[car_index].distance(my_turtle) < 25:
                return True

        return False

    def increment_level(self):
        self.car_speed = self.car_speed * 0.9
