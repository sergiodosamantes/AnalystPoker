import json
import os

# Cargar los rangos al iniciar el módulo
RUTA_RANGOS = os.path.join(os.path.dirname(__file__), "rangos_gto.json")
with open(RUTA_RANGOS, "r") as f:
    RANGOS = json.load(f)

# Orden de fuerza de cartas para comparación
VALORES_ORDENADOS = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10,
                     "9": 9, "8": 8, "7": 7, "6": 6,
                     "5": 5, "4": 4, "3": 3, "2": 2}

def analizar_preflop(c1, s1, c2, s2, posicion, jugadores, subida_previa):
    # Determinar si es pareja o suited
    es_pareja = (c1 == c2)
    suited = (s1 == s2)

    # Ordenar cartas por valor real para estandarizar la representación
    if VALORES_ORDENADOS[c1] > VALORES_ORDENADOS[c2]:
        high, low = c1, c2
    elif VALORES_ORDENADOS[c1] < VALORES_ORDENADOS[c2]:
        high, low = c2, c1
    else:
        # Si es pareja, da igual el orden
        high, low = c1, c2

    # Construir la notación de la mano: pareja (ej: "AA"), suited (ej: "AKs"), offsuit (ej: "AKo")
    if es_pareja:
        mano = high + low  # ej. "AA"
    else:
        mano = high + low + ("s" if suited else "o")

    # Obtener rango para la posición
    rango = set(RANGOS.get(posicion.upper(), []))

    # Verificar si la mano está dentro del rango
    if mano in rango:
        return "Call o 3-Bet" if subida_previa else "Raise (Open)"
    else:
        return "Fold (vs subida)" if subida_previa else "Fold"
