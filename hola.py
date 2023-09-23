import streamlit as st
import pandas as pd
    
st.write("""
# My first app
Hello *world!*
aaa que miedo
pipipi :c
""")

for i in range(10):
    st.write("am hola")

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df