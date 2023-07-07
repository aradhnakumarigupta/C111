import os
import shutil

from_dir="C:/Users/user/Downloads"
to_dir="C:/Usersu/ser/OneDrive/Desktop/Document_files"

list_of_files= os.listdir(from_dir)
print(list_of_files)

for file_name  in list_of_files:
    name,extention=os.path.splitext(file_name)
    print(extention)
    print(name)

    if extention=="":
        continue
    if extention in ["DOC","PDF","PPT"]:
        path1=from_dir+"/"+file_name
        path2=from_dir+"/"+"document_files"
        path3=from_dir+"/"+"document_files"+"/"+file_name

    if os.path.exists(path2):
       shutil.move(path1,path3)
    else:
      os.makedirs(path2)
      shutil.move(path1,path3)

