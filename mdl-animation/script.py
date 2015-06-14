""" --Commands--
  frames: set num_frames for animation
  basename: set name for animation
  vary: manipluate knob values between two given frames
        over a specified interval
  set: set a knob to a given value
  setknobs: set all knobs to a given value
  push: push a new origin matrix onto the origin stack
  pop: remove the top matrix on the origin stack
  move/scale/rotate: create a transformation matrix 
                     based on the provided values, then 
		     multiply the current top of the
		     origins stack by it.
  box/sphere/torus: create a solid object based on the
                    provided values. Store that in a 
		    temporary matrix, multiply it by the
		    current top of the origins stack, then
		    call draw_polygons.
  line: create a line based on the provided values. Store 
        that in a temporary matrix, multiply it by the
	current top of the origins stack, then call draw_lines.
  save: call save_extension with the provided filename
  display: view the image live
"""

import mdl
from display import *
from matrix import *
from draw import *

NUM_FRAMES = 0
BASENAME = ""

def first_pass( commands ):
    for command in commands:
        if command[0] == "frames":
            global NUM_FRAMES
            NUM_FRAMES = int(command[1])
            print "NUM_FRAMES set"
        if command[0] == "basename":
            global BASENAME
            BASENAME = command[1]
            print "BASENAME set"
        if command[0] == "vary":
            if NUM_FRAMES == 0:
                print "Error: Number of frames not set"
                return
            elif BASENAME == "":
                BASENAME = "animation"
                print "Warning: Basename not specified; set to default basename 'animation'"
    if NUM_FRAMES == 0:
        print "Error: Number of frames not set"
        print "First Pass Failed. Exiting."
        return
    print "--First Pass Success--"
        
"""======== second_pass( commands ) ==========

  In order to set the knobs for animation, we need to keep
  a separate value for each knob for each frame. Using an array
  of dictionaries, each array index will correspond
  to a frame (eg. knobs[0] would be the first
  frame, knobs[1] would be the 2nd frame and so on).

  Each index should contain a dictionary of knob values, each
  key will be a knob name, and each value will be the knob's
  value for that frame.

  Go through the command array, and when you find vary, go 
  from knobs[0] to knobs[frames-1] and add (or modify) the
  dictionary corresponding to the given knob with the
  appropriate value. 
  ===================="""
def second_pass( commands, num_frames ):
    knobs = []
    for command in commands:
        if command[0] == "vary":
            knob_name = command[1]
            start_frame = int(command[2])
            end_frame = int(command[3])
            start_val = int(command[4])
            end_val = int(command[5])

            step = 1.0 * (end_val - start_val) / (end_frame - start_frame)
            if len(knobs) < end_frame:
                for i in range(start_frame, end_frame+1):
                    knobs.append({})
            for index, frame in enumerate(knobs):
                frame[knob_name] = index*step
    print "--Second Pass Success--"
    return knobs
    

def run(filename):
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed"
        return
        
    stack = [ tmp ]
    screen = new_screen()    

    first_pass(commands)
    knobs = second_pass(commands, NUM_FRAMES)

    stack = [ tmp ]
    screen = new_screen()    

    for i in range(NUM_FRAMES):
        stack = [ tmp ]
        screen = new_screen()    
        
        commands[-1] = "save", "animation/" + BASENAME + "{:03}".format(i) + ".png"
        knob = knobs[i]

        for command in commands:
            if command[0] == "pop":
                stack.pop()
                if not stack:
                    stack = [ tmp ]

            if command[0] == "push":
                stack.append( stack[-1][:] )

            if command[0] == "save":
                print "saving..."
                save_extension(screen, command[1])

            if command[0] == "display":
                display(screen)

            if command[0] == "sphere":
                m = []
                add_sphere(m, command[1], command[2], command[3], command[4], 5)
                matrix_mult(stack[-1], m)
                draw_polygons( m, screen, color )

            if command[0] == "torus":
                m = []
                add_torus(m, command[1], command[2], command[3], command[4], command[5], 5)
                matrix_mult(stack[-1], m)
                draw_polygons( m, screen, color )

            if command[0] == "box":                
                m = []
                add_box(m, *command[1:])
                matrix_mult(stack[-1], m)
                draw_polygons( m, screen, color )

            if command[0] == "line":
                m = []
                add_edge(m, *command[1:])
                matrix_mult(stack[-1], m)
                draw_lines( m, screen, color )

            if command[0] == "bezier":
                m = []
                add_curve(m, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .05, 'bezier')
                matrix_mult(stack[-1], m)
                draw_lines( m, screen, color )

            if command[0] == "hermite":
                m = []
                add_curve(m, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .05, 'hermite')
                matrix_mult(stack[-1], m)
                draw_lines( m, screen, color )

            if command[0] == "circle":
                m = []
                add_circle(m, command[1], command[2], command[3], command[4], .05)
                matrix_mult(stack[-1], m)
                draw_lines( m, screen, color )

            if command[0] == "move":                
                if command[4] != None:
                    k = knob[command[4]]
                else:
                    k = 1

                xval = command[1] * k
                yval = command[2] * k
                zval = command[3] * k
                
                t = make_translate(xval, yval, zval)
                matrix_mult( stack[-1], t )
                stack[-1] = t

            if command[0] == "scale": 
                if command[4] != None:
                    k = knob[command[4]]
                else:
                    k = 1

                xval = command[1] * k
                yval = command[2] * k
                zval = command[3] * k

                t = make_scale(xval, yval, zval)
                matrix_mult( stack[-1], t )
                stack[-1] = t
            
            if command[0] == "rotate":
                if command[3] != None:
                    k = knob[command[3]]
                else:
                    k = 1

                angle = command[2] * (math.pi / 180) * k

                if command[1] == 'x':
                    t = make_rotX( angle )
                elif command[1] == 'y':
                    t = make_rotY( angle )
                elif command[1] == 'z':
                    t = make_rotZ( angle )            
                
                matrix_mult( stack[-1], t )
                stack[-1] = t
            
