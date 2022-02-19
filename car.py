import math
import typing
from statistics import mean
from typing import Optional


class _CarLike:
    max_speed: int
    real_speed: int
    accel: int
    x: int
    max_x: int
    y: int


class Car(_CarLike):
    def __init__(self, max_x: int, y: int, max_speed: int, accel: int = 1):
        self.max_speed = max_speed
        self.real_speed = self.max_speed
        self.accel = accel
        self.x = -50
        self.max_x = max_x
        self.y = y
        self.flow_data = []
        self.avg_flow = 1

    def step(self, ahead: Optional[_CarLike]):
        """
        :type ahead: Optional[Car]
        """
        if ahead is None:
            ahead_dist = 0
        else:
            ahead_dist = ahead.x - self.x
        if ahead_dist < 10:
            self.real_speed = ahead.real_speed
        elif self.real_speed < self.max_speed:
            self.real_speed += self.accel
        self.flow_data.append(self.real_speed / self.max_speed)
        self.avg_flow = mean(self.flow_data)
        self.x += self.real_speed


def step_all(cars: typing.List[Car]):
    cars_sd = sorted(cars, key=lambda c: c.x)
    for i, car in enumerate(cars_sd):
        if i == len(cars_sd) - 1:
            car.step(cars_sd[i+1])

