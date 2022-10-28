#!/usr/bin/env python3
"""
A single pacman game designed as a proof of concept:
- to learn python
- to understand ghosts algorithms
"""

from re import M
import sys
import random
import time
import math
import os
import pygame
import argparse


# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def drawtree(screen, x, y, length, ratio, angle, da, depth ):
    dx = x + length * math.cos(angle)
    dy = y - length * math.sin(angle)

    pygame.draw.line(screen, WHITE, [x, y], [dx, dy ])
    if depth == 1:
        return(0)

    drawtree(screen, dx, dy, length*ratio, ratio, angle+da/2, da, depth-1 )
    drawtree(screen, dx, dy, length*ratio, ratio, angle-da/2, da, depth-1 )
    drawtree(screen, dx, dy, length*ratio, ratio, angle+da, da, depth-1 )
    drawtree(screen, dx, dy, length*ratio, ratio, angle-da, da, depth-1 )
    #drawtree(screen, dx, dy, length*ratio, ratio, angle+da*2, da, depth-1 )
    #drawtree(screen, dx, dy, length*ratio, ratio, angle-da*2, da, depth-1 )
 
    
# Root code
def main():
    """
    main code to draw the tree
    """

    WIDTH = 800
    HEIGHT = 600

    Length = 200
    Ratio = 3/4
    Angle = math.pi / 2 # 45°
    da = math.pi/3 
    x = 400
    y = 600

    # initialize pygame and create window
    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    drawtree(screen, x, y, Length, Ratio, Angle, da, 6)
    
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    
    pygame.quit()

if __name__ == "__main__":
    main()
