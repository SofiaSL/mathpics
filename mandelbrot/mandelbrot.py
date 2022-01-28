import png


height = 1000
width = 1000

Xmin = -2
Xmax =  2
Ymin = -2  
Ymax =  2

MAX = 2000 # Maximum number of iterations
    
    
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
        x = (Xmax - Xmin) / width
        y = (Ymax - Ymin) / height
        m = iterate(0, complex(x, y), 0)

        if m == None:
            row += (255,)
        else:
            if m > MAX - 1950:
                row += (0,)
            elif m > MAX - 1900:
                row += (16,)
            elif m > MAX - 1850:
                row += (32,)
            elif m > MAX - 1800:
                row += (48,)
            elif m > MAX - 1750:
                row += (64,)
            else:
                row += (255,)
    image.append(row)

f = open('mandelbrot.png', "wb")
w = png.Writer(width, height, greyscale=True)
w.write(f, image)
f.close()