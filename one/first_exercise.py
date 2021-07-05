from collections import Counter

# Write a python function that finds the duplicate items in any given array.


def return_duplicated_items(item_array):
    # return [key for key, value in Counter(item_array).items() if value > 1]
    checked_items = []
    duplicated_items = []
    for item in item_array:
        if item in checked_items:
            duplicated_items.append(item)
        elif item not in checked_items:
            checked_items.append(item)
    return duplicated_items

