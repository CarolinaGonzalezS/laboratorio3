import math

def apotema(n):
    alfa = 360/5
    den1= 2 * math.tan (36)
    den2 = den1 * (180/ math.pi)
    ap = n/den2
    return ap
    

def area_pentagono(n, m):
    area=(5*n*m)/2
    print(area)

a=apotema(5)
area_pentagono(a, 3.6)