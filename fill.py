import math


def fill(canvas_layers, xm, ym, pixel_size, current_color):
    xm_cell = xm // pixel_size
    ym_cell = ym // pixel_size

   
    if xm_cell >= 0 and ym_cell >= 0:
        try:
            color_to_fill = canvas_layers[0][xm_cell][ym_cell]
            
            
            old_canvas_layer = canvas_layers[0].copy()
            for x in range(len(canvas_layers[0])):
                for y in range(len(canvas_layers[0][x])):
                    if canvas_layers[0][x][y] == current_color:
                        old_canvas_layer[x][y] = (-1, -1, -1, -1) # технический цвет!!!!
                        
            canvas_layers[0][xm_cell][ym_cell] = current_color
            
            for i in range(64):
                for x in range(len(canvas_layers[0])):
                    for y in range(len(canvas_layers[0][x])):
                        if canvas_layers[0][x][y] == current_color:
                            if x != 0 and canvas_layers[0][x - 1][y] == color_to_fill:
                                canvas_layers[0][x - 1][y] = current_color
                            if y != 0 and canvas_layers[0][x][y - 1] == color_to_fill:
                                canvas_layers[0][x][y - 1] = current_color
                            if x != len(canvas_layers[0]) - 1 and canvas_layers[0][x + 1][y] == color_to_fill:
                                canvas_layers[0][x + 1][y] = current_color
                            if y != len(canvas_layers[0][x]) - 1 and canvas_layers[0][x][y + 1] == color_to_fill:
                                canvas_layers[0][x][y + 1] = current_color
                                
            for x in range(len(canvas_layers[0])):
                for y in range(len(canvas_layers[0][x])):
                    if old_canvas_layer[x][y] == (-1, -1, -1, -1):
                        canvas_layers[0][x][y] = current_color 
        except IndexError:
            pass
