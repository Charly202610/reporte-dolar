# Importa la librería Pandas y le asigna el alias "pd".
# Pandas permite trabajar con datos tabulares mediante DataFrames.
import pandas as pd

# Lee el archivo CSV ubicado en la carpeta "datos_crudos"
# y lo carga en un DataFrame llamado "df".
df = pd.read_csv("datos_crudos/cotizaciones_dolar.csv")

# Muestra las primeras 5 filas del DataFrame.
# Sirve para verificar que los datos se cargaron correctamente.
print(df.head())

# Muestra información general del DataFrame:
# cantidad de registros, columnas, tipos de datos y valores no nulos.
print(df.info())

# Filtra únicamente los registros cuya columna "casa"
# tiene el valor "oficial".
oficial = df[df['casa'] == 'oficial']

# Filtra únicamente los registros cuya columna "casa"
# tiene el valor "bolsa".
bolsa = df[df['casa'] == 'bolsa']

# Muestra las primeras filas del DataFrame "oficial".
print(oficial.head())

# Muestra las primeras filas del DataFrame "bolsa".
print(bolsa.head())

# Une ambos DataFrames utilizando la columna "fecha" como clave.
# Las columnas con el mismo nombre se diferencian mediante
# los sufijos "_oficial" y "_bolsa".
comparacion = oficial.merge(
    bolsa,
    on='fecha',
    suffixes=('_oficial', '_bolsa')
)

# Muestra las primeras filas del resultado de la unión.
print(comparacion.head())

# Muestra el tipo de dato de cada columna del DataFrame.
# Es útil para verificar si los datos son numéricos,
# texto, fechas, etc.
print(comparacion.dtypes)

# Calcula la brecha porcentual entre el dólar bolsa y el dólar oficial.
#
# Fórmula:
# ((venta_bolsa - venta_oficial) / venta_oficial) * 100
#
# round(...,2) redondea el resultado a 2 decimales.
comparacion['brecha'] = round(
    (
        (comparacion['venta_bolsa'] - comparacion['venta_oficial'])
        / comparacion['venta_oficial']
    ) * 100,
    2
)

# Muestra las primeras 10 filas de las columnas seleccionadas
# para analizar la brecha calculada.
print(
    comparacion[
        ['fecha', 'venta_oficial', 'venta_bolsa', 'brecha']
    ].head(10)
)

# Guarda el DataFrame final en un nuevo archivo CSV
# dentro de la carpeta "datos_procesados".
#
# index=False evita que Pandas agregue una columna extra
# con el índice de las filas.
comparacion.to_csv(
    "datos_procesados/comparacion_oficial_bolsa.csv",
    index=False
)