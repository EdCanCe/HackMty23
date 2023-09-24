import streamlit as st
import varAux
st.set_page_config(
    page_title= "takatakata's Hackathon Proyect"
) 

if "page" not in st.session_state:
    st.session_state.page = 0

placeholder = st.empty()

def genHeader():
    st.markdown('''# Takatakata's Hackathon Proyect
---
''')

def genFooter():
    st.markdown('''---
## El proyecto fue elaborado por:
 - Mario Feng Wu
 - Gael Cumplido
 - Edgar Andrey
 - Edmundo Canedo
''')
    
def redirect(text, pid):
    if(st.button(text)):
        varAux.auxPage = pid
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
        transition: color 0.2s, background 0.2s;
        border-radius: 100px;
        font-weight: bold !important;
        display: block;
        position: fixed;
        bottom: 50px;
        right: 59px; 
    }
    button[kind="primary"]:hover {
        color: red;
        background: white;
        box-shadow: 0 0 10px red;
    }
    button[kind="primary"]:active {
        box-shadow: 0 0 20px red;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



if(st.session_state.page == 0): #Página de inicio
    with placeholder.container():
        genHeader()

        redirect("Pasar página", 1)
        genFooter()

if(st.session_state.page == 1): #Página de captura de datos
    with placeholder.container():
        genHeader()
        st.markdown('''## Proporciona tus datos:
    ''')
        # cuanto ganas mensualmente
        # 
        #
        #
        #
        #
        genFooter()

if(st.session_state.page == 2): #Página de las FAQ
    with placeholder.container():
        genHeader()
        st.markdown('''## Frecuently asked questions
    ''')
        st.write(varAux.auxPage)
        if(st.button("Volver")):
            st.session_state.page=varAux.auxPage
        genFooter()