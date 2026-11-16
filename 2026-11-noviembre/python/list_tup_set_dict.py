# Dada nums = [4, 8, 15, 16, 23, 42], obtén con slicing: los 3 primeros, los 2 últimos y los elementos en posiciones pares ([4, 15, 23]).

nums = [4, 8, 15, 16, 23, 42]

firs = nums[0:3]
lasy = nums[-2:]
pares = nums[0::2]
# print(firs, lasy, pares)
# Escribe sin_duplicados(lista) que devuelva una lista nueva sin repetidos manteniendo el orden. [3, 1, 3, 2, 1] → [3, 1, 2].

def sin_duplicados(lista):
    lista_nueva = []
    for numero in lista:
        if numero not in lista_nueva:
            lista_nueva.append(numero)
    return lista_nueva
lst =[3, 1, 3, 2, 1]

# print(sin_duplicados(lst))


# Escribe contar_letras(texto) que devuelva un dict con cuántas veces aparece cada letra. "hola" → {'h': 1, 'o': 1, 'l': 1, 'a': 1}. Hazlo sin Counter.
def contar_letras(texto):
    dict = {}
    for palabra in texto:
        if palabra not in dict:
            dict[palabra] = 1
        else:
            dict[palabra] += 1
    return dict

# print(contar_letras("hohla"))

# Dados a = {"x": 1, "y": 2} y b = {"y": 5, "z": 9}, fusiónalos en un dict nuevo donde b gane en caso de clave repetida. Resultado: {'x': 1, 'y': 5, 'z': 9}.

a = {"x": 1, "y": 2, "z": 3}
b = {"y": 5, "z": 9}
def fusionar_dict(a, b):
    dict_nuevo = {}
    for clave, valor in a.items():
        dict_nuevo[clave] = valor
    for clave, valor in b.items():
        if clave in dict_nuevo:
            dict_nuevo[clave] = valor
        else:
            dict_nuevo[clave] = valor
    return dict_nuevo


# print(fusionar_dict(a, b))

# Dadas a = [1, 2, 3, 4] y b = [3, 4, 5, 6], obtén: elementos comunes, elementos de a que no están en b, y todos sin repetir.

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

# print(set(a) & set(b))
# print(set(a) - set(b))
# print(set(a) | set(b))

# Escribe min_max(lista) que devuelva el mínimo y el máximo a la vez, y llámala desempaquetando: menor, mayor = min_max([5, 2, 9]).

def min_max(lista):
    return min(lista), max(lista)

menor, mayor = min_max([5, 2, 9])

# print(menor, mayor)

# Con una sola comprehension, saca los cuadrados de los números pares de range(1, 11). Resultado: [4, 16, 36, 64, 100].

print([x**2 for x in range(1, 11) if x % 2 == 0])

# Dada palabras = ["sol", "luna", "mar", "estrella"], devuelve una lista con la longitud de cada palabra, pero solo de las que tengan más de 3 letras.

palabras = ["sol", "luna", "mar", "estrella"]

# print([len(x) for x in palabras if len(x) > 3])


# Crea {n: n**2 for ...} para los números del 1 al 5.
# print({n: n**2 for n in range(1,6)})

# Dado precios = {"pan": 1.2, "leche": 0.9, "queso": 3.5}, crea un dict nuevo solo con los productos que cuesten más de 1, y con el precio ya con un 10 % de descuento.

precios = {"pan": 1.2, "leche": 0.9, "queso": 3.5}

print({n: y*0.9 for n, y in precios.items() if y > 1})

# Dada frase = "el sol y el mar y el cielo", crea con una comprehension un dict {palabra: veces}. Pista: frase.split() y .count(). Luego dime por qué esta solución es ineficiente.

frase = "el sol y el mar y el cielo"


lista_pal = frase.split()

print({clave: lista_pal.count(clave) for clave in lista_pal})