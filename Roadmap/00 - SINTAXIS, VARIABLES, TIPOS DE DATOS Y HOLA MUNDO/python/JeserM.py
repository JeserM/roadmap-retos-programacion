# 00
"""SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */ """

# Comentario en una linea
# https://www.python.org/

"""
Esto es un comentario
en varias lineas
"""
'''
Esto tambien es un
comentario en varias
linea
'''

my_variable = "Mi variable"
my_variable = "Nuevo valor de mi variable"

# En python no hay constantes, todo puede variar. Pero se puede hacer lo siguiente
MY_CONSTANT = "Mi constante"
MY_CONSTANT = "Constante2"

# tipos de datos primitivos
my_int = 1  # Entero
my_float = 1.5  # Float
my_bool = True
my_bool = False
my_string = "Mi cadena de texto "
my_other_string = "Mi otra cadena de texto"

# Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print("¡Hola, Phyton!")

# Imprime tipo de dato
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))

# decir el tipo de dato
my_int: int = 1
