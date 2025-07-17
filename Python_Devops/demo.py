import shutil 
import os

with open("original.txt" , "w") as f:
    f.write("This is original file")

shutil.copy("original.txt" , "copy.txt")

shutil.move("copy.txt", "devops/moved_file.txt" )

total, used , free = shutil.disk_usage(".")

print("disk usgae")
print(f"total : {total // (1024**3)} GB")
print(f"used : {used // (1024**3)} GB")
print(f"free : {free // (1024**3)} GB")

os.remove("original.txt")
