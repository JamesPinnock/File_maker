import os


def multi_file(input):
    num_of_f = input
    print(input)
    x = 0
    z = 0
    while x < num_of_f:
        with open ( f'test_{z}.txt', 'w' ) as w:
            pass
        x = x + 1
        z = z + 1


def folderMaker():
    directory_name = 'new_dir'


    try:

        dir_name = f"MadeByPython/{directory_name}"
        os.makedirs ( dir_name )
        os.chdir(dir_name)
        multi_file (10)


    except FileExistsError:
        print ( "File exists" )



folderMaker()


