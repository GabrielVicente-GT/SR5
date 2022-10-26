#Render proporcionado en clase para trabajar eficientemente
from extras import *

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
BLUE  = color(51, 114, 176)
ORANGE = color(243, 156, 18)
RED = color(255, 0, 0)

class Render(object):

    def __init__(self, width, height):
            self.width  = width
            self.heigth = height
            self.color_actual   =  BLACK
            self.texture = None


            # self.framebuffer = []
            self.clear()

    def clear(self):
        self.framebuffer = [
            [ self.color_actual for x in range(self.width)]
            for y in range(self.heigth)
        ]
        self.zbuffer = [
            [ -999999 for x in range(self.width)]
            for y in range(self.heigth)
        ]

    def write(self, filename):
        f = open(filename, 'bw')

        #pixel header

        f.write( char('B'))
        f.write( char('M'))
        f.write( dword(14 + 40 + self.width * self.heigth * 3))
        f.write( word(0))
        f.write( word(0))
        f.write( dword(14+40))

        #info header

        f.write( dword(40))
        f.write( dword(self.width))
        f.write( dword(self.heigth))
        f.write( word(1))
        f.write( word(24))
        f.write( dword(0))
        f.write( dword(self.width*self.heigth*3))
        f.write( dword(0))
        f.write( dword(0))
        f.write( dword(0))
        f.write( dword(0))

        # pixel data

        for y in range(self.heigth):
            for x in range(self.width):
                f.write(self.framebuffer[y][x])

        f.close()

    def point(self, x, y):
        self.framebuffer[y][x] = self.color_actual

    def point2(self, x, y):
        self.zbuffer[y][x] = self.color_actual

    def set_color(self, color):
        self.color_actual = color


    def line(self, v1, v2): #Función que dibuja una línea.

        x0 = round(v1.x)
        y0 = round(v1.y)
        x1 = round(v2.x)
        y1 = round(v2.y)

        #Se calcula la pendiente "diferenca" entre y1 y y0 al igual que con sus respectivas x
        dy,dx= abs(y1 - y0),abs(x1 - x0)

        #Si la pendiente es "mas inclinada" verticalmente
        pendiente = dy > dx
        if pendiente:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        #Y si es inversa
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        #Se calcula nuevamente la pendiente
        dy,dx = abs(y1 - y0),(x1 - x0)

        #Tomando en cuenta que dy implica el desplezamaiento
        limitation = dx
        compensation = 0

        y = y0
        for x in range(x0,1+x1):
            if pendiente:
                self.point(y, x)
            else:
                self.point(x, y)

            compensation += dy * 2

            if compensation >= limitation:
                y += 1 if y0 < y1 else -1
                limitation += dx * 2

