# mi84, pw221, ms2149

from PIL import Image


def mandelbrot(c: complex, m: int) -> int:
    i = 0
    n = 0
    while abs(n) <= 2 and i < m:
        n = n * n + c
        i += 1
    # if i != m:
        # return str(c) + " is not in Mandelbrot Set"
    # elif i == m:
        # return str(c) + " is in Mandelbrot Set"
    return i


def sample(z: complex, w: complex, x: int, y: int, sx: int, sy: int) -> complex:
    a = z.real
    b = z.imag
    d = w.real
    e = w.imag
    adder_x = float(abs(a - d) / sx)
    adder_y = float(abs(b - e) / sy)
    result = complex(a + (x * adder_x), b + (y * adder_y))
    return result


def color(i: int, m: int) -> tuple[int, int, int]:
    hue = int(255 * (i / m))
    value = 255 if i < m else 0
    saturation = 255
    return(hue, saturation, value)


def render_mandelbrot(z: complex, w: complex, sx: int, sy: int, m: int, name: str):
    img = Image.new('HSV', (sx, sy))
    for x in range(sx):
        for y in range(sy):
            c = sample(z, w, x, y, sx, sy)
            i = mandelbrot(c, m)
            img.putpixel((x, y), color(i, m))
    img.convert('RGB').save(name, quality=95)


render_mandelbrot(-2 - 1j, 1 + 1j, 900, 600, 50, 'output.jpg')