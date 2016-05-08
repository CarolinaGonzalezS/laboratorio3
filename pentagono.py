l=float (input('ingrese cuantos lados tiene su poligono: '))
import math
#def area_triangulo(n, m):
 #   a= (n*m)/2
  #  print(a)

def per_trinagulo(x, y, z):
	p= x + y + z
	print(p)

def calc_s(x, y, z):
    s= (x+y+z)/2
    return s

def calc_radical(s, x, y, z):
    total= s*(s-x)*(s-y)*(s-z)
    return total

def area_cuadrado(n, m):
	a= n*m
	print(a)

def per_cuadrado(n, m):
	p=(n*2) + (m*2)
	print(p)
    
def apotema(n):
	#alfa= 360/5
    #den1= 2 * math.tan (36) * (180/math.pi)
    #den2= den1 * (180/math.pi)
    apotema=n/1.45308
    a=apotema
    return a

def area_pentagono(n, m):
    area=(5*n*m)/2
    print(area)

def per_pentagono(n):
	p=n*5
	print (p)

if l==3:
    a = float (input ('ingrese el valor del lado a:'))
    b = float (input ('ingrese el valor del lado b:'))
    c = float (input ('ingrese el valor del lado c:'))
    d= calc_s(a, b, c)
    radical= calc_radical(d, a, b, c)
    t=math.sqrt(radical)
    print('el area del triangulo es:')
    print (t)
    print ('el perimetro del triangulo es:')
    per_trinagulo(a, b, c) 

elif l==4:
	l1=float(input('ingrese el valor de la base:'))
	l2=float(input('ingrese el valor de la altura:'))
	print('el valor del area es:')
	area_cuadrado(l1, l2)
	print('el valor del perimetro es:')
	per_cuadrado(l1, l2)

else:
	l==5
	print('si es un valor decimal ingreselo con un punto')
	lado=float(input('ingrese el valor del lado en cm:'))
	ap=apotema(lado)
	print('el valor del perimetro es:')
	per_pentagono(lado)
	print('el valor del area es:')
	area_pentagono(lado, ap)


#print('su area es: ' + str(total))