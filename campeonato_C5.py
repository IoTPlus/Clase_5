resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}


#Ejercicio en clases 2:
def obtener_lista_equipos(resultados):
	paises = {}
	for i in list(resultados.keys()):
		paises[i[0]] = 1
		paises[i[1]] = 1

	return list(paises)

print(obtener_lista_equipos(resultados))

def calcular_puntos(pais, resultados):
	puntaje_por_paises = {'Honduras': 0, 'Chile': 0, 'Espana': 0, 'Suiza': 0}
	for partido, marcador in resultados.items():
		if marcador[0] < marcador[1]:
			puntaje_por_paises[partido[0]] = puntaje_por_paises[partido[0]] + 0
			puntaje_por_paises[partido[1]] = puntaje_por_paises[partido[1]] + 3
		elif marcador[0] > marcador[1]:
			puntaje_por_paises[partido[0]] = puntaje_por_paises[partido[0]] + 3
			puntaje_por_paises[partido[1]] = puntaje_por_paises[partido[1]] + 0
		else:
			puntaje_por_paises[partido[0]] = puntaje_por_paises[partido[0]] + 1
			puntaje_por_paises[partido[1]] = puntaje_por_paises[partido[1]] + 1

	return puntaje_por_paises[pais]

print(calcular_puntos('Chile', resultados))


#Ejercicio extra 1 (Calcular diferencia de goles del país ingresado):
def calcular_diferencia_de_goles(pais, resultados):
	diff_goles_por_paises = {'Honduras': 0, 'Chile': 0, 'Espana': 0, 'Suiza': 0}
	for partido, marcador in resultados.items():
		diff_goles_por_paises[partido[0]] = diff_goles_por_paises[partido[0]] + marcador[0] - marcador[1]
		diff_goles_por_paises[partido[1]] = diff_goles_por_paises[partido[1]] + marcador[1] - marcador[0]

	return diff_goles_por_paises[pais]

print(calcular_diferencia_de_goles('Chile', resultados))

#Ejercicio extra 2 (Ordenar países por puntaje, diff de goles y goles anotados):
def posiciones(resultados):
	# Diccionario con puntajes:
	puntaje_por_paises = {'Honduras': 0, 'Chile': 0, 'Espana': 0, 'Suiza': 0}
	for partido, marcador in resultados.items():
		if marcador[0] < marcador[1]:
			puntaje_por_paises[partido[0]] = puntaje_por_paises[partido[0]] + 0
			puntaje_por_paises[partido[1]] = puntaje_por_paises[partido[1]] + 3
		elif marcador[0] > marcador[1]:
			puntaje_por_paises[partido[0]] = puntaje_por_paises[partido[0]] + 3
			puntaje_por_paises[partido[1]] = puntaje_por_paises[partido[1]] + 0
		else:
			puntaje_por_paises[partido[0]] = puntaje_por_paises[partido[0]] + 1
			puntaje_por_paises[partido[1]] = puntaje_por_paises[partido[1]] + 1

	#print(puntaje_por_paises)
	# Diccionario con diferencia de goles:
	diff_goles_por_paises = {'Honduras': 0, 'Chile': 0, 'Espana': 0, 'Suiza': 0}
	for partido, marcador in resultados.items():
		diff_goles_por_paises[partido[0]] = diff_goles_por_paises[partido[0]] + marcador[0] - marcador[1]
		diff_goles_por_paises[partido[1]] = diff_goles_por_paises[partido[1]] + marcador[1] - marcador[0]

	#print(diff_goles_por_paises)
	# Diccionario con golpes anotados:
	goles_por_paises = {'Honduras': 0, 'Chile': 0, 'Espana': 0, 'Suiza': 0}
	for partido, marcador in resultados.items():
		goles_por_paises[partido[0]] = goles_por_paises[partido[0]] + marcador[0]
		goles_por_paises[partido[1]] = goles_por_paises[partido[1]] + marcador[1]

	#print(goles_por_paises)
	# Ordenar por puntaje:
	tabla_equipos = list(range(0, len(obtener_lista_equipos(resultados))))
	puntos_ordenados = list(set(list(puntaje_por_paises.values())))
	puntos_ordenados
	k = -1
	for i in puntos_ordenados:
		for pais in puntaje_por_paises.keys():
			if puntaje_por_paises[pais] == i:
				tabla_equipos[k] = pais
				k = k - 1
		i += 1

	#print(tabla_equipos)
	# Puntajes duplicados:
	puntajes = list(puntaje_por_paises.values())
	dup_list = []
	new_list = []
	for i in puntajes:
		if i not in new_list:
			new_list.append(i)
		else:
			dup_list.append(i)

	#print(dup_list[0])
	# Obtener paises con mismo puntaje:
	mismo_puntaje = []
	for pais, puntaje in puntaje_por_paises.items():
		if puntaje == dup_list[0]:
			mismo_puntaje.append(pais)

	#print(mismo_puntaje)
	# Ordenar por diferencia de goles a los equipos con mismo puntaje:
	head_of_table = min([tabla_equipos.index(mismo_puntaje[0]), tabla_equipos.index(mismo_puntaje[1])])
	i = 0
	if diff_goles_por_paises[mismo_puntaje[i]] > diff_goles_por_paises[mismo_puntaje[i + 1]]:
		tabla_equipos[head_of_table] = mismo_puntaje[i]
		tabla_equipos[head_of_table + 1] = mismo_puntaje[i + 1]
	else:
		tabla_equipos[head_of_table] = mismo_puntaje[i + 1]
		tabla_equipos[head_of_table + 1] = mismo_puntaje[i]
	i += 1

	return tabla_equipos

print(posiciones(resultados))