peso = float(input("Ingrese su peso en KG:"))
estatura = float(input("Ingrese su estatura en Mts:"))

imc = peso / (estatura * estatura)
print ("Su IMC es:",imc)
if (imc < 18.5):
    print ("Desnutricion")
if (imc >= 18.5 and imc <= 24.9):
    print ("Peso normal")
if (imc >= 30.0):
    print ("Obesidad")