import png
import sys

height = 5000
width =  5000

Xmin = -2
Xmax =  2
Ymin = -2  
Ymax =  2

MAX = 100 # Maximum number of iterations
sys.setrecursionlimit(MAX + MAX)
    
    
def iterate(z, c, it):
    if z.real ** 2 + z.imag ** 2 > 4.0:
        return it
    elif it < MAX:
        return iterate(z**2+c, c, it+1)
    else:
        return None

image = []
for h in range(height):
    row = ()
    for w in range(width):
        x = h * (Xmax - Xmin) / width  + Xmin
        y = w * (Ymax - Ymin) / height + Ymin
        m = iterate(0, complex(x, y), 0)

        if m == None:
            row += (0,)
        else:
            row += (255,)
    image.append(row)

f = open('mandelbrot.png', "wb")
w = png.Writer(width, height, greyscale=True)
w.write(f, image)
f.close()