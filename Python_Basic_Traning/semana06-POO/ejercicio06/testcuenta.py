'''
Ejercicio12

'''

from ccuenta import Cuenta

def main():
    c = Cuenta()
    c.deposito(100)
    c.deposito(250)
    c.retiro(50)
    print("Balance=> " + str(c.balance()))
    

#
main()