class My(object):
  y = 5988

class Mt(object):
  z = 598


class Mat(My,Mt):
  x = 54

p1 = Mat()
print(p1.x)
print(p1.y)
print(p1.z)
