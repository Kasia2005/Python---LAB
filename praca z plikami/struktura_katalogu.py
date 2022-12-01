from os import walk

path = 'C:/Users/Kasia/PycharmProjects/pythonProject3'

files =[]
directories =[]


def main(path):
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        directories.extend(dirnames)



if __name__ == '__main__':
    main(path)

print (files, directories)
