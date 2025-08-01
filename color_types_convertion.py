def rgb_to_hex(rgb):
    if len(rgb) == 4:
        r, g, b, a = rgb
        return '#{:02X}{:02X}{:02X}{:02X}'.format(r, g, b, a)
    else:
        r, g, b = rgb[:3]  
        return '#{:02X}{:02X}{:02X}'.format(r, g, b)

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:  # #RGB
        r = int(hex_str[0]*2, 16)
        g = int(hex_str[1]*2, 16)
        b = int(hex_str[2]*2, 16)
        return (r, g, b)
    elif len(hex_str) == 4:  # #RGBA
        r = int(hex_str[0]*2, 16)
        g = int(hex_str[1]*2, 16)
        b = int(hex_str[2]*2, 16)
        a = int(hex_str[3]*2, 16)
        return (r, g, b, a)
    elif len(hex_str) == 6:  # #RRGGBB
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
        return (r, g, b)
    elif len(hex_str) == 8:  # #RRGGBBAA
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
        a = int(hex_str[6:8], 16)
        return (r, g, b, a)
    else:
        raise ValueError("Неверный HEX формат")
    
def hex_to_rgba(hex_str, alpha=255):
    rgb = hex_to_rgb(hex_str)
    if len(rgb) == 3:
        return (*rgb, alpha)
    return rgb

def rgba_to_hex(rgba):
    if len(rgba) == 3:
        return rgb_to_hex((*rgba, 255))
    return rgb_to_hex(rgba)
