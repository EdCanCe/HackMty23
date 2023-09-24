import pandas as pd

d = pd.read_excel("New.xlsx")
df = pd.DataFrame(d)
print(df)

def crear():
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
df.to_excel("C:\\Users\\gaelm\\Desktop\\Data.xlsx")

#with pd.ExcelWriter("Output.xlsx") as writer:
#df.to_excel(writer, sheet_name= "Prueba")