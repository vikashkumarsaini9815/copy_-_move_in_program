import os, shutil
from M_Copy import copyfunction, movefunction

work_opetions = (input("what is work in program like copy and move file  :-  ", ))
print(type(work_opetions))
compresin1 = "copy"
compresin2 = "move"
compresin3 = ["copy","move"]
if work_opetions in compresin3:
    if work_opetions == compresin1:
        print("copy & move") 
        scr = (input("fill your file dir path :- ", ))
        dcr = (input("fill your file drop path  :- ", ))    
        copyfunction(scr, dcr)
        print("done copy")
    elif work_opetions == compresin2:
        scr = (input("fill your file dir path :- ", ))
        dcr = (input("fill your file drop path  :- ", ))
        movefunction(scr,dcr)
        print("Done move file")
        
else:
    print("somthing wrong 1")


#   how to fill path with file name 
#  Exa : -  c:/users/pushp/desktop/python_copy_data/vvv26.txt
#   this program only works one file copy & move 