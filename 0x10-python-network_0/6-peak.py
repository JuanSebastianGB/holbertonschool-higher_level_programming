#!/usr/bin/python3

def find_peak(list_of_integers):
    """[finds a peak in a list of unsorted integers.]
    """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    middle_position = len(list_of_integers) // 2
    middle_point = list_of_integers[middle_position]
    right_point = list_of_integers[middle_position + 1]
    left_point = list_of_integers[middle_position - 1]

    if middle_point > right_point and middle_point > left_point:
        return middle_point
    if middle_point < right_point:
        return find_peak(list_of_integers[middle_position + 1:])
    else:
        return find_peak(list_of_integers[:middle_position])
