def pen(canvas_layers, xm, ym, pixel_size, current_color):
    xm_cell = xm // pixel_size
    ym_cell = ym // pixel_size
    if xm_cell >= 0 and ym_cell >= 0:
        try:
            canvas_layers[0][xm_cell][ym_cell] = current_color
        except IndexError:
            pass
