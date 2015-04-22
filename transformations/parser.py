from display import *
from matrix import *
from draw import *

color = [105, 190, 105]

def parse_file( fname, points, transform ):
  f = open(fname, 'r')
  lines = f.readlines()
  f.close
  for i in range(len(lines)):
    line = lines[i].replace("\n","")
    if i+1 in range(len(lines)):
      n = lines[i+1].replace("\n","").split(" ")
    if line == 'l':
      for j in range(len(n)):
        n[j] = float(n[j])
        print n[j]
      add_edge(points,n[0],n[1],n[2],n[3],n[4],n[5])
    elif line == 'i':
      ident(transform)  
    elif line == 's':
      for j in range(len(n)):
        n[j] = float(n[j])
      matrix_mult(make_scale(n[0],n[1],n[2]),transform)      
    elif line == 't':
      for j in range(len(n)):
        n[j] = float(n[j])
      matrix_mult(make_translate(n[0],n[1],n[2]),transform)
    elif line == 'x':
      matrix_mult(make_rotX(n[0]),transform)
    elif line == 'y':
      matrix_mult(make_rotY(n[0]),transform)
    elif line == 'z':
      matrix_mult(make_rotZ(n[0]),transform)
    elif line == 'a':
      matrix_mult(transform,points)
    elif line == 'v':
      screen = new_screen()
      draw_lines(points,screen,color)
      display(screen)
    elif line == 'g':
      screen = new_screen()
      draw_lines(points,screen,color)
      save_ppm(screen,n[0])

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
