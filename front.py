import streamlit as st

st.set_page_config(page_title= "Takatakata's Hackathon Proyect", layout= "wide")

st.header("Hola")
st.title("Presentacion")
st.write("BLa blablablalbala")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.write("hello world")
    st.write("bye world")