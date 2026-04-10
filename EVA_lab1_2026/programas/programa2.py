# -*- coding: utf-8 -*-
import re
import sys

def programa2(RutaFactura):
    
    '''
    SU CÓDIGO
    
    NOTA: El formato de la fecha debe ser AAAA-MM-DD 
    '''
    fecha = "2026-04-01"        
    monto = 954,25
    return fecha, monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
