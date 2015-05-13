import mdl
from display import *
from matrix import *
from draw import *
import copy

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        if command[0] == "push":
            m = copy.deepcopy(stack[-1])
            stack.append(m)
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "move":
            m = make_translate(command[1], command[2], command[3])
            matrix_mult(m, stack[-1])
        elif command[0] == "rotate":
            m = new_matrix()
            ident(m)
            theta = command[2] * (math.pi/180.0)
            if command[1] == "x":
                m = make_rotX(theta)
            elif command[1] == "y":
                m = make_rotY(theta)
            elif command[1] == "z":
                m = make_rotZ(theta)
            matrix_mult(stack[-1], m)
            stack[-1] = m
        elif command[0] == "scale":
            m = make_scale(command[1], command[2], command[3])
            matrix_mult(stack[-1], m)
            stack[-1] = m
        elif command[0] == "box":
            points = []
            add_box(points, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], points)    
            draw_polygons(points, screen, color)
        elif command[0] == "sphere":
            points = []
            add_sphere(points, command[1], command[2], command[3], command[4], 5)
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
        elif command[0] == "torus":
            points = []
            add_torus(points, command[1], command[2], command[3], command[4], command[5], 5)
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
        elif command[0] == "line":
            points = []
            add_edge(points, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], points)
            draw_lines(points, screen, color)
        elif command[0] == "save":
            save_extension( screen, command[1] )
        elif command[0] == "display":
            display(screen)
        print command
