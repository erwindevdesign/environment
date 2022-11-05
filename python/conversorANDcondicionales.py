menu = """ 
Bienvenido al conversor de tipos de moneda $

Opciones: selecciona según tu necesidad de cambio una de las siguientes opciones.

1 - Pesos mexicanos a dolare$
2 - Pesos mexicanos a €uro
3 - Pesos mexicanos a ¥en

 """

 # :: shortcut ascii
 # $ = shift + 4 
 # € = Alt + 0128
 # ¥ = Alt + 0165

opcion = int(input(menu))

if opcion == 1:
    
    pesos = input("¿Cuántos pesos mx tienes?: ")
    pesos = float(pesos)
    tipo_de_cambio = 20.06
    dolares = pesos / tipo_de_cambio
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dólares.")


elif opcion == 2:
    
    pesos = input("¿Cuántos pesos mx tienes?: ")
    pesos = float(pesos)
    tipo_de_cambio = 19.65
    euro = pesos / tipo_de_cambio
    euro = round(euro, 2)
    euro = str(euro)
    print("Tienes € " + euro + " euros.")


elif opcion == 3:
    
    pesos = input("¿Cuántos pesos mx tienes?: ")
    pesos = float(pesos)
    tipo_de_cambio = 0.14
    yen = pesos / tipo_de_cambio
    yen = round(yen, 2)
    yen = str(yen)
    print("Tienes ¥ " + yen + " yenes.")

else: 
    print('Ingresa una opción entre 1 y 3 por favor!')