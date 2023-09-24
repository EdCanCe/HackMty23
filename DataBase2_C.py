import pandas as pd

dat = {'IDINE': [], 'tipo': [], 'compañia': [], 'precio': [], 'fecha': []}
daf = pd.DataFrame(dat)

def agregar_datos(IDINE, tipo, compañia, precio, fecha):
    global daf

    nueva_fila = {'IDINE': IDINE, 'tipo': tipo, "compañia" : compañia, "precio" : precio, "fecha" : fecha}
    nueva_data = pd.DataFrame([nueva_fila])
    daf = pd.concat([daf, nueva_data], ignore_index=True)
    daf.to_csv('user_tra.csv', index=False)
    daf.to_excel("user_transaccions.xlsx")