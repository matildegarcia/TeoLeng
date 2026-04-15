# -*- coding: utf-8 -*-
import re
import sys

from programa2 import programa2
from programa4 import programa4

def programa5(RutaPdf,RutaXML):
    fecha, monto = programa2(RutaPdf)
    xml_text = programa4(RutaXML)

    pattern = (
        r'<BanTeng:Movimiento\b' # busco exactamente esa cadena y \b nos asegura que Movimiento termine como palabra completa
        r'(?=[^>]*\bFecha="' + re.escape(fecha) + r'")' # ?= lookahead positivo (mira hacia adelante sin consumir caracteres) y Fecha= busca ese Texto literal
        r'(?=[^>]*\bImporte="' + re.escape(monto) + r'")' # lo mismo aplica aqui con monto
        r'[^>]*/>'
    )

    resultado = re.search(pattern, xml_text) is not None #devuelve true si encuentra la ocurrencia o none en caso de no encontrarla

    if resultado:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa5(entrada_pdf,entrada_xml)      # ejecutar 
    if (ret):
        ret = "Encontrado"
    else:
        ret = "No encontrado"
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
