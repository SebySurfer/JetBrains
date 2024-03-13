nombre = input("Ingresa tu nombre: ")
apellidos = input("Ingresa tus apellidos: ")
saludo = f"Hola {nombre} {apellidos}, bienvenid@."
print(saludo)

# Ejemplos con el método format
texto = "{} + {}"
print(texto.format(1, 2))
# Controlar la posición de los valores con índices
texto = "{1} + {0}"
print(texto.format(1, 2))
# usando argumentos
texto = "{apellido}, {nombre}"
print(texto.format(nombre="Joan", apellido="Sebastian"))
# impresión de valores decimales
texto = "{pi}"
print(texto.format(pi=3.14159265359))
# Impresión con un número fijo de decimales
texto = "{pi:.4f}"
print(texto.format(pi=3.14159265359))
# Aplicando notación científica formato E o e.
fuerza = 7500
area = 0.08 * 0.03
esfuerzo = fuerza / area
texto = "El esfuerzo normal es de {:E} Pa"
print(texto.format(esfuerzo))
# notación científica con control de decimales
fuerza = 7500
area = 0.08 * 0.03
esfuerzo = fuerza / area
texto = "El esfuerzo normal es de {:.2E} Pa"
print(texto.format(esfuerzo))
# Colocando porcentaje
print("{:.1%}".format(0.75))

# Ejemplos f-strings
# sustitución directa de la cadena de valor
a = 16
b = 20
print(f"{a} + {b} = {a + b}")

fuerza = 7500
area = 0.08 * 0.03
esfuerzo = fuerza / area
texto = f"El esfuerzo normal es de {esfuerzo:.2E} Pa"
print(texto)

# equivalencia en el sistema binario de un entero expresado en el sistema decimal
n = int(input("Inserta un entero: "))
print(f"El número {n} en binario es {bin(n)}")

# Otra manera de concatenar cadenas es utilizar el método join.
# Este método nos sirve para unir una lista de cadenas mediante un separador.
primer_nombre = "Ana"
segundo_nombre = "Isabel"
separador = " "
print(separador.join([primer_nombre, segundo_nombre]))
separador = "_-:"  # separador con espacio con 3 guiones medios
print(separador.join([primer_nombre, segundo_nombre]))
# La cantidad de cadenas a unir pueden ser más dos, observa el siguiente ejemplo
print(", ".join(["Ana", "Jorge", "David", "José", "Juan"]))
# Naturalmente, el separador puede ser cualquier caracter válido, #incluyendo algunos poco usuales.
print(" \U0001F970 ".join(["Ana", "Jorge", "David", "José", "Juan"]))

# Mayúsculas y minúsculas
# En Python las cadenas de caracteres disponen de los métodos upper y lower
# que nos permiten convertir en mayúsculas y minúsculas
frase = "La vida es demasiado bella cómo para sentarse a ver Netflix"
print(frase.upper())  # Convertir todo el texto en mayúsculas
print(frase.lower())  # Convertir todo el texto en minúsculas
# El método capitalize, permite colocar la primera letra en mayúsculas
# y todas las demás en minúsculas
otra = frase.upper()
print(otra)
print(otra.capitalize())

# Se define un valor alfanumérico a la variable nombre
nombre = "Anáhuac Mayab 2024"
# podemos acceder a cada elemento del texto
print(nombre[0])
print(nombre[2])
print(nombre[4])
print(nombre[6])
# podemos obtener el tamaño del texto
print("Tamaño del texto: ", len(nombre))
# podemos imprimir por separado los elementos del texto
for i in range(len(nombre)):
    print(nombre[i], end=" -")
print()
# la siguiente línea, nos permite tomar los elementos con indices 0, 1 y 2
print(nombre[0:3])
# Esta otra línea nos permite acceder a los elementos con indices 3, 4, 5 y 6
print(nombre[3:7])
# la siguiente línea toma los elementos desde el inicio de la cadena, hasta el indice 3
print(nombre[:4])
# Esta otra línea toma los elementos desde el índice 4 hasta el final de la cadena.
print(nombre[4:])
# De una cadena de caracteres se puede obtener un conjunto de elementos #sin tomarlos de uno en uno, sino cada dos, cada tres, etc.
# Si utilizamos la notación cadena[a:b:n], nos devolverá
# el conjunto de elementos comprendidos entre los índices a y (b-1), #tomados cada n elementos.
print(nombre[0:4:2])  # valores de 2 en 2
print(nombre[0:10:4])  # valores de 4 en 4
# Si quisiéramos tomar todos los elementos de una cadena de 2 en 2, #podríamos hacer lo siguiente:
print(nombre[::2])