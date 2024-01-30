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
