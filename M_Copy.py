import shutil, os

def copyfunction(scr, dcr):
    file_resive_path = scr
    file_drop_path = dcr
    shutil.copy(file_resive_path, file_drop_path)
    data = "done copy file"
    return data


def movefunction(scr,dcr):
    file_resive_path = scr
    file_drop_path = dcr
    os.rename(file_resive_path, file_drop_path)
    data = "done move file"
    return data


    