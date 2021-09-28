#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists."""
    list_result = []
    for index in range(list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            list_result.append(result)

    return list_result
