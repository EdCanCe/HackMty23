import streamlit as st
import requests
import varAux
import DataBase as db
st.set_page_config(
    page_title= "takatakata's Hackathon Proyect"
)

if "page" not in st.session_state:
    st.session_state.page = 0

placeholder = st.empty()

from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#------Agregar valores-------
lottie_coding = load_lottieurl("https://lottie.host/53acdb1a-30ec-4187-91bd-a757253236f2/9DMM2U7ryH.json")


def genHeader():
    st.markdown('''# Takatakata's Hackathon Proyect
---
''')

def genFooter():
    st.markdown('''---
## El proyecto fue elaborado por:
 - Mario Feng Wu
 - Gael Cumplido Mendoza
 - Edgar Andrey Balvaneda Castillón
 - Edmundo Canedo Cervantes
Estudiantes del Tecnológico de Monterrey Campus Guadalajara
''')
    
def redirect(text, pid, sk):
    with st.container():
        col1, col2, col3 = st.columns(3)
        if(col2.button(text, key=sk)):
            varAux.auxPage = st.session_state.page
            st.session_state.page=pid
    
if st.button("FAQ", type="primary"):
    st.session_state.page=2

st.markdown(
    """
    <style>
    button[kind="primary"] {
        background: red;
        border: none;
        aspect-ratio: 1/1;
        width: fit-content;
        color: white;
        text-decoration: none;
        cursor: pointer;
        transition: color 0.2s, background 0.2s, box-shadow 0.2s;
        border-radius: 100px;
        font-weight: bold !important;
        display: block;
        position: fixed;
        bottom: 50px;
        right: 59px; 
    }
    button[kind="primary"]:hover, div.stButton > button:hover {
        color: red !important;
        background: white;
        box-shadow: 0 0 10px red;
    }
    button[kind="primary"]:active, div.stButton > active {
        box-shadow: 0 3px 20px red;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.write("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');
         
*{
    font-family: 'Poppins', sans-serif;
}

div.stButton > button {
    display: block;
    text-align: center;
    background: red;
    color: white !important;
    margin: auto auto;
    transition: color 0.2s, background 0.2s, box-shadow 0.2s;
}

h1, h2, span, li{
    color: black;
}

.main{
    background: linear-gradient(90deg, #ffdddd, white, white, white, white, #ffdddd)!important;
}
         
header{
    background: red !important;
}
         
.stDeployButton *, #MainMenu *{
    color: white;
}
</style>
""", unsafe_allow_html=True)


if(st.session_state.page == 0): #Página de inicio
    with placeholder.container():
        genHeader()
        #Seccion Header 
        redirect("Iniciar Sesión", 3, "hbis")
        redirect("Crear Cuenta", 1, "hbcc")
        hpct=st.container()
        with hpct:
            st.markdown("---")
            with st.container():
                image_Tec, image_HackMTY  = st.columns((7, 3))
            with image_Tec: 
                st.image("https://citris-uc.org/wp-content/uploads/2019/10/Tec-de-Monterrey-logo-horizontal-blue.png") 
            with image_HackMTY:     
                st.image("https://th.bing.com/th/id/OIP.bD70SkJLNjIoODY7YK_VnAHaFE?pid=ImgDet&rs=1")
            text_column1, image_Banorte, text_column3  = st.columns((1, 3, 1))
            with text_column1:
                st.text("") 
            with image_Banorte:
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Logo_de_Banorte.svg/2560px-Logo_de_Banorte.svg.png")
            with text_column3:
                st.text("") 
            text_column4, sticker_lottie, text_column5 = st.columns((1,2, 1))
            with sticker_lottie:
                st.write("---")
                st_lottie(lottie_coding, height = 300, key = "coding")
            with text_column4:
                st.text("") 
            with text_column5:
                st.text("") 
            genFooter()

if(st.session_state.page == 1): #Página de captura de 
    st.session_state.page=varAux.auxPage
    with placeholder.container():
        genHeader()
        st.subheader("Crear Cuenta")
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
            st.write(Nombre)
            st.write(Apellido)
            st.write(N_oficial)
            st.write(ObjetivoPrincipal)
            st.write(Riesgo)
            st.write(IngMensual)
            st.write(IngMensual)
            st.write(IngAnual)
            st.write(InvAnual)
            st.write(metaInversion)
            if "Otro" in metaInversion:
                st.write(OtroMeta)
            st.write(Necesidades)
            st.write(Gustos)
        redirect("Volver", varAux.auxPage, "dtgb")
        genFooter()

if(st.session_state.page == 2): #Página de las FAQ
    st.session_state.page=varAux.auxPage
    with placeholder.container():
        genHeader()
        redirect("Volver", varAux.auxPage, "faqgb1")
        
        redirect("Volver", varAux.auxPage, "faqgb2")
        genFooter()

if(st.session_state.page == 3): #Página de inicio de sesión
    st.session_state.page=varAux.auxPage
    with placeholder.container():
        genHeader()
        st.subheader("Iniciar Sesión")

        redirect("Iniciar sesión", 4, "isb")
        genFooter()

if(st.session_state.page == 2): #Página de usuario
    st.session_state.page=varAux.auxPage
    with placeholder.container():
        genHeader()
        st.subheader("Bienvenido usuario")
        genFooter()