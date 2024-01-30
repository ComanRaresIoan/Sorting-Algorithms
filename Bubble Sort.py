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


list = [] # We define a variabile to be the length of the list
number_of_elements = int(input("Enter the number of elements you want to add in list: "))
print("You have reserved a number of", number_of_elements,"places in the list.")
for item in range(0,number_of_elements):
    number = int(input("Enter the number to be added in the list: "))
    list.append(number)
print('The unsorted list of elements is:',list)
bubblesort(list)
print("The sorted list of elements is: ",list)
