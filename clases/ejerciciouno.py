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
for i in range(20):
    cuenta.depositar(50)
    
for i in range(60):
    cuenta.depositar(20)
    

for i in range(40):
    cuenta.retirar(100)
    
for i in range(20):
    cuenta.retirar(50)
    
for i in range(60):
    cuenta.retirar(20)
    

