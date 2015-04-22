import math

def make_translate( x, y, z ):
  m = new_matrix()
  ident(m)
  l = [x,y,z]
  for r in range(len(m)-1):
    m[3][r] = l[r]
  return m

def make_scale( x, y, z ):
  m = new_matrix()
  ident(m)
  l = [x,y,z]
  for r in range(len(m)-1):
    m[r][r] = l[r]
  return m

def make_rotX( theta ):    
  m = new_matrix()
  ident(m)
  ang = math.radians(float(theta))
  m[1][1] = math.cos(ang)
  m[2][1] = -1*math.sin(ang)
  m[1][2] = math.sin(ang)
  m[2][2] = math.cos(ang)
  return m

def make_rotY( theta ):
  m = new_matrix()
  ident(m)
  ang = math.radians(float(theta))
  m[0][0] = math.cos(ang)
  m[2][0] = -1*math.sin(ang)
  m[0][2] = math.sin(ang)
  m[2][2] = math.cos(ang)
  return m

def make_rotZ( theta ):
  m = new_matrix()
  ident(m)
  ang = math.radians(float(theta))
  m[0][0] = math.cos(ang)
  m[1][0] = -1*math.sin(ang)
  m[0][1] = math.sin(ang)
  m[1][1] = math.cos(ang)
  return m

def new_matrix(rows = 4, cols = 4):
  m = []
  for c in range( cols ):
    m.append( [] )
    for r in range( rows ):
      m[c].append( 0 )
  return m

def print_matrix( matrix ):
  s = ''
  for r in range( len( matrix[0] ) ):
    for c in range( len(matrix) ):
      s+= str(matrix[c][r]) + ' '
      s+= '\n'
      print s

def ident(matrix):
  for r in range( len( matrix[0] ) ):
    for c in range( len(matrix) ):
      if r==c:
        matrix[r][c] = 1
      else:
        matrix[r][c] = 0
  return matrix

def scalar_mult( matrix, x ):
  for r in range( len( matrix[0] ) ):
    for c in range( len(matrix) ):
      matrix[r][c]*= x
  return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
  m = new_matrix(len(m1[0]),len(m2))
  for i in range(len(m1[0])):
    for j in range(len(m2)):
      sum = 0
      for k in range(len(m2[0])):
        sum += m1[k][i] * m2[j][k]
      m[j][i] = sum
  for a in range(len(m2)):
    for b in range(len(m2[0])):
      m2[a][b] = m[a][b]
