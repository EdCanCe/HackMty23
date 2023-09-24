import streamlit as st

st.set_page_config(page_title= "tak Coach de inversión", layout= "wide")    

with st.container():
    st.image("https://citris-uc.org/wp-content/uploads/2019/10/Tec-de-Monterrey-logo-horizontal-blue.png")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Logo_de_Banorte.svg/2560px-Logo_de_Banorte.svg.png")
    st.image("https://th.bing.com/th/id/OIP.bD70SkJLNjIoODY7YK_VnAHaFE?pid=ImgDet&rs=1")
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