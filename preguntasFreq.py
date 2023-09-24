import streamlit as st
st.set_page_config(page_title= "Preguntas frecuentes", layout= "wide")

st.title('Preguntas frecuentes en Banorte')

st.subheader("¿Qué es un fondo de inversión?")

st.subheader("¿Cómo puedo empezar a invertir en un fondo?")

st.subheader("¿Por qué invertir en Banorte?")

# Crear un slider de texto
valor_seleccionado = st.slider("Selecciona un valor:", ["Opción 1", "Opción 2", "Opción 3"])

# Mostrar el valor seleccionado
st.write("Has seleccionado:", valor_seleccionado)