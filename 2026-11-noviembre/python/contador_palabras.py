"""
Ejercicio 01 · contador_palabras.py
Enunciado: Recibe la ruta de un .txt, cuenta cuántas veces aparece cada palabra (sin distinguir
mayúsculas ni puntuación) y muestra las 10 más frecuentes. Guarda el resultado completo en
resultado.json.
• Funciones separadas: limpiar(texto) devuelve una lista de palabras y contar(palabras) devuelve un
diccionario.
• Cuenta primero a mano con un dict y después compara con collections.Counter.
• Ignora una lista de stopwords (el, la, de, que, y, a, en...).
• Si el archivo no existe, muestra un mensaje claro (FileNotFoundError) sin traceback.
• Prueba con un capítulo de un libro de dominio público del Proyecto Gutenberg.
Reto extra: pasa el número de palabras a mostrar como argumento (--top 20).
Practicas: str.lower, split, dict, sorted con key, open, json.dump.
"""
import string
from collections import Counter

def limpiar(texto_sin_limpiar):
    lista_palabras = []
    texto_procesado = texto_sin_limpiar.split()
    for i in texto_procesado:
        palabra = i.lower().strip(string.punctuation)
        lista_palabras.append(palabra)
    return lista_palabras

def contar_palabras(lista_palabras):
    stopwords = ("el", "la", "de", "que", "y", "a", "en")
    num_palabras = {}
    for palabra in lista_palabras:
        if palabra not in num_palabras and palabra not in stopwords:
            num_palabras[palabra] = 1
        elif palabra in stopwords:
            continue
        else:
            num_palabras[palabra] += 1
    return num_palabras

def contar_palabras_counter(lista_palabras):
    conteo = Counter(lista_palabras)
    return conteo

print(contar_palabras(limpiar("Hola, y hola mundo")))
