#MCD
print("ingrese dos numeros para calcular su mcd")
a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(f"el mcd de {a} y {b} es {mcd(a, b)}")
#MCM
print("ingrese dos numeros para calcular su mcm")
a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
def mcm(a, b):
    return a * b // mcd(a, b)
print(f"el mcm de {a} y {b} es {mcm(a, b)}")    