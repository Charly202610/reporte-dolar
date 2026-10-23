import requests
import pandas as pd

url="https://api.argentinadatos.com/v1/cotizaciones/dolares"

respuesta=requests.get(url)
print(respuesta.status_code)

datos=respuesta.json()
df=pd.DataFrame(datos)
df.to_csv("datos_crudos/cotizaciones_dolar.csv",index=False)
