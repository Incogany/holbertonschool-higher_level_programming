#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    value = my_list[idx]
    my_list.remove(value)
    lists = my_list
    return lists
