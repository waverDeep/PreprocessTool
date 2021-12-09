import interface_file_io as file_io
import os


def convert_transcript_like_librispeech(root_dir):
    dir_list = os.listdir(root_dir)
    for dir_index, dir_name in enumerate(dir_list):
        sub_dir_list = os.listdir("{}/{}".format(root_dir, dir_name))
        for sub_dir_index, sub_dir_name in enumerate(sub_dir_list):
            temp_dir_path = "{}/{}/{}".format(root_dir, dir_name, sub_dir_name)
            txt_file_list = file_io.get_all_file_path(temp_dir_path, "txt")
            scripts = []
            for file_index, file_name in enumerate(txt_file_list):
                with open(file_name, 'r') as script:
                    scripts.append("{} {}\n".format(file_io.get_pure_filename(file_name), str(script.readline())))
            with open("{}/{}/{}/{}.trans.txt".format(root_dir, dir_name, sub_dir_name, sub_dir_name), 'w') as trans_file:
                trans_file.writelines(scripts)


if __name__ == '__main__':
    root_dir = "../dataset"
    convert_transcript_like_librispeech(root_dir)