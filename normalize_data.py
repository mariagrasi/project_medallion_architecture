import os
import pandas as pd

input_dir = '01-bronze-raw' #vamos ler os arquivos da pasta bronze (csv e json)
output_dir = '02-silver-validated' #vamos salvar com parquet

os.makedirs(output_dir, exist_ok='True') #garante que a pasta de saída exista

for file in os.listdir(input_dir):
    input_path = os.path.join(input_dir, file)
    name, ext = os.path.splitext(file)
    output_path = os.path.join(output_dir, f'{name}.parquet')

    if ext.lower() == '.csv':
        df = pd.read_csv(input_path)
    elif ext.lower() == '.json':
        #ler como lista de objetos
        try:
            df = pd.read_json(input_path)
        except ValueError:
            #Caso falhar, tenta ler como linhas separadas 
            df = pd.read_json(input_path, line =True)
    else:
        print(f"Arquivo {file} ignorado (formato não suportado)")
        continue
    
    #converte colunas do tipo list para string, permitindo o uso do drop_duplicates
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x,list)).any():
            df[col] = df[col].apply(lambda x: str(x) if isinstance(x,list) else x)

    df = df.drop_duplicates().reset_index(drop=True)

    #salva en formato parquet

    df.to_parquet(output_path, index=False)
    print(f"Arquivo {file} normalizado e salvo como {output_path}")



