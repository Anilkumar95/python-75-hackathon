def man(i):
  return lambda a : a * i

simple = man(29)
complex = man(35)

print(simple(119))
print(complex(45567))
