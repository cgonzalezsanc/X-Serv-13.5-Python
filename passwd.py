#!usr/bin/python

fd = open('/etc/passwd', 'r')
lineas = fd.readlines()
fd.close
dicc = {}

for linea in lineas:
    linea_div = linea.split(':')
    username = linea_div[0]
    shell = linea_div[-1][:-1] #con esto quitamos el /n
    dicc[username] = shell
    
print dicc["root"]    
print "En esta maquina hay", len(dicc), "usuarios"

#para excepciones:
try:
    print dicc["imaginario"]
except KeyError:    #solo salta con errores KeyError
    print "Usuario imaginario no existe"
