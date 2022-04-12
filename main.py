import os, shutil
from M_Copy import copyfunction, movefunction

work_options = (input("what is work in program like copy and move file  :-  ", ))
print(type(work_options))
comparison1 = "copy"
comparison2 = "move"
comparison3 = ["copy","move"]
if work_options in comparison3:
    if work_options == comparison1:
        print("copy & move") 
        scr = (input("fill your file dir path :- ", ))
        dcr = (input("fill your file drop path  :- ", ))    
        copyfunction(scr, dcr)
        print("done copy")
    elif work_options == comparison2:
        scr = (input("fill your file dir path :- ", ))
        dcr = (input("fill your file drop path  :- ", ))
        movefunction(scr,dcr)
        print("Done move file")
        
else:
    print("somthing wrong 1")


#   how to fill path with file name 
#  Exa : -  c:/users/pushp/desktop/python_copy_data/vvv26.txt
#   this program only works one file copy & move 