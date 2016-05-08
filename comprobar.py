def apotema(n):
	alfa= 360/5
    den1= 2 * math.tan (36) * (180/math.pi)
    den2= den1 * (180/math.pi)
    apotema=n/den2
    print(apotema)

def area_pentagono(n, m):
    area=(5*n*m)/2
    print(area)

a=apotema()
area_pentagono(a, 3.6)