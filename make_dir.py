"""
cd to the location

make a dir
"""

import os

# name_of_dir = "Dir1"

try:
    new_dir = os.makedirs ( f"MadeByPython/{name_of_dir}" )

    print(new_dir)

except FileExistsError:
    print ( "File exists" )
#
# mod_time = os.stat ( "Testing_satat" ).st_mtime
#
# print(os.environ.get('USER'))
# print(os.environ.get('HOME'))

print(os.path.splitext('/temp/temp2/text.txt'))

print(dir(os.path))



