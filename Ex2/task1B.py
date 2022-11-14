
nameList = ["Henning", "Birger", "Rasmus", "Jonathan", "Henrik"]


def write_list_to_file(output_file, *arg):
    namefile = open(output_file, "a")

    namefile.writelines(name + "\n" for name in arg)


write_list_to_file("MyFile.txt", "Svend", "Kurt", "Abdullah", "Mads")
