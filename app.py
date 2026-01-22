import os
import pandas as pd
import re
from db import PostgresDB


def normalize_table_name(filename: str) -> str:
    name = filename.replace(".parquet", "").lower()
    name = re.sub(r"[^a-z0-9_]", "_", name)
    return name


if __name__ == "__main__":
    db = PostgresDB()

    base_path = "02-silver-validated"

    for file in os.listdir(base_path):
        if not file.endswith(".parquet"):
            continue

        table_name = normalize_table_name(file)
        file_path = os.path.join(base_path, file)

        print(f"📥 Processando {file} → tabela {table_name}")

        df = pd.read_parquet(file_path)

        if df.empty:
            print(f"⚠️ Arquivo vazio ignorado: {file}")
            continue

        try:
            db.create_table_from_df(table_name, df)
            db.copy_from_dataframe(table_name, df)
            print(f"✅ Carga concluída: {table_name}")

        except Exception as e:
            db.conn.rollback()
            print(f"❌ Erro ao processar {file}: {e}")

    db.close()
