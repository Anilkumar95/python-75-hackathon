
class Elements:
  a= "hydrogen"
  b = "nitrogen"
  n = "oxygen"

e1 = Elements
#start
print("start")
print('a = ',e1.a)
print('b = ',e1.b)
print('n = ',e1.n)

delattr(Elements, 'b')

#after
print("after")
print('a = ',e1.a)
print('n = ',e1.n)


# climax
print('b = ',e1.b)
