def goat(n):
  return lambda u : u ** n

double = goat(2)

print(double(11))
