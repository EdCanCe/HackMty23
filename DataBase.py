import pandas as pd

data = {'IDINE': [], 'username': [], 'userlast': [], 'useradress': [], 'usertime': [], 'userisk': [], 'usermensual' : [], 'invemensual' : [], 'ingranual' : [], 'inveanual' : [], 'metainver' : [], 'otrameta' : [], 'necesidad' : [], 'gustos' : []}
df = pd.DataFrame(data)

def agregar_datos(IDINE, username, userlast, useradress, usertime, userisk, usermensual, invemensual, ingranual, inveanual, metainver, otrameta, necesidad, gustos):
    global df

    nueva_fila = {'IDINE': IDINE, 'username': username, 'userlast': userlast, 'useradress': useradress, 'usertime': usertime, 'userisk': userisk, "usermensual" : usermensual, "invemensual" : invemensual, "ingranual" : ingranual, "inveanual" : inveanual, "metainver" : metainver, "otrameta" : otrameta, "necesidad" : necesidad, "gustos" : gustos  }
    nueva_data = pd.DataFrame([nueva_fila])
    df = pd.concat([df, nueva_data], ignore_index=True)
    df.to_csv('datos.csv', index=False)
    df.to_excel("C:\\Users\\gaelm\\Desktop\\Data.xlsx")