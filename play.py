import shutil
import os
import glob


def getFileList(ext):
    fileList = [f for f in glob.glob("*.{}".format(ext))]
    return fileList


def getNextFile(ext, index):
    fileList = getFileList(ext)
    return fileList[index]
    # return [glob.glob("*.{}".format(ext))]


def createPath(path):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, path)
    if not os.path.exists(final_directory):
        os.mkdir(final_directory)
        print(final_directory + " created")
    else:
        print("Already existed")

    return path


def deleteFile(path):
    os.remove(path)


def moveFile(fileName, path, to_copy):
    if (to_copy):
        shutil.copy(fileName, path)
        new_path = os.path.join(path, fileName)
    else:
        shutil.move(fileName, path)
        new_path = os.path.join(path, fileName)

    return new_path


def main():
    inp = 'y'
    ext = input("Enter the extension: ")
    path = createPath("new")
    to_copy = input("Want to copy file? [y]/N: ")
    to_copy = (to_copy == 'y')
    i = 0
    while (inp == 'y'):
        list = os.listdir(path)
        number_files = len(list)

        if (number_files > 0):
            deleteFile(new_path)

        fileName = getNextFile(ext, i)
        if to_copy:
            i = i+1
        new_path = moveFile(fileName, path, to_copy)
        os.startfile(new_path)

        inp = input("Want to Play Next? [y]/N: ")


if __name__ == "__main__":
    main()
