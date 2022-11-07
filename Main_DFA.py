#Ejemplo de un Autómata Finito Determinito
estados = {0, 1} #Estados del autómata
alfabeto = {'a','b'} #Alfabeto de nuestro autómata

Funcion_Transicion = { #Función que realizará las transiciones
  (0, 'a'): 1,
  (0, 'b'): 1,
  (1, 'a'): 0,
  (1, 'b'): 0,
}

estado_Inicial = 0 #Estado inicial
estado_Aceptado = {1} #Estado aceptado

#Pruebas para obtener resultados correctos o incorrectos
Palabra = list('aba') #Palabra aceptada (ejemplo)
#Palabra = list('baba') #Palabra rechazada (ejemplo)

#Inicio de algoritmo que recorrera nuestra palabra para ver si esta será aceptada o rechazada
estado_Actual = estado_Inicial
for i in Palabra:
    if (estado_Actual, i) not in Funcion_Transicion.keys():
        print('Error al pasar a otro estado')
        break
    estado_Actual = Funcion_Transicion[(estado_Actual, i)]
if estado_Actual in estado_Aceptado:
    print('Aceptado\nEstado final:', estado_Actual)
else:
    print('Rechazado\nEstado final:', estado_Actual)