#QUINTA CLASE
#Un diccionario es una colección de elementos (par llave:valor) que no posee orden.
#Para acceder al valor asociado a cada elemento se debe usar la llave, las llaves son UNIC.

#1 Como crear diccionarios
dicc1 = {}
dicc2 = dict()
dicc3 = {'a':1,'b':2,'c':3}
dicc3['Juan'] = 10

dicc3['a']

dicc3

len(dicc3)

dicc3[65]=70

dicc3

dicc3[('f','o')]='hola'

dicc3
#Las claves no pueden ser lista, solo tuplas, numeros enteros o strings.

#2 Agregar elementos a un diccionario:
d = {}
d['a'] = 5
d['x'] = 12
d['m'] = 8
d

d['f'] = 5
d['x'] = -10

#3 Operaciones so.bre diccionarios:
patas = {'humano':2, 'pulpo':8, 'perro':4, 'gato':4, 'cienpies':100}
list(patas)

#4 Verificar si existe un espcifico key o value en el diccionario:
'perro' in patas #Pregunta implicitamente por las llaves
'perro' in patas.keys() #Pregunta explicitamente por las llaves

8 in patas  #Pregunta si 8 es una llave presente en patas
8 in patas.values() #Pregunta explicitamente si 8 esta presente en values de patas

del patas['pulpo'] #Eliminar el key: pulpo junto a su value del diccionario
patas

#4.1 Ejemplo propio

UCL_campeones = {
    '2017':'Real Madrid',
    '2018':'Real Madrid',
    '2019':'Liverpool',
    '2020':'Bayern Munich',
    '2021':'Chelsea'
}
UCL_campeones['2022'] = 'Real Madrid' #Agregar un elemento (par llave-valor)
del UCL_campeones['2017'] #Eliminar una elemento
2016 in UCL_campeones #Verifica si la llave 2016 esta en el diccionario
len(UCL_campeones) #Imprime cuantos elementos posee el diccionario

capitales = {'Chile':'Santiago',
             'Peru':'Lima',
             'Ecuador':'Quito'}

#Metodos en los diccionarios
capitales.items() #Entrega lista de tuplas en donde cada una es del tipo (key, value)
list(capitales.items()) #Convierte a una lista las tuplas creadas por .items()
capitales.keys() #Entrega una lista de llaves del diccionario
capitales.values() # Entrega una lista de valores del diccionario

#5 Recorrer diccionarios:
# Usando for
for llave in capitales:   #Se referirá solo a los keys preentes en el diccionario
    print('p= ', llave)

for pais in capitales: #Recorre implicitamente todas las llaves del diccionario
    print('La capital de ', pais, 'es: ', capitales[pais])

for capitales in capitales.values: #Recorre todos los values en el diccionario
    print(capitales, ' es una linda ciudad')

for pais, ciudad in capitales.items(): #Recorre pares llave,valor en el diccionario capitales
    print('La capital de ', pais, 'es', ciudad)

#5.1 Ejemplo propio
for llave in UCL_campeones:   #Se referirá solo a los keys preentes en el diccionario
    print('p= ', llave)

for año in UCL_campeones: #Recorre implicitamente todas las llaves del diccionario
    print('La version de la UCL del año ', año, 'la ganó: ', UCL_campeones[año])

for ganador in UCL_campeones.values: #Recorre todos los values en el diccionario
    print(ganador, ' ganó la UCL')

for año, ganador in UCL_campeones.items(): #Recorre pares llave,valor en el diccionario capitales
    print('La version de la UCL del año ', año, 'la ganó', ganador)


#Conjuntos
#Coleccion de valores que no tiene orden y no acepta repeticiones

colores = {'rojo','gris','azul','gris'}
print(colores)

set('abracadabra')

#6 Crear, agregar y eliminar elementos de un conjunto
a=set()
a.add(19)
a.add(12)
a.add(8)
a.add(12)
print(a)
a.remove(19)
print(a)

#7 Verificar si un elemento esta presente en el conjunto
12 in a

len(a)

#7.1 Ejemplo propio
Top_3_70s_actors = {'Bruce Lee', 'Jackie Chan', 'Chuck Norris'}
Top_3_80s_actors = {'Jackie Chan', 'Silvester Stallone', 'Jean Claude Van Damme'}
Top_3_90s_actors = {'Jean Claude Van Damme', 'Dolph Lundgreen', 'Jackie Chan'}

Top_3_00s_actors = set()
Top_3_00s_actors.add('Yuri Boyka')
Top_3_00s_actors.add('Marko Zaror')
Top_3_00s_actors.add('Michael Gray')
Top_3_00s_actors.add('Jackie Chan')
Top_3_00s_actors.remove('Michael Gray')
'Marko Zaror' in Top_3_00s_actors
len(Top_3_00s_actors)

#8 Operaciones sobre conjuntos
#Podemos hacer uso de las operaciones matematicas que conocemos, tales como la union, interección, resta y subconjunto:
a={1,2,3,4}
b={2,4,6,8}

#Intersección:
a&b

#Union:
a|b

#Resta:
b-a

#Subconjunto:
{1,3}<{1,2,3}

#Trabajo en clases 1:
a = {5, 2, 3, 9, 4}
b = {3, 1}
c = {7, 5, 5, 1, 8, 6}
d = [6, 2, 4, 5, 5, 3, 1, 3, 7, 8]
e = {(2, 3), (3, 4), (4, 5)}
f = [{2, 3}, {3, 4}, {4, 5}]

#1
len(c) #Ya que un conjunto solo almacena elementos unicos el set c será de largo 5 al poseer los siguientes elemento: 1, 5, 6, 7 y 8.
#2
len(set(d)) #Al convertir la lista d a un conjunto este contendrá elementos del 1 al 8, por lo tanto largo 8.
#3
a & (b | c) #Primero la union bc da como resultado: 1,3,5,6,7,8, ahora su intersección con a resulta: 3 y 5.
#4
(a & b) | c #Primero la intersección ab da como resultado: 3 y su unión con c resulta: 1,3,5,6,7,8
#5
c - a #Al conjunto c le quitamos los elementos presentes en a resultando: 1,6,7,8
#6
max(e) #Comparación de tuplas, se ve el primer elemento mayor en cada tupla resultando: (4,5)
#7
f[0] < a #f[0] es el conjunto {2,3} el cual si es un subconjunto de a.

#Trabajo en clases 2:
paises = {
        'Juan': {'Chile', 'Argentina'},
        'Pedro': {'Francia', 'Suiza', 'Chile'},
        'Diego': {'Chile', 'Italia', 'Francia', 'Peru'}
}

def cuantos_en_comun(a,b):
    return len(paises[a]&paises[b])

print(cuantos_en_comun('Juan', 'Pedro'))


def paises_visitados_en_comun(a,b):
    return paises[a]&paises[b]

print(paises_visitados_en_comun('Juan', 'Pedro'))
