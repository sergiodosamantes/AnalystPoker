import streamlit as st
from backend.preflop import analizar_preflop

st.set_page_config(page_title="Poker Analyst", layout="centered")
st.title("🃏 Evaluador Preflop de Póker")

# --- Selección de cartas ---
st.subheader("Tus cartas")
palos = ["♠", "♥", "♦", "♣"]
cartas = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

c1, p1, c2, p2 = st.columns(4)
with c1:
    carta1 = st.selectbox("Carta 1", cartas, key="carta1")
with p1:
    palo1 = st.selectbox("Palo 1", palos, key="palo1")
with c2:
    carta2 = st.selectbox("Carta 2", cartas, key="carta2")
with p2:
    palo2 = st.selectbox("Palo 2", palos, key="palo2")

# --- Posición y configuración de la mesa ---
st.subheader("Configuración de la mano")

col_pos, col_jugadores = st.columns([2, 1])
with col_pos:
    posicion = st.radio(
        "Posición en la mesa",
        ["UTG", "MP", "CO", "BTN", "SB", "BB"],
        horizontal=True
    )
with col_jugadores:
    jugadores = st.slider("Jugadores activos", 2, 9, 6)

# --- Otros factores ---
subida_previa = st.checkbox("¿Hubo subida antes de ti?")


# --- Evaluación ---
if st.button("Evaluar Mano"):
    # Validar cartas duplicadas
    if (carta1 == carta2) and (palo1 == palo2):
        st.error("❌ No puedes tener dos cartas exactamente iguales (valor y palo).")
    else:
        accion = analizar_preflop(carta1, palo1, carta2, palo2, posicion, jugadores, subida_previa)
        st.success(f"Acción recomendada: **{accion}**")