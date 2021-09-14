#!/usr/bin/python3
def element_at(my_list, idx):
    print(len(my_list))
    return None if (len(my_list) < idx + 1 or idx < 0) else my_list[idx]
