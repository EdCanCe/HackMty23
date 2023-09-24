import streamlit as st

st.set_page_config(page_title= "Datos del usuario", layout= "wide")

st.text_input("Nombre(s)")

st.text_input("Apellido(s)")

st.text_input("Número de identificación oficial")

st.text_input("Dirección actual")

st.number_input("¿Cuánto dinero ganas?")

st.radio('Pick one:', ['nose','ear'])

st.radio("¿Su objetivo principal de inversión es a ?", ["corto plazo (1-3 años)", "mediano plazo (3-5 años)" , "largo plazo (más de 5 años)"])

st.radio("¿Qué nivel de riesgo estás dispuesto a asumir en sus inversiones?", ["bajo", "moderado", "alto"])