import math

arreglo = None
n = None
llave = None
respuesta = None
r = None
l = None
a = None
ind = None
b = None
mid1 = None
mid2 = None

# Búsqueda Ternaria
#
def BusquedaTernaria(arreglo, n, llave):
  global respuesta, r, l, a, ind, b, mid1, mid2
  r = n
  l = 1
  a = 0
  b = 0
  while b != 1:
    mid1 = math.floor(l + (r - 1) / 3)
    mid2 = math.floor(r - (r - 1) / 3)
    if arreglo[int(mid1 - 1)] == llave:
      respuesta = mid1
      a = 1
      b = 1
    else:
      if arreglo[int(mid2 - 1)] == llave:
        respuesta = mid2
        a = 1
        b = 1
      else:
        if arreglo[int(mid1 - 1)] > llave:
          r = mid1 - 1
        else:
          if arreglo[int(mid2 - 1)] < llave:
            l = mid2 + 1
          else:
            l = mid1 + 1
            r = mid2 - 1
  if a == 0:
    respuesta = -1
  return respuesta


llave = 6
n = 10
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ind = BusquedaTernaria(arreglo, n, llave)
if ind != -1:
  print('El elemento: ' + str(llave))
  print('Se encontró en el lugar: ' + str(ind))
else:
  print('El elemento no se encontró en el arreglo.')