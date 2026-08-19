"""
Funciones auxiliares compartidas entre los nodos de la capsula.

Se separan aqui para mostrar que un paquete de ROS 2 puede tener varios
modulos de Python, no solo los nodos ejecutables.
"""

import math


def distancia_en_angulo(msg, angulo_grados, ventana_grados=10.0):
    """
    Devuelve la distancia minima medida por el LiDAR alrededor de un angulo.

    El mensaje sensor_msgs/LaserScan trae un arreglo 'ranges' donde cada
    elemento es una medicion a un angulo distinto. En lugar de asumir que
    ranges[0] es el frente (lo cual depende del robot), calculamos el indice
    a partir de angle_min y angle_increment. Asi el codigo funciona con
    cualquier LiDAR.

    Parametros
    ----------
    msg : sensor_msgs.msg.LaserScan
        El mensaje recibido del topico /scan.
    angulo_grados : float
        Angulo a consultar en grados. 0 = al frente, 90 = izquierda,
        -90 (o 270) = derecha.
    ventana_grados : float
        Ancho del sector a promediar. Tomar un sector en vez de un solo rayo
        evita que un dato ruidoso arruine la lectura.

    Retorna
    -------
    float
        Distancia minima valida en metros, o float('inf') si no hay
        mediciones validas en ese sector.
    """
    angulo_rad = math.radians(angulo_grados)
    ventana_rad = math.radians(ventana_grados)

    total = len(msg.ranges)
    if total == 0 or msg.angle_increment == 0.0:
        return float('inf')

    def indice_de(angulo):
        # Convertimos un angulo en radianes al indice correspondiente
        # dentro del arreglo 'ranges'.
        idx = int(round((angulo - msg.angle_min) / msg.angle_increment))
        return idx % total  # el modulo maneja el "envolvimiento" a 360 grados

    idx_inicio = indice_de(angulo_rad - ventana_rad / 2.0)
    idx_fin = indice_de(angulo_rad + ventana_rad / 2.0)

    # Recolectamos los indices del sector, cuidando el caso en que el sector
    # cruza el final del arreglo (por ejemplo, de 355 a 5 grados).
    if idx_inicio <= idx_fin:
        indices = range(idx_inicio, idx_fin + 1)
    else:
        indices = list(range(idx_inicio, total)) + list(range(0, idx_fin + 1))

    validas = []
    for i in indices:
        r = msg.ranges[i]
        # El LiDAR reporta inf o nan cuando no detecta nada, y valores fuera
        # de [range_min, range_max] no son confiables.
        if math.isinf(r) or math.isnan(r):
            continue
        if r < msg.range_min or r > msg.range_max:
            continue
        validas.append(r)

    if not validas:
        return float('inf')

    return min(validas)


def formatear_distancia(valor):
    """Convierte una distancia a texto legible para imprimir en consola."""
    if math.isinf(valor):
        return '  ---  '
    return f'{valor:6.2f}m'
