# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:04:32 2017

@author: Tom
"""

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Hello Pygame!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()