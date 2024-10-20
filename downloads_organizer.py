import os
import shutil


# C:\Users\Hp\Downloads
path = os.path.expanduser('~\Downloads')
files = os.listdir(path)


list_of_file_types = set()
default_folders = [
    "Office_docs",
    "Pdfs",
    "Images",
    "Videos",
    "Audio",
    "Compressed",
    "Html",
    "Text",
    "Executables",
    "Folders"
]
catogories = {
    "Office_docs" : ['docx', 'pptx', 'xlsx', 'doc', 'ppt', 'xls'],
    "Pdfs" : ['pdf'],
    "Images" : ['jpg', 'jpeg', 'png', 'gif', 'svg'],
    "Videos" : ['mp4', 'mkv', 'webm'],
    "Audio" : ['mp3', 'wav'],
    "Compressed" : ['zip', '7z', 'gz', 'deb', 'rar'],
    "Html" : ['htm', 'html', 'php'],
    "Text" : ['txt', 'md', 'ini', 'sh', 'csv'],
    "Executables" : ['exe', 'msi', 'bat', 'sh']
}

for file in files:
    path = os.path.expanduser('~\Downloads')
    destination = os.path.expanduser('~\Downloads')
    # if it is a file
    if os.path.isfile(f"{path}\{file}"):
        file_type = os.path.splitext(file)[1][1:]
        for cat, ext in catogories.items():
            if file_type in ext:
                if not os.path.exists(f"{path}\{cat}"):
                    os.makedirs(f"{path}\{cat}")
                shutil.move(f"{path}\{file}", f"{destination}\{cat}")
    # if it is folder
    if os.path.isdir(f"{path}\{file}"):
        if file not in default_folders:
            if not os.path.exists(f"{path}\Folders"):
                os.makedirs(f"{path}\Folders")
            shutil.move(f"{path}\{file}", f"{path}\Folders")
