import sys
input = sys.stdin.readline

def read():
  return tuple(map(int, input().split()))

def rookMoves(init, dest):
  # Posiciones iguales ya ha sido chequeado
  if (init[0] == dest[0]):
    return 1 # Solo coord X esta alineada
  if (init[1] == dest[1]):
    return 1 # Solo coord Y esta alineada
  return 2 # Ninguna coord esta alineada

def bishopMoves(init, dest):
  if ((init[0] + init[1]) % 2 != (dest[0] + dest[1]) % 2):
    return 0 # Coords son de colores distintos

  if (abs(dest[0] - init[0]) != abs(dest[1] - init[1])):
    return 2 # Coords no forman triangulo isoceles

  return 1 # Coords forman triangulo isoceles

def kingMoves(init, dest):
  return max(abs(dest[0] - init[0]), abs(dest[1] - init[1])) # Movimientos en diagonal son mejores, anulan el inferior entre deltaX o deltaY

(ri, ci, rf, cf) = read()

if (ri == rf and ci == cf):
  print("0 0 0")
else:
  print("{0} {1} {2}".format(rookMoves((ri, ci), (rf, cf)), bishopMoves((ri, ci), (rf, cf)), kingMoves((ri, ci), (rf, cf))))