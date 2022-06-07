def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    cmax = max(r, g, b)
    cMin = min(r, g, b)
    diff = cmax - cMin

    if cmax == cMin:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100

    v = cmax * 100

    return h, s, v


print(rgb_to_hsv(150, 120, 30))
print(rgb_to_hsv(128, 128, 128))
