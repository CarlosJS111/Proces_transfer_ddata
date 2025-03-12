import pandas as pd

df = pd.read_parquet("data/extracted_data.parquet")
df.rename(columns={"paid_at": "updated_at"}, inplace=True)
df.to_parquet("data/transformed_data.parquet", index=False)
print("Transformación completada.")
