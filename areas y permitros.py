#Area de un circulo
print("**Areas**")
def areaCirculo(radio):
    area = 3.1416 *(radio)**2
    return area

radio = 5
r= areaCirculo(radio)
print("areaCirculo:",r)

#Area de un cuadrado
def areaCuadrado(lado):
    area = lado**2
    return area 

lado = 8
r = areaCuadrado(lado)
print("areaCuadrado:",r)

#Area de triangulo 
def areaTriangulo(base,altura):
    area = (base * altura)/2
    return area

base = 5
altura = 7
r = areaTriangulo(base,altura)
print("areaTriangulo:",r)

#Area de un trapecio
def areaTrapecio(base1,base2,altura):
    area = (base1 + base2)*(altura)/2
    return area

base1 = 15
base2 = 12
altura = 6
r = areaTrapecio(base1,base2,altura)
print("areaTrapecio:",r)


#Perimetro de un circulo 
print("**Perimetros**")
def perimetroCirculo(radio):
    perimetro = 2 * 3.1416 * radio
    return perimetro

radio = 3
r = perimetroCirculo(radio)
print("perimetroCirculo:",r)

#Perimetro de un cuadrado
def perimetroCuadrado(lados):
    perimetro = 4*lados
    return perimetro

lados = 8
r = perimetroCuadrado(lados)
print("perimetroCuadrado:",r)

#Perimetro de un Triangulo
def perimetroTriangulo(lado1,lado2,lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

lado1 =5
lado2 =6
lado3 =7
r = perimetroTriangulo(lado1,lado2,lado3)
print("perimetroTriangulo:",r)

#Perimetro de un Trapecio
def perimetroTrapecio(base1,base2,altura,hipotenusa):
    perimetro = base1 + base2 + altura+ hipotenusa
    return perimetro

base1 = 4
base2 =10
altura =4
hipotenusa = 5
r = perimetroTrapecio (base1,base2,altura,hipotenusa)
print("perimetroTrapecio:",r)