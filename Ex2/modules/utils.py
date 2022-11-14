import os


def get_file_names(folderpath, out="output.txt"):
    with open(out, "a") as f:
        for fileName in os.listdir(folderpath):
            if os.path.isfile(os.path.join(folderpath, fileName)):
                print(fileName, file=f)


def get_all_file_names(folderpath, out="output.txt"):
    with open(out, "a") as f:
        for (root, dirs, file) in os.walk(folderpath):
            for fileName in file:
                print(fileName, file=f)


def print_line_one(file_names, folderpath):
    for file in file_names:
        if os.path.isfile(os.path.join(folderpath, file)):
            with open(os.path.join(folderpath, file), "r") as f:
                print(f.readline())


def print_emails(file_names, folderpath):
    for file in file_names:
        print(file)
        if os.path.isfile(os.path.join(folderpath, file)):
            with open(os.path.join(folderpath, file), "r") as f:
                for line in f:
                    if line.find("@") != -1:
                        print(line)


def write_headlines(md_files, folderpath, out="output.txt"):
    with open(out, "a") as outf:
        for file in md_files:
            if file.endswith(".md"):
                print(file, file=outf)
                with open(os.path.join(folderpath, file), "r") as readf:
                    for line in readf:
                        if line.startswith("#"):
                            print(line, file=outf)


if __name__ == "__main__":
    path1 = "C://Users//fiske//Desktop//sem4//pythonExercises//Ex2"
    path2 = "C://Users//fiske//Desktop//sem4//pythonExercises//Ex2//dummyTextFiles"
    path3 = "C://Users//fiske//Desktop//sem4//pythonExercises//Ex2//dummyEmailFiles"
    path4 = "C://Users//fiske//Desktop//sem4//pythonExercises//Ex2//dummyMdFiles"

    # get_file_names(path1)
    # get_all_file_names(path1)
    # print_line_one(os.listdir(path2), path2)
    # print_emails(os.listdir(path3), path3)
    # write_headlines(os.listdir(path4), path4)
