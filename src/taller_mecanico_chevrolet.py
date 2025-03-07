def iniciar():
    bienvenida=''' Bienvenido a la base de datos del taller mecanico de chevrolet'''
    print(bienvenida)
    carros=[]
    operaciones=''' ¿que operacion deseas hacer?
    1-Agregar automovil
    2-Borrar automovil
    3-leer
    4-salir:'''
    while True:
        opc=input(operaciones)
        if opc=='1':
            carro_agregar=input('¿Que carro deseas agregar?')
            carros.append(carro_agregar)
            print(carros)
            continue
        elif opc=='2':   
                carro_borrar=input('¿que carro deseas borrar?')
                if carro_borrar in carros:
                    carros.remove(carro_borrar)
                    print(carros)
                    continue
                else:
                    print('el carro no esta en la lista')
                    continue
        elif opc=='3':
            print(carros)
        elif opc=='4':
            print('Gracias por utilizar el programa')
            break
        else:
            print('opcion invalida')
            continue 
