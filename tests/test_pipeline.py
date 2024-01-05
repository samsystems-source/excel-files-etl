import pandas as pd

from app.pipelines.transform import concat_data_frame

df_1 = pd.DataFrame({"col1":[1,2], "col2":[3,4]})
df_2 = pd.DataFrame({"col2":[2,5], "col2":[7,8]})


def testar_a_concatenacao_da_lista_de_dataframe():
    data_frame_list = [df_1, df_2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    df = concat_data_frame(data_frame_list)
    # assert    
    assert data_frame.equals(df)



def test_shape_iguals_dataframe():
    data_frame_list = [df_1, df_2]
    df = concat_data_frame(data_frame_list)
    # assert  
    assert df.shape == (4, 2)

def test_shape_isnotiguals_dataframe():
    data_frame_list = [df_1, df_2]
    df = concat_data_frame(data_frame_list)
    # assert  
    assert df.shape != (5, 2)