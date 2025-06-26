# tests/test_cases.py

import pytest
from backend.preflop import analizar_preflop
from backend.postflop import analizar_postflop

def test_analizar_preflop_raise():
    resultado = analizar_preflop("A", "♠", "K", "♠", "BTN", 6, subida_previa=False)
    assert resultado in ["Raise (Open)", "Call o 3-Bet", "Fold"]

def test_analizar_preflop_fold():
    resultado = analizar_preflop("2", "♠", "7", "♣", "UTG", 6, subida_previa=True)
    assert resultado in ["Fold", "Fold (vs subida)"]

def test_analizar_postflop_retorna_dict():
    flop = [("A", "♠"), ("K", "♥"), ("Q", "♦")]
    resultado = analizar_postflop("A", "♠", "K", "♣", flop, jugadores=6, simulaciones=100)
    assert isinstance(resultado, dict)
    assert "mano" in resultado
    assert "probabilidad" in resultado
    assert "recomendacion" in resultado
