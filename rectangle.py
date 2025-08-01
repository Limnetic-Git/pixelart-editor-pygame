from canvas import CANVAS_WIDTH, CANVAS_HEIGHT, pixel_size, current_color, secondary_color

# Глобальные переменные
start_x = None
start_y = None
mode = 0  # 0 - контур, 1 - контур с заливкой, 2 - заливка без контура

def rectangle_set_mode(new_mode):
    """Устанавливает режим рисования: 0-контур, 1-контур+заливка, 2-только заливка"""
    global mode
    mode = new_mode

def rectangle_start(canvas_layers, xm, ym):
    """Запоминаем начальную точку прямоугольника"""
    global start_x, start_y
    start_x = xm // pixel_size
    start_y = ym // pixel_size
    # При однократном клике рисуем точку (как в Paint)
    if mode == 0:
        canvas_layers[0][start_x][start_y] = current_color
    elif mode == 1 or mode == 2:
        canvas_layers[0][start_x][start_y] = current_color if mode == 1 else secondary_color

def rectangle_draw(canvas_layers, xm, ym):
    """Рисуем прямоугольник с предпросмотром"""
    global start_x, start_y
    
    if start_x is None or start_y is None:
        return
    
    xm_cell = xm // pixel_size
    ym_cell = ym // pixel_size
    
    # Ограничиваем координаты в пределах холста
    x1 = min(max(start_x, 0), CANVAS_WIDTH - 1)
    y1 = min(max(start_y, 0), CANVAS_HEIGHT - 1)
    x2 = min(max(xm_cell, 0), CANVAS_WIDTH - 1)
    y2 = min(max(ym_cell, 0), CANVAS_HEIGHT - 1)
    
    # Очищаем предыдущий предпросмотр
    for layer in canvas_layers:
        for x in range(CANVAS_WIDTH):
            for y in range(CANVAS_HEIGHT):
                if layer[x][y] == (200, 200, 200, 128):  # Цвет предпросмотра
                    layer[x][y] = (0, 0, 0, 0)  # Прозрачный
    
    # Рисуем предпросмотр
    if mode == 0:  # Только контур
        draw_rectangle_outline(canvas_layers[-1], x1, y1, x2, y2, (200, 200, 200, 128))
    elif mode == 1:  # Контур + заливка
        draw_filled_rectangle(canvas_layers[-1], x1, y1, x2, y2, (200, 200, 200, 128), (200, 200, 200, 64))
    else:  # Только заливка
        draw_filled_rectangle(canvas_layers[-1], x1, y1, x2, y2, None, (200, 200, 200, 64))

def rectangle_end(canvas_layers, xm, ym):
    """Финализируем прямоугольник"""
    global start_x, start_y
    
    if start_x is None or start_y is None:
        return
    
    xm_cell = xm // pixel_size
    ym_cell = ym // pixel_size
    
    # Ограничиваем координаты
    x1 = min(max(start_x, 0), CANVAS_WIDTH - 1)
    y1 = min(max(start_y, 0), CANVAS_HEIGHT - 1)
    x2 = min(max(xm_cell, 0), CANVAS_WIDTH - 1)
    y2 = min(max(ym_cell, 0), CANVAS_HEIGHT - 1)
    
    # Очищаем предпросмотр
    for x in range(CANVAS_WIDTH):
        for y in range(CANVAS_HEIGHT):
            if canvas_layers[-1][x][y] == (200, 200, 200, 128) or \
               canvas_layers[-1][x][y] == (200, 200, 200, 64):
                canvas_layers[-1][x][y] = (0, 0, 0, 0)
    
    # Рисуем финальный прямоугольник
    if mode == 0:
        draw_rectangle_outline(canvas_layers[0], x1, y1, x2, y2, current_color)
    elif mode == 1:
        draw_filled_rectangle(canvas_layers[0], x1, y1, x2, y2, current_color, secondary_color)
    else:
        draw_filled_rectangle(canvas_layers[0], x1, y1, x2, y2, None, current_color)
    
    start_x = None
    start_y = None

# Вспомогательные функции
def draw_rectangle_outline(layer, x1, y1, x2, y2, color):
    """Рисует контур прямоугольника"""
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    
    for x in range(x1, x2 + 1):
        layer[x][y1] = color  # Верхняя граница
        layer[x][y2] = color  # Нижняя граница
    
    for y in range(y1 + 1, y2):
        layer[x1][y] = color  # Левая граница
        layer[x2][y] = color  # Правая граница

def draw_filled_rectangle(layer, x1, y1, x2, y2, border_color, fill_color):
    """Рисует закрашенный прямоугольник"""
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    
    # Заливка
    if fill_color:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                layer[x][y] = fill_color
    
    # Границы
    if border_color:
        draw_rectangle_outline(layer, x1, y1, x2, y2, border_color)
