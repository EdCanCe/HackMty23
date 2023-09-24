import streamlit as st

st.set_page_config(page_title= "Datos del usuario", layout= "wide")

st.text_input("Nombre(s)")

st.text_input("Apellido(s)")

st.text_input("Número de identificación oficial")

st.text_input("Dirección actual")

st.number_input("¿Cuánto dinero ganas?")

st.text("¿Su objetivo principal de inversión es a ?")
st.radio("corto plazo (1-3 años)", "mediano plazo (3-5 años)" , "largo plazo (más de 5 años)")

st.text("¿Qué nivel de riesgo estás dispuesto a asumir en sus inversiones?")
st.radio("bajo", "moderado", "alto")