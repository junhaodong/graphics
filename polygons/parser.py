from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    
    f = open( fname )
    commands = f.readlines()
    f.close()
    
    screen = new_screen()
    color = [ 255, 0, 255 ]

    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()

        if cmd[0] == '#':
            pass

        elif cmd in 'lstxyzcbhmdp':
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'l':
                add_edge( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                
            elif cmd == 'm':
                add_sphere( points, args[0], args[1], 0, args[2], 5 )

            elif cmd == 'd':
                add_torus( points, args[0], args[1], 0, args[2], args[3], 5 )

            elif cmd == 'p':
                add_box( points, args[0], args[1], args[2], args[3], args[4], args[5] )

            elif cmd == 'c':
                add_circle( points, args[0], args[1], 0, args[2], .01 )
            
            elif cmd == 'b':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )

            elif cmd == 'h':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )

            elif cmd == 's':
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult( s, transform )

            elif cmd == 't':
                t = make_translate( args[0], args[1], args[2] )
                matrix_mult( t, transform )

            else:
                angle = args[0] * ( math.pi / 180 )
                if cmd == 'x':
                    r = make_rotX( angle )
                elif cmd == 'y':
                    r = make_rotY( angle )
                elif cmd == 'z':
                    r = make_rotZ( angle )
                matrix_mult( r, transform )

        elif cmd == 'i':
            ident( transform )
            
        elif cmd == 'a':
            matrix_mult( transform, points )

        elif cmd == 'w':
            points = []

        elif cmd in 'vg':
            screen = new_screen()
            draw_polygons( points, screen, color )
            
            if cmd == 'v':
                display( screen )

            elif cmd == 'g':
                c+= 1
                save_extension( screen, commands[c].strip() )
        else:
            print 'Invalid command: ' + cmd
        c+= 1


points = []
transform = new_matrix()

parse_file( 'script_test', points, transform )
