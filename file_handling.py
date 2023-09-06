# f=open("sid.txt","a") # a module append the file 
# # print(f.readline())
# # print(f.read())

# # print(f.readlines()[1])
# f.write("\n There are different types of files such as text files, data files, directory files, binary and graphic files, and these different types of files store different types of information. \n In a computer operating system, files can be stored on optical drives, hard drives or other types of storage devices. ")

# f.close()


# import os
# os.remove("filetext.txt")


try:
    f=open("send.txt","a")
    f.write("\n k xa solti")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("file not found")
    
except:
    print("something went wrong")


