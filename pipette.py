def pipette(canvas_layers, xm, ym, pixel_size):
    xm_cell = xm // pixel_size
    ym_cell = ym // pixel_size
    if xm_cell >= 0 and ym_cell >= 0:
        try:
            return canvas_layers[0][xm_cell][ym_cell]
        except IndexError:
            pass
