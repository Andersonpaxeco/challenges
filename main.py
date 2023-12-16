import os
from tkinter.filedialog import askdirectory

folder_from = askdirectory(title = "From")
folder_to = askdirectory(title = "To")

rules_files = {
    "Jan" : "January",
    "Fev" : "February",
    "Mar" : "March"
}

list_files = os.listdir(folder_from)
print(list_files)

for file_name in list_files:
    for key in rules_files.keys():
        if key in file_name:
            new_folder = rules_files[key]
            full_path_from = os.path.join(folder_from, file_name)
            full_path_to = os.path.join(folder_to, new_folder, file_name)
            path_new_folder = os.path.join(folder_to, new_folder)
            if not os.path.exists(path_new_folder):
                os.mkdir(path_new_folder)
            os.rename(full_path_from, full_path_to)
