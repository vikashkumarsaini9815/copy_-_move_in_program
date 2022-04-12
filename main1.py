import os, shutil, glob


work_opetions = (input("what is work in program like copy and move file  :-  ", ))
print(type(work_opetions))
compresin1 = "copy"
compresin2 = "move"
compresin3 = ["copy","move"]
if work_opetions in compresin3 :

    if work_opetions == compresin1:
        which_file = (input( "which file (like .pdf, .txt, .png, .mp4, .... )", ))
        path_dir = (input("insert path  : -   ", ))
        result = os.chdir(path_dir)
        list_file = [ ]
        print(which_file)
        for file in glob.glob("*.{}".format(which_file)):
            list_file.append(file)

        print(list_file)
        dst = (input("dir drop path :-  ", ))
        for file1 in list_file:
            shutil.copy(file1, dst)
        print("done")
    elif work_opetions == compresin2:
        which_file = (input( "which file (like .pdf, .txt, .png, .mp4, .... )", ))
        path_dir = (input("insert path  : -  ", ))
        result = os.chdir(path_dir)
        list_file = [ ]
        print(which_file)
        for file in glob.glob("*.{}".format(which_file)):
            list_file.append(file)

        print(list_file)
        dst = (input("dir drop path :-  ", ))
        for file1 in list_file:
            shutil.move(file1, dst)
        print("done")   
else :
    print("somthing wrong 1")