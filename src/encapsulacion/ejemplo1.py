class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial

    cantidad=50000
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False
    
cuenta = CuentaBancaria("Ana García", 1000)
# Esto funciona, pero no es recomendable
print(cuenta._saldo)  # Imprime: 1000