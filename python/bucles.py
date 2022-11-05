""" cont = 0

print('2 elavado a ' + str(cont) + ' es igual a: ' + str(2**cont) )

cont = 1

print('2 elavado a ' + str(cont) + ' es igual a: ' + str(2**cont) )

cont = 2

print('2 elavado a ' + str(cont) + ' es igual a: ' + str(2**cont) )

cont = 3

print('2 elavado a ' + str(cont) + ' es igual a: ' + str(2**cont) )

cont = 4

print('2 elavado a ' + str(cont) + ' es igual a: ' + str(2**cont) )

cont = 

print('2 elavado a ' + str(cont) + ' es igual a: ' + str(2**cont) )
 """

def run():
    LIMIT = 1000000
    
    cont = 0
    potencia_2 = 2**cont
    while potencia_2 < LIMIT:
        print('2 elevado a ' + str(cont) + 
              ' es igual a: ' + str(potencia_2))
        cont = cont + 1
        potencia_2 = 2**cont

if __name__ == '__main__':
    run() 