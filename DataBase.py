import pandas as pd

data = {'IDINE': [], 'username': [], 'userlast': [], 'useradress': [], 'usertime': [], 'userisk': [], 'usermensual' : [], 'invemensual' : [], 'ingranual' : [], 'inveanual' : [], 'metainver' : [], 'otrameta' : [], 'necesidad' : [], 'gustos' : []}
df = pd.DataFrame(data)

def agregar_datos(IDINE, username, userlast, useradress, usertime, userisk, usermensual, invemensual, ingranual, inveanual, metainver, otrameta, necesidad, gustos):
    global df

    nueva_fila = {'IDINE': IDINE, 'username': username, 'userlast': userlast, 'useradress': useradress, 'usertime': usertime, 'userisk': userisk, "usermensual" : usermensual, "invemensual" : invemensual, "ingranual" : ingranual, "inveanual" : inveanual, "metainver" : metainver, "otrameta" : otrameta, "necesidad" : necesidad, "gustos" : gustos  }
    nueva_data = pd.DataFrame([nueva_fila])
    df = pd.concat([df, nueva_data], ignore_index=True)
    return df

while True:
    respuesta = input("¿Deseas agregar datos? (s/n): ")
    if respuesta.lower() == 's':
        df = agregar_datos()
        print("\nDatos agregados:")
        print(df)
    else:
        break

df.to_csv('datos.csv', index=False)
df.to_excel("C:\\Users\\gaelm\\Desktop\\Data.xlsx")


"""
    IDINE = input("Ingresa el ID: ")
    username = input("Ingresa el nombre: ")
    userlast = input("Ingresa tus apellidos: ")
    useradress = input("Ingresa tu dirección: ")
    usertime = input("Tiempo de inversion: ")
    userisk = input("Riesgo: ")
    usermensual = float(input("ingreso mensual: "))
    invemensual = float(input("cuanto dinero planeas invertir mensualmente: "))
    ingranual = float(input("ingreso anual: "))
    inveanual = float(input("cuanto dinero planeas invertir anualmente: "))
    metainver = input("meta de inversion: ")
    otrameta = input("otra meta: ")
    necesidad = input("necesidades donde se va el dinero: ")
    gustos = input("en que gustos gastas tu dinero: ")
"""