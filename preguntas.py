import streamlit as st
import DataBase as db
st.set_page_config(page_title= "Datos del usuario", layout= "wide")

Nombre = st.text_input("Nombre(s)") # Para insertar texto
st.write("Tu nombre(s) es: ", Nombre)

Apellido = st.text_input("Apellido(s)")
st.write("Tu apellido(s) es: ", Apellido)

N_oficial = st.text_input("Número de identificación oficial")
st.write("Tu Número de identificación oficial es: ", N_oficial)

Direccion = st.text_input("Dirección actual")
st.write("Tu Dirección actual es: ", Direccion)

# Preguntas de opción múltiple

ObjetivoPrincipal = st.radio("¿Su objetivo principal de inversión es a ?", 
                             ["Corto plazo (1-3 años)", "Mediano plazo (3-5 años)" , "Largo plazo (más de 5 años)"], 
                             index = None, horizontal = True,
)
st.write("Tu objetivo principal es: ", ObjetivoPrincipal)

Riesgo = st.radio("¿Qué nivel de riesgo estás dispuesto a asumir en sus inversiones?",
                   ["Bajo", "Moderado", "Alto"], 
                   index = None, horizontal = True,
)
st.write("El nivel de riesgo que seleccionaste fue: ", Riesgo)

IngMensual = st.number_input("¿Cuánto es su ingreso mensual?")
st.write("Tu ingreso mensual es de: ", IngMensual)

InvMensual = st.number_input("¿Cuánto dinero planea invertir mensualmente sin afectar su calidad de vida actual?")
st.write("Tu inversión mensual es de: ", IngMensual)

IngAnual = st.number_input("¿Cuánto es su ingreso anual?")
st.write("Tu ingreso mensual es de: ", IngAnual)

InvAnual = st.number_input("¿Cuánto dinero planea invertir anualmente sin afectar su calidad de vida actual?")
st.write("Tu ingreso anual es de: ", InvAnual)

# Preguntas de varias opciones

metaInversion = st.multiselect("¿Cuáles son tus metas de inversión?", ["Casa", "Coche", "Retiro", "Educación de sus hijos", "Vacaciones", "Deudas", "Fondos de emergencia", "Otro"])
st.write("Seleccionaste como metas: ", metaInversion)
if "Otro" in metaInversion:
    OtroMeta = st.text_input('Ingresa los otros')
    st.write("En otros pusiste: ", OtroMeta)

# Compras

Necesidades = st.number_input("¿Cuánto gastas en necesidades (comida, servicios básico, agua, entre otros) al mes?")
st.write("Esto es lo que gastas en necesidades: ", Necesidades)

Gustos = st.number_input("¿Cuánto gastas en gustos (compras de impulso, innecesarios, vicios, entre otros) al mes?")
st.write("Esto es lo que gastas en gustos: ", Gustos)
