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


# Define a variable to be the length of the list
list = []

# Take user input for the number of elements in the list
number_of_elements = int(input("Enter the number of elements you want to add in the list: "))
print("You have reserved a number of", number_of_elements, "places in the list.")

# Take user input for each element
for item in range(0, number_of_elements):
    number = int(input("Enter the number to be added in the list: "))
    list.append(number)

print('The unsorted list of elements is:', list)

# Sort the list using shellSort
shellSort(list)

print("The sorted list of elements is: ", list)
