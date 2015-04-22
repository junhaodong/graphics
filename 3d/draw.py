from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
  t = 0
  x0 = cx + r
  y0 = cy
  while t < 1.0+step:
    x = r*math.cos(2*math.pi*t) + cx
    y = r*math.sin(2*math.pi*t) + cy
    add_edge(points,x0,y0,0,x,y,0)
    x0 = x
    y0 = y
    t += step

def add_sphere(points, cx, cy, r):
  t = 0
  t2 = 0
  step = 0.03
  while t < 1.0 + step:
    while t2 < 1.0 + step:
      x = r*math.cos(2*math.pi*t2) + cx
      y = r*math.sin(2*math.pi*t2)*math.cos(math.pi*t) + cy
      z = r*math.sin(2*math.pi*t2)*math.sin(math.pi*t)
      add_point(points, x, y, z)
      add_point(points, x, y, z)
      t2 += step
    t2 = 0
    t += step

def add_torus( points, cx, cy, r1, r2 ):
  t = 0
  t2 = 0
  step = 0.03
  while t < 1.0 + step:
    while t2 < 1.0 + step:
      x = math.cos(2*math.pi*t) * (r1*math.cos(2*math.pi*t2) + r2) + cx
      y = r1*math.sin(2*math.pi*t2) + cy
      z = -1*math.sin(2*math.pi*t) * (r1*math.cos(2*math.pi*t2) + r2)
      add_point(points, x, y, z)
      add_point(points, x, y, z)
      t2 += step
    t2 = 0
    t += step

def add_box( points,x,y,z,w,h,d ):
  add_point(points,x,y,z)
  add_point(points,x,y,z)
  add_point(points,x+w,y,z)
  add_point(points,x+w,y,z)
  add_point(points,x+w,y+h,z)
  add_point(points,x+w,y+h,z)
  add_point(points,x+w,y+h,z+d)
  add_point(points,x+w,y+h,z+d)
  add_point(points,x,y+h,z)
  add_point(points,x,y+h,z)
  add_point(points,x,y+h,z+d)
  add_point(points,x,y+h,z+d)
  add_point(points,x,y,z+d)
  add_point(points,x,y,z+d)
  add_point(points,x+w,y,z+d)
  add_point(points,x+w,y,z+d)

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
  t = 0
  xc = generate_curve_coefs(x0,x1,x2,x3,curve_type)[0]
  yc = generate_curve_coefs(y0,y1,y2,y3,curve_type)[0]
  while t < 1.0 + step:
    x = mult(t,xc)
    y = mult(t,yc)
    add_edge(points, x0, y0, 0, x, y, 0)
    x0 = x
    y0 = y
    t +=step

def mult(t,m):
    a = 0
    a += m[0]
    a *= t
    a += m[1]
    a *= t
    a += m[2]
    a *= t
    a += m[3]
    return a

def draw_lines( matrix, screen, color ):
  if len( matrix ) < 2:
      print "Need at least 2 points to draw a line"
  p = 0
  while p < len( matrix ) - 1:
    draw_line( screen, matrix[p][0], matrix[p][1],
               matrix[p+1][0], matrix[p+1][1], color )
    p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
  add_point( matrix, x0, y0, z0 )
  add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
  matrix.append( [x, y, z, 1] )

def draw_line( screen, x0, y0, x1, y1, color ):
  dx = x1 - x0
  dy = y1 - y0
  if dx + dy < 0:
    dx = 0 - dx
    dy = 0 - dy
    tmp = x0
    x0 = x1
    x1 = tmp
    tmp = y0
    y0 = y1
    y1 = tmp
    
  if dx == 0:
    y = y0
    while y <= y1:
      plot(screen, color,  x0, y)
      y = y + 1
  elif dy == 0:
    x = x0
    while x <= x1:
      plot(screen, color, x, y0)
      x = x + 1
  elif dy < 0:
    d = 0
    x = x0
    y = y0
    while x <= x1:
      plot(screen, color, x, y)
      if d > 0:
        y = y - 1
        d = d - dx
      x = x + 1
      d = d - dy
  elif dx < 0:
    d = 0
    x = x0
    y = y0
    while y <= y1:
      plot(screen, color, x, y)
      if d > 0:
        x = x - 1
        d = d - dy
      y = y + 1
      d = d - dx
  elif dx > dy:
    d = 0
    x = x0
    y = y0
    while x <= x1:
      plot(screen, color, x, y)
      if d > 0:
        y = y + 1
        d = d - dx
      x = x + 1
      d = d + dy
  else:
    d = 0
    x = x0
    y = y0
    while y <= y1:
      plot(screen, color, x, y)
      if d > 0:
        x = x + 1
        d = d - dy
      y = y + 1
      d = d + dx


