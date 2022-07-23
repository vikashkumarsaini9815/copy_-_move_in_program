import os, shutil, glob

path_dir = (input("insert path  : -   ", ))
result = os.chdir(path_dir)
list_file = [ ]
print(path_dir)
type1 = ("*.txt","*.pdf","*.dir")
for file in type1:
    list_file.extend(glob.glob(file))

print(list_file)