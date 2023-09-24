import streamlit as st
import requests

from streamlit_lottie import st_lottie
st.set_page_config(page_title= "tak Coach de inversión", layout= "wide")    

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#------Agregar valores-------
lottie_coding = load_lottieurl("https://lottie.host/60707005-ac51-4186-bf8d-ec558648f6e2/GUWk8gO9eR.json")


#Seccion Header
with st.container():
    image_Tec, image_HackMTY  = st.columns((2, 1))
    with image_Tec: 
        st.image("https://citris-uc.org/wp-content/uploads/2019/10/Tec-de-Monterrey-logo-horizontal-blue.png")
    with image_HackMTY:     
        st.image("https://th.bing.com/th/id/OIP.bD70SkJLNjIoODY7YK_VnAHaFE?pid=ImgDet&rs=1")
    text_column1, image_Banorte  = st.columns((1, 2))
    with text_column1:
        st.text("Caca") 
    with image_Banorte:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Logo_de_Banorte.svg/2560px-Logo_de_Banorte.svg.png")
    st.title("Presentacion")
    st.write("BLa blablablalbala")
    st.write("hello world")
    st.write("bye ola")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Que se hace")
        st.write("##")
        st.write(
"""Hola, quienes somos, etc ,,,,,
.......
......
""")
    with right_column:
        st_lottie(lottie_coding, height 300, key "coding")