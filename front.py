import streamlit as st

st.set_page_config(page_title= "tak Coach de inversión", layout= "wide")    

with open("style.css") as f:
    st.image("https://citris-uc.org/wp-content/uploads/2019/10/Tec-de-Monterrey-logo-horizontal-blue.png")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Logo_de_Banorte.svg/2560px-Logo_de_Banorte.svg.png")
    st.title("Presentacion")
    st.write("BLa blablablalbala")
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.write("hello world".format(f.read()))
    st.write("bye ola")