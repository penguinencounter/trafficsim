import math
from statistics import mean


class Car:
    def __init__(self, max_x: int, y: int, max_speed: int, accel: int = 1):
        self.max_speed = max_speed
        self.real_speed = self.max_speed
        self.accel = accel
        self.x = -50
        self.max_x = max_x
        self.y = y
        self.flow_data = []
        self.avg_flow = 1

    def _get_next_ahead_car(self, cars: list):
        next_car = None
        next_dist = math.inf
        for car in cars:
            if car.x <= self.x:
                continue
            if car.x < next_dist:
                next_car = car
                next_dist = car.x
        return next_car, next_dist

    def update(self, cars: list, fps: float):
        ahead, ahead_dist = self._get_next_ahead_car(cars)
        if fps == 0:
            return False
        if ahead_dist < 10:
            self.real_speed = ahead.real_speed
        elif self.real_speed < self.max_speed:
            self.real_speed += self.accel
        self.flow_data.append(self.real_speed / self.max_speed)
        self.avg_flow = mean(self.flow_data)
        self.x += self.real_speed / fps

