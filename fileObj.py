# with open ( 'fileObj1', 'r' ) as rf:
#     with open ( 'test_copy.txt', 'w' ) as wf:
#         for line in rf:
#             wf.write ( line )

# f.write ( "test" )
# size_to_read = 10
# print ( "Possition: " + str ( f.tell () ) )
# f_contetnts = f.read ( size_to_read )
#
# while len ( f_contetnts ) > 0:
#     print ( "Possition: " + str ( f.tell () ) )
#
#     print ( f_contetnts, end="*" )
#
#     f_contetnts = f.read ( size_to_read )
#
#     print ( len ( f_contetnts ) )


# print ( f.closed )
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


