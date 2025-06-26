import streamlit as st
from backend.preflop import analizar_preflop
from backend.postflop import analizar_postflop

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



####################### --- Análisis Postflop ---
st.title("🃏 Evaluador Postflop de Póker")


st.subheader("🔀 Flop")
flop_col1, flop_col2, flop_col3 = st.columns(3)
with flop_col1:
    flop1 = st.selectbox("Carta 1", cartas, key="flop1")
    palo_flop1 = st.selectbox("Palo 1", palos, key="palo_flop1")
with flop_col2:
    flop2 = st.selectbox("Carta 2", cartas, key="flop2")
    palo_flop2 = st.selectbox("Palo 2", palos, key="palo_flop2")
with flop_col3:
    flop3 = st.selectbox("Carta 3", cartas, key="flop3")
    palo_flop3 = st.selectbox("Palo 3", palos, key="palo_flop3")

if st.button("Analizar Postflop"):
    flop = [(flop1, palo_flop1), (flop2, palo_flop2), (flop3, palo_flop3)]

    resultado = analizar_postflop(carta1, palo1, carta2, palo2, flop, jugadores)
    st.write(f"🃏 Mano: {resultado['mano']}")
    st.write(f"📊 Probabilidad de ganar: **{resultado['probabilidad']}%**")
    st.success(f"✅ Recomendación: {resultado['recomendacion']}")