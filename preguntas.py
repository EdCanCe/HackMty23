import streamlit as st
import DataBase as db


pagina = st.set_page_config(page_title= "Datos del usuario", layout= "wide")

Nombre = st.text_input("Nombre(s)") # Para insertar texto


Apellido = st.text_input("Apellido(s)")


N_oficial = st.text_input("Número de identificación oficial")


Direccion = st.text_input("Dirección actual")
st.write("Tu Dirección actual es: ", Direccion)

# Preguntas de opción múltiple

ObjetivoPrincipal = st.radio("¿Su objetivo principal de inversión es a ?", 
                             ["Corto plazo (1-3 años)", "Mediano plazo (3-5 años)" , "Largo plazo (más de 5 años)"], 
                             index = None, horizontal = True,
)


Riesgo = st.radio("¿Qué nivel de riesgo estás dispuesto a asumir en sus inversiones?",
                   ["Bajo", "Moderado", "Alto"], 
                   index = None, horizontal = True,
)


IngMensual = st.number_input("¿Cuánto es su ingreso mensual?")


InvMensual = st.number_input("¿Cuánto dinero planeas invertir mensualmente sin afectar tu calidad de vida actual?")


IngAnual = st.number_input("¿Cuánto es su ingreso anual?")


InvAnual = st.number_input("¿Cuánto dinero planeas invertir anualmente sin afectar tu calidad de vida actual?")


# Preguntas de varias opciones

metaInversion = st.multiselect("¿Cuáles son tus metas de inversión?", ["Casa", "Coche", "Retiro", "Educación de sus hijos", "Vacaciones", "Deudas", "Fondos de emergencia", "Otro"])

if "Otro" in metaInversion:
    OtroMeta = st.text_input('Ingresa los otros')
else:
    OtroMeta = ""   


# Compras

Necesidades = st.number_input("¿Cuánto gastas en necesidades (comida, servicios básico, agua, entre otros) al mes?")


Gustos = st.number_input("¿Cuánto gastas en gustos (compras de impulso, innecesarios, vicios, entre otros) al mes?")


if(st.button("Continuar")):
    if(db.agregar_datos(N_oficial, Nombre, Apellido, Direccion, ObjetivoPrincipal, Riesgo, IngMensual, InvMensual, IngAnual, InvAnual, metaInversion, OtroMeta, Necesidades, Gustos) == True):
        st.write("YA EXISTE LA CUENTA")
    else:
        st.write("Iniciando sesión")