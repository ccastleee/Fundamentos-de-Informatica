import const

def pasajero():
    nombre = input("\nIngrese su nombre: ").title()
    apellido = input("\nIngrese su apellido: ").title()
    dni = int(input("\nIngrese su DNI (sin puntos): "))
    return nombre, apellido, dni

def seleccion_dia():
    ferrocarril = ""
    fecha_salida = ""
    print(f"\nIngrese que dia desea elegir:\n\n1.{const.dias[0]}\n\n2.{const.dias[1]}\n\n3.{const.dias[2]}\n")
    dia = input("Elija una opcion (1, 2 o 3): ")
    dia = validacion_dia(dia)
    if dia == "1":
        ferrocarril = const.fecha_ferrocarril[3]
        fecha_salida = const.fecha_ferrocarril[0]
    elif dia == "2":
        ferrocarril = const.fecha_ferrocarril[4]
        fecha_salida = const.fecha_ferrocarril[1]
    else:
        ferrocarril = const.fecha_ferrocarril[5]
        fecha_salida = const.fecha_ferrocarril[2]
    return ferrocarril, fecha_salida

def seleccion_destino():
    lugar_llegada = ""
    print("\nElija donde desea ir:\n\n1.Dolores\n\n2.Mar del Plata\n")
    destino = input("Elija una opcion (1 o 2): ")
    destino = validacion_destino(destino)
    if destino == "1":
        lugar_llegada = const.destinos[0]
    else:
        lugar_llegada = const.destinos[1]
    return destino, lugar_llegada

def seleccion_asiento():
    tipo_asiento = ""
    print("\nEliga el tipo de asiento:\n\n1.Asiento simple (sin precio adicional)\n\n2.Asiento semi-cama (+$2500)\n")
    asiento = input("Elija una opcion (1 o 2): ")
    asiento = validacion_asiento(asiento)
    if asiento == "1":
        tipo_asiento = const.asientos[0]
    else:
        tipo_asiento = const.asientos[1]
    return asiento, tipo_asiento

def validacion_dia(dia):
    while dia != "1" and dia != "2" and dia != "3":
        print("Error, ingrese un dia correcto.")
        dia = input("Ingrese que dia desea elegir (1, 2 o 3): ")
    return dia

def validacion_destino(destino):
    while destino != "1" and destino != "2":
        print("Error, ingrese un destino correcto.")
        destino = input("Elija una opcion (1 o 2): ")
    return destino

def validacion_asiento(asiento):
    while asiento != "1" and asiento != "2":
        print("Error, elija el asiento correctamente.")
        asiento = input("Elija su opcion (1 o 2): ")
    return asiento

def total_pasaje(destino, asiento):
    total = 0
    if destino == "1":
        total += const.dolores
    else:
        total += const.mdq
    if asiento == "2":
        total += const.semi_cama
    return total

def mayor_ganancia_indice(ganancias):
    mayor = -9999
    indice_mayor = -1
    for i in range(len(ganancias)):
        if ganancias[i] > mayor:
            mayor = ganancias[i]
            indice_mayor = i
    return mayor, indice_mayor

def total_recaudado(ganancias):
    sum = 0
    for i in range(len(ganancias)):
        sum += ganancias[i]
    return sum

def ordernar_reserva_matriz(ganancias):
    matriz = []
    indices = [i+1 for i in range(len(ganancias))]
    for i in range(len(ganancias)):
        min_indice = i
        for j in range(i+i, len(ganancias)):
            if ganancias[j] < ganancias[min_indice]:
                min_indice = j
        aux_1 = ganancias[i]
        ganancias[i] = ganancias[min_indice]
        ganancias[min_indice] = aux_1
        aux_2 = indices[i]
        indices[i] = indices[min_indice]
        indices[min_indice] = aux_2
    for i in range(len(ganancias)):
        fila = [indices[i], ganancias[i]]
        matriz.append(fila)
    for i in range(len(matriz)):
        print(matriz[i][0], matriz[i][1])