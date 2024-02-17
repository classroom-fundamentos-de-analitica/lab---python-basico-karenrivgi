"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# leer el archivo data.csv
def leer_archivo():
    with open("data.csv", "r") as file:
        data = file.read().splitlines()
    return data


# Preguntas
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    archivo = leer_archivo()

    # extrae la segunda columna, donde cada linea es una cadena de texto separada por tabulaciones
    columna_2 = [int(linea.split("\t")[1]) for linea in archivo]
    resultado = sum(columna_2)

    return resultado


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    archivo = leer_archivo()
    columna_1 = [linea.split("\t")[0] for linea in archivo]

    # cuenta la cantidad de veces que aparece cada letra en la primera columna, eliminando repetidos
    registros = list(set([(letra, columna_1.count(letra)) for letra in columna_1]))

    # ordena la lista de tuplas por la clave (letra)
    resultado = sorted(registros, key=lambda x: x[0])

    return resultado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    

    """
    archivo = leer_archivo()

    # Extrae la primera y segunda columna del archivo, por cada línea
    columnas_1y2 = [(linea.split("\t")[0], int(linea.split("\t")[1])) for linea in archivo]

    # Suma los valores de la columna 2 por cada letra de la columna 1
    grupos = {}
    for letra, valor in columnas_1y2:
        if letra in grupos:
            grupos[letra] += valor
        else:
            grupos[letra] = valor
    
    # Ordena la lista de tuplas por la clave (letra)
    resultado = sorted(list(grupos.items()), key=lambda x: x[0])

    return resultado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    archivo = leer_archivo()

    # Extrae el mes de la columna 3, por cada línea
    columna_3_mes = [linea.split("\t")[2].split("-")[1] for linea in archivo]

    # Cuenta la cantidad de veces que aparece cada mes en la columna 3, eliminando repetidos
    registros = list(set([(mes, columna_3_mes.count(mes)) for mes in columna_3_mes]))

    # Ordena la lista de tuplas por la clave (mes)
    resultado = sorted(registros, key=lambda x: x[0])

    return resultado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    archivo = leer_archivo()

    # Obtenemos la primera y segunda columna del archivo
    columna_1 = [linea.split("\t")[0] for linea in archivo]
    columna_2 = [int(linea.split("\t")[1]) for linea in archivo]

    # Agrupamos los valores de la columna 2 por cada letra de la columna 1
    grupo = {}
    for i in range (len(archivo)):
        letra = columna_1[i]
        if letra in grupo:
            grupo[letra].append(columna_2[i])
        else:
            grupo[letra] = [columna_2[i]]

    # Obtenemos el valor maximo y minimo de la columna 2 por cada letra de la columna 1 y los ordenamos por su clave
    registros = [(letra, max(valores), min(valores)) for letra, valores in grupo.items()]
    resultado = sorted(registros, key=lambda x: x[0])
    
    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    archivo = leer_archivo()
    columna_5 = [linea.split("\t")[4].split(',') for linea in archivo]
    tuplas_columna_5 = [item for sublista in columna_5 for item in sublista]

    # Agrupamos los valores de la columna 2 por cada letra de la columna 1
    grupo = {}
    for i in range (len(tuplas_columna_5)):
        letras = tuplas_columna_5[i].split(":")[0]
        valor = int(tuplas_columna_5[i].split(":")[1])
        if letras in grupo:
            grupo[letras].append(valor)
        else:
            grupo[letras] = [valor]

    # Obtenemos el valor maximo y minimo de la columna 2 por cada letra de la columna 1 y los ordenamos por su clave
    registros = [(letras, min(valores), max(valores)) for letras, valores in grupo.items()]
    resultado = sorted(registros, key=lambda x: x[0])
    
    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    archivo = leer_archivo()

    # Obtenemos la primera y segunda columna del archivo
    letras = [linea.split("\t")[0] for linea in archivo] # columna 1
    valores = [int(linea.split("\t")[1]) for linea in archivo] # columna 2
    
    # Agrupamos los valores de la columna 1 por cada valor de la columna 2 (sin repetir)
    registros = [(num, [letras[i] for i in range(len(valores)) if valores[i] == num]) 
                 for num in set(valores)]
    
    return registros


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    archivo = leer_archivo()

    # Obtenemos la primera y segunda columna del archivo
    letras = [linea.split("\t")[0] for linea in archivo] # columna 1
    valores = [int(linea.split("\t")[1]) for linea in archivo] # columna 2

    # Agrupamos los valores de la columna 1 por cada valor de la columna 2 (sin repetir)
    # (Con la misma lógica del anterior, pero sin usar list comprehension)

    registros = []

    # Recorremos los números de la columna 2 sin repetir
    for num in set(valores):
        letras_asociadas = []

        # Recorremos ambas columnas, y si el valor de la columna 2 es igual a num, agregamos la letra asociada a la lista 
        for i in range(len(valores)):
            if valores[i] == num:
                letras_asociadas.append(letras[i])
        
        # Ordenamos y eliminamos las letras repetidas
        letras_sort_reduce = sorted(list(set(letras_asociadas)))
        registros.append((num, letras_sort_reduce))

    return registros


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    archivo = leer_archivo()
    columna_5 = [linea.split("\t")[4].split(',') for linea in archivo]
    columna_5_plana = [item for sublista in columna_5 for item in sublista]

    # Contamos la cantidad de veces que aparece cada clave de letras en la columna 5
    grupo = {}
    for i in range (len(columna_5_plana)):
        letras = columna_5_plana[i].split(":")[0]
        if letras in grupo:
            grupo[letras] += 1
        else:
            grupo[letras] = 1

    grupo_ordenado = {k:grupo[k] for k in sorted(grupo.keys())}
    return grupo_ordenado


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    archivo = leer_archivo()

    # Extrae la primera, cuarta y quinta columna del archivo
    columna_1 = [linea.split("\t")[0] for linea in archivo]
    columna_4 = [linea.split("\t")[3] for linea in archivo]
    columna_5 = [linea.split("\t")[4] for linea in archivo]

    # Cuenta la cantidad de elementos de las columnas 4 y 5 por cada letra de la columna 1 en el archivo
    resultado = [(columna_1[i], len(columna_4[i].split(',')), len(columna_5[i].split(','))) 
                 for i in range(len(columna_1))]
    
    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    archivo = leer_archivo()
    diccionario = {}

    # Extrae la segunda y cuarta columna del archivo
    valores = [linea.split("\t")[1] for linea in archivo] # columna 2
    conjunto_letras = [linea.split("\t")[3] for linea in archivo] # columna 4

    # Recorre línea por línea el archivo
    for i in range(len(conjunto_letras)):

        # Separa las letras de la columna 4 
        letras = conjunto_letras[i].split(",")

        # Recorre letra por letra de la columna 4 y suma el valor de la columna 2 en el diccionario
        for j in range(len(letras)):
            letra = letras[j]
            valor = int(valores[i])
            if letra in diccionario:
                diccionario[letra] += valor
            else:
                diccionario[letra] = valor

    diccionario_ordenado = {k:diccionario[k] for k in sorted(diccionario.keys())}
    return diccionario_ordenado


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    archivo = leer_archivo()

    columna_1 = [linea.split("\t")[0] for linea in archivo]
    columna_5 = [linea.split("\t")[4].split(',') for linea in archivo]
    
    for sublist in columna_5:
        for i in range(len(sublist)):
            sublist[i] = int(sublist[i].split(':')[1])
    
    diccionario = {}
    for i in range(len(columna_1)):
        letra = columna_1[i]
        suma = sum(columna_5[i])
        if letra in diccionario:
            diccionario[letra] += suma
        else:
            diccionario[letra] = suma
    
    diccionario_ordenado = {k:diccionario[k] for k in sorted(diccionario.keys())}
    return diccionario_ordenado