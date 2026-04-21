# -*- coding: utf-8 -*-
from datetime import datetime
import re
import sys
from programa1 import programa1
def programa2(RutaFactura):
    text = programa1(RutaFactura)

    # Buscar la fecha y monto utilizando una expresión regular
    patronFecha = r'FECHA:\s*(?:\n*\s*)?(\d{2}[-/]\d{2}[-/]\d{4})'
    patronDebBancario = r'DÉBITO\s*BANCARIO\s*(?:\n*\s*)?(\d*,\d{2})' #Estuvo dificil, hay que mirar la salida del programa1 en salidas para entenderlo mejor

    fecha_match = re.search(patronFecha, text)
    monto_match = re.search(patronDebBancario, text)

    #Si no encuentra dichos patrones devuelve None, None
    if not fecha_match or not monto_match:
        return None, None

    fecha_str = fecha_match.group(1)
    monto_str = monto_match.group(1)

    # Normalizar separadores de fecha y convertir a formato YYYY-MM-DD
    fecha_str = fecha_str.replace('-', '/')
    date_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
    fecha_normalizada = date_obj.strftime("%Y-%m-%d")

    return fecha_normalizada, monto_str

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)

    fecha,monto = programa2(entrada)      # ejecutar
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
