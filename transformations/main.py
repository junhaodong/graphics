from display import *
from draw import *
import random

screen = new_screen()
color = [105, 190, 105]
matrix = []

#Tests for octants 1/5, 2/6, 4/8, 3/7
add_edge( matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge( matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )
add_edge( matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge( matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )

'''
random.seed(17)

for y in range(650):
    add_point(matrix, random.randint(0, YRES), y)
    add_point(matrix, random.randint(0,YRES), random.randint(0, XRES))
'''

draw_lines( matrix, screen, color )

display(screen)
