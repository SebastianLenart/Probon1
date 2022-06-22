import os
from datetime import datetime
import time
import shutil
from pprint import pprint

directories = ["AM1", "AM2"]
dirDeep = ["AE1", "AE2", "AE3", "AE4"]

path = "C:\\Ujazdowek\\dR2"
path2 = "C:\\Users\\Dell\\Downloads"
path3 = "C:\\Ujazdowek\\U3_V3"
dirs = os.listdir(path2)
dirs2 = os.listdir(path)
fromTime = datetime(2022, 6, 20, 8, 0)
toTime = datetime(2022, 6, 20, 18, 0)

for dir in directories:
    try:
        os.makedirs(os.path.join(path3, dir))
        # for dir2 in 
    except FileExistsError:
        print("Plik istnieje juz ")

    for dirD in dirDeep:
        try:
            os.makedirs(os.path.join(os.path.join(path3, dir), dirD))
        except FileExistsError:
            print("Plik istnieje juz ")
            
# from download
# for filename in dirs:
#     if ".csv" in filename or ".xlsx" in filename:
#         fullFileName = os.path.join(path2, filename)
#         dt = datetime.fromtimestamp(os.path.getmtime(fullFileName))
#         print(f"date of modyfication {filename} : ", dt)
#         if toTime > dt > fromTime:
#             # copy 
#             shutil.copy(fullFileName, path3)

# from directory to specify directory
for filename in dirs2:
     if ".xlsx" in filename:
        for am in directories:
            for ae in dirDeep:
                if ae in filename and am in filename:
                    shutil.copy(os.path.join(path, filename), 
                    os.path.join(path3, am, ae, filename))
                    # print(os.path.join(path3, am, ae, filename))
                    continue
                
                try:
                    if (am in filename and not "AE" in filename):
                        shutil.copy(os.path.join(path, filename), 
                        os.path.join(path3, am, filename))
                except FileNotFoundError:
                    # pass # nie wiem czemu ale tylko tak dziala
                    print("File not Found")
                        

            
        
# for pathx, subdirsx, filesx in os.walk(path3):
#     # pprint(pathx)
#     # pprint(os.listdir(pathx))
#     # pprint(subdirsx)
#     # pprint(filesx)
#     for file in filesx:
#         print(file)
#     # print(os.path.join(pathx, *filesx), "@@@@@@@@@")




def check_extension(ex1, ex2, file):
    if ex1 or ex2 in file:
        return True
    else: 
        return False















































