import os
from typing import ParamSpec

main_path = "D:\\Desktop\\Test Sort"

directory_set = {
    "Video": ['mp4', 'avi', 'gif', 'mkv', 'mov', 'mpeg'],
    "Image": ['jpg', 'png', 'bmp', 'ico', 'svg', 'jpeg'],
    "DCIM-Video": ['mp4', 'mov'],
    "DCIM-Image": ['jpg', 'png', 'bmp', 'jpeg'],
    "Audio": ['mp3', 'ogg', 'wav', 'midi'],
    "Archive": ['rar', 'zip', '7z'],
    "Docs": ['txt', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx'],
    "3D": ['obj', 'fbx', 'stl', 'dae', '3ds', 'blend', 'c4d'],
    "Adobe": ['psd', 'prproj', 'aep', 'ai'],
    "Other": ['db', 'py', 'sln', 'ttf', 'otf', 'apk']
}


def check_dir(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


if __name__ == "__main__":
    check_dir(main_path, directory_set)

