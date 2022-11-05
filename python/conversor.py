
# conversor colombiano 
""" 
pesos = input('¿Cuántos pesos colombianos tienes?: ')
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tienes $' + dolares + ' dólares')
 """



# conversor mx
""" 
pesos = input("¿Cuántos pesos mx tienes?: ")
pesos = float(pesos)
tipo_de_cambio = 20.05
dolares = pesos / tipo_de_cambio
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $ " + dolares + " dólares.")

 """

# conversor Dolar = Pesos mx
""" 
dolar = input("¿Cuantos dolares tienes homs: ")
dolar = float(dolar)
tipo_de_cambio = 20.05
pesos = dolar * tipo_de_cambio
pesos = round(pesos)
pesos = str(pesos)
print("Tienes $ " + pesos + " pesos mexicanos perro!!")
 """

# funciones, bloque de codigo que contiene instrucciones quue se ejecutan en diferentes partes de la vida del código

""" def imp_mensage():
    print ('Mensaje de prueba: ')
    print ('¡Comprendiendo las funciones en PYTHON!')


imp_mensage()
imp_mensage()
imp_mensage() 
"""



def text(mensaje):
    print('Hola!!')
    print('¿Cómo estás?')
    print(mensaje)
    print('Bye :)')

opcion = int(input(""" 

Elige un opción entre:

1
2
3

para legir una región y su tipo de cambio monetario

 """))

if opcion == 1:
    text('Elegiste la opción: 1 (Dolares $)')
elif opcion == 2:
    text('Elegiste la opción: 2 (Euros €)')
elif opcion == 3:
    text('Elegiste la opción: 3 (Yenes ¥)')
else:
    print('Selcciona una de las opciones!')
