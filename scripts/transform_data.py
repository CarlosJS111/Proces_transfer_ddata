import pandas as pd

df = pd.read_parquet("data/extracted_data.parquet")

# Renombrar columnas según esquema propuesto
df.rename(columns={"paid_at": "updated_at"}, inplace=True)

# Guardar en un nuevo archivo Parquet transformado
df.to_parquet("data/transformed_data.parquet", index=False)
print("Transformación completada.")
