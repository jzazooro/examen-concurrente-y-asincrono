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
        