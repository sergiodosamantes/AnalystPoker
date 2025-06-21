# backend/postflop.py
from treys import Card, Evaluator, Deck
import random

VALORES = {'A': 'A', 'K': 'K', 'Q': 'Q', 'J': 'J', 'T': 'T',
           '9': '9', '8': '8', '7': '7', '6': '6',
           '5': '5', '4': '4', '3': '3', '2': '2'}
PALOS = {'♠': 's', '♥': 'h', '♦': 'd', '♣': 'c'}

def traducir_carta(valor, palo):
    return Card.new(VALORES[valor] + PALOS[palo])

def analizar_postflop(c1, s1, c2, s2, flop, jugadores=6, simulaciones=1000):
    evaluator = Evaluator()
    mano = [traducir_carta(c1, s1), traducir_carta(c2, s2)]
    flop_cards = [traducir_carta(c, s) for c, s in flop]

    victorias = 0

    for _ in range(simulaciones):
        mazo = Deck()
        # Remover nuestras cartas y el flop del mazo
        usados = mano + flop_cards
        mazo.cards = [c for c in mazo.cards if c not in usados]
        random.shuffle(mazo.cards)

        # Simular turn y river
        board = flop_cards + [mazo.draw(1)[0], mazo.draw(1)[0]]
        score_jugador = evaluator.evaluate(board, mano)

        gana = True
        for _ in range(jugadores - 1):
            mano_rival = [mazo.draw(1)[0], mazo.draw(1)[0]]
            score_rival = evaluator.evaluate(board, mano_rival)
            if score_rival <= score_jugador:
                gana = False
                break

        if gana:
            victorias += 1

    probabilidad = round((victorias / simulaciones) * 100, 2)
    nombre_mano = evaluator.class_to_string(evaluator.get_rank_class(evaluator.evaluate(flop_cards, mano)))

    if probabilidad >= 70:
        recomendacion = "Apostar fuerte o hacer raise"
    elif probabilidad >= 40:
        recomendacion = "Seguir o hacer una apuesta pequeña"
    else:
        recomendacion = "Considerar hacer fold"

    return {
        "mano": nombre_mano,
        "probabilidad": probabilidad,
        "recomendacion": recomendacion
    }
