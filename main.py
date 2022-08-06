from math import sqrt

def min(a, b):
	if b>a:
		res1 = a
	else:
		res1 = b
	return res1

def salto(arreglo, item, n):
	bloque = int()
	res = int()
	previo = int()
	bloque = int(sqrt(n))
	previo = 1
	while arreglo[min(bloque,n)-1]<item:
		previo = bloque
		bloque = bloque+int(sqrt(n))
		if previo>=n:
			res = -1
	while arreglo[previo-1]<item:
		previo = previo+1
		if arreglo[previo-1]==item:
			res = previo
		else:
			res = -1
	return res

if __name__ == '__main__':
	arreglo = int()
	arreglo = [int() for ind0 in range(16)]
	arreglo[0] = 0
	arreglo[1] = 1
	arreglo[2] = 1
	arreglo[3] = 2
	arreglo[4] = 3
	arreglo[5] = 5
	arreglo[6] = 8
	arreglo[7] = 13
	arreglo[8] = 21
	arreglo[9] = 55
	arreglo[10] = 77
	arreglo[11] = 89
	arreglo[12] = 101
	arreglo[13] = 201
	arreglo[14] = 256
	arreglo[15] = 780
	item = int()
	n = int()
	busc = int()
	print("Ingrese valor a buscar: ")
	item = int(input())
	n = 16
	busc = salto(arreglo,item,n)
	if busc>=0:
		if busc==0:
			busc = 1
			print("El numero esta en la posicion: ",busc)
		else:
			print("El numero esta en la posicion: ",busc)
	else:
		print("No se encontro el numero")