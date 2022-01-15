import os
import typing

import pygame
from pygame.locals import *


try:
    os.environ["DISPLAY"]
except KeyError:
    os.environ["SDL_VIDEODRIVER"] = "dummy"


def init_screen(size):
    pygame.init()
    print([k for k in dir(pygame) if k.islower()])
    return pygame.display.set_mode(size)


def mainloop(target: typing.Callable, clean: typing.Optional[typing.Callable]):
    cont = True
    clk = pygame.time.Clock()
    while cont:
        clk.tick(120)
        cont = target(clk.get_fps())


if __name__ == '__main__':
    init_screen((400, 500))
