from clases.ejerciciouno import*
from clases.ejerciciodos import*

def main():
    seleccion=input("Ingrese el ejercicio que desea ejecutar: ")
    if seleccion=="1":
        cuenta = CuentaBancaria(100)
            
        for i in range(40):
            cuenta.depositar(100)
            print("Se ha realizado un deposito en su cuenta de 100 euros, su saldo actual es de: ", cuenta.saldo)
        for i in range(20):
            cuenta.depositar(50)
            print("Se ha realizado un deposito en su cuenta de 50 euros, su saldo actual es de: ", cuenta.saldo)
        for i in range(60):
            cuenta.depositar(20)
            print("Se ha realizado un deposito en su cuenta de 20 euros, su saldo actual es de: ", cuenta.saldo)
            
        for i in range(40):
            cuenta.retirar(100)
            print("Se ha realizado un retiro en su cuenta de 100 euros, su saldo actual es de: ", cuenta.saldo)
        for i in range(20):
            cuenta.retirar(50)
            print("Se ha realizado un retiro en su cuenta de 50 euros, su saldo actual es de: ", cuenta.saldo)
        for i in range(60):
            cuenta.retirar(20)
            print("Se ha realizado un retiro en su cuenta de 20 euros, su saldo actual es de: ", cuenta.saldo)
            
        print("Ya se han realizado todas las operaciones, su saldo actual es de: ", cuenta.saldo)
    elif seleccion=="2":
        ruleta = Ruleta()
        jugador = Jugador("Juan", 1000)
        
        while jugador.saldo>100 or jugador.saldo<50000:
            jugador.elegir_numero("17")
            monto_apuesta = 10
            if jugador.realizar_apuesta(monto_apuesta):
                resultado, color = ruleta.girar()
                print("El número ganador es:", resultado)
                if resultado == jugador.apuesta_valor:
                    pago = monto_apuesta * 36
                    jugador.recibir_pago(pago)
                    print("¡Felicidades! Ganaste", pago)
                else:
                    print("Lo siento, perdiste")
            else:
                print("Saldo insuficiente para realizar la apuesta")
            
            jugador.elegir_par_impar("par")
            monto_apuesta = 10
            if jugador.realizar_apuesta(monto_apuesta):
                resultado, color = ruleta.girar()
                print("El número ganador es:", resultado)
                if resultado != '0' and resultado != '00' and int(resultado) % 2 == 0 and jugador.apuesta_valor == "par":
                    pago = monto_apuesta
                    jugador.recibir_pago(pago)
                    print("¡Felicidades! Ganaste", pago)
                elif resultado != '0' and resultado != '00' and int(resultado) % 2 != 0 and jugador.apuesta_valor == "impar":
                    pago = monto_apuesta
                    jugador.recibir_pago(pago)
                    print("¡Felicidades! Ganaste", pago)
                else:
                    print("Lo siento, perdiste")
            else:
                print("Saldo insuficiente para realizar la apuesta")
            
            jugador.elegir_color("rojo")
            monto_apuesta = 10
            if jugador.realizar_apuesta(monto_apuesta):
                resultado, color = ruleta.girar()
                print("El número ganador es:", resultado)
                if color == jugador.apuesta_valor:
                    pago = monto_apuesta
                    jugador.recibir_pago(pago)
                    print("¡Felicidades! Ganaste", pago)
                else:
                    print("Lo siento, perdiste")
            print("El saldo final del jugador es: ", jugador.obtener_saldo())
            if jugador.obtener_saldo()==0:
                print("El jugador se quedó sin dinero")
                break
