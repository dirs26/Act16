import random
import pandas as pd
import matplotlib.pyplot as plt


lista = []
for n in range(10):
    lista.append(random.randint(1,100))
lista.sort()
print(lista)

frase = input('Escriba la frase: ')
print(frase.count('a'))


datos = pd.read_csv("casasboston.csv")
# datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
df = datos[["RM", "CRIM", "MEDV", "TOWN", "CHAS"]]

df = datos.rename(columns={
    "TOWN": "CIUDAD",
    "CRIM": "INDICE_CRIMEN",
    "INDUS": "PCT_ZONA_INDUSTRIAL",
    "CHAS": "RIO_CHARLES",
    "RM": "N_HABITACIONES_MEDIO",
    "MEDV": "VALOR_MEDIANO",
    "LSTAT": "PCT_CLASE_BAJA"
})
df.RIO_CHARLES.value_counts().plot.pie()
plt.show()