from AutomataFinitoDeterminista import * #Importamos nuestra clase main

#Ejemplo de un Autómata Finito Determinito
estados = {0, 1} #Estados del autómata
alfabeto = {'0','1'} #Alfabeto de nuestro autómata

transicion =	{ #Transicion
  (0, '0'): 1,
  (0, '1'): 1,
  (1, '0'): 0,
  (1, '1'): 0,
}

estado_Inicial = 0 #Estado inicial
estado_Aceptado = {1} #Estado aceptado

#Parametros de nuestro DFA
dfa_Automata = AutomataFinitoDeterminista(estados, alfabeto, transicion, estado_Inicial, estado_Aceptado)

Palabra = list('010') #Aceptado
#Palabra= list('1010') #Rechazado

print(dfa_Automata.run(Palabra))
