#while condicion = True False:
    


entrada = ""
intentos = 0
contraseña = "UCA123"

#bucle hasta llegar a 3... (3 intentos)
while entrada != contraseña and intentos < 3:
    entrada = input("ingrese su contraseña:  ")
    if entrada != contraseña:
        print("contraseña incorrecta")
        intentos += 1

if entrada == contraseña:
    print("contraseña correcta")
else:
    print("contraseña incorrecta")