# -*- coding: utf-8 -*-
import re
import sys
from pypdf import PdfReader

def programa1(RutaPdf):
    reader = PdfReader(RutaPdf)
    page = reader.pages[0]
    text = page.extract_text()
    return text


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)

    ret = programa1(entrada)      # ejecutar

    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
