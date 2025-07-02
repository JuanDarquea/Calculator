def sumar (a, b):   #creacin de la funcion sumar
    resultado = a + b #suma de los dos numeros
    return resultado #retorno del resultado
sumar1 = sumar(9, 1)
print (sumar(sumar1, 3)) #prueba de la funcion sumar
print (sumar(10, 5)) #prueba de la funcion sumar
resultado = sumar(48, 52) #asignacin del resultado de la suma a una variable
print ("El resultado de la suma es igual a", resultado) #impresin del resultado de la suma

def restar (a, b):   #creacin de la funcion restar
    resultado = a - b #resta de los dos numeros
    return resultado #retorno del resultado
print (restar(10, 3)) #prueba de la funcion restar
print (restar(20, 5)) #prueba de la funcion restar
def multiplicar (a, b):   #creacin de la funcion multiplicar
    resultado = a * b #multiplicacion de los dos numeros
    return resultado #retorno del resultado
print (multiplicar(5, 3)) #prueba de la funcion multiplicar
print (multiplicar(10, 5)) #prueba de la funcion multiplicar
def dividir (a, b):   #creacion de la funcion dividir
    if b == 0:  #verificacion de que el divisor no sea cero
        return "Error: Division por cero" #mensaje de error
   # resultado = a / b #division de los dos numeros
    return a / b #retorno del resultado
print (dividir(10, 2)) #prueba de la funcion dividir
print (dividir(10, 0)) #prueba de la funcion dividir con divisor cero