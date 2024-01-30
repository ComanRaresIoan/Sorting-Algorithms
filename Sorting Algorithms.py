"""It is a comparision-based algorithm in which eachpair of adjacent elements is compared and the elements are swapped
if they are not in order"""

def bubblesort(list):
    # Swap elements to arrange in order
    for iter_num in range(len(list)-1, 0 ,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp



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
print(merge_sort(unsorted_list))

"""Insertion sort involves finding the right place for a given element in a sorted list. So in the beginning we
compare the first two elements and sort thm by comparing them. Then we pick the third element and find it proper
position among the previous two sorted elements. This way we gradually go on adding more elements to the already
sorted list by putting them in their proper position. """

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i - 1
        next_element = InputList[i]
# Compare the current element with the next one
        while (InputList[j] > next_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j = j - 1
        InputList[j+1] = next_element



"""Shell Sort involves sorting elements which are away from each other. We sort a large sublist of a given list and
go on reducing the size of the list until all elements are sorted. The below program finds the gap by equating it to
half of the length of the list size and then starts sorting all elements in it. Then we keep resetting the gap until the
 entire list is sorted. """

def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

            # Sorting the sub list for this gap
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap

            input_list[j] = temp

        # Reduce the gap for the next iteration
        gap = gap // 2

"""Insertion sort involves finding the right place for a given element in a sorted list. So in the begininng we compare
the first to element and sort them by comparing them. Then we pick the third element and find its proper position among
the previous two sorted elements. This way we gradually go on adding more elements to the already sorted list by putting
them in their proper position. """
def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i - 1
        nxt_element = InputList[i]
        # Compare the current element with the next one
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j + 1] = InputList[j]
            j = j - 1
        InputList[j + 1] = nxt_element

list = [] # We define a variabile to be the length of the list
number_of_elements = int(input("Enter the number of elements you want to add in list: "))
print("You have reserved a number of", number_of_elements,"places in the list.")
for item in range(0,number_of_elements):
    number = int(input("Enter the number to be added in the list: "))
    list.append(number)
print('The unsorted list of elements is:',list)
insertion_sort(list)
print("The sorted list of elements is: ",list)