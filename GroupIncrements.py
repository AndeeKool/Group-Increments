import os
import shutil

path = "D:\\Documents - HDD\\PyProjects\\Group-Increments\\project"
print ("current directory: " + path)

#for file in os.listdir(path):
for (path, dirs, files) in os.walk(path):
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        f_title, f_increment = file_name.split('-')

        full_dest = os.path.join(path, f_title)
        source = os.path.join(full_dest, file)

        try:
            #if os.path.isdir(f_title):
            if os.path.exists(full_dest):
                print("Folder exists, moving file")
                shutil.move(os.path.join(path, file), full_dest)

            else:
                print("Folder doesn't exist. Create new folder, moving file")
                os.makedirs(full_dest)
                shutil.move(os.path.join(path, file), full_dest)

        except (FileNotFoundError, PermissionError):
            pass
