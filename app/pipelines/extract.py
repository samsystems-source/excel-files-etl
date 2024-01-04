import glob
import os
from typing import List

import pandas as pd


"""
args - path for directory files xlsx
"""

    
#this make the same think
#lambda_extractor_from_excel = list(map(lambda x: pd.read_excel(x), glob.glob(os.path.join(path, "*.xlsx"))))

def extract_from_excel(path:str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path,"*.xlsx"))
    
    data_frame_list = []
    for file in all_files:
        data = pd.read_excel(file)
        data_frame_list.append(data)

    return data_frame_list




if __name__ == "__main__":
    
    path = "data/input"
    lambda_extractor_from_excel = extract_from_excel(path)
    print(lambda_extractor_from_excel)