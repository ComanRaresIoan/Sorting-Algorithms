"""Merge sort first divides the array into equal halves and then combines them in a sorted manner"""
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    # Find the middle point and divide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)  # Fix: Call merge instead of merge_sort

# Merge the sorted halves
def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half = left_half[1:]  # Fix: Use slicing to remove the first element
        else:
            res.append(right_half[0])
            right_half = right_half[1:]  # Fix: Use slicing to remove the first element

    if len(left_half) == 0:
        res += right_half
    else:
        res += left_half
    return res

unsorted_list = []
number_of_elements = int(input("Enter the number of elements you want to add in list: "))
print("You have reserved a number of", number_of_elements,"places in the list.")
for item in range(0,number_of_elements):
    number = int(input("Enter the number to be added in the list: "))
    unsorted_list.append(number)
print('The unsorted list of elements is:',unsorted_list)
print("The sorted list of elements is",merge_sort(unsorted_list))