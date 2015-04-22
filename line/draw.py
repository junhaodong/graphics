from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    for i in range(0, len(matrix), 2):
        p0 = matrix[i]
        p1 = matrix[i+1]
        draw_line(screen, p0[0], p0[1], p1[0], p1[1], color)

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0)
    add_point(matrix, x1, y1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if (x0 > x1):
        draw_line(screen, x1, y1, x0, y0, color)
        return
    x = x0
    y = y0
    A = 2*(y1-y0)
    B = -2*(x1-x0)
    m = -1.0*A/B
    if (y1 > y0):
        # Octant 1,5
        if (m <= 1):
            d = A + 0.5*B
            while (x <= x1):
                plot(screen, color, x, y)
                if (d > 0):
                    y+=1
                    d+=B
                x+=1
                d+=A
        # Octant 2,6
        else:
            d = 0.5*A + B
            while (y <= y1):
                plot(screen, color, x, y)
                if (d < 0):
                    x+=1
                    d+=A
                y+=1
                d+=B
    else:
        # Octant 4,8
        if (m >= -1):
            d = A - 0.5*B
            while (x <= x1):
                plot(screen, color, x, y)
                if (d < 0):
                    y-=1
                    d-=B
                x+=1
                d+=A
        # Octant 3,7
        else:
            d = 0.5*A - B
            while (y >= y1):
                plot(screen, color, x, y)
                if (d > 0):
                    x+=1
                    d+=A
                y-=1
                d-=B
