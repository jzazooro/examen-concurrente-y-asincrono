import random

class Jugador:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def elegir_numero(self, numero):
        self.apuesta_tipo = "Número"
        self.apuesta_valor = numero

    def elegir_par_impar(self, paridad):
        self.apuesta_tipo = "Par/Impar"
        self.apuesta_valor = paridad

    def elegir_color(self, color):
        self.apuesta_tipo = "Color"
        self.apuesta_valor = color

    def realizar_apuesta(self, monto):
        if monto <= self.saldo:
            self.apuesta_monto = monto
            self.saldo -= monto
            return True
        else:
            return False

    def recibir_pago(self, monto):
        self.saldo += monto

    def obtener_saldo(self):
        return self.saldo

class Ruleta:
    def __init__(self):
        self.numeros = ['0', '00'] + [str(i) for i in range(1, 37)]
        self.colores = ['verde', 'verde'] + ['rojo' if i % 2 == 0 else 'negro' for i in range(1, 37)]

    def girar(self):
        resultado = random.choice(self.numeros)
        color = self.colores[self.numeros.index(resultado)]
        return resultado, color

ruleta = Ruleta()
jugador = Jugador("Juan", 1000)


while jugador.saldo>100 or jugador.saldo<50000:
    jugador.elegir_numero("17")
    monto_apuesta = 10
    if jugador.realizar_apuesta(monto_apuesta):
        resultado, color = ruleta.girar()
        if resultado == jugador.apuesta_valor:
            pago = monto_apuesta * 36
            jugador.recibir_pago(pago)
        
    jugador.elegir_par_impar("par")
    monto_apuesta = 10
    if jugador.realizar_apuesta(monto_apuesta):
        resultado, color = ruleta.girar()
        if resultado != '0' and resultado != '00' and int(resultado) % 2 == 0 and jugador.apuesta_valor == "par":
            pago = monto_apuesta
            jugador.recibir_pago(pago)
        elif resultado != '0' and resultado != '00' and int(resultado) % 2 != 0 and jugador.apuesta_valor == "impar":
            pago = monto_apuesta
            jugador.recibir_pago(pago)

    
    jugador.elegir_color("rojo")
    monto_apuesta = 10
    if jugador.realizar_apuesta(monto_apuesta):
        resultado, color = ruleta.girar()
        if color == jugador.apuesta_valor:
            pago = monto_apuesta
            jugador.recibir_pago(pago)
    if jugador.obtener_saldo()==0:
        break