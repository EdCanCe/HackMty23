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
    
fixedFAQ = st.markdown('<style> .faq{ position: fixed; bottom: 100px; right: 100px; color: red; background: white; display: block; padding: 10px; border-radius: 100px; transition: color 0.2s} .faq:hover{ color: white; background: red; box-shadow: 0px 0px 10px red; cursor: pointer; } .faq:active{ transform: scale(0.9); }</style><a href=# id="faqid" class="faq"">FAQ</a>', unsafe_allow_html=True)

if fixedFAQ:
    st.write("Link clicked!")
    st.session_state.page=2
    st.write("aaa")

st.write("<a href='#' id='my-link'>Click me</a>", unsafe_allow_html=True)

if st.button("my-link"):
    st.write("Link clicked!")


if(st.session_state.page == 0):
    with placeholder.container():
        genHeader()

        if(st.button("Pasa página")):
            st.session_state.page=1
        genFooter()

if(st.session_state.page == 1):
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

if(st.session_state.page == 2):
    with placeholder.container():
        genHeader()
        st.markdown('''## Frecuently asked questions
    ''')
        genFooter()