import math
import os
import typing
from sys import platform

import pygame
from pygame.locals import *

if 'linux' in platform:
    os.environ["SDL_VIDEODRIVER"] = "dummy"


def init_screen(size):
    pygame.init()
    return pygame.display.set_mode(size)


def mainloop(screen: pygame.Surface, target: typing.Callable, clean: typing.Optional[typing.Callable]):
    cont = True
    clk = pygame.time.Clock()
    while cont:
        clk.tick(250)
        cont = target(screen, clk.get_fps())
    if clean is not None:
        clean()


def _keepalive(s, f):
    print('\b' * 21, end='', flush=True)
    print(f'{math.floor(f)} fps'.ljust(20), end='', flush=True)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            return False
    colpercent = (f / 250) * 255
    areapercent = (f / 250) * 400
    col = (255 - colpercent, colpercent, 0)
    s.fill((0, 0, 0))
    s.fill(col, (0, 0, areapercent, 10))
    pygame.display.flip()
    return True


if __name__ == '__main__':
    size = width, height = 400, 500
    scn = init_screen(size)
    mainloop(scn, _keepalive, None)
