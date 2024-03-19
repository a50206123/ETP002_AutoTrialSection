from yc_etabs_api.yc_etabs_api import ETABS

def read_input_excel(filename:str) -> list:
    pass

def get_frame_section(etabs) -> list:
    pass

def change_mat_process(etabs, frame_section, story_mat_list) -> None:
    pass

def main () :
    etabs = ETABS()

    story_mat_list = read_input_excel

    frame_section = get_frame_section(etabs)

    change_mat_process(etabs, frame_section, story_mat_list)

if __name__ == '__main__'  :
    main()