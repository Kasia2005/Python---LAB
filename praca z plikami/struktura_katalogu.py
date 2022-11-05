from os import walk

path = 'C:/Users/Kasia/PycharmProjects/pythonProject3'

files =[]
directories =[]


def file_in_directory_tree(path):
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        directories.extend(dirnames)



file_in_directory_tree(path)

print (files, directories)