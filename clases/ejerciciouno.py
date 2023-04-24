class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad==100 or cantidad==50 or cantidad==20:
            self.saldo += cantidad
        else:
            print("No se puede depositar esa cantidad")

    def retirar(self, cantidad):
        if cantidad == 100 or cantidad == 50 or cantidad == 20:
            self.saldo -= cantidad
        else:
            print("No se puede retirar esa cantidad")

    def consultar(self):
        print(self.saldo)

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