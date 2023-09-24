import streamlit as st

st.set_page_config(page_title= "Datos del usuario", layout= "wide")

st.text_input("Nombre(s)") # Para insertar texto

st.text_input("Apellido(s)")

st.text_input("Número de identificación oficial")

st.text_input("Dirección actual")

st.number_input("¿Cuánto dinero ganas?") # Para insertar numero

# Preguntas de opción múltiple
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)

ObjetivoPrincipal = st.radio("¿Su objetivo principal de inversión es a ?", 
                             ["Corto plazo (1-3 años)", "Mediano plazo (3-5 años)" , "Largo plazo (más de 5 años)"], 
                             index = None, horizontal = True,
)
st.text("Tu objetivo principal es:", ObjetivoPrincipal)

Riesgo = st.radio("¿Qué nivel de riesgo estás dispuesto a asumir en sus inversiones?",
                   ["Bajo", "Moderado", "Alto"], 
                   index = None, horizontal = True,
)
st.text("El nivel de riego que seleccionaste fue:", Riesgo)
st.number_input("¿Cuánto es su ingreso mensual?")
st.number_input("¿Cuánto dinero planea invertir mensualmente sin afectar su calidad de vida actual?")

st.number_input("¿Cuánto es su ingreso anual?")
st.number_input("¿Cuánto dinero planea invertir anualmente sin afectar su calidad de vida actual?")

# Preguntas de varias opciones
metaInversion = st.multiselect("¿Cuáles son tus metas de inversión", ["Casa", "Coche", "Retiro", "Educación de sus hijos", "Vacaciones", "Deudas", "Fondos de emergencia", "Otro"])
if metaInversion == "Otro":
    st.text_input('Ingresa los otros')