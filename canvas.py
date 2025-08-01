import pygame
pygame.init()

def draw_canvas(pixel_size, grid):
    
    for layer in canvas_layers:
        for x in range(len(layer)):
            for y in range(len(layer[x])):
                pygame.draw.rect(canvas, layer[x][y], (x * pixel_size, y * pixel_size, pixel_size, pixel_size))
                if grid:
                    pygame.draw.rect(canvas, 'black', (x * pixel_size, y * pixel_size, pixel_size, pixel_size), 1)
                    
canvas_layers = []

CANVAS_LAYERS_NUMBER = 1
CANVAS_WIDTH = 32
CANVAS_HEIGHT = 32

pixel_size = 20
current_color = (255, 0 ,0)
default_canvas_color = (255, 255, 255, 255)

for _ in range(CANVAS_LAYERS_NUMBER):
    canvas_layers.append([[default_canvas_color for i in range(CANVAS_HEIGHT)] for j in range(CANVAS_WIDTH)])

canvas = pygame.Surface((3200, 3200))


