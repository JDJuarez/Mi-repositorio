
municipios = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}

print(municipios)

#Longitud
print(len(municipios))

#Tipo de estructura
print(type(municipios),'\n')

#Para pasar por cada elemento del conjunto
for m in municipios:
    print('Tuvives en ',m,'\n')

#Si Zacatecas en el conjunto municipios
print('Zacatecas' in municipios)

#Añadir un municipio / elemento
municipios.add('Teul')

#Añadir 3 elementos al conjunto
otros = ('Luis Moya', 'Ojocaliente', 'Tepetongo')
municipios.update(otros)
print(municipios, len(municipios), '\n')

#Eliminar algun elemento del conjunto
municipios.remove('Zacatecas')
print(municipios, len(municipios), '\n')

#Eliminar otro municipio Ojocaliente
municipios.discard('Ojocaliente')
print(municipios, len(municipios), '\n')

#Quitar elemento de la izquierda (pop)
municipios.pop()
print(municipios, len(municipios), '\n')

#Eliminar todos
municipios.clear()
print(municipios, len(municipios), '\n')