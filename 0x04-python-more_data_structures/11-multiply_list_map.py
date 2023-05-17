def multiply_list_map(my_list=[], number=0):
    return list(i * number for i in map(lambda x: x, my_list))
