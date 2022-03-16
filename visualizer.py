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
        clk.tick()
        cont = target(screen, clk.get_fps())
    if clean is not None:
        clean()


def run(s, f):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            return False  # Stop
    s.fill((55, 95, 55))
    pygame.display.flip()
    return True           # Don't stop
