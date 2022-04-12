import os, shutil, glob


work_options = (input("what is work in program like copy and move file  :-  ", ))
print(type(work_options))
comparison1 = "copy"
comparison2 = "move"
comparison3 = ["copy","move"]
if work_options in comparison3 :

    if work_options == comparison1:
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
    elif work_options == comparison2:
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