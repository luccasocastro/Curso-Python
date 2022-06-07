import math

def rgb_to_hsi(r, g, b):
    i = (1/3) * (r + g + b)

    s = 1 - (3 / (r + g + b)) * (min(r, g, b))

    h = math.cos(-1) * ( (((r - g) + (r - b)) / 2) / (math.sqrt((r - g)**2 + (r - b) * (g - b))))

    return h, s, i

print(rgb_to_hsi(150, 120, 30))
print(rgb_to_hsi(128, 128, 128))