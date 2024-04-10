import unittest

def contador_vocales(palabra):
    palabra = palabra.lower
    vocales = ("a", "e", "i", "o", "u")
    resultado = {}
    for letra in palabra:
        if letra in vocales:      
            if letra in resultado.keys():
                resultado [letra] += 1
            else:
                resultado[letra] = 1
            
    return resultado
   
def vocal_counter(word: str) -> dict:
    vocales = {}
    for letter in word:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            vocales[letter] = 1 + vocales.get(letter, 0)
    return vocales

def vocal_counter_des(word: str):
    resultado = vocal_counter(word)
    return \
        resultado.get('a', 0), \
        resultado.get('e', 0), \
        resultado.get('i', 0), \
        resultado.get('o', 0), \
        resultado.get('u', 0)
