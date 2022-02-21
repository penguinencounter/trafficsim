import random

import pygame
from pygame import Rect

from car import Car, step_all
from visualizer import init_screen, mainloop


cars = [Car(1000, 125, 10), Car(1000, 125, 8)]


def run(s: pygame.Surface, f: float):
    global cars
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            return False  # Stop
    cars = step_all(cars)
    if cars[0].x > 200:
        cars.append(Car(10000, 125, random.randint(2, 12)))
    s.fill((55, 95, 55))
    for c in cars:
        w = 100 + c.x if c.x <= 0 else 100
        x = c.x if c.x > 0 else 0
        s.fill((65, 65, 65), Rect(x, c.y, w, 50))
    pygame.display.flip()
    return True  # Don't stop


def main():
    cars[1].x = 100
    size = width, height = 1000, 300
    scn = init_screen(size)
    mainloop(scn, run, None)


if __name__ == '__main__':
    main()
