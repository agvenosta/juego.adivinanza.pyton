
import random 

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5

adivinado = False 

print("Bienvenido al juego del numero secreto")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("GAME OVER. No has podido adivinar dentro de los 5 intentos!")
        break
    
    entrada = input("Introduce un número del 1 al 99: ")
    numero = int(entrada) # CASTEO

    if numero == numero_secreto:
        print("Felicidades! Has adivinado el numero secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")

    cant_intentos += 1

