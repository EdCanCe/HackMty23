import streamlit as st

st.set_page_config(page_title= "Datos del usuario", layout= "wide")

st.text("Nombre(s)")
st.text_input("")

st.text("Apellido(s)")
st.text_input("a")

st.text("Número de identificación oficial")
st.text_input("b")

st.text("Dirección actual")
st.text_input("c")

st.text("¿Cuánto dinero ganas?")
st.number_input("")

st.text("¿Su objetivo principal de inversión es a ?")
st.selectbox("corto plazo (1-3 años), mediano plazo (3-5 años), largo plazo (más de 5 años)")
st.text("¿Qué nivel de riesgo está dispuesto a asumir en sus inversiones?")
st.selectbox("bajo, moderado, alto")