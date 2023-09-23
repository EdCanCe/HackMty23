import streamlit as st

st.set_page_config(page_title= "tak Coach de inversión", layout= "wide")    

with open("style.css") as f:
    st.header("Hola")
    st.title("Presentacion")
    st.write("BLa blablablalbala")
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.write("hello world".format(f.read()))
    st.write("bye ola")