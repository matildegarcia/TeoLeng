# -*- coding: utf-8 -*-
import re
import sys

def programa3(RutaFactura):
    
    '''
    SU CÓDIGO
    
    
    '''
    
    res=f"Cant: 10 |Desc: PRUEBA | 10,10 c/u |Total: 101\n"
    
    
    return res

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)    
 
    ret = programa3(entrada)      # ejecutar 
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
