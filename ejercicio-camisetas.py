dic_talla_precio={'S':2500,
'M':3400,
'L':5200,
'XL':6000,
'XXL':9000}
dic_ciudad_tallas={'Cartagena': ['M', 'S', 'L', 'L', 'L', 'L', 'L', 'XL', 'XXL', 'S', 'S', 'L', 'M', 'M', 'M', 'S', 'S', 'M', 'M'],
'Barranquilla': ['S', 'S', 'L', 'M', 'XL', 'S', 'L', 'M', 'M', 'M', 'S', 'S', 'M', 'M', 'XL', 'S', 'M', 'S', 'XXL', 'XL', 'L'],
'Medellín': ['L', 'L', 'XL', 'XXL', 'S', 'S', 'S', 'S', 'L', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'M', 'M', 'S', 'S', 'S', 'S', 'XL', 'L'],
'Bogotá': ['M', 'S', 'S', 'M', 'M', 'XL', 'S', 'M', 'S', 'S', 'S', 'L', 'S', 'S', 'S', 'M', 'M','M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL' ]}
#1. Diseña un programa que lea el diccionario - HECHO
#2. indique el total de ventas HECHO
#3. las tallas más vendidas HECHO
#4. el total de tallas por ciudad
print('==== Punto 2 ====')
#2. indique el total de ventas (VENTAS EN PESOS)
suma=0
for x in dic_ciudad_tallas:
  for y in dic_ciudad_tallas[x]:
    suma+=dic_talla_precio[y]
print('total de ventas:',suma)
print('==== Punto 3 ====')
#3. las tallas más vendidas
dic_cantidad_por_talla={'S':0,
'M':0,
'L':0,
'XL':0,
'XXL':0}
for x in dic_ciudad_tallas:
  for y in dic_ciudad_tallas[x]:
    dic_cantidad_por_talla[y]+=1
print(dic_cantidad_por_talla)
mayor=0
w=0
for z in dic_cantidad_por_talla:
  if dic_cantidad_por_talla[z]>mayor:
    mayor=dic_cantidad_por_talla[z]
    w=z
print(mayor)
print(w)
print(f'la talla {w} tiene {mayor} unidades vendidas')
print('== 4. el total de tallas por ciudad ==')
for ciudad in dic_ciudad_tallas:
  dic_cantidad_por_talla={'S':0,
  'M':0,
  'L':0,
  'XL':0,
  'XXL':0}
  for talla in dic_ciudad_tallas[ciudad]:
    dic_cantidad_por_talla[talla]+=1
  print(ciudad,dic_cantidad_por_talla)