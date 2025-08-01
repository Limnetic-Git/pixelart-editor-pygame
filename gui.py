import pygame
from canvas import *

pygame.init()

icons = {
    'pencil': pygame.image.load('UI/pen.png'),
    'fill': pygame.image.load('UI/fill.png'),
    'grid': pygame.image.load('UI/grid.png'),
    'max': pygame.image.load('UI/max.png'),
    'pipette': pygame.image.load('UI/pipette.png'),
    'selection': pygame.image.load('UI/selection.png'),
    }

def draw_tools_icons(sc):
    sc.blit(icons['pencil'], (100, 48))
    sc.blit(icons['fill'], (145, 48))
    sc.blit(icons['pipette'], (190, 48))
    sc.blit(icons['selection'], (235, 48))

def draw_actions_icons(sc,):
    sc.blit(icons['grid'], (750, 100))
    #sc.blit(icons['max'], (750, 140))


def draw_palette(sc, palette, xm, ym, LKM, current_color):
    answer = None
    for x in range(len(palette)):
        for y in range(len(palette[0])):
            pygame.draw.rect(sc, palette[x][y], (6 + x * 30, 100 + y * 30, 24, 24))
            if palette[x][y] == current_color:
                pygame.draw.rect(sc, 'white', (3 + x * 30, 97 + y * 30, 28, 28), 2)
            if LKM:
                if xm >= 6 + x * 30 and xm <= 6 + x * 30 + 24 and ym >= 100 + y * 30 and ym <= 100 + y * 30 + 24:
                    answer = palette[x][y]
    pygame.draw.rect(sc, current_color, (3, 50, 30, 30))
    pygame.draw.rect(sc, 'black', (3, 50, 30, 30), 2)
    return answer
