nameList = ["Henning", "Birger", "Rasmus", "Jonathan", "Henrik"]


def print_name(index):
    if index > len(nameList) - 1:
        return
    print(nameList[index])
    return print_name(index + 1)


print_name(0)
