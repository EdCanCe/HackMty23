import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

def init_model():
    le = preprocessing.LabelEncoder()
    data = pd.read_excel("copynew.xlsx")

    data_clean = data[["usertime", "userisk", "usermensual", "invemensual", "inveanual", "metainver", "necesidad", "gustos"]]
    data_clean = data_clean.drop(13, axis=0)
    data_clean['usertime']= le.fit_transform(data_clean["usertime"])
    data_clean['userisk']= le.fit_transform(data_clean["usertime"])

    n = 0
    for i in data_clean["metainver"]:
    
        aux = "".join(i[1:-2].split("'"))
        data_clean["metainver"][n] = aux.split(", ")
        n+=1

    n = 0
    for j in data_clean["metainver"]:
        data_clean["metainver"][n] = len(j)
        n+=1

    modelo = KMeans(n_clusters = 3, max_iter = 100)
    modelo.fit(data_clean)

    return modelo

init_model()
