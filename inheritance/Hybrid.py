class My(object):
  y = 5988

class Mt(My):
  z = 598

class M(My):
  q = 598

class Mat(M,Mt):
  x = 54

p1 = Mat()
print(p1.x)
print(p1.y)
print(p1.z)
print(p1.q)
