import random
"""Comentar su nombre, apellido y legajo o DNI.
Declare tres listas de nombres “codigo”, “perro” y “edad” y mediante funciones cargue la primera con 7 números del 1 al 7, la segunda de 7 nombres de perro, y la última de valores aleatorios entre el 0 y el 17.
Imprimir las tres listas cargadas.
Mediante una función determinar qué porcentaje de perros tienen más de 7 años.
Imprimir el resultado.
Mediante otra función, mostrar el promedio de edad de los perros.
Mediante otra función, imprimir la mayor y menor edad de la lista edad.
Mediante una función, mostrar la cantidad de perros que tienen entre 0 y 2 años inclusive, entre 3 y 12 inclusive, y los que tienen más o igual a 13.
Mediante una función, ordenar la lista edad con alguno de los métodos vistos en clase.
Mediante una función, crear una matriz 7x3 con las tres listas e imprimir el resultado, tener en cuenta que los datos deben coincidir y debe estar ordenado de menor a mayor de acuerdo a la edad de los perros.
Mediante una última función buscar el nombre de un perro, si coincide mostrar el código, nombre y edad del mismo, sino mostrar un mensaje de no coincidencia.
Indicación complementaria: Al momento de solicitar datos por consola o mostrar los resultados, intente que el algoritmo indique correctamente lo que se requiere o presente a fin de que sea más amigable con el usuario.
"""
comentario = """
Nombre: Matias
Apellido: Castillo
Legajo: 1221635
DNI: 43323817
"""

def uno_siete(lista):
    print("Ingrese numero del 1 al 7 inclusive: ")
    for i in range(7):
        n = int(input("Ingrese: "))
        n = validar_uno_siete(n)
        lista.append(n)
    return lista

def nombres_perros(lista):
    print("Ingrese 7 nombres de perros")
    for i in range(7):
        perro = input("Ingrese: ").capitalize()
        lista.append(perro)
    return lista

def valores_aleatorios(lista):
    for i in range(7):
        ran = random.randint(0,17)
        lista.append(ran)
    return lista

def validar_uno_siete(n):
    while n < 1 or n > 7:
        print("Error, ingrese numeros entre el 1 y 7 inclusive!")
        n = int(input("Ingrese: "))
    return n

def porcentaje_edad(lista):
    cont = 0
    for i in range(len(lista)):
        if lista[i] > 7:
            cont += 1
    porcentaje = (cont*100)/len(lista)
    porcentaje = round(porcentaje, 1)
    return porcentaje

def promedio_edad(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    promedio = sum/len(lista)
    promedio = round(promedio,1)
    return promedio

def mayor_menor_edad(lista):
    mayor = -9999
    menor = 9999
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    return mayor, menor

def rango_edades(lista):
    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    for i in range(len(lista)):
        if lista[i] >= 0 and lista[i] <= 2:
            cont_1 += 1
        elif lista[i] >= 3 and lista[i] <= 12:
            cont_2 += 1
        else:
            cont_3 += 1
    return cont_1, cont_2, cont_3

def ordenar(lista):
    for i in range(len(lista)):
        min_indice = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_indice]:
                min_indice = j
        aux = lista[i]
        lista[i] = lista[min_indice]
        lista[min_indice] = aux
    return lista

def matriz(lista, lista_1, lista_2):
    matriz = []
    for i in range(len(lista)):
        fila = [lista[i], lista_1[i], lista_2[i]]
        matriz.append(fila)
    for i in range(len(matriz)):
        print(matriz[i][0], matriz[i][1],matriz[i][2])
    return matriz

def coincidendia(matriz):
    encontrado = 0
    nombre = input("Ingrese el nombre de perro: ").capitalize()
    for i in range(len(matriz)):
        if matriz[i][1] == nombre:
            print(f"Codigo: {matriz[i][0]}\nNombre: {matriz[i][1]}\nEdad: {matriz[i][2]}")
            encontrado += 1
    if encontrado == 0:
        print("No se encontro el nombre.")

codigo = []
perro = []
edad = []
codigo = uno_siete(codigo)
perro = nombres_perros(perro)
edad = valores_aleatorios(edad)
print(codigo)
print(perro)
print(edad)
print(f"El porcentaje de perros con mas de 7 anos es del {porcentaje_edad(edad)}%")
print(f"El promedio de edad de los perros es de {promedio_edad(edad)}")
mayor, menor = mayor_menor_edad(edad)
print(f"La mayor edad es {mayor} y la menor edad es {menor}")
cont_1, cont_2 , cont_3 = rango_edades(edad)
print(f"La cantidad de edades entre 0-2 son {cont_1}, entre 3-12 son {cont_2}, y de 13 o mas son {cont_3}")
print(f"Edades ordenadas\n{ordenar(edad)}")
print("Matriz 7x3")
matriz_1 = matriz(codigo,perro,edad)
coincidendia(matriz_1)




