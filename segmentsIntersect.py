# Función de dirección
def direction(pi, pj, pk):
    return (pk[0] - pi[0]) * (pj[1] - pi[1]) - (pj[0] - pi[0]) * (pk[1] - pi[1])

# Función para verificar si un punto está en un segmento
def on_segment(pi, pj, pk):
    if (min(pi[0], pj[0]) <= pk[0] <= max(pi[0], pj[0]) and
        min(pi[1], pj[1]) <= pk[1] <= max(pi[1], pj[1])):
        return True
    return False

# Función principal para verificar si dos segmentos se intersecan
def segmentos_intersecan(p1, p2, p3, p4):
    # Calcular las direcciones
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)

    # Verificar las condiciones del algoritmo
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and on_segment(p3, p4, p1):
        return True
    elif d2 == 0 and on_segment(p3, p4, p2):
        return True
    elif d3 == 0 and on_segment(p1, p2, p3):
        return True
    elif d4 == 0 and on_segment(p1, p2, p4):
        return True
    else:
        return False

# Puntos de ejemplo
P1 = (-1, 3)
P2 = (4, 5)
P3 = (0, 5)
P4 = (1, 1)
P5 = (-3, -2)
P6 = (-1, 1)
P7 = (-1, -1)
P8 = (3, 3)

# Verificar si los segmentos P1P2 y P3P4 se intersecan
print("Segmentos P1P2 y P3P4:", segmentos_intersecan(P1, P2, P3, P4))
print("Segmentos P5P6 y P7P8:", segmentos_intersecan(P5, P6, P7, P8))
print("Segmentos P3P4 y P7P8:", segmentos_intersecan(P3, P4, P7, P8))
print("Segmentos P1P7 y P5P6:", segmentos_intersecan(P1, P7, P5, P6))
print("Segmentos P1P2 y P7P8:", segmentos_intersecan(P1, P2, P7, P8))