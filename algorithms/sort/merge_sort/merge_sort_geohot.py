"""
Created by Joseph Edradan
Github: https://github.com/josephedradan

Date created: 3/4/2021

Purpose:

Details:

Description:

Notes:
    The Traversal is the the preorder traversal if that helps
        (Root, Left, Right)

IMPORTANT NOTES:

Explanation:

Reference:
    Why Is Merge Sort O(n * log(n))? The Really Really Long Answer.
        Reference:
            https://www.youtube.com/watch?v=alJswNJ4P3U

    geohot / mergesorts
        Reference:
            https://github.com/geohot/mergesorts/blob/master/mergesort.py
"""


def merge_sort(list_given: list) -> list:
    print(list_given)

    """ ----- Split (base cases) ---- """
    # Len == 1 list
    if len(list_given) == 1:
        return list_given

    # Len == 2 List (Mini optimization)
    elif len(list_given) == 2:
        # Sort immediately for 2 items
        if list_given[0] > list_given[1]:
            return [list_given[1], list_given[0]]
        else:
            return list_given

    """ ----- Split call ---- """
    pivot = len(list_given) // 2

    list_left = merge_sort(list_given[:pivot])
    list_right = merge_sort(list_given[pivot:])

    print("After Splits", list_left, list_right)

    """ ----- Merge ---- """
    list_new = []
    while True:
        # If both left and right list still have elements in them
        if len(list_left) > 0 and len(list_right) > 0:
            # If first item from left list <= first item of right list
            if list_left[0] <= list_right[0]:
                """
                Add the left list first element because it's smaller
                Increment left list pivot forward via list slicing
                """
                list_new.append(list_left[0])
                list_left = list_left[1:]
            else:
                """
                Add the right list first element because it's smaller
                Increment right list pivot forward via list slicing
                """
                list_new.append(list_right[0])
                list_right = list_right[1:]

        # If their are items on the left list when right list if empty
        elif len(list_left) > 0:
            # Aad all elements from left list to new list then empty left list
            list_new += list_left
            list_left = []

        # If their are items on the right list when left list if empty
        elif len(list_right) > 0:
            # Aad all elements from right list to new list then empty right list
            list_new += list_right
            list_right = []
        else:
            break

    print("List new:", list_new)
    return list_new


if __name__ == '__main__':
    x = [5, 9, 1, 3, 4, 6, 6, 3, 2]

    result = merge_sort(x)
    print()
    print(result)
