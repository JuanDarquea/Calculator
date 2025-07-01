# -*- coding: utf-8 -*-
import os # Importar el módulo os para limpiar la pantalla
def limpiar_pantalla(): # Definir la funcion para limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear') # Comando para limpiar la pantalla en Windows o Unix

def pausar(): # Definir la funcion para pausar la ejecucion
    input("Presiona Enter para continuar...") # Espera a que el usuario presione Enter

# Tus funciones de calculadora aqui
def sumar (a, b):   #creacin de la funcion sumar
    resultado = a + b #suma de los dos numeros
    return resultado #retorno del resultado

def restar (a, b):   #creacin de la funcion restar
    resultado = a - b #resta de los dos numeros
    return resultado #retorno del resultado

def multiplicar (a, b):   #creacin de la funcion multiplicar
    resultado = a * b #multiplicacion de los dos numeros
    return resultado #retorno del resultado

def dividir (a, b):   #creacion de la funcion dividir
    if b == 0:  #verificacion de que el divisor no sea cero
        return "Error: Division por cero" #mensaje de error
   # resultado = a / b #division de los dos numeros
    return a / b #retorno del resultado
limpiar_pantalla()
while True:
    limpiar_pantalla()
    print("=== CALCULADORA ===") #impresión del titulo de la calculadora
    print("1. Sumar") #impresion de las opciones de la calculadora
    print("2. Restar") #impresion de las opciones de la calculadora
    print("3. Multiplicar") #impresion de las opciones de la calculadora
    print("4. Dividir") #impresion de las opciones de la calculadora
    print("5. Salir") #impresion de las opciones de la calculadora
    opcion = input("Seleccione una opción (1-5): ") #solicitud de la opcin al usuario
    if opcion == "1": #verificacion de la opcion seleccionada
        limpiar_pantalla() #limpieza de la pantalla
        num1 = float(input("Ingrese el primer numero: ")) #solicitud del primer numero al usuario
        num2 = float(input("Ingrese el segundo numero: ")) #solicitud del segundo numero al usuario
        resultado = sumar(num1, num2) #llamada a la funcion sumar
        print("El resultado de la suma es:", resultado) #impresion del resultado de la suma
        print()  #espacio en blanco para mejorar la legibilidad
        pausar() #pausa la ejecucion para que el usuario pueda ver el resultado
    elif opcion == "2": #verificacion de la opcion seleccionada
            limpiar_pantalla()
            num1 = float(input("Ingrese el primer numero: "))   #solicitud del primer numero al usuario
            num2 = float(input("Ingrese el segundo numero: ")) #solicitud del segundo numero al usuario
            resultado = restar(num1, num2) #llamada a la funcion restar
            print("El resultado de la resta es:", resultado) #impresion del resultado de la resta
            print()  #espacio en blanco para mejorar la legibilidad
            pausar()
    elif opcion == "3": #verificacion de la opcion seleccionada
            limpiar_pantalla()
            num1 = float(input("Ingrese el primer numero: "))  #solicitud del primer numero al usuario
            num2 = float(input("Ingrese el segundo numero: ")) #solicitud del segundo numero al usuario
            resultado = multiplicar(num1, num2) #llamada a la funcion multiplicar
            print("El resultado de la multiplicacion es:", resultado) #impresion del resultado de la multiplicacion
            print()  #espacio en blanco para mejorar la legibilidad
            pausar()
    elif opcion == "4": #verificacion de la opcion seleccionada
            limpiar_pantalla()
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = dividir(num1, num2)
            print("El resultado de la division es:", resultado)
            print()  #espacio en blanco para mejorar la legibilidad
            pausar()
    elif opcion == "5": #verificacion de la opcion seleccionada
        limpiar_pantalla()
        print("Saliendo de la calculadora...")
        print()  #espacio en blanco para mejorar la legibilidad
        break
    else: #si la opcion no es valida
        print("Opcion no valida. Por favor, seleccione una opcion entre 1 y 5.")
        print()  #espacio en blanco para mejorar la legibilidad
        pausar()

