import pandas as pd
import os


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name:str) -> pd.DataFrame:
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo criado com sucesso."


