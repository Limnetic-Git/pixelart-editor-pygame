import pygame
from canvas import canvas, canvas_layers, draw_canvas, pixel_size
from pen import pen
from fill import fill
from pipette import pipette
#from rectangle import *
from selection import *
from gui import *
from color_types_convertion import *

def import_palette(palette_name):
    palette = [[(0, 0, 0, 0) for i in range(10)] for j in range(3)]
    with open(f'palettes/{palette_name}.hex', 'r+') as f:
        data = f.readlines()
    for i in range(len(data)): data[i] = f'#{data[i][:-1]}'

    number = 0
    for x in range(len(palette)):
        for y in range(len(palette[0])):
            palette[x][y] = hex_to_rgba(data[number])
            number += 1
    return palette

FPS = 60

pygame.init()

w, h = 800, 800
sc = pygame.display.set_mode((w, h), pygame.RESIZABLE)
clock = pygame.time.Clock()

canvas_x, canvas_y = 0, 0
canvas_window_width, canvas_window_height = 640, 640
canvas_window_x, canvas_window_y = 100, 100
LKM, PKM = False, False
canvas_window = pygame.Surface((canvas_window_width, canvas_window_height))


palette = import_palette('my-ghast-friend')

current_color = palette[0][0]
current_tool = 'selection'

grid = True

dragging = False
last_mouse_pos = (0, 0)

x, y = 0, 0

selection = False
while True:
    xm, ym = pygame.mouse.get_pos()
    canvas_xm, canvas_ym = xm - canvas_x - canvas_window_x - x , ym - canvas_y - canvas_window_y - y
    
    clock.tick(FPS)
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit(0)
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1: LKM = True
            if ev.button == 2: dragging = True; last_mouse_pos = ev.pos
            if ev.button == 3: PKM = True
            if ev.button == 4: pixel_size += 1
            if ev.button == 5: pixel_size -= 1
        if ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 1: LKM = False
            if ev.button == 2: dragging = False
            if ev.button == 3: PKM = False
        if ev.type == pygame.MOUSEMOTION:
            if dragging:
                dx, dy = ev.pos[0] - last_mouse_pos[0], ev.pos[1] - last_mouse_pos[1]
                x += dx; y += dy
                last_mouse_pos = ev.pos
                
    sc.fill((0, 34, 64))
    draw_tools_icons(sc)
    draw_actions_icons(sc)

    color = draw_palette(sc, palette, xm, ym, LKM, current_color)
    if color != None: current_color = color; LKM = False
    
    canvas_window.fill((0, 0, 0))
    canvas_window.blit(canvas, (x, y))
    canvas.fill((0, 0, 0))
    sc.blit(canvas_window, (canvas_window_x, canvas_window_y))
    
    draw_canvas(pixel_size, grid)
    
    if LKM:
        if current_tool == 'pen':
            pen(canvas_layers, canvas_xm, canvas_ym, pixel_size, current_color)
        if current_tool == 'fill':
            fill(canvas_layers, canvas_xm, canvas_ym, pixel_size, current_color)
            LKM = False
        if current_tool == 'pipette':
            color = pipette(canvas_layers, canvas_xm, canvas_ym, pixel_size)
            if color != None: current_color = color
            LKM = False
        if current_tool == 'selection':
            if not selection:
                start_selection(canvas_layers, canvas_xm, canvas_ym, pixel_size)
                selection = True
                print('vd')
            else:
                draw_selection_rect(canvas, canvas_layers, canvas_xm, canvas_ym, pixel_size)

                
        if xm >= 750 and xm <= 750+32 and ym >= 100 and ym <= 100+32:
            grid = not grid
            LKM = False
        if xm >= 100 and xm <= 100+32 and ym >= 48 and ym <= 48+32:
            current_tool = 'pen'
        if xm >= 145 and xm <= 145+32 and ym >= 48 and ym <= 48+32:
            current_tool = 'fill'
        if xm >= 190 and xm <= 190+32 and ym >= 48 and ym <= 48+32:
            current_tool = 'pipette'
        if xm >= 235 and xm <= 235+32 and ym >= 48 and ym <= 48+32:
            current_tool = 'selection'
            
  #  sc.blit(icons['pencil'], (100, 48))
   # sc.blit(icons['fill'], (145, 48))
    
    
    pygame.display.update()
