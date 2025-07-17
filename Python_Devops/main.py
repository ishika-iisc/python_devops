# # import os
# # # os.system('echo Hello World !')

# # #get your current directory 
# # cwd=os.getcwd()
# # # print("current working directory: ", cwd)

# # # list all files and folders in current directory
# # # items = os.listdir(cwd)
# # # print("contents :", items)

# # # # create a new folder
# # # new_folder = "test"
# # # os.mkdir(new_folder)
# # # print(f"Created folder : {new_folder}")


# # # # rename a folder 
# # # os.rename("renamed", "new_folder")
# # # print("folder name renamed")

# # # delete a folder 
# # os.rmdir("new_folder")
# # print("folder deleted")


# # ------------------------------------------------------------------------------------

import subprocess

subprocess.run(["python","-m","pip","install","-r","requirements.txt"],check =True)



# # subprocess.run(["echo","hello world !"])

# # result = subprocess.run(["echo","hello world"], capture_output= True, text = True)
# # print(result.stdout)

# # handle errors:
# try:
#     subprocess.run(["ls", "not_here.txt"], check=True)
# except subprocess.CalledProcessError:
#     print("Something went wrong!")