import os


directory_name = 'Test_dir'


try:
    # Create target Directory
    os.mkdir(directory_name)
    print("Directory " , directory_name ,  " Created ")
except FileExistsError:
    print("Directory " , directory_name ,  " already exists")

# dir_names = ["Apple", "D"]
#
# try:
#     for item in dir_names:
#         print ( item )
#         os.mkdir ( item )
# except FileExistsError:
#     print ( "Directory ", item, " already exists" )

#
# def file_maker(i):
#     items = ["a","b","c"]
#
#
#
#     for item in items:
#         with open ( f"{item}.txt", "w+" ) as f:
#             f.write ( "This is my first line of code" )
#
# file_maker ( "String p")


from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("/Users/jamespinnock/PycharmProjects/File_and_dir_maker") if isfile(join("/Users/jamespinnock/PycharmProjects/File_and_dir_maker", f))]

