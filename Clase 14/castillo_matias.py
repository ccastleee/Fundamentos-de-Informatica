import random

def lista_sector(lista):
    for i in range(5*5):
        n = random.randint(0, 20)
        lista.append(n)
    return lista

def lista_capacitacion(lista):
    for i in range (20+5):
        n = random.randint(0, 144)
        lista.append(n)
    return lista

def porcentaje_1(lista):
    cont = 0
    for i in range(len(lista)):
        if lista[i] < 1:
            cont += 1
    porcentaje = (cont*100)/len(lista)
    porcentaje = round(porcentaje, 1)
    return porcentaje

def porcentaje_2(lista):
    cont = 0
    for i in range(len(lista)):
        if lista[i] >= 1 and lista[i] <= 5:
            cont += 1
    porcentaje = (cont*100)/len(lista)
    porcentaje = round(porcentaje, 1)
    return porcentaje

def porcentaje_3(lista):
    cont = 0
    for i in range(len(lista)):
        if lista[i] > 5:
            cont += 1
    porcentaje = (cont*100)/len(lista)
    porcentaje = round(porcentaje, 1)
    return porcentaje

def promedio_tiempo(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma/len(lista)
    promedio = round(promedio, 1)
    return promedio

def mayor_tiempo(lista):
    mayor = -9999
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def ordenar_lista(lista):
    for i in range(len(lista)):
        min_indice = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_indice]:
                min_indice = j
        aux = lista[i]
        lista[i] = lista[min_indice]
        lista[min_indice] = aux
    return lista
    
def matriz(lista_1, lista_2):
    matriz = []
    for i in range(len(lista_1)):
        fila = [lista_1[i], lista_2[i]]
        matriz.append(fila)
    for i in range(len(matriz)):
        print(matriz[i][0], matriz[i][1])
    return matriz

def buscar_coincidencia(lista):
    encontrado = 0
    for i in range(len(lista)):
        posicion = i
        if lista[i] == 20:
            print(f"El empleado con 20 años en el sector esta en la posición {posicion+1} de la lista.")
            encontrado += 1
    if encontrado == 0:
        print("No existe un empleado con 20 años en el sector.")
        
def main():
    comentario = """
    Nombre: Matias
    Apellido: Castillo
    Legajo: 1221635"""
    print(f"{comentario}\n")
    print("                    ----------BIENVENIDO A LA ENCUESTA DE EMPLEADOS----------\n")
    tiempo_sector = []
    tiempo_capacitacion = []
    tiempo_sector = lista_sector(tiempo_sector)
    tiempo_capacitacion = lista_capacitacion(tiempo_capacitacion)
    print(f"Lista de tiempo en el sector\n{tiempo_sector}\n")
    tiempo_sector = ordenar_lista(tiempo_sector)
    print(f"Lista de tiempo en el sector ordenada\n{tiempo_sector}\n")
    print(f"Lista de tiempo de capacitación\n{tiempo_capacitacion}\n")
    porcentaje_año = porcentaje_1(tiempo_sector)
    porcentaje_uno_cinco = porcentaje_2(tiempo_sector)
    porcentaje_cinco = porcentaje_3(tiempo_sector)
    promedio_cursos = promedio_tiempo(tiempo_capacitacion)
    print(f"Porcentaje de empleados que no superan el año es de {porcentaje_año}%\nPorcentaje de empleados entre 1-5 es de {porcentaje_uno_cinco}%\nPorcentaje de empleados con mas de 5 años es de {porcentaje_cinco}%")
    print(f"El promedio de tiempo que dedica los empleados a los cursos de capacitación mensual es de {promedio_cursos} horas.\n")
    print("Matriz 25x2")
    matriz(tiempo_sector, tiempo_capacitacion)
    buscar_coincidencia(tiempo_sector)
        
main()