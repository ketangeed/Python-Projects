import os

def arrange_file(file, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]

    if not os.path.exists("images"):
        os.mkdir("images")


    for i,file in enumerate(files_with_ext):
        os.rename(file, f"images/Photo.{i}{ext}")
    

if __name__ =="__main__":
    files = os.listdir()
    arrange_file(files, ".jpg")