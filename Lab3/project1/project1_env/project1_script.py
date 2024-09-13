import pandas as pd

# Imprimir la versión de pandas
print("Versión de pandas:", pd.__version__)

# Crear un DataFrame simple
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

print("Proyecto 1 - DataFrame de Pandas 2:")
print(df)