from pipelines.extract import extract_from_excel
from pipelines.transform import concat_data_frame
from pipelines.load import load_excel


if __name__ == "__main__":
    data_frame_list = extract_from_excel('data/input')
    data_frame = concat_data_frame(data_frame_list)
    load_excel(data_frame, "data/output", "final_file")
