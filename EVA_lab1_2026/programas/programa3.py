# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1

def programa3(RutaFactura):

    texto = programa1(RutaFactura)

    patron = r'(\d+)\s+([^\n]+?)\s+(\d+,\d{2})\s+(\d+,\d{2})'
    coincidencias = re.findall(patron, texto)

    res = ""
    for cant, desc, precio, total in coincidencias:
        res += f"Cant: {cant} |Desc: {desc} | {precio} c/u |Total:  {total}\n"
    return res

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)

    ret = programa3(entrada)      # ejecutar

    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
