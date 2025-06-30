def pasajero():
    nombre = input("\nIngrese su nombre: ").title()
    apellido = input("\nIngrese su apellido: ").title()
    dni = int(input("\nIngrese su DNI (sin puntos): "))
    return nombre, apellido, dni

def seleccion_dia():
    ferrocarril = ""
    fecha_salida = ""
    print(f"\nIngrese que dia desea elegir:\n\n1.{dias[0]}\n\n2.{dias[1]}\n\n3.{dias[2]}\n")
    dia = input("Elija una opcion (1, 2 o 3): ")
    dia = validacion_dia(dia)
    if dia == "1":
        ferrocarril = fecha_ferrocarril[3]
        fecha_salida = fecha_ferrocarril[0]
    elif dia == "2":
        ferrocarril = fecha_ferrocarril[4]
        fecha_salida = fecha_ferrocarril[1]
    else:
        ferrocarril = fecha_ferrocarril[5]
        fecha_salida = fecha_ferrocarril[2]
    return ferrocarril, fecha_salida

def seleccion_destino():
    lugar_llegada = ""
    print("\nElija donde desea ir:\n\n1.Dolores\n\n2.Mar del Plata\n")
    destino = input("Elija una opcion (1 o 2): ")
    destino = validacion_destino(destino)
    if destino == "1":
        lugar_llegada = destinos[0]
    else:
        lugar_llegada = destinos[1]
    return destino, lugar_llegada

def seleccion_asiento():
    tipo_asiento = ""
    print("\nEliga el tipo de asiento:\n\n1.Asiento simple (sin precio adicional)\n\n2.Asiento semi-cama (+$2500)\n")
    asiento = input("Elija una opcion (1 o 2): ")
    asiento = validacion_asiento(asiento)
    if asiento == "1":
        tipo_asiento = asientos[0]
    else:
        tipo_asiento = asientos[1]
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
        total += dolores
    else:
        total += mdq
    if asiento == "2":
        total += semi_cama
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

def main():
    print(f"                          ----------GRUPO 7----------\nIntegrantes: {grupo[0]}, {grupo[1]}, {grupo[2]}, {grupo[3]}, {grupo[4]}\n-----------------------------------------------------------------------------------------")
    for i in range(3):
        datos_pasajero = []
        print(f"\nReserva numero: {i+1}\n")
        nombre, apellido, dni = pasajero()
        datos_pasajero.append(nombre)
        datos_pasajero.append(apellido)
        datos_pasajero.append(dni)
        ferrocarril, fecha_salida = seleccion_dia()
        datos_pasajero.append(ferrocarril)
        datos_pasajero.append(fecha_salida)
        destino, lugar_llegada = seleccion_destino()
        datos_pasajero.append(destino)
        datos_pasajero.append(lugar_llegada)
        asiento, tipo_asiento = seleccion_asiento()
        datos_pasajero.append(tipo_asiento)
        total = total_pasaje(destino, asiento)
        total = round(total, 2)
        datos_pasajero.append(total)
        ganancias.append(total)
        print(f"\n----------DATOS----------\n\nNUMERO DE FERROCARRIL: {datos_pasajero[3]}\n\nFECHA Y HORA DE SALIDA: {datos_pasajero[4]}\n\nLUGAR DE SALIDA: {lugar_salida[0]}\n\nLUGAR DE LLEGADA: {datos_pasajero[6]}\n\nNOMBRE: {datos_pasajero[0]}\n\nAPELLIDO: {datos_pasajero[1]}\n\nDNI: {datos_pasajero[2]}\n\nNUMERO DE RESERVA: {i+1}\n\nTIPO DE ASIENTO: {datos_pasajero[7]}\n\nTOTAL A PAGAR: {total}$\n")
    mayor, indice_mayor = mayor_ganancia_indice(ganancias)
    print(f"Lista de ganancias\n{ganancias}\n")
    ordernar_reserva_matriz(ganancias)
    print(f"\nLa reserva {indice_mayor+1} es la mas alta con {mayor}$.\n")
    print(f"Total recaudado: {total_recaudado(ganancias)}$.")

dolores = 5500
mdq = 8500
semi_cama = 2500
lugar_salida = ["Plaza Constitución"]
grupo = ["Diaz Juan", "Castillo Matias", "Regueira Camila", "Castillo Melani", "Lucero Micaela"]
fecha_ferrocarril = ["07/05/2025", "08/05/2025", "09/05/2025", "F234", "F543", "F045"]
dias = ["Miercoles 9:00 AM", "Jueves 9:00 AM", "Viernes 9:00 AM"]
destinos = ["Dolores", "Estación Mar del Plata"]
asientos = ["Simple", "Semi-cama"]
ganancias = []
main()