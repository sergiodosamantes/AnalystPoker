import json
import os

# Cargar los rangos al iniciar el módulo
RUTA_RANGOS = os.path.join(os.path.dirname(__file__), "rangos_gto.json")
with open(RUTA_RANGOS, "r") as f:
    RANGOS = json.load(f)

def analizar_preflop(c1, s1, c2, s2, posicion, jugadores, en_boton, subida_previa):
    suited = s1 == s2
    mano_base = "".join(sorted([c1, c2], reverse=True))
    mano = f"{mano_base}{'s' if suited else 'o'}"

    # Si la mano aparece sin 's' ni 'o', es porque es pareja
    mano_sin_sufijo = mano_base if c1 == c2 else mano

    rango = set(RANGOS.get(posicion, []))

    if subida_previa:
        if mano_sin_sufijo in rango or mano in rango:
            return "Call o 3-Bet"
        else:
            return "Fold (vs subida)"
    else:
        if mano_sin_sufijo in rango or mano in rango:
            return "Raise (Open)"
        else:
            return "Fold"