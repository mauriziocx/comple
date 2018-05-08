'''
Ejercicio 11
Una cuenta bancaria es un contrato financiero con una entidad bancaria en virtud del cual,
seregistran el balance y los subsiguientes movimientos de dinero que el cliente realiza.

Los movimientos son depositos y retiros.Cuando se realiza un retiro el monto no puede exceder
al balance que el cliente tiene y tampoco puede retirar cantidades negativas.

Se pide:
Implementar la clase cuena con sus operaciones de deposito y retiro

'''

class Cuenta(object):

    def balance(self):
        return self.saldo
    
    def deposito(self, monto):
        if(monto>0):
            self.saldo = self.saldo + monto
    
    def retiro(self, monto):
        if(monto<=0 and monto>self.saldo):
            return(False)
        else:
            self.saldo = self.saldo - monto
            return(True)
    
    def __init__(self, saldoInicial=0):
        if(saldoInicial >= 0):
            self.saldo = saldoInicial