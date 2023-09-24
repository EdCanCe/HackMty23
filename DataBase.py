import pandas as pd

data = {'Nombre': [], 'Edad': [], 'Ciudad': []}
df = pd.DataFrame(data)

def agregar_datos():
    global df
    nombre = input("Ingresa el nombre: ")
    edad = int(input("Ingresa la edad: "))
    ciudad = input("Ingresa la ciudad: ")

    nueva_fila = {'Nombre': nombre, 'Edad': edad, 'Ciudad': ciudad}
    df = df.loc[0:]  # Añade esta línea para crear una copia del DataFrame
    df += pd.DataFrame([nueva_fila], columns=df.columns)
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








#d = pd.read_excel("New.xlsx")
#df = pd.DataFrame(d)
#print(df)




"""IDINE = ["C13"]
username = ["Mario"]
lastname = ["Feng Wu"]
useradress = ["Tec de Monterrey"]
useropen = ["13,000"]
usertime =["3"]
userisk = ["Low"]

df = pd.DataFrame()

df["ID"] = IDINE
df["Username"] =  username
df["Lastname"] = lastname
df["Useradress"] = useradress
df["UserOpen"] = useropen
df["UserTime"] = usertime
df["Userisk"] = userisk
    print(df)
"""
#df.to_excel("C:\\Users\\gaelm\\Desktop\\Data.xlsx")

#with pd.ExcelWriter("Output.xlsx") as writer:
#df.to_excel(writer, sheet_name= "Prueba")