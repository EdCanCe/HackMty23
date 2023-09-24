import yfinance as yf #Modulo para las bases de datos
import pandas as pd #Modulo para visualizar y trajar mejor con los datos
import numpy as np #Libreria de matrices que nos facilita varias cosas
import datetime #Funciona para obtener la fecha

data = yf.download("GOOG", start = "2005-01-01", end = datetime.date)

 
