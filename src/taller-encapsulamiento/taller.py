class CuentaBancaria:
    def __init__(self,titular : str,saldo: float = 0.0):
        self._titular= titular
        self._saldo = saldo
    
    #Getters

    def get_titular(self):
        return self._titular
    
    def get_saldo(self):
        return self._saldo
    
    #Setter

    def set_saldo(self,nuevo_saldo):
        if not isinstance(nuevo_saldo,(float,int)) or nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo= nuevo_saldo

    #Metodos para depositar y retirar
    def depositar(self,cantidad):
        if not isinstance(cantidad, (float,int)) or cantidad <= 0:
            return False
        else:
            self._saldo += cantidad
            return True
        
    def retirar(self,cantidad):
         if not isinstance(cantidad, (float,int)) or  cantidad > self._saldo or cantidad <=0:
             return False
         else:
             self._saldo -= cantidad
             return True
         
cuenta= CuentaBancaria("Simon",6000000.00)

print(f'Titular: {cuenta.get_titular()}')
print(f'Saldo: {cuenta.get_saldo()}')

#Modificar saldo
cuenta.set_saldo(10000000)
print(f'Nuevo saldo: {cuenta.get_saldo()}')

# operaciones

cuenta.depositar(6000000)
print(f'Nuevo saldo despues de depositar: {cuenta.get_saldo()}')

print(f'Retirar 1000000: {cuenta.retirar(10000000)}')
print(f'Saldo despues de retirar: {cuenta.get_saldo()}')

        
    
            
