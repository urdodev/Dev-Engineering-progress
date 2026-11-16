# Escribe potencia(base, exp=2) que devuelva base ** exp. Comprueba que potencia(3) da 9 y potencia(2, 5) da 32.

def potencia (base, exp = 2):
    return base ** exp

# Escribe agregar(elemento, lista=None) que añada el elemento a la lista y la devuelva. Si no se pasa lista, debe crear una nueva en cada llamada. Prueba que agregar(1) y luego agregar(2) devuelven [1] y [2].
def agregar(elemento, lista=None):
    lista = []
    lista.append(elemento)
    return lista

# Escribe maximo(*numeros) que devuelva el mayor sin usar max(). Si no se pasa nada, que devuelva None.
def maximo(*numeros):
    mayor = numeros[0]
    for numero in numeros:
        if numero >= mayor: 
            mayor = numero
        else:
            continue
    return mayor

# Escribe unir(separador, *palabras) tal que unir("-", "a", "b", "c") devuelva "a-b-c".
def unir(separador, *palabras):
    resultado = ""
    for palabra in palabras:
        if resultado == "":
            resultado += f"{palabra}"
        else:
            resultado += (f"{separador}{palabra}")
    return resultado
print(unir(",", "a", "b", "c"))
# def unir(separador, *palabras):
    # return separador.join(palabras)

# Escribe describir(**datos) que imprima una línea clave: valor por cada dato. Prueba con describir(nombre="Ana", edad=20).
def describir(**datos):
    resultado = ""
    for clave, dato in datos.items():
        resultado += f"{clave}: {dato}\n"
    return resultado
# print(describir(nombre="Ana", edad=20))


# Escribe crear_usuario(nombre, rol="user", **extra) que devuelva un diccionario con nombre, rol y todo lo de extra. Prueba con crear_usuario("Ana", ciudad="BCN", activo=True).
def crear_usuario(nombre, rol="user", **extra):
    resultado = {}
    resultado["nombre"] = nombre
    resultado["rol"] = rol
    for clave, valor in extra.items():
        resultado[clave] = valor
    return resultado

# print(crear_usuario("Ana", ciudad="BCN", activo=True))
    
# Dada def area(base, altura): return base * altura / 2, llámala con datos = {"base": 4, "altura": 3} usando **, y con valores = [4, 3] usando *.

def area(base, altura): 
    return base * altura / 2

datos = {"base": 4, "altura": 3} 
valores = [4, 3]

# print(area(*valores))

# Escribe registrar(mensaje, *etiquetas, nivel="info", **meta) que devuelva un diccionario con las cuatro cosas. Llámala con registrar("hola", "a", "b", nivel="warn", usuario="Ana").

def registrar(mensaje, *etiquetas, nivel="info", **meta):

    return {"mensaje":mensaje, "nivel": nivel, **meta, "etiquetas": etiquetas}

print(registrar("hola", "a", "b", nivel="warn", usuario="Ana"))