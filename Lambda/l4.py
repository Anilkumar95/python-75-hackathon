def goat(n):
  return lambda u : u / n

double = goat(9)

print(double(900))
