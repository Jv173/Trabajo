def animar_nombre():
    nombre = input("Introduce un nombre: ")
    animacion = ""
    for letra in nombre:
        animacion += "Dame una " + letra.upper()
        print(animacion)
        animacion = ""
    print("\n" + "-".join(nombre.upper()))
 
def calcular_operacion():
    operacion = input("Introduce una operación: ")
    resultado = eval(operacion)
    print("Resultado:", resultado)

while True:
    print("----- Menú -----")
    print("1. Animarme")
    print("2. Calcular")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        animar_nombre()
    elif opcion == "2":
        calcular_operacion()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")