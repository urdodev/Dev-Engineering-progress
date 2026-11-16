# Escribe a_entero(texto) que devuelva int(texto), o None si el texto no es un número. Prueba con "42", "abc" y "".
def a_entero(texto):
    try:
        entero = int(texto)
    except ValueError:
        return None
    else:
        return entero
# print(a_entero("Hola"))


# Escribe dividir(a, b) que devuelva a / b. Si b es 0, que imprima un aviso y devuelva None. Captura la excepción específica, no un except: vacío.

def dividir(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return None
    else:
        return division

# print(round(dividir(5, 3), 2))

# Escribe obtener(diccionario, clave) que devuelva el valor de la clave, o "no existe" si no está, usando try/except KeyError (no .get()).
def obtener(dict, clave):
    try:
        return dict[clave]
    except KeyError:
        print("No existe la clave")
        return None
    
tienda = {"pan": 1.2, "leche": 0.9}
# print(obtener(tienda, "pan"))     # 1.2
# print(obtener(tienda, "queso")) 


# Escribe elemento_dividido(lista, i, divisor) que devuelva lista[i] / divisor. Debe manejar por separado IndexError, ZeroDivisionError y TypeError, con un mensaje distinto para cada uno. Prueba con ([10, 20], 5, 2), ([10, 20], 0, 0) y ([10, 20], 0, "a").
def elemento_dividido(lista, i, divisor):
    try:
        return lista[i] / divisor
    except Exception as e: # mejor por separado.
        print(e)
# print(elemento_dividido([10, 20], 0, "a"))
# Escribe leer_numero(texto) que haga int(texto) dentro de un try, imprima "Convertido: ..." en el else y "Fin" en el finally. Pruébalo con "7" y con "x" y comprueba en qué orden salen los mensajes.
def leer_numero(texto):
    try:
        entero = int(texto)
    except ValueError:
        print("Asegurese de poner un numero!")
    else:
        print(f"Convertido: {entero}")
    finally:
        print("Fin")
# print(leer_numero("HOla"))

# Sin ejecutarlo, predice la salida y explica por qué:
# python
def f():
    try:
        return "try"
    finally:
        print("finally")

# print(f())
#imprimira try y seguidamente finally, ya que la funcion devolvera try en el try: y como finally siempre se ejecuta luego imrpimara finally



# Escribe set_edad(edad) que lance ValueError("La edad no puede ser negativa") si edad < 0 y TypeError("La edad debe ser un entero") si no es int. Si es válida, la devuelve.
def set_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("Debe ser un entero!")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa!")
    return edad
# print(set_edad("15"))

# Llama a set_edad(-5) dentro de un try/except y muestra solo el mensaje del error usando as e.
# try:
#     set_edad(-5)
# except Exception as e:
#     print(e)
# finally:
#     print("Do some cleanup here!")

# Crea la excepción SaldoInsuficiente y la función retirar(saldo, cantidad) que la lance si cantidad > saldo, con un mensaje que diga cuánto falta. Si no, devuelve el saldo restante.
class SaldoInsuficiente(Exception): #Crea una excepcion
    pass
def retirar(saldo, cantidad):
    if cantidad > saldo:
        raise SaldoInsuficiente("No hay saldo suficiente")
    else:
        print(f"Cantidad retirada: {cantidad}")
# Captura SaldoInsuficiente al llamar a retirar(50, 80) e imprime el mensaje.
try:
    retirar(50, 80)
except SaldoInsuficiente as e:
    print(e)
# Reto final

# Escribe procesar_lista(datos) que reciba ["10", "abc", "5", "", "7"] y devuelva la suma de los números válidos, además de la lista de los valores que dieron error. Debe devolver ambas cosas a la vez. Resultado esperado: (22, ['abc', '']).

def procesar_lista(datos):
    lst_error = []
    lst_valida = []
    for dato in datos:
        try:
            dato_int = int(dato)
        except ValueError:
            lst_error.append(dato)
        else:
            lst_valida.append(dato_int)

    return sum(lst_valida), lst_error

print(procesar_lista(["10", "abc", "5", "", "7"]))