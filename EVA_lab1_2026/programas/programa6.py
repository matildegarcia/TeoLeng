# -*- coding: utf-8 -*-
import re
import sys
from programa2 import programa2
from programa4 import programa4

def programa6(RutaFactura, RutaXML):
    fecha, monto = programa2(RutaFactura)
    xml = programa4(RutaXML)

    #  no se encontraron datos coincidentes, se devuelve el XML sin modificaciones
    if not fecha or not monto:
        return xml

     #busca en el xml una linea que :
    patron = (
        r'(?m)^[ \t]*<BanTeng:Movimiento' # empiece con indentación + "<BanTeng:Movimiento"
        r'(?=[^/]*Importe="' + re.escape(monto) + r'")' # dentro del mismo tag tenga el monto buscado
        r'(?=[^/]*Fecha="' + re.escape(fecha) + r'")'    # dentro del mismo tag tenga la fecha buscada
        r'[^/]*/>' # termine con "/>"
        r'[ \t]*\r?\n' # y luego un salto de línea
    )

    xml_nuevo = re.sub(patron, '', xml)  # elimina la línea completa que coincide con el patrón

    # cuenta las lineas de contenido <BanTeng:Movimiento para actualizar el total de movimientos
    total = len(re.findall(r'<BanTeng:Movimiento\s', xml_nuevo))

    # actualiza TotalMovimientos
    xml_nuevo = re.sub(
        r'<BanTeng:TotalMovimientos>\d+</BanTeng:TotalMovimientos>',
        f'<BanTeng:TotalMovimientos>{total}</BanTeng:TotalMovimientos>',
        xml_nuevo
    )

    return xml_nuevo

if __name__ == '__main__':
    entrada = sys.argv[1]      # ruta al PDF de la factura
    xml_entrada = sys.argv[2]  # ruta al XML del estado bancario
    salida = sys.argv[3]       # ruta al archivo de salida

    ret = programa6(entrada, xml_entrada)
    f = open(salida, 'w', encoding='utf-8')
    f.write(ret)
    f.close()
