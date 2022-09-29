#ejercicio 2
numero1=int(input('Introduce un número: '))
print(str(numero1).zfill(6))
print("\n")
numero2=float(input('Introduce otro número: '))
print(str(numero2).zfill(7),"{:.3f}".format(numero2))