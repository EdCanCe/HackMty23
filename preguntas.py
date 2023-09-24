import streamlit as st
import DataBase as db
st.set_page_config(page_title= "Datos del usuario", layout= "wide")

st.text_input("Nombre(s)") # Para insertar texto

st.text_input("Apellido(s)")

st.text_input("Número de identificación oficial")

st.text_input("Dirección actual")

# Preguntas de opción múltiple

ObjetivoPrincipal = st.radio("¿Su objetivo principal de inversión es a ?", 
                             ["Corto plazo (1-3 años)", "Mediano plazo (3-5 años)" , "Largo plazo (más de 5 años)"], 
                             index = None, horizontal = True,
)
st.write("Tu objetivo principal es:", ObjetivoPrincipal)

Riesgo = st.radio("¿Qué nivel de riesgo estás dispuesto a asumir en sus inversiones?",
                   ["Bajo", "Moderado", "Alto"], 
                   index = None, horizontal = True,
)
st.write("El nivel de riesgo que seleccionaste fue:", Riesgo)

st.number_input("¿Cuánto es su ingreso mensual?")
st.number_input("¿Cuánto dinero planea invertir mensualmente sin afectar su calidad de vida actual?")

st.number_input("¿Cuánto es su ingreso anual?")
st.number_input("¿Cuánto dinero planea invertir anualmente sin afectar su calidad de vida actual?")


# Preguntas de varias opciones

metaInversion = st.multiselect("¿Cuáles son tus metas de inversión?", ["Casa", "Coche", "Retiro", "Educación de sus hijos", "Vacaciones", "Deudas", "Fondos de emergencia", "Otro"])
if "Otro" in metaInversion:
    st.text_input('Ingresa los otros')

# Compras

st.number_input("¿Cuánto gastas en necesidades (comida, servicios básico, agua, entre otros) al mes?")

st.number_input("¿Cuánto gastas en gustos (compras de impulso, innecesarios, vicios, entre otros) al mes?")