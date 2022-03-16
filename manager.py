import random
import statistics
from numpy import conj

import pygame
from pygame import Rect

from car import Car, step_all
from visualizer import init_screen, mainloop


def is_congested(prev_state: bool, cars):
    new_count = 0
    THRESHOLD_ON = 5
    THRESHOLD_OFF = 3
    for car in cars:
        if car.real_speed < car.max_speed:
            new_count += 1
    if prev_state and new_count <= THRESHOLD_OFF:
        return False
    elif (not prev_state) and new_count >= THRESHOLD_ON:
        return True
    return prev_state


def draw(s: pygame.Surface, cars, congested: bool):
    s.fill((55, 95, 55) if not congested else (255, 0, 0))
    s.fill((20, 20, 20), Rect(0, 110, s.get_width(), 80))
    for c in cars:
        w = 100 + c.x if c.x <= 0 else 100
        x = c.x if c.x > 0 else 0
        r = 125 if c.real_speed < c.max_speed else 65
        s.fill((r, 65, 65), Rect(x, 125, w, 50))
        s.fill((0, 0, 255), Rect(x, 125, 10, c.max_speed * 2))
    pygame.display.flip()


def main():
    size = width, height = 1000, 300
    scn = init_screen(size)
    congested = False
    cars = [Car(1000, 10)]
    steps = 0
    MAX_STEPS = 0
    scores = []

    def run(s: pygame.Surface, fps: float):
        nonlocal congested, cars, steps, MAX_STEPS, scores
        steps += 1
        print('\b' * 31, end='', flush=True)
        print(f'{steps} steps'.ljust(30), end='', flush=True)
        congested = is_congested(congested, cars)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                return False  # Stop
        if steps == MAX_STEPS:
            pygame.display.quit()
            pygame.quit()
            return False  # Stop
        cars, done = step_all(cars)  # imported
        if cars[0].x > 150:
            cars.append(Car(1000, random.randint(2, 12)))
        if len(done) > 0:
            for c in done:
                scores.append(c.avg_flow)
        draw(s, cars, congested)
        return True  # Don't stop

    mainloop(scn, run, None)
    print(statistics.mean(scores), 'avg score over', len(scores))


if __name__ == '__main__':
    main()
