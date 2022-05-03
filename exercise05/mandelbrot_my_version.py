# mi84, pw221, ms2149
from PIL import Image


def mandelbrot(c: complex, m: int) -> int:
    i = 0
    n = 0
    while abs(n) <= 2 and i < m:
        n = n * n + c
        i += 1
    #if i != m:
        #return str(c) + " is not in Mandelbrot Set"
    #elif i == m:
        #return str(c) + " is in Mandelbrot Set"
    return i
    

def sample(z: complex, w: complex, x: int, y: int, sx: int, sy: int) -> complex:
    a = z.real
    b = z.imag
    c = w.real
    d = w.imag
    adder_x = float(abs(a - c) / sx)
    adder_y = float(abs(b - d) / sy)
    result = complex(a + (x * adder_x), b + (y * adder_y))
    return result


def render_mandelbrot(z: complex, w: complex, sx: int , sy: int, m: int, output: str):
    size = (sx, sy)
    x = 0
    y = 0
    img = Image.new('HSV', size)
    for x in range(0, sx):
        for y in range(0, sy):
            a = z.real
            b = z.imag
            c = w.real
            d = w.imag
            adder_x = float(abs(a - c) / sx)
            adder_y = float(abs(b - d) / sy)
            c = complex(a + (x * adder_x), b + (y * adder_y))
            i = 0
            n = 0
            while abs(n) <= 2 and i < m:
                n = n * n + c
                i += 1
    #if i != m:
        #return str(c) + " is not in Mandelbrot Set"
    #elif i == m:
        #return str(c) + " is in Mandelbrot Set"
            max_i = m
            hue = int(255 * (i / max_i))
            value = 255 if i < max_i else 0
            saturation = 255
            colors = (hue, saturation, value)
            img.putpixel((x,y), colors)
    img.convert('RGB').save(output, quality=95)


if __name__ == '__main__':
    render_mandelbrot(-2-1j, 1+1j,900, 600,50,'output.jpg')