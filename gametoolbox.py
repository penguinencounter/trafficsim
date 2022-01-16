import os
import typing
from sys import platform

import pygame
from pygame.locals import *

if 'linux' in platform:
    os.environ["SDL_VIDEODRIVER"] = "dummy"


def init_screen(size):
    pygame.init()
    print([k for k in dir(pygame) if k.islower()])
    return pygame.display.set_mode(size)


def mainloop(screen: pygame.Surface, target: typing.Callable, clean: typing.Optional[typing.Callable]):
    cont = True
    clk = pygame.time.Clock()
    while cont:
        clk.tick(250)
        cont = target(screen, clk.get_fps())


def _keepalive(s, f):
    print(f'{f} fps')
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            return False
    col = (0, f, 0)
    s.fill(col)
    pygame.display.flip()
    return True


if __name__ == '__main__':
    size = width, height = 400, 500
    scn = init_screen(size)
    mainloop(scn, _keepalive, None)
