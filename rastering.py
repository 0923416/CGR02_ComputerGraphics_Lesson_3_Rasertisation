from grid import Grid

def rasterline(x0, y0, x1, y1):
    # to do

# testcode
# let op: de beoordeling wordt gedaan op basis van andere waarden
g = Grid(20, 20)
rasterline(0, 0, 19, 19)
rasterline(0, 10, 19, 0)
g.draw()
