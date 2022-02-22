import random

import pygame
from pygame import Rect

from car import Car, step_all
from visualizer import init_screen, mainloop


cars = [Car(1000, 10), Car(1000, 8)]


def run(s: pygame.Surface, f: float):
    global cars
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            return False  # Stop
    cars = step_all(cars)  # imported
    if cars[0].x > 200:
        cars.append(Car(1000, random.randint(2, 12)))
    s.fill((55, 95, 55))
    for c in cars:
        w = 100 + c.x if c.x <= 0 else 100
        x = c.x if c.x > 0 else 0
        r = 125 if c.real_speed < c.max_speed else 65
        s.fill((r, 65, 65), Rect(x, 125, w, 50))
        s.fill((0, 0, 255), Rect(x, 125, 10, c.max_speed*2))
    pygame.display.flip()
    return True  # Don't stop


def main():
    cars[1].x = 100
    size = width, height = 1000, 300
    scn = init_screen(size)
    mainloop(scn, run, None)


if __name__ == '__main__':
    main()
