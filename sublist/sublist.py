SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    elif first_list in slicer(second_list, len(first_list)):
        return SUBLIST
    elif second_list in slicer(first_list, len(second_list)):
        return SUPERLIST
    else:
        return UNEQUAL


def slicer(lst: list, slice_size: int):
    return (lst[i:i+slice_size] for i in range(len(lst) - slice_size + 1))
