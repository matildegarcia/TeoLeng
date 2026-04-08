# -*- coding: utf-8 -*-
import re
import sys

def programa4(RutaXML):
    '''
    SU CÓDIGO
    '''
    text = ""
    return text
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa4(entrada)      # ejecutar 
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
