import streamlit as st
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
    
if(st.session_state.page == 0):
    with placeholder.container():
        genHeader()
        if(st.button("Pasa página")):
            st.session_state.page+=1
        genFooter()

if(st.session_state.page == 1):
    with placeholder.container():
        genHeader()
        st.markdown('''Esto es una prueba
    ''')
        genFooter()