#! /usr/bin/python

# este es el ejercicio 13.5

fd = open("/etc/passwd", "r")
lineas = fd.readlines()
diccionario={}
for linea in lineas:
	elementos = linea.split(":")
	user = elementos[0]
	shell = elementos[-1][:-1]
	diccionario[user]=shell
	
try:
	print 'root:', diccionario['root']
	print 'invisible:', diccionario['invisible']
except KeyError:
	print 'llave no encontrada en el diccionario'
	
fd.close
