#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    copy = []
    for i in range(len(my_list)):
        if i == idx:
            copy.append(element)
        else:
            copy.append(my_list[i])
    return copy
