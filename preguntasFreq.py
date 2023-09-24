import streamlit as st
st.set_page_config(page_title= "Preguntas frecuentes", layout= "wide")

st.title('Preguntas frecuentes en Banorte')

st.subheader("¿Qué es un fondo de inversión?")
st.text_area("Fondos de Inversión","Son una excelente forma para obtener rendimientos "
            "de tus ahorros. Su función principal es captar, invertir y administrar los recursos "
            "de clientes como tú para invertirlos en distintos instrumentos financieros "
            "y ponerlos a tu alcance. Funcionan como una sociedad que reúne el ahorro de varias " 
            "personas que también buscan invertir, pero que por los montos o instrumentos "
            "no puede hacerlo de manera individual")

st.subheader("¿Cómo puedo empezar a invertir en un fondo?")

st.text_area("Invertir en un fondo","Solo tienes que elegir el o los Fondos que te más te interesen "
            "de acuerdo a tu elección irás recibiendo rendimientos, que son resultado de la rentabilidad "
            "o ganancia de los activos en los que invirtió el Fondo que elegiste "
            "y ponerlos a tu alcance. Funcionan como una sociedad que reúne el ahorro de varias "
            "personas que también buscan invertir, pero que por los montos o instrumentos "
            "no puede hacerlo de manera individual")

st.subheader("¿Por qué invertir en Banorte?")
st.markdown("**Banorte brinda**")
st.text_area("Crecimiento:"," Busca el incremento de tu patrimonio con la " 
             "tranquilidad de que estás en buenas manos con una amplia oferta. ")
st.text_area("Experiencia: ","Contarás con asesoría personalizada y recibirás toda " 
             "la información necesaria para que puedas tomar la mejor decisión de inversión para ti.")
st.text_area("Diversificación: ","Podrás diversificar tu dinero de acuerdo con la estrategia de cada Fondo, "
             "así minimizas el riesgo e incertidumbre")
st.text_area("Flexibilidad: ","Encontrarás diferentes opciones que se acomoden a tus necesidades y objetivos.")

st.subheader("¿A partir de cuánto dinero puedo empezar a invertir?")
st.text_area("A partir de $100 pesos ","La inversión inicial es dependiendo del Fondo a contratar y en cualquier "
            "momento puedes incrementarlo para generar mayores ganancias.")

st.subheader("¿Existe algún riesgo de perder parte de mi inversión en Fondos?")
st.text_area("Todas las inversiones tienen riesgo asociado", "Puede ser desde extremadamente bajo hasta alto, "
            "en general los Fondos con menor rendimiento esperado tienen menor riesgo " 
            "y viceversa. Depende directamente del tipo de activos que conforman la cartera del Fondo")

st.subheader("¿Mis rendimientos generan algún tipo de impuesto?")
st.text_area("Sí","Por ley todas las inversiones generan impuestos. "
             "Sin embargo, al recibir tus ganancias ya serán libres de impuestos.")

st.subheader("¿Puedo comprar más de un Fondo?")
st.text_area("Sí","Tu contrato de Fondos te permite invertir en todos los Fondos que te interesen y "
            "se ajusten a tu perfil como inversionista. " 
            "Es recomendable diversificar entre corto, mediano y largo plazo.")

st.subheader("¿Por cuánto tiempo debo de mantener mi inversión?")
st.text_area("No hay tiempo límite","Una ventaja de los Fondos es que no hay un plazo o tiempo obligado, sin embargo, "
            "existe un tiempo recomendado llamado horizonte de inversión, "
            "para mantener lo invertido y así lograr optimizar los rendimientos.")

st.subheader("¿Qué tipo de Fondos existen?")
st.text_area("Existen varios: ", "Fondos de Deuda, de Renta Variable, "
             "Mixtos (Renta Fija y Variable), de Cobertura, entre otros.")

st.subheader("¿Cómo se determina el rendimiento de un Fondo?")
st.text_area("Por la rentabilidad o ganancia","El rendimiento de un Fondo de inversión es consecuencia de la rentabilidad o ganancia "
             "que proporcione cada uno de los activos que componen su cartera. "
             "Se calcula con el diferencial de precio de venta vs. precio de compra.")