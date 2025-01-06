import pandas as pd
import os
import glob

# função de extrair
def extract_data(folder: str) -> pd.DataFrame:
    # Lendo os arquivos json
    json_files = glob.glob(os.path.join(folder, '*.json'))
    # Criar os dataframes de cada arquivo json
    df_list = [pd.read_json(file) for file in json_files]
    # Concatenando os dataframes e renumerando os indices
    final_df = pd.concat(df_list, ignore_index=True)
    return final_df


# Função de calculo total da vendas
def calc_total_sales_value(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# Função para gerar o arquivo final
def load_data(df: pd.DataFrame, output_format: list):
    for output in output_format:    
        if output == "csv":
            df.to_csv("output/data.csv", index=False)
        if output == "parquet":
            df.to_parquet("output/data.parquet", index=False)

            
def pipeline_calc_total_sales(folder: str, output_format:list):
    extract_datas = extract_data(folder=folder)
    calc_sales_value = calc_total_sales_value(extract_datas)
    load_data(calc_sales_value, output_format=output_format)

