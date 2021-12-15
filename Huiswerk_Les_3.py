import OpenGL
from grid import *

def rasterline(x0, y0, x1, y1):
    resolution = 0.5
    rc = (y1-y0)/(x1-x0)
    print('standaard formule voor een lijn: ')
    print('y = rc * x + b')
    print('rc: ' + str(rc))
    hpos = y0 - (rc*x0)
    print('b: ' + str(hpos))
    print('te gebruiken formule voor deze rasterline:')
    print('y = ' + str(rc) + 'x + ' + str(hpos))
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            calcX = ((rc*x) + hpos)
            if y >= (calcX - resolution) and y <= (calcX + resolution):
                print('#####')
                print('x: ' + str(x))
                print('~~~~~')
                print(str(y) + ' = ' + str(rc) + '*' + str(x) + '+' + str(hpos))
                print(str(calcX-resolution) + ' <= ' + str(y) + ' <= ' + str(calcX + resolution))
                print('calculation is true with resolution of ' + str(resolution))
                print('#####')
                g.addPoint(x,y)









g = Grid(100,100)

rasterline(1,1,50,70)


g.draw()



