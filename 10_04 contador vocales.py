texto = str(input("ingrese su palabra: "))
vocal = "aeiou"
contador = 0

for letra in texto:
    if letra in vocal:
        contador += 1

print("Número de vocales:", contador)


