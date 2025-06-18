import streamlit as st
from backend.preflop import analizar_preflop

st.set_page_config(page_title="Poker Analyst", layout="centered")

st.title("🃏 Evaluador Preflop de Póker")

st.subheader("Tus cartas")
col1, col2 = st.columns(2)
palos = ["♠", "♥", "♦", "♣"]

with col1:
    carta1 = st.selectbox("Carta 1", ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
    palo1 = st.selectbox("Palo Carta 1", palos)
with col2:
    carta2 = st.selectbox("Carta 2", ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
    palo2 = st.selectbox("Palo Carta 2", palos)

st.subheader("Información de la mano")
posicion = st.selectbox("Posición", ["UTG", "MP", "CO", "BTN", "SB", "BB"])
jugadores = st.slider("Jugadores activos", 2, 9, 6)
en_boton = st.checkbox("¿Estás en el botón?", value=(posicion == "BTN"))
subida_previa = st.checkbox("¿Hubo subida antes de ti?")

if st.button("Evaluar Mano"):
    accion = analizar_preflop(carta1, palo1, carta2, palo2, posicion, jugadores, en_boton, subida_previa)
    st.success(f"Acción recomendada: **{accion}**")