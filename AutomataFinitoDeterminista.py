class AutomataFinitoDeterminista:
    
    def __init__(self, estados, alfabeto, funcion_Transicion, estado_Inicial, estado_Aceptado):
        self.estados = estados
        self.alfabeto = alfabeto
        self.funcion_Transicion = funcion_Transicion
        self.estado_Inicial = estado_Inicial
        self.estado_Aceptado = estado_Aceptado
        self.estado_Actual = estado_Inicial
        return
    
    def transition(self, Palabra):
        self.estado_Actual = self.funcion_Transicion[(self.estado_Actual, Palabra)]
        return
    
    def estadoAceptado(self):
        if(self.estado_Actual in self.estado_Aceptado):
            return print('Aceptado\nEstado final:',self.estado_Actual)
        return print('Rechazado\nEstado final:',self.estado_Actual)
    
    def run(self, String):
        for i in String:
            self.transition(i)
            continue
        return self.estadoAceptado()