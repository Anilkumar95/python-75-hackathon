class delete:
  f1 ="atlantic"
  f2 = "Pacific"

oceans = delete()
print('Warm currents= ',oceans.f1)
print('silent nd shallow = ',oceans.f2)

del delete.f1
print('Warm currents= ',oceans.f1)
print('silent nd shallow = ',oceans.f2)
