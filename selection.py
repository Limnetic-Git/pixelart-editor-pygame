import pygame

pygame.init()

start_point_xm, start_point_ym = None, None
start_point_pixel_size = None

def start_selection(canvas_layers, xm, ym, pixel_size):
    global start_point_xm, start_point_ym, start_point_pixel_size
    xm_cell = xm // pixel_size
    ym_cell = ym // pixel_size
    if xm_cell >= 0 and ym_cell >= 0:
        try:
            start_point_xm, start_point_ym = xm, ym
            start_point_pixel_size = pixel_size
        except IndexError:
            start_point_xm, start_point_ym = None, None
            start_point_pixel_size = None
        
def draw_selection_rect(sc, canvas_layers, xm, ym, pixel_size):
    global start_point_x, start_point_y
    start_point_x, start_point_y = start_point_xm // pixel_size, start_point_ym // pixel_size
    xm_cell = xm // start_point_pixel_size
    ym_cell = ym // start_point_pixel_size
    if xm_cell >= 0 and ym_cell >= 0:
        try:
            sx = min(start_point_x * pixel_size , xm_cell * pixel_size)
            sy = min(start_point_y  * pixel_size, ym_cell * pixel_size)
            width = abs(start_point_x * pixel_size - xm_cell * pixel_size)
            height = abs(start_point_y * pixel_size - ym_cell * pixel_size)
            pygame.draw.rect(sc, 'blue', (sx, sy, width, height), 4)
        except IndexError:
            pass
