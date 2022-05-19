#1) Crear una lista que contenga nombres de ciudades del mundo que 
# contenga más de 5 elementos e imprimir por pantalla

lista_ciudades=['Montreal','Nueva York','Monterrey','Caracas','Buenos Aires']
print(lista_ciudades)

#2) Imprimir por pantalla el segundo elemento de la lista

print(lista_ciudades[1])

#3) Imprimir por pantalla del segundo al cuarto elemento

print(lista_ciudades[1:4])

#4) Visualizar el tipo de dato de la lista

print(type(lista_ciudades))

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica,.
#   es decir, sin explicitar la posición del último elemento

print(lista_ciudades[2:])

#6) Visualizar los primeros 4 elementos de la lista

print(lista_ciudades[:4])

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

lista_ciudades.append('Caracas')
lista_ciudades.append('Monterrey')

print(lista_ciudades)

#8) Agregar otra ciudad, pero en la cuarta posición

lista_ciudades.insert(3,'Santiago')
print(lista_ciudades)

#9) Concatenar otra lista a la ya creada

lista_ciudades.extend(['Tegucigalpa','kito'])
print(lista_ciudades)

#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. 
# ¿Se nota alguna particularidad?

print(lista_ciudades.index('Monterrey'))
#Detecta la primera aparicion en la lista para arrojar el resultado de posicion

#11) ¿Qué pasa si se busca un elemento que no existe?.
#lista_ciudades.index('Puebla')
#Error

#12) Eliminar un elemento de la lista
print(lista_ciudades)
lista_ciudades.remove('Monterrey')
print(lista_ciudades)

#13) ¿Qué pasa si el elemento a eliminar no existe?
#lista_ciudades.remove('Queretaro')
#Error

#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
last=lista_ciudades.pop()
print(last)

#15) Mostrar la lista multiplicada por 4
print(lista_ciudades*4)

#16) Crear una tupla que contenga los números enteros del 1 al 20

tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(tupla)
print(type(tupla))

#17) Imprimir desde el índice 10 al 15 de la tupla

print(tupla[9:15])

#18) Evaluar si los números 20 y 30 están dentro de la tupla

print(20 in tupla)
print(30 in tupla)

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' 
# y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

ciudad='Paris'
if not ciudad in lista_ciudades:
    lista_ciudades.append('Paris')
    print('La ciudad se agrego con exito')
    print(lista_ciudades)
else:
    print('La ciudad ya existe')
    print(lista_ciudades)
 

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de 
# la tupla y de la lista

print(lista_ciudades.count('Monterrey'))
print(tupla.count(10))

#21) Convertir la tupla en una lista

lista=list(tupla)
print(type(lista))
print(lista[:])

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

nueva_tupla='1', '2', '3', '4', '5', '6'
primero,segundo,tercero,cuarto,quinto,sexto=nueva_tupla
print('El primer valor es',primero)
print('El segundo valor es',segundo)
print('El tercer valor es',tercero)

#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave
#  "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

diccionario={'Ciudades':[lista_ciudades],
'Pais':['Canada','USA','Chile','Venezuela','Argentina','Venezuela','Mexico','Honduras','Francia'],
'Continente':['America','America','America','America','America','America','America','America','America',]}
print(diccionario)
#24) Imprimir las claves del diccionario
print(diccionario.keys())

#25) Imprimir las ciudades a través de su clave
print(diccionario['Ciudades'])




